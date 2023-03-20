from collections import defaultdict
from scanner.scanner import Scanner
from scanner.graph import *

if __name__ == '__main__':
    output_dict = defaultdict(list)
    lexical_dict = defaultdict(list)
    scanner = Scanner('input.txt')
    has_line_number_been_printed = False
    while True:
        output = scanner.scan()
        if output[0] == 'Invalid input':
            if (scanner.reader.file_ended):
                break
            output_string = "(" + str(output[1]) + ', ' + str(output[0]) + ")"
            lexical_dict[scanner.reader.get_lineno()].append(output_string)
        elif output[0] == Type.ERROR1 or output[0] == Type.ERROR2 or output[0] == Type.ERROR3:
            tmp = str(output[1])
            if len(tmp) >= 7:
                tmp = tmp[:7] + '...'
            output_string = "(" + tmp + ', ' + str(output[0].value) + ")"
            lexical_dict[output[2]].append(output_string)
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
    f = open('tokens.txt', 'w')
    f.write(token_print)
    f.close()

    #Symbol table
    symbol_table_print = ''
    for i in range(len(scanner.symbol_table)):
        symbol_table_print += str(i + 1) + '.\t' + scanner.symbol_table[i] + '\n'
    
    print(symbol_table_print)
    f = open('symbol_table.txt', 'w')
    f.write(symbol_table_print)
    f.close()
    
    lexical_print = ''
    for key in lexical_dict.keys():
        lexical_print += f'{key}.\t'
        for i in lexical_dict[key]:
            lexical_print += i + " "
        lexical_print += '\n'

    if lexical_print == '':
        lexical_print = 'There is no lexical error.'
    print(lexical_print)
    f = open('lexical_errors.txt', 'w')
    f.write(lexical_print)
    f.close()