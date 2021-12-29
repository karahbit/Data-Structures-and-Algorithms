def create_graph(projects, dependencies):
    project_graph = {}
    for project in projects:
        project_graph[project] = []
    for pairs in dependencies:
        project_graph[pairs[0]].append(pairs[1])
    return project_graph


graph = create_graph([0, 1, 2, 3, 4, 5], [
                     (0, 3), (5, 1), (1, 3), (5, 0), (3, 2)])


def is_cyclic(graph):

    def is_cyclic_util(graph, visited, node, top_order):
        if visited[node] == 1:
            return True

        visited[node] = 1
        for neighbor in graph[node]:
            if visited[neighbor] != 2 and is_cyclic_util(graph, visited, neighbor, top_order):
                return True

        visited[node] = 2
        top_order.append(node)
        return False

    visited = [0] * len(list(graph))  # same as [0] * numCourses
    top_order = []

    for node in graph:
        if not visited[node]:
            if is_cyclic_util(graph, visited, node, top_order):
                return False

    print(top_order[::-1])
    return True


is_cyclic(graph)
