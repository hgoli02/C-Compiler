import os

class Reader:
    
    def __init__(self, file):
        self.line_number = 1
        print (os.getcwd())
        self.file = open(file, "rb")
        self.file_ended = False
        
    def read_char(self):
        char = self.file.read(1).decode('ascii')
        if '\n' in char:
            self.line_number += 1
        if not char:
            self.file.close()
            self.file_ended = True
            return 'eof'
        return char
    
    def get_lineno(self):
        return self.line_number

    def move_pointer_back(self):
        if not self.file_ended:
            self.file.seek(-1, 1)

    def output_tree(self, parse_tree):
        flag = False
        with open ('input.txt', 'r') as file:
            test = file.read()
            file.close()
        with open("parse_tree.txt", 'w', encoding='utf-8') as f:
            f.write(parse_tree)
            f.close()
        return flag

    def output(self, syntax_errors):
        with open ('input.txt', 'r') as file:
            test = file.read()
            file.close()
        with open("syntax_errors.txt", 'w') as g:
            g.write(syntax_errors)
            g.close()
        return flag