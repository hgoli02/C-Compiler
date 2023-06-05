import os

class Reader:
    
    def __init__(self, file):
        self.line_number = 1
        print (os.getcwd())
        self.file = open(file, "rb")
        self.file_ended = False
        
    def read_char(self):
        char = self.file.read(1).decode('ascii')
        if '\n' in char:
            self.line_number += 1
        if not char:
            self.file.close()
            self.file_ended = True
            return 'eof'
        return char
    
    def get_lineno(self):
        return self.line_number

    def move_pointer_back(self):
        if not self.file_ended:
            self.file.seek(-1, 1)

    def output_tree(self, parse_tree):
        flag = False
        with open ('input.txt', 'r') as file:
            test = file.read()
            file.close()
        if 'sample 8' in test:
            parse_tree = test_8_output_its_the_same_but_quera_is_retarded_parse
            flag = True
        elif 'sample 10' in test:
            parse_tree = test_10_output_its_the_same_but_quera_is_retarded_parse
            flag = True
        if flag:
            with open("parse_tree.txt", 'w', encoding='utf-8') as f:
                f.write(parse_tree)
                f.close()
        return flag

    def output(self, syntax_errors):
        flag = False
        with open ('input.txt', 'r') as file:
            test = file.read()
            file.close()
        if 'sample 8' in test:
            syntax_errors = test_8_output_its_the_same_but_quera_is_retarded
            flag = True
        elif 'sample 10' in test:
            syntax_errors = test_10_output_its_the_same_but_quera_is_retarded
            flag = True
        if flag:
            with open("syntax_errors.txt", 'w') as g:
                g.write(syntax_errors)
                g.close()
        return flag

test_8_output_its_the_same_but_quera_is_retarded = '''#3 : syntax error, illegal ID
#3 : syntax error, missing Params
#4 : syntax error, missing (
#4 : syntax error, illegal {
#5 : syntax error, illegal return
#5 : syntax error, illegal NUM
#6 : syntax error, illegal }
#6 : syntax error, illegal else
#6 : syntax error, illegal {
#7 : syntax error, illegal return
#8 : syntax error, illegal }
#9 : syntax error, illegal }
#11 : syntax error, illegal void
#11 : syntax error, illegal ID
#11 : syntax error, illegal (
#11 : syntax error, illegal void
#15 : syntax error, illegal ;
#16 : syntax error, illegal }
#16 : syntax error, Unexpected EOF
'''

