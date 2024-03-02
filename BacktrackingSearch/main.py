from collections import defaultdict
from backtrackingsearch import *
from bfs import *

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.explored_nodes = []


    def add_edge(self, n1, n2, cost =1):
        self.graph[n1].append((n2, cost))

    def get_cost(self, n1, n2):
        for node, cost in self.graph[n1]:
            if node == n2:
                return cost

    def actions(self, n1):
        return self.graph[n1]





graph = Graph()

graph.add_edge('A', 'B')
graph.add_edge('B', 'C')
graph.add_edge('B', 'D')
graph.add_edge('D', 'E')
graph.add_edge('A', 'E', 1)
graph.add_edge('E', 'F', 2)
graph.add_edge('F', 'I', 3)
graph.add_edge('A', 'G', 2)
graph.add_edge('G', 'H', 1)
graph.add_edge('H', 'I', 7)




print(backtrackingsearch('A', 'I', graph))

print(bfs('A', 'F', graph))