from anytree import Node as AnyNode, RenderTree
from scanner.scanner import Scanner
from scanner.graph import Type
EPSILON = 'EPSILON'
import anytree
import json
class Parser:
    """
    A predictive bottom up parser for the C- language.
    using Transitional Diagrams.
    """
    def __init__(self, scanner):
        self.scanner = scanner
        self.update_current_token()
        self.stack = []
        self.root_nodes = {}

        #read data.json
        with open('parser/data.json', 'r') as f:
            data = json.load(f)
            f.close()
        self.terminals = data['terminals']
        self.non_terminals = data['non-terminal']
        self.firsts = data['first']
        self.follows = data['follow']
        self.anyroot = AnyNode('Program')

        with open('parser/grammer.txt', 'r') as f:
            grammer_input = f.read()
            f.close()

        self.build_tree(grammer_input)


    def parse(self):
        self.program()
        if self.current_token_type != Type.EOF:
            self.error()
            
    def build_tree(self, inputs):
        """
        sample input:
        1. Program -> Declaration-list
        2. Declaration-list -> Declaration Declaration-list | EPSILON 
        """
        for line in inputs.split('\n'):
            line = line.split('->')
            root = line[0].strip()
            children = line[1].split('|')
            self.root_nodes[root] = Node({}, root, False)
            for child in children:
                child = child.strip()
                transitions = child.split(' ')
                curr_node = self.root_nodes[root]
                #build transition diagram
                for transition in transitions:
                    curr_node.transitions[transition] = Node({}, root, False)
                    curr_node = curr_node.transitions[transition]
                curr_node.is_terminal = True
        

    def update_current_token(self):
        self.current_token = self.scanner.scan()
        self.current_token_type = self.current_token[0]
        self.current_token_value = self.current_token[1]
        self.current_token_grammer = self.current_token_type

        print(f"updating current token: {self.current_token_value}")
        
        if self.current_token_type == Type.KEYWORD:
            self.current_token_grammer = self.current_token_value
        elif self.current_token_type == Type.IDENTIFIER:
            self.current_token_grammer = 'ID'
        elif self.current_token_type == Type.NUMBER:
            self.current_token_grammer = 'NUM'
        elif self.current_token_type == Type.SYMBOL:
            self.current_token_grammer = self.current_token_value

    def parse(self):
        
        current_node = self.root_nodes['Program'] #TODO: get start node
        current_anynode = self.anyroot
        while True:
            print(current_node)
            if current_node.is_terminal:
                node = self.stack.pop()
                current_node = node
                for pre, fill, node in RenderTree(self.anyroot):
                    print("%s%s" % (pre, node.name))
                continue

            else:
                flag = False
                for transition in current_node.transitions:
                    if transition in self.terminals and self.current_token_grammer == transition:
                        print(transition)
                        current_anynode = AnyNode(transition, parent=current_anynode)
                        current_node = current_node.get_next_node(transition)
                        self.update_current_token()
                        flag = True
                        break
                    elif transition in self.non_terminals and self.current_token_grammer in self.firsts[transition]:
                        current_anynode = AnyNode(transition, parent=current_anynode)
                        stack_node = current_node.get_next_node(transition)
                        self.stack.append(stack_node)
                        current_node = self.root_nodes[transition]
                        flag = True
                        break
                    elif transition in self.non_terminals and EPSILON in self.firsts[transition] and self.current_token_grammer in self.follows[transition]:
                        current_anynode = AnyNode(transition, parent=current_anynode)
                        stack_node = current_node.get_next_node(transition)
                        self.stack.append(stack_node)
                        current_node = self.root_nodes[transition]
                        flag = True
                        break
                if flag == True:
                    continue
                if EPSILON in current_node.transitions:
                    current_node = self.stack.pop()
                    continue 


                
class Node:
    node_id = 0
    
    # transitions = {(non) terminal: node_id}
    def __init__(self, transitions, tree_value, is_terminal=False):
        self.transitions = transitions
        self.is_terminal = is_terminal
        self.tree_value = tree_value
        Node.node_id += 1
        self.node_id = Node.node_id

    def get_next_node(self, transition):
        #error handling later
        return self.transitions[transition]

    def get_id(self):
        return self.node_id

    def __str__(self):
        return str(self.tree_value) + "|" + str(self.transitions.keys())    
    
    def __repr__(self):
        return str(self.tree_value) + "|" + str(self.transitions.keys())


