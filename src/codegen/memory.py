"""
The Data Structure for the memory management
it should support the following operations:
    1. get_temp() : allocate a new memory block
    2. find_addr(input) : find address of the input

"""

class Memory():
    
    def __init__(self):
        self.Data = {}
        self.DataType = {}
        self.data_pointer = 100
        self.temp_pointer = 500
        

    def get_temp(self):
        self.temp_pointer += 4
        return self.temp_pointer - 4

    def find_addr(self, input):
        if input in self.Data:
            return self.Data[input]
        else:
            #Throw an error
            # print("Error: variable not found")
            return None
    
    def find_type(self, input):
        if input in self.DataType:
            return self.DataType[input]
        else: 
            return None

    def add_var(self, input):
        if input in self.Data:
            #Throw an error
            print("Error: variable already exists")
        else:
            self.Data[input] = self.data_pointer
            self.DataType[input] = 'var'
            self.data_pointer += 4
    
    def find_var(self, input):
        #loop through memroy to find the variable
        for key, value in self.Data.items():
            if value == input:
                return key
        return None
        

    def add_array(self, input, size):
        if input in self.Data:
            #Throw an error
            print("Error: variable already exists")
        else:
            self.Data[input] = self.data_pointer
            self.DataType[input] = 'array'
            self.data_pointer += 4*size
    