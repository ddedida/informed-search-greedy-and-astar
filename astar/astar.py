import queue
import time

class Graph:
    def __init__(self, Nodes):
        self.nodes = Nodes
        self.adj_List = {}

        for node in self.nodes:
            self.adj_List[node] = []

    def add_edges(self, u, v, weight):
        self.adj_List[u].append([v, weight])
        self.adj_List[v].append([u, weight])

    def degree(self, node):
        deg = len(self.adj_List[node])
        return deg
    
    def get_weight(self, u, v):
        for edge in self.adj_List[u]:
            if edge[0] == v:
                return edge[1]
        return None

    def print_adj_list(self):
        for node in self.nodes:
            if(node == "Ngawi" or node == "Madiun" or node == "Gresik"):
                print(node, "\t\t->", self.adj_List[node])
            else:
                print(node, "\t->", self.adj_List[node])

def Astar(startNode, heuristics, graph, goalNode="Surabaya"):
    startTime = time.time()
    priorityQueue = queue.PriorityQueue()
    distance = 0
    path = []

    priorityQueue.put((heuristics[startNode] + distance, [startNode, 0]))

    while priorityQueue.empty() == False:
        current = priorityQueue.get()[1]
        path.append(current[0])
        distance += int(current[1])

        if current[0] == goalNode:
            break

        priorityQueue = queue.PriorityQueue()

        for i in graph[current[0]]:
            if i[0] not in path:
                priorityQueue.put((heuristics[i[0]] + int(i[1]) + distance, i))

    endTime = time.time()
    totalTime = endTime - startTime

    return path, totalTime

city_heuristic = {
    "Magetan": 162, "Ngawi": 130, "Ponorogo": 128, "Madiun": 126, 
    "Bojonegoro": 60, "Nganjuk": 70, "Jombang": 36, "Lamongan": 36, 
    "Gresik": 12, "Surabaya": 0, "Sidoarjo": 22, "Probolinggo": 70, 
    "Situbondo": 146, "Bangkalan": 140, "Sampang": 90, "Pamekasan": 104,
    "Sumenep": 150
}

all_edges = [
    ("Magetan", "Ngawi", 32), ("Magetan", "Ponorogo", 34), ("Magetan", "Madiun", 22),
    ("Ponorogo", "Madiun", 29), ("Ngawi", "Madiun", 30), ("Ngawi", "Bojonegoro", 44),
    ("Madiun", "Nganjuk", 48), ("Nganjuk", "Jombang", 40), ("Bojonegoro", "Jombang", 70),
    ("Bojonegoro", "Nganjuk", 33), ("Bojonegoro", "Lamongan", 42), ("Jombang", "Surabaya", 72),
    ("Lamongan", "Gresik", 14), ("Gresik", "Surabaya", 12), ("Surabaya", "Sidoarjo", 25),
    ("Sidoarjo", "Probolinggo", 78), ("Probolinggo", "Situbondo", 99), ("Surabaya", "Bangkalan", 44),
    ("Bangkalan", "Sampang", 52), ("Sampang", "Pamekasan", 31), ("Pamekasan", "Sumenep", 54)
]

graph = Graph(city_heuristic.keys())

for u, v, x in all_edges:
    graph.add_edges(u, v, x)

astar_path, astar_time = Astar("Magetan", city_heuristic, graph.adj_List)

sum = 0
i = 0
j = 1
for city in astar_path:
    length = len(astar_path)
    if(j < length):
        temp = graph.get_weight(astar_path[i], astar_path[j])
        sum += temp
        i += 1
        j += 1

print("Path Greedy\t:", astar_path)
print("Jarak Total\t:", sum)
print("Waktu\t\t:", astar_time)
