from collections import deque #Double-ended queue

class Graph:
    def __init__(self, graph: dict):
        self.graph = graph

    def add_node(self, node: str, neighbors: list[str]):
        self.graph[node] = neighbors

    def bfs(self, start_node: str, end_node: str):
        search_queue = deque()
        search_queue += self.graph[start_node]
        visited: list[str] = []
        while search_queue:
            curr_node = search_queue.popleft()
            if not curr_node in visited:
                if curr_node == end_node:
                    print(f"Path to {end_node} was found!")
                    return True
                else:
                    search_queue += self.graph[curr_node]
                    visited.append(curr_node)
        print(f"No path to {end_node} was found!")
        return False

if __name__ == "__main__":
    graph_one = Graph({})
    graph_one.add_node("you", ["alice", "bob", "claire"])
    graph_one.add_node("bob", ["anuj", "peggy"])
    graph_one.add_node("alice",  ["peggy"])
    graph_one.add_node("claire", ["thom","jonny"])
    graph_one.add_node("anuj",  [])
    graph_one.add_node("peggy", ["you"])
    graph_one.add_node("thom",  [])
    graph_one.add_node("jonny", [])

    print(graph_one.bfs("you", "anuj"))
    print(graph_one.bfs("you", "thom"))
    print(graph_one.bfs("you", "carl"))
