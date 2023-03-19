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
```
Output:
```
Path Greedy     : ['Magetan', 'Madiun', 'Nganjuk', 'Jombang', 'Surabaya']
Jarak Total     : 182
Waktu           : 0.0010008811950683594
```

<b>Kesimpulan</b>
Dilihat dari output, algoritma A* memiliki jarak yang lebih pendek dibandingkan Greedy. Namun, dilihat dari waktu eksekusi, Greedy memiliki waktu yang lebih cepat. Perbedaan ini dikarenakan Greedy hanya melihat heuristik dari suatu kota, sedangkan A* melihat heuristik serta actual cost.