from scanner.scanner import Scanner
from scanner.graph import *
from parser import Parser
import sys

def __main__():
    scanner = Scanner('input.txt')
    parser = Parser(scanner)
    generated_code, semantic_errors = parser.parse()
    #write to output.txt
    with open('output.txt', 'w') as f:
        if len(semantic_errors) > 0:
            generated_code = 'The output code has not been generated.'
        f.write(generated_code)
        f.close()
    with open('semantic_errors.txt', 'w') as f:
        if len(semantic_errors) == 0:
            semantic_errors = 'The input program is semantically correct.'
        else :
            semantic_errors = '\n'.join(semantic_errors)
        f.write(semantic_errors)
        f.close()


if __name__ == '__main__':
    __main__()
    pass
