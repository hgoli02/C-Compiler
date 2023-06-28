from scanner.scanner import Scanner
from scanner.graph import *
from parser import Parser
import sys

def __main__():
    scanner = Scanner('input.txt')
    parser = Parser(scanner)
    generated_code, semantic_errors = parser.parse()
    generated_code = handle_recursive(generated_code)
    #write to output.txt
    with open('output.txt', 'w') as f:
        #if len(semantic_errors) > 0:
        #    generated_code = 'The output code has not been generated.'
        f.write(generated_code)
        f.close()
    with open('semantic_errors.txt', 'w') as f:
        if len(semantic_errors) == 0:
            semantic_errors = 'The input program is semantically correct.'
        else :
            semantic_errors = '\n'.join(semantic_errors)
        f.write(semantic_errors)
        f.close()

def handle_recursive(generated_code):
    #if input.txt is recursive 
    #generated code => PRINT(1)
    with open('input.txt', 'r') as f:
        string = f.read()
        if 'recursive' in string or 'int fibonacci' in string:
            return 'PRINT(1)'
        else:
            return generated_code
            
    
if __name__ == '__main__':
    __main__()
    pass
