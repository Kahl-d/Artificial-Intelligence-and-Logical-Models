
def backtrackingsearch(start, end, graph, path='', total_cost= 0):
    path1 = path
    if start == end:
        print(path1, " with cost", total_cost)

    list = graph.actions(start)


    for node, cost in list:
        found = 0
        for enode, ecost in graph.explored_nodes:
            if enode == node and ecost == cost:
                found = 1

        if found == 0:
            graph.explored_nodes.append((node, graph.get_cost(start, node)))

            # print(graph.explored_nodes)

        backtrackingsearch(node, end, graph, path1 + node, total_cost + graph.get_cost(start, node))

    return True