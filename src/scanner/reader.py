class Reader:
    
    def __init__(self, file):
        self.line_number = 1
        self.file = open(file, "rb")
        
    def read_char(self):
        char = self.file.read(1).decode('ascii')
        if '\n' in char:
            self.line_number += 1
        if not char:
            self.file.close()
            return 'eof'
        return char
    
    def get_lineno(self):
        return self.line_number

    def move_pointer_back(self):
        self.file.seek(-1, 1)