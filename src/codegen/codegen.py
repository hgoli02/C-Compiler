from codegen.memory import Memory
from codegen.semantic_stack import semantic_stack
from codegen.program_block import ProgramBlock


class CodeGenerator:
    def __init__(self):
        self.ss = semantic_stack()
        self.pb = ProgramBlock()
        self.memory = Memory()
        self.loop_stack = []
        self.semantic_errors = []
        self.actions = ['PNUM', 'PUSH_TYPE', 'PID', 'VAR_DEC', 'ARR_ACC', 'LABEL', 'UNTIL', 'BREAK', 'PID_DEC', 'FUN_DEC',
         'ASSIGN', 'PUSHOP', 'ADD_SUB', 'OUTPUT', 'MUL', 'CMP', 'ARRAY_DEC', 'SAVE', 'JPF_SAVE', 'JP', 'PUSH_ASSIGN','BREAK','ARR_DEC_PARAM', 'RETURN']
    
    def run(self, type, current_token, current_line):
        #print("Code Gen executed")
        print(f'type: {type}, current_token: {current_token}')
        if type == 'PNUM':
            number = current_token
            t = self.memory.get_temp()
            self.pb.add_code('ASSIGN', f'#{number}', f'{t}')
            self.ss.push(t)
        elif type == 'PUSH_TYPE':
            data_type = current_token
            self.ss.push(data_type)
        elif type == 'PID':
            if self.memory.find_addr(current_token) is None:
                self.semantic_errors.append(f'#{current_line}: Semantic Error! \'{current_token}\' is not defined.')
                self.ss.push("SEMANTIC PID")
                return
            id = current_token
            addr = self.memory.find_addr(id)
            self.ss.push(addr)
        elif type == 'PID_DEC':
            id = current_token
            addr = self.memory.find_addr(id)
            id = addr if addr is not None else id
            self.ss.push(id)
        elif type == 'VAR_DEC':
            data_type = self.ss.get_top(1)
            ## soomantic
            if data_type != 'int':
                self.semantic_errors.append(f'#{current_line}: Semantic Error! Illegal type of void for \'{self.ss.get_top()}\'.')
                self.ss.pop(1)
                return                               
            ## end soomantic
            id = self.ss.get_top()
            self.memory.add_var(id)
            id = self.memory.find_addr(id)
            self.ss.pop(2)
            self.pb.add_code('ASSIGN', f'#0', f'{id}')  
        elif type == 'FUN_DEC':
            data_type = self.ss.get_top(1)
            ## soomantic
            if data_type != 'int':
                self.ss.pop(1)
                return                               
            ## end soomantic
            id = self.ss.get_top()
            self.memory.add_var(id)
            id = self.memory.find_addr(id)
            self.ss.pop(2)
            self.pb.add_code('ASSIGN', f'#0', f'{id}')  
        elif type == 'ARRAY_DEC':
            data_type = self.ss.get_top(1)   
            id = self.ss.get_top()
            self.memory.add_array(id, int(current_token))
            id = self.memory.find_addr(id)
            self.ss.pop(2)
            self.pb.add_code('ASSIGN', f'#0', f'{id}') 
        elif type == 'ARR_DEC_PARAM':
            data_type = self.ss.get_top(1)   
            id = self.ss.get_top()
            self.memory.add_array(id, 1)
            self.ss.pop(2)
        elif type == 'ASSIGN':
            to_id = self.ss.get_top(2)
            op = self.ss.get_top(3)
            from_id = self.ss.get_top()
            self.ss.pop(3)
            self.pb.add_code('ASSIGN', f'{from_id}', f'{to_id}') 
            if op == '=':
                self.ss.push(from_id)
        elif type == 'PUSH_ASSIGN':
            self.ss.push(current_token)     
        elif type == 'PUSHOP':
            operation = current_token
            if operation == "+":
                operation = 'ADD'
            elif operation == '-':
                operation = 'SUB'
            elif operation == '<':
                operation = 'LT'
            elif operation == '==':
                operation = 'EQ'
            else:
                print(f'wtf is this: {operation}')
            self.ss.push(operation)
        elif type == 'ADD_SUB':
            id1 = self.ss.get_top(2)
            operation = self.ss.get_top(1)
            id2 = self.ss.get_top()
            self.ss.pop(3)
            if self.memory.find_type(self.memory.find_var(id1)) == 'array':
                self.semantic_errors.append(f'#{current_line}: Semantic Error! Type mismatch in operands, Got array instead of int.')
                self.ss.push("SEMANTIC SUB_ADD")
                return
            if self.memory.find_type(self.memory.find_var(id2)) == 'array':
                self.semantic_errors.append(f'#{current_line}: Semantic Error! Type mismatch in operands, Got array instead of int.')
                self.ss.push("SEMANTIC SUB_ADD")
                return
            t = self.memory.get_temp()
            self.pb.add_code(operation, f'{id1}', f'{id2}', f'{t}')  
            self.ss.push(t)
        elif type == 'MUL':
            id1 = self.ss.get_top()
            id2 = self.ss.get_top(1)
            self.ss.pop(2)
            t = self.memory.get_temp()
            self.pb.add_code('MULT', f'{id1}', f'{id2}', f'{t}')
            self.ss.push(t)
        elif type == 'CMP':
            id1 = self.ss.get_top(2)
            id2 = self.ss.get_top(0)
            operation = self.ss.get_top(1)
            self.ss.pop(3)
            t = self.memory.get_temp()
            self.pb.add_code(operation, f'{id1}', f'{id2}', f'{t}')
            self.ss.push(t)
        elif type == 'ARR_ACC':
            symbol = self.ss.get_top(1)
            idx = self.ss.get_top()
            self.ss.pop(2)
            t = self.memory.get_temp()
            self.pb.add_code("MULT", f'{idx}', f'#4', f'{t}')
            self.pb.add_code("ADD", f'{t}', f'#{symbol}', f'{t}')
            self.ss.push(f'@{t}')
        elif type == 'LABEL':
            idx = self.pb.get_line()
            self.ss.push(idx)
        elif type == 'BREAK':
            idx = self.pb.add_empty_block()
            self.loop_stack.append(idx)
        elif type == 'UNTIL':
            cond = self.ss.get_top()
            idx = self.ss.get_top(1)
            self.ss.pop(2)
            self.pb.add_code('JPF', f'{cond}', f'{idx}')
            if len(self.loop_stack) > 0:
                idx = self.loop_stack.pop()
                self.pb.set_instruction(idx,'JP', f'{self.pb.get_line()}')
        elif type == 'SAVE':
            idx = self.pb.add_empty_block()
            self.ss.push(idx)
        elif type == 'JPF_SAVE': #SAVE #JPF
            idx = self.ss.get_top()
            cond = self.ss.get_top(1)
            self.ss.pop(2)
            i = self.pb.get_line()
            self.ss.push(i)
            self.pb.add_empty_block()
            self.pb.set_instruction(idx, 'JPF', f'{cond}', f'{i + 1}')
        elif type == 'JP':
            idx = self.ss.get_top()
            i = self.pb.get_line()
            self.pb.set_instruction(idx, 'JP', f'{i}')
            self.ss.pop()
        elif type == 'OUTPUT':
            t = self.ss.get_top()
            self.ss.pop(1)
            self.pb.add_code('PRINT', f'{t}')
        elif type == 'RETURN':
            t = self.ss.pop() #TODO: NEXT PHASE
        
        print(f'stack: {self.ss.stack}')
        self.pb.print_block()
        print("************************************"*10)

    def get_printed_code(self):
        out_str = ''
        for i, line in enumerate(self.pb.codes):
            if line is None:
                break
            out_str += f'{i}\t{line}\n'
        return out_str
