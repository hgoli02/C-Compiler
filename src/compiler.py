from collections import defaultdict
from scanner.scanner import Scanner
from scanner.graph import *
from parser.parser import Parser

def __main__():
    scanner = Scanner('input.txt')
    parser = Parser(scanner)
    parser.parse()

if __name__ == '__main__':
    __main__()
    pass
