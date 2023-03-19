import string
from node import Node

digits = set([str(i) for i in range(10)])
letters = set(string.ascii_letters)
definite_symbols = set([*';:,[](){}+-<'])
all_symbols = set([*';:,[](){}+-<=*/'])
whitespace = ' ', '\n', '\r', '\t', '\v', '\f'
language = set([*digits, *letters, *all_symbols, *whitespace])

if __name__ == '__main__':
    print(language - digits - letters)
    print(language - set('=',))

class DFA:
    
    def __init__(self):
        self.all_nodes = []
        #Number
        node0 = Node(0, False, False)
        node1 = Node(1, False, False)
        node2 = Node(2, True, False, error=True) #invalid number
        node3 = Node(3, True, True) #number
        
        #Identifier
        node4 = Node(4, False, False)
        node5 = Node(5, True, True) #digit
        
        #Symbol
        node6 = Node(6, True, False) #symbol
        node7 = Node(7, False, False) #
        node8 = Node(8, True, False) #symbol ==
        node9 = Node(9, True, True)  #symbol =
        node10 = Node(10, False, False) #symbol 
        node11 = Node(11, True, True) #symbol /
        
        #Comment
        node12 = Node(12, False, False) #
        node13 = Node(13, False, False) #
        node14 = Node(14, True, False) #comment
        node16 = Node(16, True, False, error=True) #unclosed comment
        
        #WhiteSpace
        node15 = Node(15, True, False) #Whitespace
        
        #Symbol *
        node17 = Node(17, False, False)
        node18 = Node(18, True, True) #symbol *
        
        #unmatched comment
        node19 = Node(19, True, False, error=True) 
    
        node0.add_path(1, digits)
        node0.add_path(6, definite_symbols)
        node0.add_path(7, set('='))
        node0.add_path(10, '/')
        node0.add_path(17, '*')
        node0.add_path(15, whitespace)
        node0.add_path(4, letters)
        
        node1.add_path(1, digits)
        node1.add_path(2, letters)
        node1.add_path(3, language - digits - letters)
        
        node4.add_path(4, digits + letters)
        node4.add_path(5, whitespace + all_symbols)
        
        node7.add_path(8, set('=',))
        node7.add_path(9, language - set('=',))
        
        node10.add_path(11, language - set('*',))
        node10.add_path(12, set('*',))
        
        node12.add_path(12, language - set('*',))
        node12.add_path(13, set('*',))
        node12.add_path(16, set('eof',))
        
        node13.add_path(12, language - set('/', '*'))
        node13.add_path(13, set('*',))
        node13.add_path(14, set('/',))
        node13.add_path(16, set('eof',))
        
        node17.add_path(18, language - set('/',))
        node17.add_path(19, set('/',))


        
        self.all_nodes.append(node0)
        self.all_nodes.append(node1)
        self.all_nodes.append(node2)
        self.all_nodes.append(node3)
        self.all_nodes.append(node4)
        self.all_nodes.append(node5)
        self.all_nodes.append(node6)
        self.all_nodes.append(node7)
        self.all_nodes.append(node8)
        self.all_nodes.append(node9)
        self.all_nodes.append(node10)
        self.all_nodes.append(node11)
        self.all_nodes.append(node12)
        self.all_nodes.append(node13)
        self.all_nodes.append(node14)
        self.all_nodes.append(node15)
        self.all_nodes.append(node16)
        self.all_nodes.append(node17)
        self.all_nodes.append(node18)
        self.all_nodes.append(node19)        