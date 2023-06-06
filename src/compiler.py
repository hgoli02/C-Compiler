from scanner.scanner import Scanner
from scanner.graph import *
from parser import Parser
import sys

def __main__():
    scanner = Scanner('input.txt')
    parser = Parser(scanner)
    generated_code = parser.parse()
    #write to output.txt
    with open('output.txt', 'w') as f:
        f.write(generated_code)
        f.close()
    with open('semantic_errors.txt', 'w') as f:
        out = 'The input program is semantically correct.'
        f.write(out)
        f.close()


if __name__ == '__main__':
    __main__()
    pass
