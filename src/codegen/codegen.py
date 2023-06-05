from codegen.memory import Memory
from codegen.semantic_stack import semantic_stack
from codegen.program_block import ProgramBlock


class CodeGenerator:
    def __init__(self):
        self.ss = semantic_stack()
        self.pb = ProgramBlock()
        self.memory = Memory()
        self.actions = ['PNUM', 'PUSH_TYPE', 'PID', 'VAR_DEC', 'ASSIGN', 'PUSHOP', 'ADD_SUB', 'OUTPUT', 'MUL']
    
    def run(self, type, current_token):
        #print("Code Gen executed")
        #print(f'type: {type}, current_token: {current_token}')
        if type == 'PNUM':
            number = current_token
            t = self.memory.get_temp()
            self.pb.add_code('ASSIGN', f'#{number}', f'{t}')
            self.ss.push(t)
        elif type == 'PUSH_TYPE':
            data_type = current_token
            self.ss.push(data_type)
        elif type == 'PID':
            id = current_token
            self.ss.push(id)
            addr = self.memory.find_addr(id)
            id = addr if addr is not None else id
            self.semantic_stack.push(id)
        elif type == 'VAR_DEC':
            data_type = self.ss.get_top(1)   
            id = self.ss.get_top()
            self.memory.add_var(id)
            self.ss.pop(2)
            self.pb.add_code('ASSIGN', f'#0', f'{id}')  
            id = self.memory.find_addr(id)
            self.semantic_stack.pop(2)
            self.program_block.add_code('ASSIGN', f'#0', f'{id}')  
        elif type == 'ASSIGN':
            to_id = self.ss.get_top(1)
            from_id = self.ss.get_top()
            self.ss.pop(2)
            self.pb.add_code('ASSIGN', f'{from_id}', f'{to_id}')      
        elif type == 'PUSHOP':
            operation = current_token
            self.ss.push(operation)
            if operation == "+":
                operation = 'ADD'
            elif operation == '-':
                operation = 'SUB'
            else:
                print(f'wtf is this: {operation}')
        elif type == 'ADD_SUB':
            id1 = self.ss.get_top()
            id2 = self.ss.get_top(2)
            operation = self.ss.get_top(1)
            self.ss.pop(3)
            t = self.memory.get_temp()
            self.pb.add_code(operation, f'{id1}', f'{id2}', f'{t}')  
        elif type == 'MUL':
            id1 = self.ss.get_top()
            id2 = self.ss.get_top(1)
            t = self.memory.get_temp()
            self.pb.add_code('MUL', f'{id1}', f'{id2}', f'{t}')
        elif type == 'OUTPUT':
            t = self.ss.get_top()
            self.ss.pop(1)
            self.pb.add_code('PRINT', f'{t}')
        
        print(f'stack: {self.ss.stack}')
        print(f'memory: {self.memory.Data}')
