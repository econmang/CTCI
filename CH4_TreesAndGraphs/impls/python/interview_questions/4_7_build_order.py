# You are given a list of projects and a list of dependencies (which is a list of pairs of projects, where the second project is dependent on the first project).
# All of a project's dependencies must be built before the project is. Find a build order that will allow the projects to be built.
# If there is no valid build order, return an error.

class Graph:
    def __init__(self):
        self.vertices = []
        self.edges = {}

projects = ['a', 'b', 'c', 'd', 'e', 'f']
dependencies = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]

def build_graph(projects, dependencies):
    graph = Graph()
    for project in projects:
        graph.vertices.append(project)
        graph.edges[project] = []
    for dependency in dependencies:
        graph.edges[dependency[1]].append(dependency[0])
    return graph

def get_build_order(graph):
    build_order = []
    for key in graph.edges:
        if len(graph.edges[key]) == 0:
            if key not in build_order:
                build_order.append(key)
        else:
            for dependency in graph.edges[key]:
                if dependency not in build_order:
                    build_order.append(dependency)
    for project in graph.vertices:
        if project not in build_order:
            build_order.append(project)
    return build_order

proj_graph = build_graph(projects, dependencies)
print(get_build_order(proj_graph))
