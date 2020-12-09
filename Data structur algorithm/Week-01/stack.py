class Stack:
    def __init__(self, max_size): #initialize a stack of max_size
        self.top_pointer = -1 #Keep track of top element using this
        self.stack = [None for x in range(max_size)]  #create a list of max_size
    
    def push(self, new_element):
        self.top_pointer = self.top_pointer + 1 #Move the pointer
        self.stack[self.top_pointer] = new_element #Add the new_element to the top
    
    def pop(self):
        last_element = self.stack[self.top_pointer]
        self.top_pointer = self.top_pointer - 1 #Move the pointer
        return last_element #Pop the last element
    
    def peek(self):
        return self.stack[self.top_pointer]

    def is_empty(self):
        return self.top_pointer == -1

def check_string(s):
    test_stack = Stack(len(s))
    if s == "":
        return True
    for i in s:
        if i=="(" or i=="{":
            test_stack.push(i)
        else:
            if test_stack.is_empty():
                return False
            elif i=="}" and test_stack.peek()!="{":
                return False
            elif i=="(" and test_stack.peek()!=")":
                return False
            test_stack.pop()
    if test_stack.is_empty():
        return True
    else:
        return False

        
print(check_string("(){}"))
print(check_string("()("))
print("ok")