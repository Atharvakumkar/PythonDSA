class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getInfo(self):
        print("Node Details: " + str(self.data))


class NodeList:
    def __init__(self):
        self.start = None
        self.last = None

    def appendLast(self, data):
        newnode = Node(data)
        if self.start is None:
            self.start = newnode
            self.last = newnode
        else:
            self.last.next = newnode
            self.last = newnode

    def traverse(self):
        if self.start is None:
            print("The list is empty")
        else:
            ptr = self.start
            while ptr is not None:
                ptr.getInfo()
                ptr = ptr.next


print("Starting the linked list test...")

lst = NodeList()
lst.appendLast(10)
lst.appendLast(20)
lst.appendLast(30)
lst.traverse()
