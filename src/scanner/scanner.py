from graph import *
from reader import Reader

if __name__ == '__main__':
    print(digits)

class Scaner():
    
    def __init__(self, file):
        self.reader = Reader(file)
        self.dfa = DFA()
        set_current_node(0)
        self.buffer = ''
        
    def scan(self):
        while True:
            char = self.reader.read_char()
            if (char == 'eof'):
                return 'eof','eof'
            self.buffer += char
            next_node_id = self.current_node.get_next_node(char)

            if self.next_node_id == -1:
                buffer = self.buffer
                empty_buffer()
                set_current_node(0)
                return buffer, "Invalid input"

            set_current_node(next_node_id)

            if self.current_node.terminal:
                if self.current_node.type == Type.ERROR1 or self.current_node.type == Type.ERROR2 or self.current_node.type == Type.ERROR3:
                    buffer = self.buffer
                    type_ = self.current_node.type.value
                    empty_buffer()
                    set_current_node(0)
                    return buffer, type_
                else:
                    if self.current_node.move_pointer_back:
                        self.reader.move_pointer_back()

                    token = self.get_token()

                    empty_buffer()
                    set_current_node(0)

                    if token == None:
                        continue
                    return token
                
    def get_token(self):
        if (self.current_node.type == Type.IDENTIFIER):
            if (self.buffer.lower() in keywords):
                return Type.KEYWORD.value, self.buffer
            else:
                return Type.IDENTIFIER.value, self.buffer
        elif (self.current_node.type == Type.COMMENT or self.current_node.type == Type.WHITESPACE):
            return None
        else:
            return self.buffer, self.current_node.type.value

    def set_current_node(self, node_id):
        self.current_node = self.dfa.all_nodes[node_id]
        self.current_node_id = node_id
    
    def empty_buffer(self):
        self.buffer = ''    