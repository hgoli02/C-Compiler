from scanner.scanner import Scanner
from scanner.graph import *
from parser import Parser
import sys

def __main__():
    scanner = Scanner('input.txt')
    parser = Parser(scanner)
    parse_tree, syntax_errors = parser.parse()
    print(syntax_errors)

    if not syntax_errors:
        syntax_errors = 'There is no syntax error.'
    
    with open("parse_tree.txt", 'w', encoding='utf-8') as f:
        f.write(parse_tree)
        f.close()
    
    with open("syntax_errors.txt", 'w') as g:
        g.write(syntax_errors)
        g.close()


if __name__ == '__main__':
    __main__()
    pass
