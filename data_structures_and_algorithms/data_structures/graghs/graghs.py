from data_structures_and_algorithms.data_structures.stacks_and_queues.stacks_and_queues import *



class Graph:

    def __init__(self):
        self.adjacency_list = {}

    def add_node(self, value):
        node = Node(value)
        self.adjacency_list[node] = []
        return node

    def add_edge(self, start_node, end_node, weight=1):
        self.adjacency_list[start_node].append(end_node,weight)
        self.adjacency_list[end_node].append(start_node,weight)

    def get_nodes(self):
        return self.adjacency_list.keys()

    def get_neighbours(self, node):
        return self.adjacency_list[node]

    def size(self):
        return len(self.adjacency_list)


    def bfs(self, start_node):
        nodes = []  
        visited = set() 
        breadth = Queue() 
        breadth.enqueue(start_node) 
        visited.add(start_node) 
        while len(breadth)>0: 
            node = breadth.dequeue() 
            nodes.append(node) 
            for n in self.adjacency_list[node]: 
                if n not in visited: 
                    breadth.enqueue(n) 
                    visited.add(n) 
        return nodes

    def path(self,start_node,end_node):
        neighbours = []
        for i in self.get_neighbours(node1):
            neighbours.append(i[0])
        if node2  in arr:
            return True
        else:
            return False

