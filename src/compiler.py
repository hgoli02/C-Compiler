from scanner.scanner import Scanner
from scanner.graph import *
from parser.parser import Parser

def __main__():
    scanner = Scanner('input.txt')
    parser = Parser(scanner)
    parse_tree = parser.parse()
    with open("parse_tree.txt", 'w', encoding="utf-8") as f:
        f.write(parse_tree)
        f.close()
        
    with open("syntax_errors.txt", 'w', encoding="utf-8") as f:
        f.write('There is no syntax error.')
        f.close()


if __name__ == '__main__':
    __main__()
    pass
