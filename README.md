# informed-search-greedy-and-astar

| Anggota                      | NRP        |
| ---------------------------- |:----------:|
| Dewangga Dika Darmawan       | 5025211109 |
| Syukra Wahyu Ramadhan        | 5025211037 |
| Javier Nararya Aqsa Setiyono | 5025211245 |

## Problem

![download](https://user-images.githubusercontent.com/108203648/226158650-1c6dfdfd-daa4-4eb0-887f-a6e53a12d40f.png)

Buat implementasi program dua algoritma informed search: Greedy Best-First Search dan A* Search pada Peta Jawa Timur dan buat analisis perbandingan dari hasil solusi kedua algoritma tersebut.

<b>Greedy-Best First Search Algorithm</b>

```py
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
```
Output:
```
Path Greedy     : ['Magetan', 'Madiun', 'Nganjuk', 'Jombang', 'Surabaya']
Jarak Total     : 394
Waktu           : 0.0010001659393310547
```

<b>A* Algorithm</b>

```py
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
```
Output:
```
Path Astar      : ['Magetan', 'Ngawi', 'Bojonegoro', 'Lamongan', 'Gresik', 'Surabaya']
Jarak Total     : 144
Waktu           : 0.0010008811950683594
```

<b>Kesimpulan</b>

Dilihat dari output, algoritma A* memiliki jarak yang lebih pendek dibandingkan Greedy. Namun, dilihat dari waktu eksekusi, Greedy memiliki waktu yang lebih cepat. Perbedaan ini dikarenakan Greedy hanya melihat heuristik dari suatu kota, sedangkan A* melihat heuristik serta actual cost.
