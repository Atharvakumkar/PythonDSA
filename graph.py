class GraphNode:
    def __init__(self, value=None):
        self.value = value
        self.status = 1  # Add status attribute here
        # You had 'node.data' in bfs, but your value is stored in 'value',
        # so let's keep using 'value'

class Graph:
    def __init__(self):
        self.nodelist = []
        self.matrix = []

    def addNodes(self):
        n = int(input("Enter how many nodes: "))
        
        # Initialize adjacency matrix with zeros
        for i in range(n):
            self.matrix.append([])
            for j in range(n):
                self.matrix[i].append(0)

            node = input(f"Enter node {i+1}: ")  # Your existing prompt
            graph = GraphNode(node)
            self.nodelist.append(graph)

    def display(self):
        print("Nodes:")
        for i, node in enumerate(self.nodelist):
            print(f"{i}: {node.value}")
        print("\nAdjacency Matrix:")
        for row in self.matrix:
            print(row)

    def bfs(self):
        templist = list()
        for i in range(len(self.nodelist)):
            self.nodelist[i].status = 1
        templist.append(self.nodelist[0])
        self.nodelist[0].status = 2
        traversal = ""
        while len(templist) != 0:
            node = templist[0]
            templist.remove(node)
            traversal += node.value  # changed from node.data to node.value
            node.status = 3
            n = self.nodelist.index(node)
            if n >= 0:
                for t in range(0, len(self.nodelist)):
                    if self.matrix[n][t] == 1 and self.nodelist[t].status == 1:
                        templist.append(self.nodelist[t])
                        self.nodelist[t].status = 2
        print("BFS Traversal:", traversal)

# Usage
g1 = Graph()
g1.addNodes()
g1.display()
g1.bfs()
