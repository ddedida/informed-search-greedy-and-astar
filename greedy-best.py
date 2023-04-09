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

    def print_adj_list(self):
        for node in self.nodes:
            if(node == "Ngawi" or node == "Madiun" or node == "Gresik"):
                print(node, "\t\t->", self.adj_List[node])
            else:
                print(node, "\t->", self.adj_List[node])

def Greedy(startNode, heuristics, graph, goalNode="Surabaya"):
    startTime = time.time()
    priorityQueue = queue.PriorityQueue()
    priorityQueue.put((heuristics[startNode], startNode))

    path = []

    while priorityQueue.empty() == False:
        current = priorityQueue.get()[1]
        path.append(current)

        if current == goalNode:
            break

        priorityQueue = queue.PriorityQueue()

        for i in graph[current]:
            if i[0] not in path:
                priorityQueue.put((heuristics[i[0]], i[0]))
    
    sum = 0
    for value in path:
        sum += heuristics[value]
    
    endTime = time.time()
    totalTime = endTime - startTime

    return path, sum, totalTime

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

gbfs_path, gbfs_sum, gbfs_time = Greedy("Magetan", city_heuristic, graph.adj_List)
print("Path Greedy\t:", gbfs_path)
print("Jarak Total\t:", gbfs_sum)
print("Waktu\t\t:", gbfs_time)