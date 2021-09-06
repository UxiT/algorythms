import random


G = {
    "a": {"b": 7, "e": 2},
    "b": {"d": 14, "h": 11},
    "c": {"a": 2, "d": 6, "f": 15},
    "d": {"c": 10},
    "e": {"b": 4},
    "f": {},
    "g": {"c": 3},
    "h": {"g": 9}
}

outcome = "a"
income = "f"

def set_edges(graph):

    vertices = [x for x in graph] #get all of the graph vertices

    map = {outcome: {"distance": 0, "visited": False}}

    for item in graph[outcome]:
        map[item] =  {"distance": graph[outcome][item], "visited": False}

    map[outcome]["visited"] = True
    # poped__distance = map.copy()
    # poped__distance.pop(outcome)

    # vertices.remove(outcome)
    min = 999

    print(map)

    # find a minmal mark in the current dict sequence
    for vertice in map:
        if(map[vertice]["visited"]):
            pass
        else:
            if(map[vertice]["distance"] < min):
                min = vertice

    print(map)
    
    # for item in graph[min]:
    #     print("Current V is:", min)

    #     way = map[min] + graph[min][item]
        
    #     print("Detecting the minimal distance...")
    #     if((item in map) & (way < map[item])):
    #         map[item] = way
    #         print("Shortest way for Vert '", item, "' is updated")

    # print(map)


set_edges(G)