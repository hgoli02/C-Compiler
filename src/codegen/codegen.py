from memory import Memory
from semantic_stack import semantic_stack
from program_block import ProgramBlock


class CodeGenerator:
    def __init__(self):
        self.semantic_stack = semantic_stack()
        self.memory = Memory()
        self.program_block = ProgramBlock()
        self.actions = []
        
    
    def run(self, type):
        if type == 'PTEMP':
            number = get_input()
            t = self.memory.get_temp()
            self.program_block.add_code('ASSIGN', f'#{number}', f'{t}')
            self.semantic_stack.push(t)
        elif type == 'PUSH_TYPE':
            data_type = get_input()
            self.semantic_stack.push(data_type)
        elif type == 'PID':
            id = get_input()
            self.semantic_stack.push(id)
        elif type == 'VAR_DEC':
            data_type = self.semantic_stack.get_top(1)   
            id = self.semantic_stack.get_top()
            self.semantic_stack.pop(2)
            self.program_block.add_code('ASSIGN', f'#0', f'{id}')  
        elif type == 'ASSIGN':
            to_id = self.semantic_stack.top(1)
            from_id = self.semantic_stack.top()
            self.semantic_stack.pop(2)
            self.program_block.add_code('ASSIGN', f'{from_id}', f'{to_id}')      
        elif type == 'PUSHOP':
            operation = get_input()
            self.semantic_stack.push(operation)
        
    