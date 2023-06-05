from codegen.memory import Memory
from codegen.semantic_stack import semantic_stack
from codegen.program_block import ProgramBlock


class CodeGenerator:
    def __init__(self):
        self.semantic_stack = semantic_stack()
        self.memory = Memory()
        self.program_block = ProgramBlock()
        self.actions = ['PNUM', 'PUSH_TYPE', 'PID', 'VAR_DEC', 'ASSIGN', 'PUSHOP', 'ADD_SUB']
    
    def run(self, type, current_token):
        #print("Code Gen executed")
        #print(f'type: {type}, current_token: {current_token}')
        if type == 'PNUM':
            number = current_token
            t = self.memory.get_temp()
            self.program_block.add_code('ASSIGN', f'#{number}', f'{t}')
            self.semantic_stack.push(t)
        elif type == 'PUSH_TYPE':
            data_type = current_token
            self.semantic_stack.push(data_type)
        elif type == 'PID':
            id = current_token
            addr = self.memory.find_addr(id)
            id = addr if addr is not None else id
            self.semantic_stack.push(id)
        elif type == 'VAR_DEC':
            data_type = self.semantic_stack.get_top(1)   
            id = self.semantic_stack.get_top()
            self.memory.add_var(id)
            id = self.memory.find_addr(id)
            self.semantic_stack.pop(2)
            self.program_block.add_code('ASSIGN', f'#0', f'{id}')  
        elif type == 'ASSIGN':
            to_id = self.semantic_stack.get_top(1)
            from_id = self.semantic_stack.get_top()
            self.semantic_stack.pop(2)
            self.program_block.add_code('ASSIGN', f'{from_id}', f'{to_id}')      
        elif type == 'PUSHOP':
            operation = current_token
            if operation == "+":
                operation = 'ADD'
            elif operation == '-':
                operation = 'SUB'
            else:
                print(f'wtf is this: {operation}')
            self.semantic_stack.push(operation)
        elif type == 'ADD_SUB':
            id1 = self.semantic_stack.get_top()
            id2 = self.semantic_stack.get_top(2)
            operation = self.semantic_stack.get_top(1)
            self.semantic_stack.pop(3)
            t = self.memory.get_temp()
            self.program_block.add_code(operation, f'{id1}', f'{id2}', f'{t}')  
            self.semantic_stack.push(t)
        
        #print(f'stack: {self.semantic_stack.stack}')
        #print(f'memory: {self.memory.Data}')
