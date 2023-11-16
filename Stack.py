class Stack:
    def __init__(self):
        self.stack = []

    def add(self, dataval):
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False
        
    def peek(self):
        return self.stack[-1]
    
    def remove(self):
        if len(self.stack) <= 0:
            print("Stack is empty")
        else:
            return self.stack.pop()    
    
AStack = Stack()
AStack.add("Mon")
AStack.add("Tue")

AStack.peek()
print(AStack.peek())
