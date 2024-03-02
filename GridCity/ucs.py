
def ucs(grid, start, goal):
    frontier = []
    visited = set()


    frontier.append((start, 0, [(start.x, start.y)]))

    while frontier:
        current_element = min(frontier, key=lambda x: x[1])
        frontier.remove(current_element)
        # print(current_element)
        state_object, cost_data, path = current_element
        visited.add((state_object.x, state_object.y))

        if state_object.x == goal.x and state_object.y == goal.y:
            # print(visited)
            print(cost_data)
            print(path)
            return path, visited
        # print(state_object.x, state_object.y)


        # print(state_object.x, state_object.y)
        actions = grid.actions(state_object)

        for action in actions:
            neighbour = grid.Succ(state_object, action)
            find = (neighbour.x, neighbour.y)
            if find not in visited:
                path1 = path + [(neighbour.x, neighbour.y)]
                frontier.append((neighbour, cost_data + grid.cost(state_object), path1))



