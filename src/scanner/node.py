class Node:
    
    def __init__(self, number, is_finished, move_pointer_back):
        self.number = number
        self.is_finished = is_finished
        self.move_pointer_back = move_pointer_back
        self.moves = {}
        
    def add_path(self, destination_num, move):
        self.moves[move] = destination_num
        
    def get_next_node(self, move):
        for key in self.moves.keys():
            if move in key:
                return self.moves[key]
        return -1