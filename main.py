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

income = "f"

def Dijkstra(graph, outcome):

    vertices = [x for x in graph] #get all of the graph vertices

    map = {outcome: {"distance": 0, "visited": False}}

    for item in graph[outcome]:
        map[item] =  {"distance": graph[outcome][item], "visited": False}

    map[outcome]["visited"] = True
    visitCount = 1

    print("First iteration: \n", map, "\n")

    while(visitCount < len(vertices)):
        for item in map:
            if map[item]["visited"] == False:
                min = item

        print("Minimal mark is:", min)

        # find a minmal mark in the current dict sequence
        for vertice in map:
            if(map[vertice]["visited"]):
                pass
            else:
                if(map[vertice]["distance"] < map[min]["distance"]):
                    min = vertice
                    
        for item in graph[min]:
            if(item in map.keys()):
                way = map[min]["distance"] + graph[min][item]

                if(way < map[item]["distance"]): #ERROR HERE!!
                    map[item]["distance"] = way
                    print("The distance to vertice", item.upper(), "was updated")
                
            else:
                map[item] = {"distance": graph[min][item], "visited": False}
        
        map[min]["visited"] =  True
        visitCount += 1

        print(map, "\n")

Dijkstra(G, "b")
