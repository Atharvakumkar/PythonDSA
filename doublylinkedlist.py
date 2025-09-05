class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.start = None
        self.last = None

    def insert(self, data):
        newNode = Node(data)
        if self.start is None:  
            self.start = newNode
            self.last = newNode
        else:
            self.last.next = newNode
            newNode.prev = self.last
            self.last = newNode

    def traverse(self):
        current = self.start
        while current:
            print(current.data, end=" ")
            current = current.next
        print()
        
    def traverse_reverse(self):
        current = self.last
        while current:
            print(current.data, end=" ")
            current = current.prev
        print()
        
    def insert_before(self, data, bef_data):
        newNode = Node(data)
        if self.start == None:
            print("List is empty")
        else:
            ptr = self.start
            while ptr:
                print(ptr.data)
                if ptr.data == bef_data:
                    break
                ptr = ptr.next
                
            if ptr == None:
                print("node is not present")
            else:
                newNode.next = ptr
                newNode.prev = ptr.prev
                if ptr.prev != None:
                    ptr.prev.next = newNode
                ptr.prev = newNode
            if newNode.prev == None:
                self.start = newNode
                
    def insert_after(self, data, aft_data):
        newNode = Node(data)
        if self.start == None:
            print("List is empty")
        else:
            ptr = self.last
            while ptr:
                print(ptr.data)
                if ptr.data == aft_data:
                    break
                ptr = ptr.prev
                
            if ptr == None:
                print("node is not present")
            else:
                newNode.prev = ptr              
                newNode.next = ptr.next
                if ptr.next != None:
                    ptr.next.prev = newNode
                ptr.next = newNode
            if newNode.next == None:
                self.last = newNode


doublelinkedlist = DoublyLinkedList()
doublelinkedlist.insert(10)
doublelinkedlist.insert(20)
doublelinkedlist.insert(30)
doublelinkedlist.insert(40)
doublelinkedlist.insert_before(50, 30)
doublelinkedlist.insert_after(80, 20)
doublelinkedlist.traverse()
