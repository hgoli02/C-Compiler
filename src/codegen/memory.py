"""
The Data Structure for the memory management
it should support the following operations:
    1. get_temp() : allocate a new memory block
    2. find_addr(input) : find address of the input

"""
from collections import defaultdict
class Memory():

    #DATA: {scope: {a:123, b:245}, scope2: {...} }
    def __init__(self):
        self.Data = defaultdict(dict)
        self.DataType = defaultdict(dict)
        self.functions = defaultdict(str)
        self.data_pointer = 100
        self.temp_pointer = 500
        self.param_pointer = 1000
        

    def get_temp(self):
        self.temp_pointer += 4
        return self.temp_pointer - 4

    def get_param(self):
        self.param_pointer += 4
        return self.param_pointer - 4

    def reset_param(self):
        self.param_pointer = 1000

    def find_addr(self, input, func):
        if input in self.Data[func]:
            return self.Data[func][input]
        elif input in self.Data['global']:
             return self.Data['global'][input]           
        else:
            #Throw an error
            # print("Error: variable not found")
            return None
    
    def find_type(self, input, func):
        if input in self.DataType[func]:
            return self.DataType[func][input]
        elif input in self.DataType['global']:
            return self.DataType['global'][input]
        else: 
            return None

    def add_var(self, input, func):
        if input in self.Data:
            #Throw an error
            print("Error: variable already exists")
        else:
            self.Data[func][input] = self.data_pointer
            self.DataType[func][input] = 'var'
            self.data_pointer += 4
    
    def find_var(self, input, func):
        #loop through memroy to find the variable
        for key, value in self.Data[func].items():
            if value == input:
                return key
        for key, value in self.Data['global'].items():
            if value == input:
                return key
        return None
        

    def add_array(self, input, size, func):
        if input in self.Data:
            #Throw an error
            print("Error: variable already exists")
        else:
            self.Data[func][input] = self.data_pointer
            self.DataType[func][input] = 'array'
            self.data_pointer += 4*size
    
    def add_function(self, input, line):
        self.functions[input] = line
    
    def get_function_line(self, input):
        return self.functions[input]