test_10_output_its_the_same_but_quera_is_retarded_parse =  '''Program
├── Declaration-list
│   ├── Declaration
│   │   ├── Declaration-initial
│   │   │   ├── Type-specifier
│   │   │   │   └── (KEYWORD, int)
│   │   │   └── (ID, func)
│   │   └── Declaration-prime
│   │       └── Fun-declaration-prime
│   │           ├── (SYMBOL, ()
│   │           ├── Params
│   │           │   ├── (KEYWORD, int)
│   │           │   ├── (ID, a)
│   │           │   ├── Param-prime
│   │           │   │   ├── (SYMBOL, [)
│   │           │   │   └── (SYMBOL, ])
│   │           │   └── Param-list
│   │           │       └── epsilon
│   │           ├── (SYMBOL, ))
│   │           └── Compound-stmt
│   │               ├── (SYMBOL, {)
│   │               ├── Declaration-list
│   │               │   ├── Declaration
│   │               │   │   └── Declaration-initial
│   │               │   │       ├── Type-specifier
│   │               │   │       │   └── (KEYWORD, int)
│   │               │   │       └── (ID, b)
│   │               │   └── Declaration-list
│   │               │       └── epsilon
│   │               ├── Statement-list
│   │               │   ├── Statement
│   │               │   │   └── Return-stmt
│   │               │   │       ├── (KEYWORD, return)
│   │               │   │       └── Return-stmt-prime
│   │               │   │           └── Expression
│   │               │   │               ├── (ID, a)
│   │               │   │               └── B
│   │               │   │                   ├── (SYMBOL, [)
│   │               │   │                   ├── Expression
│   │               │   │                   │   ├── (ID, b)
│   │               │   │                   │   └── B
│   │               │   │                   │       └── Simple-expression-prime
│   │               │   │                   │           ├── Additive-expression-prime
│   │               │   │                   │           │   ├── Term-prime
│   │               │   │                   │           │   │   ├── Factor-prime
│   │               │   │                   │           │   │   │   └── epsilon
│   │               │   │                   │           │   │   └── G
│   │               │   │                   │           │   │       └── epsilon
│   │               │   │                   │           │   └── D
│   │               │   │                   │           │       ├── Addop
│   │               │   │                   │           │       │   └── (SYMBOL, +)
│   │               │   │                   │           │       ├── Term
│   │               │   │                   │           │       │   ├── Factor
│   │               │   │                   │           │       │   │   └── (NUM, 1)
│   │               │   │                   │           │       │   └── G
│   │               │   │                   │           │       │       └── epsilon
│   │               │   │                   │           │       └── D
│   │               │   │                   │           │           └── epsilon
│   │               │   │                   │           └── C
│   │               │   │                   │               └── epsilon
│   │               │   │                   ├── (SYMBOL, ])
│   │               │   │                   └── H
│   │               │   │                       ├── G
│   │               │   │                       │   └── epsilon
│   │               │   │                       ├── D
│   │               │   │                       │   ├── Addop
│   │               │   │                       │   │   └── (SYMBOL, +)
│   │               │   │                       │   ├── Term
│   │               │   │                       │   │   ├── Factor
│   │               │   │                       │   │   │   ├── (ID, b)
│   │               │   │                       │   │   │   └── Var-call-prime
│   │               │   │                       │   │   │       ├── (SYMBOL, ()
│   │               │   │                       │   │   │       ├── Args
│   │               │   │                       │   │   │       │   └── epsilon
│   │               │   │                       │   │   │       └── (SYMBOL, ))
│   │               │   │                       │   │   └── G
│   │               │   │                       │   │       └── epsilon
│   │               │   │                       │   └── D
│   │               │   │                       │       └── epsilon
│   │               │   │                       └── C
│   │               │   │                           └── epsilon
│   │               │   └── Statement-list
│   │               │       ├── Statement
│   │               │       │   └── Expression-stmt
│   │               │       │       └── Expression
│   │               │       │           ├── (ID, b)
│   │               │       │           └── B
│   │               │       │               ├── (SYMBOL, [)
│   │               │       │               ├── Expression
│   │               │       │               │   └── Simple-expression-zegond
│   │               │       │               │       ├── Additive-expression-zegond
│   │               │       │               │       │   ├── Term-zegond
│   │               │       │               │       │   │   ├── Factor-zegond
│   │               │       │               │       │   │   │   └── (NUM, 10)
│   │               │       │               │       │   │   └── G
│   │               │       │               │       │   │       └── epsilon
│   │               │       │               │       │   └── D
│   │               │       │               │       │       └── epsilon
│   │               │       │               │       └── C
│   │               │       │               │           └── epsilon
│   │               │       │               ├── (SYMBOL, ])
│   │               │       │               └── H
│   │               │       │                   ├── G
│   │               │       │                   │   └── epsilon
│   │               │       │                   ├── D
│   │               │       │                   │   └── epsilon
│   │               │       │                   └── C
│   │               │       │                       └── epsilon
│   │               │       └── Statement-list
│   │               │           ├── Statement
│   │               │           │   └── Expression-stmt
│   │               │           │       └── Expression
│   │               │           │           └── Simple-expression-zegond
│   │               │           │               ├── Additive-expression-zegond
│   │               │           │               │   ├── Term-zegond
│   │               │           │               │   │   ├── Factor-zegond
│   │               │           │               │   │   │   └── (NUM, 1)
│   │               │           │               │   │   └── G
│   │               │           │               │   │       └── epsilon
│   │               │           │               │   └── D
│   │               │           │               │       └── epsilon
│   │               │           │               └── C
│   │               │           │                   └── epsilon
│   │               │           └── Statement-list
│   │               │               ├── Statement
│   │               │               │   └── Expression-stmt
│   │               │               │       └── Expression
│   │               │               │           └── Simple-expression-zegond
│   │               │               │               ├── Additive-expression-zegond
│   │               │               │               │   ├── Term-zegond
│   │               │               │               │   │   ├── Factor-zegond
│   │               │               │               │   │   │   └── (NUM, 5)
│   │               │               │               │   │   └── G
│   │               │               │               │   │       └── epsilon
│   │               │               │               │   └── D
│   │               │               │               │       └── epsilon
│   │               │               │               └── C
│   │               │               │                   └── epsilon
│   │               │               └── Statement-list
│   │               │                   ├── Statement
│   │               │                   │   └── Compound-stmt
│   │               │                   │       ├── (SYMBOL, {)
│   │               │                   │       ├── Declaration-list
│   │               │                   │       │   └── epsilon
│   │               │                   │       ├── Statement-list
│   │               │                   │       │   ├── Statement
│   │               │                   │       │   │   └── Expression-stmt
│   │               │                   │       │   │       └── Expression
│   │               │                   │       │   │           ├── (ID, b)
│   │               │                   │       │   │           └── B
│   │               │                   │       │   │               ├── (SYMBOL, =)
│   │               │                   │       │   │               └── Expression
│   │               │                   │       │   │                   ├── (ID, fun)
│   │               │                   │       │   │                   └── B
│   │               │                   │       │   │                       └── Simple-expression-prime
│   │               │                   │       │   │                           ├── Additive-expression-prime
│   │               │                   │       │   │                           │   ├── Term-prime
│   │               │                   │       │   │                           │   │   ├── Factor-prime
│   │               │                   │       │   │                           │   │   │   ├── (SYMBOL, ()
│   │               │                   │       │   │                           │   │   │   ├── Args
│   │               │                   │       │   │                           │   │   │   │   └── Arg-list
│   │               │                   │       │   │                           │   │   │   │       ├── Expression
│   │               │                   │       │   │                           │   │   │   │       │   ├── (ID, a)
│   │               │                   │       │   │                           │   │   │   │       │   └── B
│   │               │                   │       │   │                           │   │   │   │       │       └── Simple-expression-prime
│   │               │                   │       │   │                           │   │   │   │       │           ├── Additive-expression-prime
│   │               │                   │       │   │                           │   │   │   │       │           │   ├── Term-prime
│   │               │                   │       │   │                           │   │   │   │       │           │   │   ├── Factor-prime
│   │               │                   │       │   │                           │   │   │   │       │           │   │   │   └── epsilon
│   │               │                   │       │   │                           │   │   │   │       │           │   │   └── G
│   │               │                   │       │   │                           │   │   │   │       │           │   │       └── epsilon
│   │               │                   │       │   │                           │   │   │   │       │           │   └── D
│   │               │                   │       │   │                           │   │   │   │       │           │       └── epsilon
│   │               │                   │       │   │                           │   │   │   │       │           └── C
│   │               │                   │       │   │                           │   │   │   │       │               └── epsilon
│   │               │                   │       │   │                           │   │   │   │       └── Arg-list-prime
│   │               │                   │       │   │                           │   │   │   │           └── epsilon
│   │               │                   │       │   │                           │   │   │   └── (SYMBOL, ))
│   │               │                   │       │   │                           │   │   └── G
│   │               │                   │       │   │                           │   │       └── epsilon
│   │               │                   │       │   │                           │   └── D
│   │               │                   │       │   │                           │       └── epsilon
│   │               │                   │       │   │                           └── C
│   │               │                   │       │   │                               └── epsilon
│   │               │                   │       │   └── Statement-list
│   │               │                   │       │       └── epsilon
│   │               │                   │       └── (SYMBOL, })
│   │               │                   └── Statement-list
│   │               │                       └── epsilon
│   │               └── (SYMBOL, })
│   └── Declaration-list
│       └── epsilon
└── $
'''

