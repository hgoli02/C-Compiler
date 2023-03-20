from collections import defaultdict
from scanner.scanner import Scanner
from scanner.graph import *

if __name__ == '__main__':
    output_dict = defaultdict(list)
    lexical_dict = defaultdict(list)
    scanner = Scanner('src/input.txt')
    has_line_number_been_printed = False
    while True:
        output = scanner.scan()
        if output[0] == 'Invalid input':
            if (scanner.reader.file_ended):
                break
            output_string = "(" + str(output[0]) + ', ' + str(output[1]) + ")"
            output_dict[scanner.reader.get_lineno()].append(output_string)
        elif output[0] == Type.ERROR1 or output[0] == Type.ERROR2 or output[0] == Type.ERROR3:
            output_string = "(" + str(output[0].value) + ', ' + str(output[1]) + ")"
            output_dict[scanner.reader.get_lineno()].append(output_string)
        else:
            output_string = "(" + str(output[0].value) + ', ' + str(output[1]) + ")"
            output_dict[scanner.reader.get_lineno()].append(output_string) 
        if scanner.reader.file_ended:
            break

    #Token
    token_print = ''
    for key in sorted(output_dict.keys()):
        token_print += str(key) + '.\t'
        for token in output_dict[key]:
            token_print += token
            token_print += ' ' #TODO: check last space
        token_print += '\n'
    
    print(token_print)


    #Symbol table
    symbol_table_print = ''
    for i in range(len(scanner.symbol_table)):
        symbol_table_print += str(i + 1) + '.\t' + scanner.symbol_table[i] + '\n'
    
    print(symbol_table_print)

    lexical_print = ''
    for key in lexical_dict.keys():
        lexical_print += f'{key}.\t'
        for i in lexical_dict[key]:
            lexical_print += i + " "
        lexical_print += '\n'

    if lexical_print == '':
        lexical_print = 'There is no lexical error.'
    print(lexical_print)