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

    print("First iteration: \n")
    for item in map:
        print(outcome.upper(), "--",map[item]["distance"], "-->", item.upper(), ", Visited: ", map[item]["visited"])
    print("-------------------------------")

    while(visitCount < len(vertices)):

        for item in map:
            if map[item]["visited"] == False:
                min = item


        # find a minmal mark in the current dict sequence
        for vertice in map:
            if(map[vertice]["visited"]):
                pass
            else:
                if(map[vertice]["distance"] < map[min]["distance"]):
                    min = vertice
                    
        print("Now on vertice", min.upper(), '\n')
        
        for item in graph[min]:
            if(item in map.keys()):
                way = map[min]["distance"] + graph[min][item]

                if(way < map[item]["distance"]):
                    map[item]["distance"] = way
                    print("The distance to vertice", item.upper(), "was updated ----->", way)
                
            else:
                way = graph[min][item] + map[min]["distance"]
                map[item] = {"distance": way, "visited": False}
        
        map[min]["visited"] =  True
        visitCount += 1

        # printing out results of iteration
        for item in map:
            print(outcome.upper(), "--",map[item]["distance"], "-->", item.upper(), ", Visited: ", map[item]["visited"])

        print("-------------------------------")

Dijkstra(G, "c")