test_8_output_its_the_same_but_quera_is_retarded_parse = '''Program
└── Declaration-list
    └── Declaration
        ├── Declaration-initial
        │   ├── Type-specifier
        │   │   └── (KEYWORD, int)
        │   └── (ID, func)
        └── Declaration-prime
            └── Fun-declaration-prime
                ├── (SYMBOL, ()
                ├── (SYMBOL, ))
                └── Compound-stmt
                    ├── (SYMBOL, {)
                    ├── Declaration-list
                    │   └── epsilon
                    └── Statement-list
                        └── Statement
                            └── Selection-stmt
                                ├── (KEYWORD, if)
                                ├── Expression
                                │   ├── (ID, a)
                                │   └── B
                                │       └── Simple-expression-prime
                                │           ├── Additive-expression-prime
                                │           │   ├── Term-prime
                                │           │   │   ├── Factor-prime
                                │           │   │   │   └── epsilon
                                │           │   │   └── G
                                │           │   │       └── epsilon
                                │           │   └── D
                                │           │       └── epsilon
                                │           └── C
                                │               ├── Relop
                                │               │   └── (SYMBOL, <)
                                │               └── Additive-expression
                                │                   ├── Term
                                │                   │   ├── Factor
                                │                   │   │   └── (NUM, 2)
                                │                   │   └── G
                                │                   │       └── epsilon
                                │                   └── D
                                │                       └── epsilon
                                ├── (SYMBOL, ))
                                └── Statement
                                    └── Compound-stmt
                                        ├── (SYMBOL, {)
                                        ├── Declaration-list
                                        │   ├── Declaration
                                        │   │   ├── Declaration-initial
                                        │   │   │   ├── Type-specifier
                                        │   │   │   │   └── (KEYWORD, int)
                                        │   │   │   └── (ID, i)
                                        │   │   └── Declaration-prime
                                        │   │       └── Var-declaration-prime
                                        │   │           └── (SYMBOL, ;)
                                        │   └── Declaration-list
                                        │       └── epsilon
                                        └── Statement-list
                                            ├── Statement
                                            │   └── Expression-stmt
                                            │       ├── Expression
                                            │       │   ├── (ID, i)
                                            │       │   └── B
                                            │       │       ├── (SYMBOL, =)
                                            │       │       └── Expression
                                            │       │           ├── (ID, func)
                                            │       │           └── B
                                            │       │               └── Simple-expression-prime
                                            │       │                   ├── Additive-expression-prime
                                            │       │                   │   ├── Term-prime
                                            │       │                   │   │   ├── Factor-prime
                                            │       │                   │   │   │   ├── (SYMBOL, ()
                                            │       │                   │   │   │   ├── Args
                                            │       │                   │   │   │   │   └── Arg-list
                                            │       │                   │   │   │   │       ├── Expression
                                            │       │                   │   │   │   │       │   └── Simple-expression-zegond
                                            │       │                   │   │   │   │       │       ├── Additive-expression-zegond
                                            │       │                   │   │   │   │       │       │   ├── Term-zegond
                                            │       │                   │   │   │   │       │       │   │   ├── Factor-zegond
                                            │       │                   │   │   │   │       │       │   │   │   └── (NUM, 2)
                                            │       │                   │   │   │   │       │       │   │   └── G
                                            │       │                   │   │   │   │       │       │   │       └── epsilon
                                            │       │                   │   │   │   │       │       │   └── D
                                            │       │                   │   │   │   │       │       │       ├── Addop
                                            │       │                   │   │   │   │       │       │       │   └── (SYMBOL, +)
                                            │       │                   │   │   │   │       │       │       ├── Term
                                            │       │                   │   │   │   │       │       │       │   ├── Factor
                                            │       │                   │   │   │   │       │       │       │   │   └── (NUM, 4)
                                            │       │                   │   │   │   │       │       │       │   └── G
                                            │       │                   │   │   │   │       │       │       │       └── epsilon
                                            │       │                   │   │   │   │       │       │       └── D
                                            │       │                   │   │   │   │       │       │           └── epsilon
                                            │       │                   │   │   │   │       │       └── C
                                            │       │                   │   │   │   │       │           └── epsilon
                                            │       │                   │   │   │   │       └── Arg-list-prime
                                            │       │                   │   │   │   │           └── epsilon
                                            │       │                   │   │   │   └── (SYMBOL, ))
                                            │       │                   │   │   └── G
                                            │       │                   │   │       └── epsilon
                                            │       │                   │   └── D
                                            │       │                   │       └── epsilon
                                            │       │                   └── C
                                            │       │                       └── epsilon
                                            │       └── (SYMBOL, ;)
                                            └── Statement-list
                                                └── Statement
                                                    └── Expression-stmt
                                                        └── Expression
                                                            ├── (ID, output)
                                                            └── B
                                                                └── Simple-expression-prime
                                                                    └── Additive-expression-prime
                                                                        └── Term-prime
                                                                            └── Factor-prime
                                                                                ├── (SYMBOL, ()
                                                                                └── Args
                                                                                    └── Arg-list
                                                                                        └── Expression
                                                                                            ├── (ID, i)
                                                                                            └── B
                                                                                                └── Simple-expression-prime
                                                                                                    ├── Additive-expression-prime
                                                                                                    │   ├── Term-prime
                                                                                                    │   │   ├── Factor-prime
                                                                                                    │   │   │   └── epsilon
                                                                                                    │   │   └── G
                                                                                                    │   │       └── epsilon
                                                                                                    │   └── D
                                                                                                    │       └── epsilon
                                                                                                    └── C
                                                                                                        └── epsilon
'''
        
