class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None  

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top  
        self.top = new_node       

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        popped_node = self.top
        self.top = self.top.next  
        return popped_node.data

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.top.data

    def traverse(self):
        elements = []
        current = self.top
        while current:
            elements.append(current.data)
            current = current.next
        return elements  



stack = Stack()
stack.push(5)
stack.push(10)
stack.push(15)

print("Stack elements:", stack.traverse())  
print("Peek:", stack.peek())                 
print("Pop:", stack.pop())                   
print("Stack after pop:", stack.traverse())
print("stack lemenets ,",stack.push(100)) 
