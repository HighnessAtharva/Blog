---
title: "DSA in Python - Graph"
date: 2022-07-09T13:14:34+05:30
draft: false
cover: 
    image: blog/dsa/Graph.jpg
    alt: Graph
    caption: Learn Graph Algorithms in Python
tags: ["python"] 

---

## Free Preview - 5 Graph Problems

### Implement Graph

```python
class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]
        for (src, dest) in edges:
            self.adjList[src].append(dest)
 
 
def printGraph(graph):
    for src in range(len(graph.adjList)):
        for dest in graph.adjList[src]:
            print(f'({src} —> {dest}) ', end='')
        print()
 
edges = [(0, 1), (1, 2), (2, 0), (2, 1), (3, 2), (4, 5), (5, 4)]
n = 6
graph = Graph(edges, n)
printGraph(graph)
```

### Implement Weighted Graph

```python
class Graph:
    def __init__(self, edges, n):
        self.adjList = [None] * n
        for i in range(n):
            self.adjList[i] = []
        for (src, dest, weight) in edges:
            self.adjList[src].append((dest, weight))
 
 
def printGraph(graph):
    for src in range(len(graph.adjList)):
        for (dest, weight) in graph.adjList[src]:
            print(f'({src} —> {dest}, {weight}) ', end='')
        print()
 
 
# Input: Edges in a weighted digraph (as per the above diagram)
# Edge (x, y, w) represents an edge from `x` to `y` having weight `w`
edges = [(0, 1, 6), (1, 2, 7), (2, 0, 5), (2, 1, 4), (3, 2, 10),
        (4, 5, 1), (5, 4, 3)]
n = 6
graph = Graph(edges, n)
printGraph(graph)
```

### Implement BFS algorithm

```python
from collections import deque

class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)


def BFS(graph, v, discovered):
    q = deque()
    discovered[v] = True
    q.append(v)
    while q:
        v = q.popleft()
        print(v, end=' ')
        for u in graph.adjList[v]:
            if not discovered[u]:
                discovered[u] = True
                q.append(u)

edges = [
    (1, 2), (1, 3), (1, 4), (2, 5), (2, 6), (5, 9),
    (5, 10), (4, 7), (4, 8), (7, 11), (7, 12)
    # vertex 0, 13, and 14 are single nodes
]
n = 15
graph = Graph(edges, n)
discovered = [False] * n
for i in range(n):
    if not discovered[i]:
        BFS(graph, i, discovered)

```

### Implement DFS Algo

```python
from collections import deque
class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)
 
def iterativeDFS(graph, v, discovered):
    stack = deque()
    stack.append(v)
    while stack:
        v = stack.pop()
        if discovered[v]:
            continue
        discovered[v] = True
        print(v, end=' ')
        adjList = graph.adjList[v]
        for i in reversed(range(len(adjList))):
            u = adjList[i]
            if not discovered[u]:
                stack.append(u)
 
 
edges = [
    # Notice that node 0 is unconnected
    (1, 2), (1, 7), (1, 8), (2, 3), (2, 6), (3, 4),
    (3, 5), (8, 9), (8, 12), (9, 10), (9, 11)
    # (6, 9) introduces a cycle
]
n = 13
graph = Graph(edges, n)
discovered = [False] * n
for i in range(n):
    if not discovered[i]:
        iterativeDFS(graph, i, discovered)
```

### Detect Cycle in Directed Graph using BFS/DFS Algo

```python
class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]
        for (src, dest) in edges:
            self.adjList[src].append(dest)
 
 
# Perform DFS on the graph and set the departure time of all vertices of the graph
def DFS(graph, v, discovered, departure, time):
 
    # mark the current node as discovered
    discovered[v] = True
 
    # do for every edge (v, u)
    for u in graph.adjList[v]:
        # if `u` is not yet discovered
        if not discovered[u]:
            time = DFS(graph, u, discovered, departure, time)
 
    # ready to backtrack set departure time of vertex `v`
    departure[v] = time
    time = time + 1
 
    return time
 
 
# Returns true if the given directed graph is DAG
def isDAG(graph, n):
 
    # keep track of whether a vertex is discovered or not
    discovered = [False] * n
 
    # keep track of the departure time of a vertex in DFS
    departure = [None] * n
 
    time = 0
 
    # Perform DFS traversal from all undiscovered vertices to visit all connected components of a graph
    for i in range(n):
        if not discovered[i]:
            time = DFS(graph, i, discovered, departure, time)
 
    # check if the given directed graph is DAG or not
    for u in range(n):
 
        # check if (u, v) forms a back-edge.
        for v in graph.adjList[u]:
 
            # If the departure time of vertex `v` is greater than equal
            # to the departure time of `u`, they form a back edge.
 
            # Note that `departure[u]` will be equal to `departure[v]`
            # only if `u = v`, i.e., vertex contain an edge to itself
            if departure[u] <= departure[v]:
                return False
 
    # no back edges
    return True
 
 

# List of graph edges as per the above diagram
edges = [(0, 1), (0, 3), (1, 2), (1, 3), (3, 2), (3, 4), (3, 0), (5, 6), (6, 3)]
# total number of nodes in the graph (labelled from 0 to 6)
n = 7
graph = Graph(edges, n)
if isDAG(graph, n):
    print('Does not contain a Cycle')
else:
    print('Contains a Cycle')
 
```

## Buy the Interview Guide

{{< gumroad "https://highnessatharva.gumroad.com/l/dsa-python-graph" "/blog/gumroad-marketing.png" >}}