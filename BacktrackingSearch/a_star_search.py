adjaceny_list = {
    "arad": [("zerind", 75), ("timisoara", 118), ("sibiu", 140)],
    "zerind": [("arad", 75), ("oradea", 71)],
    "oradea": [("sibiu", 151), ("zerind", 71)],
    "sibiu": [("fagaras", 99), ("rimnicu vilcea", 80), ("arad", 140), ("oradea", 151)],
    "fagaras": [("sibiu", 99), ("bucharest", 211)],
    "rimnicu vilcea": [("pitesti", 97), ("craiova", 146), ("sibiu", 80)],
    "pitesti": [("rimnicu vilcea", 97), ("bucharest", 101), ("craiova", 138)],
    "bucharest": [("fagaras", 211), ("giurgiu", 90), ("pitesti", 101), ("urziceni", 85)],
    "urziceni": [("bucharest", 85), ("hirsova", 98), ("vaslui", 142)],
    "hirsova": [("eforie", 86), ("urziceni", 98)],
    "vaslui": [('lasi', 92), ('urziceni', 142)],
    "lasi": [("vaslui", 92), ("neamt", 87)],
    "neamt": [("lasi", 92)],
    "timisoara": [("lugoj", 111), ('arad', 118)],
    "lugoj": [("mehadia", 70), ("timisoara", 111)],
    "mehadia": [("lugoj", 70), ("dobreta", 75)],
    "dobreta": [("craiova", 120), ("mehadia", 75)],
    "craiova": [("dobreta", 120), ("rimnicu vilcea", 146), ("pitesti", 138)],
    "giurgiu": [("bucharest", 90)],
    "eforei": [("hirsova", 86)]
}


heuristic_data= {
    "arad": 366,
    "bucharest": 0,
    "craiova": 160,
    "dobreta": 242,
    "eforei": 161,
    "fagaras": 178,
    "giurgiu": 77,
    "hirsova": 151,
    "lasi": 226,
    "lugoj": 244,
    "mehadia": 241,
    "neamt": 234,
    "oradea": 380,
    "pitesti": 98,
    "rimnicu vilcea": 193,
    "sibiu": 253,
    "timisoara": 329,
    "urziceni": 80,
    "vaslui": 199,
    "zerind": 374,
}



def a_star_search(start, goal):
    frontier = []
    frontier.append((start, 0, heuristic_data[start], []))
    visited = set()

    while frontier:
        current_node = min(frontier, key=lambda x: x[1] + x[2])

        if current_node[0] == goal:
            current_node[3].append(current_node[0])
            print(current_node[3])
            return True

        if current_node[0] not in visited:
            visited.add(current_node[0])
            new_path = current_node[3] + [current_node[0]]
            frontier.remove(current_node)

            for neighbor in adjaceny_list[current_node[0]]:
                if neighbor not in visited:

                    frontier.append((neighbor[0], current_node[1] + neighbor[1], heuristic_data[neighbor[0]], new_path))







a_star_search('arad', 'bucharest')
