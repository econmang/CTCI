# You are given a list of projects and a list of dependencies (which is a list of pairs of projects, where the second project is dependent on the first project).
# All of a project's dependencies must be built before the project is. Find a build order that will allow the projects to be built.
# If there is no valid build order, return an error.

class Graph:
    def __init__(self):
        self.vertices = []
        self.edges = {}

    def add_edge(self, project, dependency):
        if self.edges[project] is None:
            self.edges[project] = []
        self.edges[project].append(dependency)

    @staticmethod
    def build_graph(projects, dependencies):
        graph = Graph()
        for project in projects:
            graph.vertices.append(project)
            graph.edges[project] = []
        for dependency in dependencies:
            graph.add_edge(dependency[1], dependency[0])
        return graph

    def get_builds_with_no_dependencies(self, projects, dependencies):
        builds = []
        for project in projects:
            if len(self.edges[project]) == 0:
                builds.append(project)
                projects.remove(project)
                for key in dependencies.keys():
                    if project in dependencies[key]:
                        dependencies[key].remove(project)
        return builds

    def get_build_order(self):
        projects = self.vertices.copy()
        dependencies = self.edges.copy()
        build_order = []
        while len(projects) > 0:
            new_builds = self.get_builds_with_no_dependencies(projects, dependencies)
            if new_builds == []:
                Exception("No valid builds")
            build_order += new_builds
        return build_order

if __name__ == "__main__":
    projects = ['a', 'b', 'c', 'd', 'e', 'f']
    dependencies = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]
    print("PROJECT:",projects)
    print("DEPS:",dependencies)
    proj_graph = Graph.build_graph(projects, dependencies)
    print("VERTICES:", proj_graph.vertices)
    print("EDGES:", proj_graph.edges)
    print("BUILD ORDER:",proj_graph.get_build_order())
