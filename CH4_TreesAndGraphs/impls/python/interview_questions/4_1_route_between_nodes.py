# Problem 4.1
# Given a directed graph and two nodes (S and E), design an algorithm to find out whether there is a route from S to E.

class Graph:
    def __init__(self, vertices: list[str], edges: dict):
        self.vertices = vertices
        self.edges = edges

    def add_vert(self, vertex: str):
        self.vertices.append(vertex)

    def add_edges(self, vertex: str, vertex_edges: list[str]):
        self.edges[vertex] = vertex_edges

    def path_exists(self, start: str, end: str, processed: list[str]):
        for neighbor in self.edges[start]:
            if neighbor not in processed and neighbor == end:
                return True
            else:
                processed.append(neighbor)
                return self.path_exists(neighbor, end, processed)
        return False

if __name__ == "__main__":
    g =  Graph([], {})
    g.add_vert("start")
    g.add_vert("a")
    g.add_vert("b")
    g.add_vert("c")
    g.add_vert("d")
    g.add_vert("e")
    g.add_vert("q")
    g.add_edges("start", ["a","b"])
    g.add_edges("a",["b", "c", "d"])
    g.add_edges("b",["c","e"])
    g.add_edges("c",["d"])
    g.add_edges("d",["e"])
    g.add_edges("e",[])
    processed = []
    print(g.path_exists("start","q", processed))
    processed = []
    print(g.path_exists("start","e", processed))
