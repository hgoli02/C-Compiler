class Node:
    
    def __init__(self, number, terminal, move_pointer_back, type=None):
        self.number = number
        self.terminal = terminal
        self.move_pointer_back = move_pointer_back
        self.moves = {}
        self.type = type
        
    def add_path(self, destination_num, move):
        for char in move:
            self.moves[char] = destination_num
        
    def get_next_node(self, move):
        for key in self.moves.keys():
            if move == key:
                return self.moves[key]
        return -1