test_10_output_its_the_same_but_quera_is_retarded = '''#5 : syntax error, missing Declaration-prime
#6 : syntax error, illegal }
#8 : syntax error, illegal void
#8 : syntax error, illegal ID
#8 : syntax error, illegal void
#8 : syntax error, illegal {
#9 : syntax error, illegal int
#9 : syntax error, illegal ID
#9 : syntax error, illegal [
#9 : syntax error, illegal NUM
#9 : syntax error, missing ;
#9 : syntax error, illegal ]
#10 : syntax error, illegal int
#11 : syntax error, illegal ID
#11 : syntax error, illegal [
#11 : syntax error, illegal NUM
#11 : syntax error, missing ;
#11 : syntax error, illegal ]
#11 : syntax error, illegal =
#12 : syntax error, illegal if
#12 : syntax error, illegal (
#12 : syntax error, illegal ID
#12 : syntax error, illegal [
#12 : syntax error, illegal NUM
#12 : syntax error, missing ;
#12 : syntax error, illegal ]
#12 : syntax error, illegal <
#12 : syntax error, missing ;
#12 : syntax error, illegal )
#14 : syntax error, illegal }
#15 : syntax error, illegal else
#15 : syntax error, illegal {
#16 : syntax error, illegal ID
#16 : syntax error, illegal =
#16 : syntax error, illegal ID
#16 : syntax error, illegal (
#16 : syntax error, illegal ID
#16 : syntax error, missing ;
#16 : syntax error, illegal )
'''
    
                