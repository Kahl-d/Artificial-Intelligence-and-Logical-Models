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

def get_neighbors(node):

    return adjaceny_list[node]



def get_heuristic(node):
    return heuristic_data[node]




def a_star(start, goal):
    frontier = []
    explored_set = set()
    path = []

    frontier.append((start, 0, get_heuristic(start)))

    while frontier:
        min_tuple = min(frontier, key=lambda x: x[1] + x[2])
        frontier.remove(min_tuple)

        if min_tuple[0] == goal:
            print(path)

        if min_tuple[0] not in explored_set:
            path.append(min_tuple[0])
            explored_set.add(min_tuple[0])
            neighbours = get_neighbors(min_tuple[0])
            new_elements = []

            for neighbour, distance in neighbours:
                if neighbour not in explored_set:
                    explored_set.add(neighbour)
                    new_elements.append((neighbour, distance + min_tuple[1], get_heuristic(neighbour)))

            frontier.extend(new_elements)
            print(frontier)




def main():
    a_star('arad', 'bucharest')


if __name__ == "__main__":
    main()