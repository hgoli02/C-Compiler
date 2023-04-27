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