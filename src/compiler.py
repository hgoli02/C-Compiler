from collections import defaultdict
from scanner.scanner import Scanner
from scanner.graph import *

if __name__ == '__main__':
    output_dict = defaultdict(list)
    scanner = Scanner('src/input.txt')
    has_line_number_been_printed = False
    while True:
        output = scanner.scan()
        if output[0] == 'Invalid input':
            pass
        elif output[0] == Type.ERROR1:
            pass
        elif output[0] == Type.ERROR2:
            break
        elif output[0] == Type.ERROR3:
            pass
        else:
            if output[0] == Type.WHITESPACE:
                pass
            elif output[0] == Type.COMMENT:
                pass
            else:
                output_string = "(" + str(output[0].value) + ', ' + str(output[1]) + ")"
                output_dict[scanner.reader.get_lineno()].append(output_string) 

        if scanner.reader.file_ended:
            break

    for key in output_dict.keys():
        print(f"{key}.\t")
        for i in output_dict[key]:
            print(i)

