import string

digits = [str(i) for i in range(10)]
letters = list(string.ascii_letters)
definite_symbols = [*';:,[](){}+-<']
all_symbols = [*';:,[](){}+-<=*/']
whitespace = [' ', '\n', '\r', '\t', '\v', '\f']

class DFA:
    
    def __init__(self):
        self.all_nodes = []
        