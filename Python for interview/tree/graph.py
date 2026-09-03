class Graph:

    def __init__(self):
        self.adjacency_list = {}

    # add vertex (node) 
    def add_vertex(self, vertex):

        # Agar vertex pehle se exist nahi karta
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    # add edge b/w node/vertex
    def add_edge(self, source_vertex, destination_vertex):

        # Agar source vertex exist nahi karta to add karo
        if source_vertex not in self.adjacency_list:
            self.add_vertex(source_vertex)

        # Agar destination vertex exist nahi karta to add karo
        if destination_vertex not in self.adjacency_list:
            self.add_vertex(destination_vertex)

        # Source ko destination se connect karo
        self.adjacency_list[source_vertex].append(destination_vertex)

        # Destination ko source se connect karo
        self.adjacency_list[destination_vertex].append(source_vertex)

    # Graph print karo
    def display_graph(self):

        for vertex in self.adjacency_list:
            print(vertex, "->", self.adjacency_list[vertex])


# Graph object banao
graph = Graph()

# Vertices add karo
graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)
graph.add_vertex(4)

# Edges add karo
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)
graph.add_edge(3, 4)

# Graph display karo
graph.display_graph()