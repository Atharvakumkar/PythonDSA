class node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def showInfo(self):
        print("Brace: ", self.b)


class MyStack:
    def __init__(self):
        self.top = None

    def push(self, newnode):
        if self.top == None:
            self.top = newnode
        else:
            newnode.next = self.top
            self.top = newnode

    def pop(self):
        if self.top == None:
            return None
        else:
            s = self.top.data
            self.top = self.top.next
            return s

    def isEmpty(self):
        if (self.top == None):
            return True
        else:
            return False

    def peek(self):
        if (self.top == None):
            return None
        else:
            return self.top.data


def BraceStacks():
    mystack = MyStack()
    expr = input("Enter Arithmatic Equation: ")

    for i in expr:
        if i in "{[(":
            # print(i)
            bnd = node(i)
            mystack.push(bnd)
            print("pushed ", bnd.data)
        elif i in "]})":
            p = mystack.peek()
            print("Peek Value", p)
            x = mystack.pop()
            print("popped ", x)

            if (i == '(' and x != ')') or (i == '{' and x != '}') or (i == '[' and x != ']'):
                return False
            if (x != p):
                return False

    return mystack.isEmpty()


if BraceStacks():
    print('Delimeters are Balanced')
else:
    print('Imbalanced')