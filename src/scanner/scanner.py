from scanner.graph import *
from scanner.reader import Reader

if __name__ == '__main__':
    print(digits)

class Scanner():
    
    def __init__(self, file):
        self.reader = Reader(file)
        self.dfa = DFA()
        self.set_current_node(0)
        self.buffer = ''
        self.symbol_table = ['break', 'else', 'if', 'int', 'repeat', 'return', 'until', 'void']
        
    def scan(self):
        while True:
            char = self.reader.read_char()                
            self.buffer += char
            next_node_id = self.current_node.get_next_node(char)

            if next_node_id == -1:
                buffer = self.buffer
                self.empty_buffer()
                self.set_current_node(0)
                return "Invalid input", buffer

            self.set_current_node(next_node_id)

            if self.current_node.terminal:
                if self.current_node.type == Type.ERROR1 or self.current_node.type == Type.ERROR2 or self.current_node.type == Type.ERROR3:
                    buffer = self.buffer
                    type_ = self.current_node.type
                    self.empty_buffer()
                    self.set_current_node(0)
                    return type_, buffer
                else:
                    if self.current_node.move_pointer_back:
                        self.buffer = self.buffer[:-1]
                        self.reader.move_pointer_back()

                    token = self.get_token()

                    self.empty_buffer()
                    self.set_current_node(0)

                    if token == None:
                        continue
                    return token
                
    def get_token(self):
        if (self.current_node.type == Type.IDENTIFIER):
            if (self.buffer.lower() in keywords):
                return Type.KEYWORD, self.buffer
            else:
                if (self.buffer not in self.symbol_table):
                    self.symbol_table.append(self.buffer)
                return  Type.IDENTIFIER, self.buffer
        elif (self.current_node.type == Type.COMMENT or self.current_node.type == Type.WHITESPACE):
            return None
        else:
            return self.current_node.type, self.buffer 

    def set_current_node(self, node_id):
        self.current_node = self.dfa.all_nodes[node_id]
        self.current_node_id = node_id
    
    def empty_buffer(self):
        self.buffer = ''    