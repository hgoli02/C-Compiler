from scanner.graph import *
from scanner.reader import Reader

class Scanner():
    
    def __init__(self, file):
        self.reader = Reader(file)
        self.dfa = DFA()
        self.buffer = ''
        self.set_current_node(0)
        self.symbol_table = ['break', 'else', 'if', 'int', 'repeat', 'return', 'until', 'void']

    def scan(self):
        start_line = None
        while True:
            if self.current_node_id == 0:
                start_line = self.reader.get_lineno()
            char = self.reader.read_char()                
            self.buffer += char
            next_node_id = self.current_node.get_next_node(char)

            if next_node_id == -1:
                buffer = self.buffer
                self.empty_buffer()
                self.set_current_node(0)
                return Type.ERROR4, buffer, start_line

            self.set_current_node(next_node_id)

            if self.current_node.terminal:
                if self.current_node.type == Type.ERROR1 or self.current_node.type == Type.ERROR2 or self.current_node.type == Type.ERROR3 or self.current_node.type == Type.ERROR4:
                    if self.current_node.move_pointer_back:
                        self.remove_last_buff()
                        self.reader.move_pointer_back()
                    buffer = self.buffer
                    type_ = self.current_node.type
                    self.empty_buffer()
                    self.set_current_node(0)
                    return type_, buffer, start_line
                else:
                    if self.current_node.move_pointer_back:
                        self.remove_last_buff()
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

    def remove_last_buff(self):
        if len(self.buffer) > 3 and self.buffer[-3:] == 'eof':
            self.buffer = self.buffer[:-3]
        else:
            self.buffer = self.buffer[:-1]
    

