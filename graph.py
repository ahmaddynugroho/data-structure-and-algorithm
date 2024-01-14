# %%
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
        if vertex_2 not in self.adjacency_list[vertex_1]:
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


# %%
g = Graph()

g.add_vertex("A")
g.add_vertex("B")

g.add_edge("A", "B")
g.add_edge("B", "A")

g.remove_vertex("B")
g.adjacency_list
