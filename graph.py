# %%
from collections import deque


class Graph:
    def __init__(self) -> None:
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex in self.adjacency_list:
            raise Exception("vertex already in graph")
        self.adjacency_list[vertex] = []
        return self

    def add_edge(self, vertex_1, vertex_2):
        if vertex_1 not in self.adjacency_list or vertex_2 not in self.adjacency_list:
            raise Exception("vertex does not exist")
        if vertex_2 not in self.adjacency_list[vertex_1]:
            self.adjacency_list[vertex_1].append(vertex_2)
        if vertex_1 not in self.adjacency_list[vertex_2]:
            self.adjacency_list[vertex_2].append(vertex_1)
        return self

    def remove_edge(self, vertex_1, vertex_2):
        if vertex_1 not in self.adjacency_list or vertex_2 not in self.adjacency_list:
            raise Exception("vertex does not exist")
        if vertex_2 not in self.adjacency_list[vertex_1]:
            self.adjacency_list[vertex_1].remove(vertex_2)
        if vertex_2 not in self.adjacency_list[vertex_1]:
            self.adjacency_list[vertex_2].remove(vertex_1)
        return self

    def remove_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            raise Exception("vertex not in graph")
        for neighbour in self.adjacency_list[vertex]:
            self.adjacency_list[neighbour].remove(vertex)
        self.adjacency_list.pop(vertex)
        return self

    def bft(self, start):  # Breath First Traversal
        q = deque([start])  # queue
        r = []  # result
        while q:
            cur = q.popleft()
            r.append(cur)
            for v in self.adjacency_list[cur]:
                if v not in q and v not in r:
                    q.append(v)
        return r


# %%
g = Graph()
vertices = list("ABCDEFGHIJK")
for v in vertices:
    g.add_vertex(v)
edges = "AB.AC.AD.BC.CD.CJ.DE.DI.EF.EG.FH.GH.GK.IJ.JK".split(".")
for e in edges:
    g.add_edge(e[0], e[1])

# g.adjacency_list
g.bft("E")
