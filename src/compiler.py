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

# from anytree import Node, RenderTree
# udo = Node("Udo")
# marc = Node("Marc", parent=udo)
# lian = Node("Lian", parent=marc)
# dan = Node("Dan", parent=udo)
# jet = Node("Jet", parent=dan)
# jan = Node("Jan", parent=dan)
# joe = Node("Joe", parent=dan)

# for pre, fill, node in RenderTree(udo):
#     print("%s%s" % (pre, node.name))