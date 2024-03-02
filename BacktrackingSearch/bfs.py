def bfs(start, goal, graph):
    visited = set()
    queue = [start]

    while len(queue) > 0:
        print(queue)
        vertex = queue.pop(0)
        if vertex == goal:
            return True
        actions = graph.actions(vertex)
        for action, cost in actions:
            if action not in visited:
                visited.add(action)
                queue.append(action)
