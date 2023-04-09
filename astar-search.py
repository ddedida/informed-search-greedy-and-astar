import time
import heapq

class priority_queue:
    def __init__(self):
        self.cities = []

    def push(self, city, cost):
        heapq.heappush(self.cities, (cost, city))

    def pop(self):
        return heapq.heappop(self.cities)[1]

    def isEmpty(self):
        return True if self.cities == [] else False

    def check(self):
        print(self.cities)

class ctNode:
    def __init__(self, city, distance):
        self.city = str(city)
        self.distance = str(distance)

city = {}

def make_dictionary():
    f = open("actual_costs.txt")
    for line in f.readlines():
        word = line.split()
        ct1 = word[0]
        ct2 = word[1]
        dist = int(word[2])
        city.setdefault(ct1, []).append(ctNode(ct2, dist))
        city.setdefault(ct2, []).append(ctNode(ct1, dist))

def get_heuristics():
    h = {}
    with open("cities_heuristic.txt", 'r') as f:
        for line in f:
            line = line.strip().split()
            node = line[0].strip()
            sld = int(line[1].strip())
            h[node] = sld
    return h

def heuristic(node, values):
    return values[node]

def astar(start, end):
    startTime = time.time()
    path = {}
    distance = {}
    q = priority_queue()
    h = get_heuristics()

    q.push(start, 0)
    distance[start] = 0
    path[start] = None
    expandedList = []

    while (q.isEmpty() == False):
        current = q.pop()
        expandedList.append(current)

        if (current == end):
            break

        for new in city[current]:
            g_cost = distance[current] + int(new.distance)

            if (new.city not in distance or g_cost < distance[new.city]):
                distance[new.city] = g_cost
                f_cost = g_cost + heuristic(new.city, h)
                q.push(new.city, f_cost)
                path[new.city] = current

    endTime = time.time()
    totalTime = endTime - startTime
    return start, end, path, distance, totalTime

if __name__ == "__main__":
    src = "Magetan"
    dst = "Surabaya"
    make_dictionary()
    astar_start, astar_end, astar_path, astar_distance, astar_time = astar(src, dst)
    
    final_path = []
    i = astar_end
    while(astar_path.get(i) != None):
        final_path.append(i)
        i = astar_path[i]
    final_path.append(astar_start)
    final_path.reverse()

    print("Path Astar\t:", final_path)
    print("Jarak Total\t:", astar_distance[astar_end])
    print("Waktu\t\t:", astar_time)