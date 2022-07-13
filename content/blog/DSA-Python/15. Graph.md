---
title: "DSA in Python - Graph"
date: 2022-07-09T13:14:34+05:30
draft: false
cover: 
    image: blog/dsa/graph.jpg
    alt: Graph
    caption: Learn Graph Algorithms in Python
tags: ["DSA-Python"] 

---

- [Implement Graph](#implement-graph)
- [Implement Weighted Graph](#implement-weighted-graph)
- [Implement BFS algorithm](#implement-bfs-algorithm)
- [Implement DFS Algo](#implement-dfs-algo)
- [Detect Cycle in Directed Graph using BFS/DFS Algo](#detect-cycle-in-directed-graph-using-bfsdfs-algo)
- [Detect Cycle in UnDirected Graph using BFS/DFS Algo](#detect-cycle-in-undirected-graph-using-bfsdfs-algo)
- [Minimum Step by Knight](#minimum-step-by-knight)
- [flood fill algo](#flood-fill-algo)
- [Clone a graph](#clone-a-graph)
- [Making wired Connections](#making-wired-connections)
- [word Ladder](#word-ladder)
- [Dijkstra algo](#dijkstra-algo)
- [Implement Topological Sort](#implement-topological-sort)
- [Minimum time taken by each job to be completed given by a Directed Acyclic Graph](#minimum-time-taken-by-each-job-to-be-completed-given-by-a-directed-acyclic-graph)
- [Find whether it is possible to finish all tasks or not from given dependencies](#find-whether-it-is-possible-to-finish-all-tasks-or-not-from-given-dependencies)
- [Find the no. of Islands](#find-the-no-of-islands)
- [Given a sorted Dictionary of an Alien Language, find order of characters](#given-a-sorted-dictionary-of-an-alien-language-find-order-of-characters)
- [Implement Kruksal’sAlgorithm](#implement-kruksalsalgorithm)
- [Implement Prim’s Algorithm](#implement-prims-algorithm)
- [Total no. of Spanning tree in a graph](#total-no-of-spanning-tree-in-a-graph)
- [Implement Bellman Ford Algorithm](#implement-bellman-ford-algorithm)
- [Implement Floyd warshallAlgorithm](#implement-floyd-warshallalgorithm)
- [Travelling Salesman Problem](#travelling-salesman-problem)
- [Graph ColouringProblem](#graph-colouringproblem)
- [Snake and Ladders Problem](#snake-and-ladders-problem)
- [Find bridge in a graph](#find-bridge-in-a-graph)
- [Count Strongly connected Components(Kosaraju Algo)](#count-strongly-connected-componentskosaraju-algo)
- [Check whether a graph is Bipartite or Not](#check-whether-a-graph-is-bipartite-or-not)
- [Longest path in a Directed Acyclic Graph](#longest-path-in-a-directed-acyclic-graph)
- [Journey to the Moon](#journey-to-the-moon)
- [Cheapest Flights Within K Stops](#cheapest-flights-within-k-stops)
- [Oliver and the Game](#oliver-and-the-game)
- [Water Jug problem using BFS](#water-jug-problem-using-bfs)
- [Find if there is a path of more thank length from a source](#find-if-there-is-a-path-of-more-thank-length-from-a-source)
- [Minimum edges to reverse o make path from source to destination](#minimum-edges-to-reverse-o-make-path-from-source-to-destination)
- [Paths to travel each nodes using each edge(Seven Bridges)](#paths-to-travel-each-nodes-using-each-edgeseven-bridges)
- [Vertex Cover Problem](#vertex-cover-problem)
- [Chinese Postman or Route Inspection](#chinese-postman-or-route-inspection)
- [Number of Triangles in a Directed and Undirected Graph](#number-of-triangles-in-a-directed-and-undirected-graph)
- [Minimise the cashflow among a given set of friends who have borrowed money from each other](#minimise-the-cashflow-among-a-given-set-of-friends-who-have-borrowed-money-from-each-other)
- [Two Clique Problem](#two-clique-problem)

## Implement Graph

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

## Implement Weighted Graph

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

## Implement BFS algorithm

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

## Implement DFS Algo

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

## Detect Cycle in Directed Graph using BFS/DFS Algo

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

## Detect Cycle in UnDirected Graph using BFS/DFS Algo

```python
class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)
 
 
# Function to perform DFS traversal on the graph on a graph
def DFS(graph, v, discovered, parent=-1):
 
    # mark the current node as discovered
    discovered[v] = True
 
    # do for every edge (v, w)
    for w in graph.adjList[v]:
 
        # if `w` is not discovered
        if not discovered[w]:
            if DFS(graph, w, discovered, v):
                return True
 
        # if `w` is discovered, and `w` is not a parent
        elif w != parent:
            # we found a back-edge (cycle)
            return True
 
    # No back-edges were found in the graph
    return False
 
 

edges = [
    (0, 1), (0, 6), (0, 7), (1, 2), (1, 5), (2, 3),
    (2, 4), (7, 8), (7, 11), (8, 9), (8, 10), (10, 11)
    # edge (10, 11) introduces a cycle in the graph
]

# total number of nodes in the graph (0 to 11)
n = 12

graph = Graph(edges, n)
discovered = [False] * n
if DFS(graph, 0, discovered):
    print('The graph contains a cycle')
else:
    print('The graph doesn\'t contain any cycle')
```


## Minimum Step by Knight

```python
"""Given a chessboard, find the shortest distance (minimum number of steps) taken by a knight to reach a given destination from a given source.

For example,

Input:
 
N = 8 (8 × 8 board)
Source = (7, 0)
Destination = (0, 7)
 
Output: Minimum number of steps required is 6
"""

import sys
from collections import deque
 
 
class Node:
    # (x, y) represents chessboard coordinates `dist` represents its minimum distance from the source
    def __init__(self, x, y, dist=0):
        self.x = x
        self.y = y
        self.dist = dist
 
    # As we are using `Node` as a key in a dictionary, we need to override the `__hash__()` and `__eq__()` function
    def __hash__(self):
        return hash((self.x, self.y, self.dist))
 
    def __eq__(self, other):
        return (self.x, self.y, self.dist) == (other.x, other.y, other.dist)
 
 
# Below lists detail all eight possible movements for a knight
row = [2, 2, -2, -2, 1, 1, -1, -1]
col = [-1, 1, 1, -1, 2, -2, 2, -2]
 
 
# Check if (x, y) is valid chessboard coordinates.
# Note that a knight cannot go out of the chessboard
def isValid(x, y, N):
    return x >= 0 and y >= 0 and x < N and y < N
 
 
# Find the minimum number of steps taken by the knight
# from the source to reach the destination using BFS
def findShortestDistance(src, dest, N):

    # set to check if the matrix cell is visited before or not
    visited = set()
 
    # create a queue and enqueue the first node
    q = deque()
    q.append(src)
 
    # loop till queue is empty
    while q:
 
        # dequeue front node and process it
        node = q.popleft()
 
        x = node.x
        y = node.y
        dist = node.dist
 
        # if the destination is reached, return distance
        if x == dest.x and y == dest.y:
            return dist
 
        # skip if the location is visited before
        if node not in visited:
            # mark the current node as visited
            visited.add(node)
 
            # check for all eight possible movements for a knight
            # and enqueue each valid movement
            for i in range(len(row)):
                # get the knight's valid position from the current position on
                # the chessboard and enqueue it with +1 distance
                x1 = x + row[i]
                y1 = y + col[i]
 
                if isValid(x1, y1, N):
                    q.append(Node(x1, y1, dist + 1))
 
    # return infinity if the path is not possible
    return sys.maxsize


N = 8               # N x N matrix
src = Node(0, 7)    # source coordinates
dest = Node(7, 0)   # destination coordinates
print("The minimum number of steps required is",findShortestDistance(src, dest, N))
 
```

## flood fill algo

```python
"""Flood fill (also known as seed fill) is an algorithm that determines the area connected to a given node in a multi-dimensional array.
"""

# Below lists detail all eight possible movements
row = [-1, -1, -1, 0, 0, 1, 1, 1]
col = [-1, 0, 1, -1, 1, -1, 0, 1]
 
 
# check if it is possible to go to pixel (x, y) from the
# current pixel. The function returns false if the pixel
# has a different color, or it's not a valid pixel
def isSafe(mat, x, y, target):
    return 0 <= x < len(mat) and 0 <= y < len(mat[0]) and mat[x][y] == target
 
 
# Flood fill using DFS
def floodfill(mat, x, y, replacement):
 
    # base case
    if not mat or not len(mat):
        return
 
    # get the target color
    target = mat[x][y]
 
    # target color is same as replacement
    if target == replacement:
        return
 
    # replace the current pixel color with that of replacement
    mat[x][y] = replacement
 
    # process all eight adjacent pixels of the current pixel and
    # recur for each valid pixel
    for k in range(len(row)):
 
        # if the adjacent pixel at position (x + row[k], y + col[k]) is
        # a valid pixel and has the same color as that of the current pixel
        if isSafe(mat, x + row[k], y + col[k], target):
            floodfill(mat, x + row[k], y + col[k], replacement)
 
 

mat = [
        ['Y', 'Y', 'Y', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],
        ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'G', 'X', 'X', 'X'],
        ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'X', 'X', 'X'],
        ['W', 'W', 'W', 'W', 'W', 'G', 'G', 'G', 'G', 'X'],
        ['W', 'R', 'R', 'R', 'R', 'R', 'G', 'X', 'X', 'X'],
        ['W', 'W', 'W', 'R', 'R', 'G', 'G', 'X', 'X', 'X'],
        ['W', 'B', 'W', 'R', 'R', 'R', 'R', 'R', 'R', 'X'],
        ['W', 'B', 'B', 'B', 'B', 'R', 'R', 'X', 'X', 'X'],
        ['W', 'B', 'B', 'X', 'B', 'B', 'B', 'B', 'X', 'X'],
        ['W', 'B', 'B', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
    ]

# start node
x, y = (3, 9)   # having a target color `X`

# replacement color
replacement = 'C'

# replace the target color with a replacement color using DFS
floodfill(mat, x, y, replacement)

# print the colors after replacement
for r in mat:
    print(r)
```

## Clone a graph

```python
TODO
```

## Making wired Connections

```python
"""There are n computers numbered from 0 to n-1 connected by ethernet cables connections forming a network where connections[i] = [a, b] represents a connection between computers a and b. Any computer can reach any other computer directly or indirectly through the network.

Given an initial computer network connections. You can extract certain cables between two directly connected computers, and place them between any pair of disconnected computers to make them directly connected. Return the minimum number of times you need to do this in order to make all the computers connected. If it’s not possible, return -1.

Example 1:

Input: n = 4, connections = [[0,1],[0,2],[1,2]]
Output: 1
Explanation: Remove cable between computer 1 and 2 and place between computers 1 and 3.
Example 2:

Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
Output: 2
Example 3:

Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
Output: -1
Explanation: There are not enough cables.
Example 4:

Input: n = 5, connections = [[0,1],[0,2],[3,4],[2,3]]
Output: 0
"""

def makeConnected(n, connections):
    uf = {i: i for i in range(n)}

    def find(x):
        uf.setdefault(x, x)
        if uf[x] != x:
            uf[x] = find(uf[x])
        return uf[x]

    def union(a, b):
        uf[find(a)] = find(b)
    if len(connections) < n - 1:
        return -1
    for a, b in connections:
        union(a, b)
    islands = len({find(x) for x in uf})
    return islands - 1
n = 4

connections = [[0,1],[0,2],[1,2]]
print(makeConnected(n, connections))
```

## word Ladder

```python
"""
Given two words (beginWord and endWord), and a dictionary's word list,
find the length of shortest transformation sequence from beginWord to endWord, such that:
(i) Only one letter can be changed at a time, and (ii) each transformed word must exist in
the word list. Note that beginWord is not a transformed word.

EXAMPLES
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
-> 5 (because "hit" -> "hot" -> "dot" -> "dog" -> "cog")

"""

from collections import deque
def ladderLength(beginWord, endWord, wordList):
    """
    :type beginWord: str
    :type endWord: str
    :type wordList: Set[str]
    :rtype: int
    """

    queue = deque()
    queue.append((beginWord, [beginWord]))
    while queue:
        node, path = queue.popleft()
        for next in next_nodes(node, wordList) - set(path):
            if next == endWord:
                return len(path) + 1
            else:
                queue.append((next, path + [next]))
    return 0

def next_nodes(word, word_list):
    to_return = set()
    for w in word_list:
        mismatch_count, w_length = 0, len(w)
        for i in range(w_length):
            if w[i] != word[i]:
                mismatch_count += 1
        if mismatch_count == 1:
            to_return.add(w)
    return to_return

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(ladderLength(beginWord, endWord, wordList))
```

## Dijkstra algo

```python
"""
Given a source vertex s from a set of vertices V in a weighted digraph where all its edge weights w(u, v) are non-negative, find the shortest path weights d(s, v) from source s for all vertices v present in the graph    
"""
import sys
from heapq import heappop, heappush
 
class Node:
    def __init__(self, vertex, weight=0):
        self.vertex = vertex
        self.weight = weight
 
    # Override the __lt__() function to make `Node` class work with a min-heap
    def __lt__(self, other):
        return self.weight < other.weight
 
class Graph:
    def __init__(self, edges, n):
        # allocate memory for the adjacency list
        self.adjList = [[] for _ in range(n)]
 
        # add edges to the directed graph
        for (source, dest, weight) in edges:
            self.adjList[source].append((dest, weight))
 
def get_route(prev, i, route):
    if i >= 0:
        get_route(prev, prev[i], route)
        route.append(i)
 

def findShortestPaths(graph, source, n):
 
    # create a min-heap and push source node having distance 0
    pq = []
    heappush(pq, Node(source))
 
    # set initial distance from the source to `v` as infinity
    dist = [sys.maxsize] * n
 
    # distance from the source to itself is zero
    dist[source] = 0
 
    # list to track vertices for which minimum cost is already found
    done = [False] * n
    done[source] = True
 
    # stores predecessor of a vertex (to a print path)
    prev = [-1] * n
 
    # run till min-heap is empty
    while pq:
 
        node = heappop(pq)      # Remove and return the best vertex
        u = node.vertex         # get the vertex number
 
        # do for each neighbor `v` of `u`
        for (v, weight) in graph.adjList[u]:
            if not done[v] and (dist[u] + weight) < dist[v]:        # Relaxation step
                dist[v] = dist[u] + weight
                prev[v] = u
                heappush(pq, Node(v, dist[v]))
 
        # mark vertex `u` as done so it will not get picked up again
        done[u] = True
 
    route = []
    for i in range(n):
        if i != source and dist[i] != sys.maxsize:
            get_route(prev, i, route)
            print(f'Path ({source} —> {i}): Minimum cost = {dist[i]}, Route = {route}')
            route.clear()

# initialize edges as per the above diagram (u, v, w) represent edge from vertex `u` to vertex `v` having weight `w`
edges = [(0, 1, 10), (0, 4, 3), (1, 2, 2), (1, 4, 4), (2, 3, 9), (3, 2, 7),
        (4, 1, 1), (4, 2, 8), (4, 3, 2)]
# total number of nodes in the graph (labelled from 0 to 4)
n = 5
graph = Graph(edges, n)
for source in range(n):
    findShortestPaths(graph, source, n)
```

## Implement Topological Sort

```python
"""
Given a Directed Acyclic Graph (DAG), print it in topological order using topological sort algorithm. If the graph has more than one topological ordering, output any of them. Assume valid Directed Acyclic Graph (DAG).

A Topological sort or Topological ordering of a directed graph is a linear ordering of its vertices such that for every directed edge uv from vertex u to vertex v, u comes before v in the ordering. A topological ordering is possible if and only if the graph has no directed cycles, i.e. if the graph is DAG.

"""
# A class to represent a graph object
class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]
        for (src, dest) in edges:
            self.adjList[src].append(dest)
 
 
# Perform DFS on the graph and set the departure time of all vertices of the graph
def DFS(graph, v, discovered, departure, time):
    discovered[v] = True
    time = time + 1
    for u in graph.adjList[v]:
        if not discovered[u]:
            time = DFS(graph, u, discovered, departure, time)
    departure[time] = v
    time = time + 1
    return time
 
 
# Function to perform a topological sort on a given DAG
def doTopologicalSort(graph, n):
 
    # departure[] stores the vertex number using departure time as an index
    departure = [-1] * 2 * n
 
    ''' If we had done it the other way around, i.e., fill the array
        with departure time using vertex number as an index, we would
        need to sort it later '''
 
    # to keep track of whether a vertex is discovered or not
    discovered = [False] * n
    time = 0
 
    # perform DFS on all undiscovered vertices
    for i in range(n):
        if not discovered[i]:
            time = DFS(graph, i, discovered, departure, time)
 
    # Print the vertices in order of their decreasing
    # departure time in DFS, i.e., in topological order
    for i in reversed(range(2*n)):
        if departure[i] != -1:
            print(departure[i], end=' ')
 

# List of graph edges as per the above diagram
edges = [(0, 6), (1, 2), (1, 4), (1, 6), (3, 0), (3, 4), (5, 1), (7, 0), (7, 1)] 
# total number of nodes in the graph (labelled from 0 to 7)
n = 8
graph = Graph(edges, n) 
doTopologicalSort(graph, n)
```

## Minimum time taken by each job to be completed given by a Directed Acyclic Graph

```python
"""
Given a Directed Acyclic Graph having V vertices and E edges, where each edge {U, V} represents the Jobs U and V such that Job V can only be started only after completion of Job U. The task is to determine the minimum time taken by each job to be completed where each Job takes unit time to get completed.   
"""

from collections import defaultdict

class Graph:
	def __init__(self, vertices, edges):
		self.graph = defaultdict(list)
		self.n = vertices
		self.m = edges
		
	# Function to add an edge to graph
	def addEdge(self, u, v):
		self.graph[u].append(v)
	
	# Function to find the minimum time needed by each node to get the task
	def printOrder(self, n, m):
	
		# Create a vector to store indegrees of all vertices. Initialize all indegrees as 0.
		indegree = [0] * (self.n + 1)
		
		# Traverse adjacency lists to fill indegrees of vertices. This step takes O(V + E) time
		for i in self.graph:
			for j in self.graph[i]:
				indegree[j] += 1
				
		# Array to store the time in which the job i can be done
		job = [0] * (self.n + 1)
		
		# Create an queue and enqueue all vertices with indegree 0
		q = []
		
		# Update the time of the jobs who don't require any job to be completed before this job
		for i in range(1, self.n + 1):
			if indegree[i] == 0:
				q.append(i)
				job[i] = 1
				
		# Iterate until queue is empty
		while q:
			
			# Get front element of queue
			cur = q.pop(0)
			
			for adj in self.graph[cur]:
				
				# Decrease in-degree of the current node
				indegree[adj] -= 1
			
				# Push its adjacent elements
				if (indegree[adj] == 0):
					job[adj] = 1 + job[cur]
					q.append(adj)
					
		# Print the time to complete the job
		for i in range(1, n + 1):
			print(job[i], end = " ")
			
		print()

# Given Nodes N and edges M
n = 10
m = 13
g = Graph(n, m)
g.addEdge(1, 3)
g.addEdge(1, 4)
g.addEdge(1, 5)
g.addEdge(2, 3)
g.addEdge(2, 8)
g.addEdge(2, 9)
g.addEdge(3, 6)
g.addEdge(4, 6)
g.addEdge(4, 8)
g.addEdge(5, 8)
g.addEdge(6, 7)
g.addEdge(7, 8)
g.addEdge(8, 10)
g.printOrder(n, m)

```

## Find whether it is possible to finish all tasks or not from given dependencies

```python
"""
There are a total of n tasks you have to pick, labelled from 0 to n-1. Some tasks may have prerequisites, for example to pick task 0 you have to first pick task 1, which is expressed as a pair: [0, 1]
Given the total number of tasks and a list of prerequisite pairs, is it possible for you to finish all tasks?
Examples:
 

Input: 2, [[1, 0]] 
Output: true 
Explanation: There are a total of 2 tasks to pick. To pick task 1 you should have finished task 0. So it is possible.
Input: 2, [[1, 0], [0, 1]] 
Output: false 
Explanation: There are a total of 2 tasks to pick. To pick task 1 you should have finished task 0, and to pick task 0 you should also have finished task 1. So it is impossible.
Input: 3, [[1, 0], [2, 1], [3, 2]] 
Output: true 
Explanation: There are a total of 3 tasks to pick. To pick tasks 1 you should have finished task 0, and to pick task 2 you should have finished task 1 and to pick task 3 you should have finished task 2. So it is possible. 
"""


class Solution:
	
	arr = []
	# parameterized constructor
	def __init__(self,n):
		# Initially, everyone is their own child
		self.arr = list(range(n))

	def makeParent(self,a, b):
		# find parent of b and make it a's parent
		self.arr[a] = self.findParent(b)

	def findParent(self,c):
		# when an independent task is found
		return c if (c == self.arr) else self.findParent(self.arr)

	def isPossible(self,N , prerequisites):
		# traverse through pre-requisites array
		for i in range(len(prerequisites)):
			# check whether given pre-requisite pair already have a common pre-requisite(parent)
			if (self.findParent(prerequisites[i][0]) == self.findParent(prerequisites[i][1])):
			# tasks cannot be completed because there was a cyclic condition in the tasks
				return False
			# make parent-child relation between pre-requisite task and the task dependent on it
			self.makeParent(prerequisites[i][0], prerequisites[i][1])
		# if there was no cycle found, tasks can be completed
		return True
	

prerequisites = [[1, 0], [2, 1], [3, 2]]
ob = Solution(4)
if ob.isPossible(4,prerequisites ):
	print("Yes")
else:
	print("No")
```

## Find the no. of Islands

```python
"""
Given a boolean 2D matrix, find the number of islands. A group of connected 1s forms an island. For example, the below matrix contains 5 islands

Example: 

Input : mat[][] = {{1, 1, 0, 0, 0},
                   {0, 1, 0, 0, 1},
                   {1, 0, 0, 1, 1},
                   {0, 0, 0, 0, 0},
                   {1, 0, 1, 0, 1}}
Output : 5
"""


# Program to count islands in boolean 2D matrix
class Graph:
	def __init__(self, row, col, graph):
		self.ROW = row
		self.COL = col
		self.graph = graph

	# A utility function to do DFS for a 2D boolean matrix. It only considers the 8 neighbours as adjacent vertices
	def DFS(self, i, j):
		if i < 0 or i >= len(self.graph) or j < 0 or j >= len(self.graph[0]) or self.graph[i][j] != 1:
			return

		# mark it as visited
		self.graph[i][j] = -1

		# Recur for 8 neighbours
		self.DFS(i - 1, j - 1)
		self.DFS(i - 1, j)
		self.DFS(i - 1, j + 1)
		self.DFS(i, j - 1)
		self.DFS(i, j + 1)
		self.DFS(i + 1, j - 1)
		self.DFS(i + 1, j)
		self.DFS(i + 1, j + 1)

	# The main function that returns count of islands in a given boolean 2D matrix
	def countIslands(self):
		# Initialize count as 0 and traverse through the all cells of given matrix
		count = 0
		for i in range(self.ROW):
			for j in range(self.COL):
				# If a cell with value 1 is not visited yet, then new island found
				if self.graph[i][j] == 1:
					# Visit all cells in this island and increment island count
					self.DFS(i, j)
					count += 1

		return count


graph = [
	[1, 1, 0, 0, 0],
	[0, 1, 0, 0, 1],
	[1, 0, 0, 1, 1],
	[0, 0, 0, 0, 0],
	[1, 0, 1, 0, 1]
]
row = len(graph)
col = len(graph[0])
g = Graph(row, col, graph)
print("Number of islands is:", g.countIslands())

```

## Given a sorted Dictionary of an Alien Language, find order of characters

```python
"""
Given a dictionary of ancient origin where the words are arranged alphabetically, find the correct order of alphabets in the ancient language.

For example,

Input:  Ancient dictionary { ¥€±, €±€, €±‰ð, ðß, ±±ð, ±ßß }
Output: The correct order of alphabets in the ancient language is {¥ € ‰ ð ± ß}.
 
Since the input is small, more than one ordering is possible. Another such ordering is {¥ € ð ± ß ‰}.
 
 
Input:  Ancient dictionary { ÿ€±š, €€€ß, €€‰ð, ðß, ±ß¥š }
Output: The correct order of alphabets in the ancient language is {ÿ € ‰ ð ±}.
 
The alphabets {š, ß, ¥} are not included in the order as they are not properly defined.
"""


class Graph:
    def __init__(self, N):
        self.adj = [[] for _ in range(N)]
 

def DFS(graph, v, discovered, departure, time):
    discovered[v] = True
    time = time + 1
    for u in graph.adj[v]:
        if not discovered[u]:
            time = DFS(graph, u, discovered, departure, time)
    departure[time] = v
    return time + 1
 
 
# Utility function to performs topological sort on a given DAG
def doTopologicalSort(graph, d):
 
    # `departure[]` stores the vertex number using departure time as an index
    departure = [-1] * (2 * N)
 
    ''' If we had done it the other way around, i.e., fill the array
        with departure time using vertex number as an index, we would
        need to sort it later '''
 
    # to keep track of whether a vertex is discovered or not
    discovered = [False] * N
    time = 0
 
    # perform DFS on all undiscovered connected vertices
    for i in range(N):
        if not discovered[i] and len(graph.adj[i]):
            time = DFS(graph, i, discovered, departure, time)
 
    print('\nThe correct order of alphabets in the ancient language is', end=' ')
 
    # Print the vertices in order of their decreasing
    # departure time in DFS, i.e., in topological order
    for i in reversed(range(2*N)):
        if departure[i] != -1:
            print(d[departure[i]], end=' ')
 
 
# Utility function to print adjacency list representation of a graph
def printGraph(graph, d):
 
    for i in range(N):
        # ignore vertices with no outgoing edges
        if graph.adj[i]:
            # print current vertex and all neighboring vertices of a vertex `i`
            print(d[i], '—>', [d[v] for v in graph.adj[i]])
 
 
# Function to find the correct order of alphabets in a given dictionary of
# ancient origin. This function assumes that the input is correct.
def findAlphabetsOrder(dictionary):
    # create a dictionary to map each non-ASCII character present in the given dictionary with a unique integer
    d = {}
    k = 0
    # do for each word
    for word in dictionary:
        # do for each non-ASCII character of the word
        for s in word:
            # if the current character is not present in the dictionary, insert it
            d.setdefault(s, k)
            k = k + 1
    # create a graph containing `N` nodes
    graph = Graph(N)

    # iterate through the complete dictionary and compare adjacent words for character mismatch
    for i in range(1, len(dictionary)):
        # previous word in the dictionary
        prev = dictionary[i - 1]

        # current word in the dictionary
        curr = dictionary[i]

        # iterate through both `prev` and `curr` simultaneously and find the first mismatching character
        j = 0
        while j < len(prev) and j < len(curr):
            # mismatch found
            if prev[j] is not curr[j]:

                # add an edge from the current character of `prev` to the
                # current character of `curr` in the graph
                graph.adj[d[prev[j]]].append(d[curr[j]])
                break

            j += 1

    # create a reverse dict
    reverse = {v: k for k, v in d.items()}
    printGraph(graph, reverse)
    # perform a topological sort on the above graph
    doTopologicalSort(graph, reverse)
 

# define the maximum number of alphabets in the ancient dictionary
N = 100
dictionary = [
    ["¥", "€", "±"],
    ["€", "±", "€"],
    ["€", "±", "‰", "ð"],
    ["ð", "ß"],
    ["±", "±", "ð"],
    ["±", "ß", "ß"]
]
findAlphabetsOrder(dictionary)
```

## Implement Kruksal’sAlgorithm

```python
"""
Below are the steps for finding MST using Kruskal’s algorithm

1. Sort all the edges in non-decreasing order of their weight. 
2. Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far. If cycle is not formed, include this edge. Else, discard it. 
3. Repeat step#2 until there are (V-1) edges in the spanning tree.
"""

from collections import defaultdict
class Graph:

	def __init__(self, vertices):
		self.V = vertices # No. of vertices
		self.graph = [] # default dictionary
		# to store graph

	# function to add an edge to graph
	def addEdge(self, u, v, w):
		self.graph.append([u, v, w])

	# A utility function to find set of an element i (uses path compression technique)
	def find(self, parent, i):
		return i if parent[i] == i else self.find(parent, parent[i])

	# A function that does union of two sets of x and y (uses union by rank)
	def union(self, parent, rank, x, y):
		xroot = self.find(parent, x)
		yroot = self.find(parent, y)

		# Attach smaller rank tree under root of high rank tree (Union by Rank)
		if rank[xroot] < rank[yroot]:
			parent[xroot] = yroot
		elif rank[xroot] > rank[yroot]:
			parent[yroot] = xroot

		# If ranks are same, then make one as root and increment its rank by one
		else:
			parent[yroot] = xroot
			rank[xroot] += 1

	# The main function to construct MST using Kruskal's algorithm
	def KruskalMST(self):

		result = [] # This will store the resultant MST
		i = 0 # An index variable, used for sorted edges
		e = 0 # An index variable, used for result[]

		# Step 1: Sort all the edges in non-decreasing order of their
		# weight. If we are not allowed to change the given graph, we can create a copy of graph
		self.graph = sorted(self.graph, key=lambda item: item[2])

		parent = []
		rank = []

		# Create V subsets with single elements
		for node in range(self.V):
			parent.append(node)
			rank.append(0)

		# Number of edges to be taken is equal to V-1
		while e < self.V - 1:

			# Step 2: Pick the smallest edge and increment the index for next iteration
			u, v, w = self.graph[i]
			i = i + 1
			x = self.find(parent, u)
			y = self.find(parent, v)

			# If including this edge doesn't cause cycle, include it in result and increment the indexof 
            # result for next edge
			if x != y:
				e += 1
				result.append([u, v, w])
				self.union(parent, rank, x, y)
				# Else discard the edge

		minimumCost = 0
		print ("Edges in the constructed MST")
		for u, v, weight in result:
			minimumCost += weight
			print("%d -- %d == %d" % (u, v, weight))
		print("Minimum Spanning Tree" , minimumCost)

g = Graph(4)
g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)
g.KruskalMST()
```

## Implement Prim’s Algorithm

```python
# A Python program for Prim's Minimum Spanning Tree (MST) algorithm.
# The program is for adjacency matrix representation of the graph

import sys # Library for INT_MAX

class Graph():

	def __init__(self, vertices):
		self.V = vertices
		self.graph = [[0 for column in range(vertices)]
					for row in range(vertices)]

	# A utility function to print the constructed MST stored in parent[]
	def printMST(self, parent):
		print ("Edge \tWeight")
		for i in range(1, self.V):
			print (parent[i], "-", i, "\t", self.graph[i][parent[i]])

	# A utility function to find the vertex with minimum distance value, from the set of vertices not yet included in shortest path tree
	def minKey(self, key, mstSet):

		# Initialize minValue value
		minValue = sys.maxsize

		for v in range(self.V):
			if key[v] < minValue and mstSet[v] == False:
				minValue = key[v]
				min_index = v

		return min_index

	# Function to construct and print MST for a graph represented using adjacency matrix representation
	def primMST(self):

		# Key values used to pick minimum weight edge in cut
		key = [sys.maxsize] * self.V
		parent = [None] * self.V # Array to store constructed MST
		# Make key 0 so that this vertex is picked as first vertex
		key[0] = 0
		mstSet = [False] * self.V

		parent[0] = -1 # First node is always the root of

		for cout in range(self.V):

			# Pick the minimum distance vertex from the set of vertices not yet processed. u is always equal to src in first iteration
			u = self.minKey(key, mstSet)

			# Put the minimum distance vertex in the shortest path tree
			mstSet[u] = True

			# Update dist value of the adjacent vertices of the picked vertex only if the current
			# distance is greater than new distance and the vertex in not in the shortest path tree
			for v in range(self.V):

				# graph[u][v] is non zero only for adjacent vertices of m mstSet[v] is false for vertices not yet included in MST
				# Update the key only if graph[u][v] is smaller than key[v]
				if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
						key[v] = self.graph[u][v]
						parent[v] = u
		self.printMST(parent)

g = Graph(5)
g.graph = [ [0, 2, 0, 6, 0],
			[2, 0, 3, 8, 5],
			[0, 3, 0, 0, 7],
			[6, 8, 0, 0, 9],
			[0, 5, 7, 9, 0]]
g.primMST();
```

## Total no. of Spanning tree in a graph

```python
TODO
```

## Implement Bellman Ford Algorithm

```python
"""
We are given a directed graph. We need to compute whether the graph has a negative cycle or not. A negative cycle is one in which the overall sum of the cycle becomes negative.
"""

# a structure to represent a weighted edge in graph
class Edge:
	def __init__(self):
		self.src = 0
		self.dest = 0
		self.weight = 0

# a structure to represent a connected, directed and weighted graph
class Graph:
	def __init__(self):
		# V. Number of vertices, E. Number of edges
		self.V = 0
		self.E = 0

		# graph is represented as an array of edges.
		self.edge = None

# Creates a graph with V vertices and E edges
def createGraph(V, E):

	graph = Graph()
	graph.V = V;
	graph.E = E;
	graph.edge = [Edge() for _ in range(graph.E)]
	return graph;

# The main function that finds shortest distances from src to all other vertices using Bellman- Ford algorithm. The function also detects negative weight cycle
def isNegCycleBellmanFord(graph, src):

	V = graph.V;
	E = graph.E;
	dist = [1000000 for _ in range(V)];
	dist[src] = 0;

	# Step 2: Relax all edges |V| - 1 times. 
    # A simple shortest path from src to any other vertex can have at-most |V| - 1 edges
	for _ in range(1, V):
		for j in range(E):

			u = graph.edge[j].src;
			v = graph.edge[j].dest;
			weight = graph.edge[j].weight;
			if (dist[u] != 1000000 and dist[u] + weight < dist[v]):
				dist[v] = dist[u] + weight;

	# Step 3: check for negative-weight cycles.
	# The above step guarantees shortest distances if graph doesn't contain negative weight cycle.
	# If we get a shorter path, then there is a cycle.
	for i in range(E):

		u = graph.edge[i].src;
		v = graph.edge[i].dest;
		weight = graph.edge[i].weight;
		if (dist[u] != 1000000 and dist[u] + weight < dist[v]):
			return True;

	return False;


# Let us create the graph given in above example
V = 5; # Number of vertices in graph
E = 8; # Number of edges in graph
graph = createGraph(V, E)

source= [0,0,1,1,1,3,3,4]
destination= [1,2,2,3,4,2,1,3]
weight=[-1,4,3,2,2,5,1,-3]

for i in range(E):
    graph.edge[i].src=source[i]
    graph.edge[i].dest=destination[i]
    graph.edge[i].weight=weight[i]

if (isNegCycleBellmanFord(graph, 0)):
	print("Yes")
else:
	print("No")

```

## Implement Floyd warshallAlgorithm

```python
"""
The Floyd Warshall Algorithm is for solving the All Pairs Shortest Path problem. The problem is to find shortest distances between every pair of vertices in a given edge weighted directed Graph. 
Example: 

Input:
       graph[][] = { {0,   5,  INF, 10},
                    {INF,  0,  3,  INF},
                    {INF, INF, 0,   1},
                    {INF, INF, INF, 0} }
which represents the following graph
             10
       (0)------->(3)
        |         /|\
      5 |          |
        |          | 1
       \|/         |
       (1)------->(2)
            3       
Note that the value of graph[i][j] is 0 if i is equal to j 
And graph[i][j] is INF (infinite) if there is no edge from vertex i to j.

Output:
Shortest distance matrix
      0      5      8      9
    INF      0      3      4
    INF    INF      0      1
    INF    INF    INF      0
"""


def floydWarshall(graph):
	dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
	for k in range(V):
		# pick all vertices as source one by one
		for i in range(V):
			# Pick all vertices as destination for the above picked source
			for j in range(V):

				# If vertex k is on the shortest path from i to j, then update the value of dist[i][j]
				dist[i][j] = min(dist[i][j],dist[i][k] + dist[k][j])
	printSolution(dist)


# A utility function to print the solution
def printSolution(dist):
	print ("Following matrix shows the shortest distances\
between every pair of vertices")
	for i in range(V):
		for j in range(V):
			if(dist[i][j] == INF):
				print ("%7s" % ("INF"),end=" ")
			else:
				print ("%7d\t" % (dist[i][j]),end=' ')
			if j == V-1:
				print ()



# Let us create the following weighted graph
"""
			10
	(0)------->(3)
		|		 /|\
	5 |		 |
		|		 | 1
	\|/		 |
	(1)------->(2)
			3		 
"""
# Number of vertices in the graph
V = 4
INF = 99999

graph = [[0, 5, INF, 10],
		[INF, 0, 3, INF],
		[INF, INF, 0, 1],
		[INF, INF, INF, 0]
		]

floydWarshall(graph)

```

## Travelling Salesman Problem

```python
"""
Travelling Salesman Problem (TSP): 

Given a set of cities and the distance between every pair of cities, the problem is to find the shortest possible route that visits every city exactly once and returns to the starting point.
"""
n = 4 # there are four nodes in example graph (graph is 1-based)

# dist[i][j] represents shortest distance to go from i to  this matrix can be calculated for any given graph usin all-pair shortest path algorithms
dist = [[0, 0, 0, 0, 0], [0, 0, 10, 15, 20], [
	0, 10, 0, 25, 25], [0, 15, 25, 0, 30], [0, 20, 25, 30, 0]]

# memoization for top down recursion
memo = [[-1]*(1 << (n+1)) for _ in range(n+1)]


def fun(i, mask):
	# base case
	# if only ith bit and 1st bit is set in our mask, it implies we have visited all other nodes already
	if mask == ((1 << i) | 3):
		return dist[1][i]

	# memoization
	if memo[i][mask] != -1:
		return memo[i][mask]

	res = 10**9 # result of this sub-problem

	# we have to travel all nodes j in mask and end the path at ith node so for every node j in mask, recursively calculate cost of travelling all nodes in mask except i and then travel back from node j to node i taking
	# the shortest path take the minimum of all possible j nodes
	for j in range(1, n+1):
		if (mask & (1 << j)) != 0 and j != i and j != 1:
			res = min(res, fun(j, mask & (~(1 << i))) + dist[j][i])
	memo[i][mask] = res # storing the minimum value
	return res



ans = 10**9
for i in range(1, n+1):
	# try to go from node 1 visiting all nodes in between to i then return from i taking the shortest route to 1
	ans = min(ans, fun(i, (1 << (n+1))-1) + dist[i][1])
print(f"The cost of most efficient tour = {str(ans)}")
```

## Graph ColouringProblem

```python
TODO
```

## Snake and Ladders Problem

```python
"""
On an N x N board, the numbers from 1 to N*N are written boustrophedonically starting from the bottom left of the board, and alternating direction each row. For example, for a 6 x 6 board, the numbers are written as follows:

You start on square 1 of the board (which is always in the last row and first column). Each move, starting from square x, consists of the following:

You choose a destination square S with number x+1, x+2, x+3, x+4, x+5, or x+6, provided this number is <= N*N.
(This choice simulates the result of a standard 6-sided die roll: ie., there are always at most 6 destinations, regardless of the size of the board.)
If S has a snake or ladder, you move to the destination of that snake or ladder. Otherwise, you move to S. A board square on row r and column c has a “snake or ladder” if board[r][c] != -1. The destination of that snake or ladder is board[r][c].
Note that you only take a snake or ladder at most once per move: if the destination to a snake or ladder is the start of another snake or ladder, you do not continue moving. (For example, if the board is [[4,-1],[-1,3]], and on the first move your destination square is 2, then you finish your first move at 3, because you do not continue moving to 4.)

Return the least number of moves required to reach square N*N. If it is not possible, return -1.
"""
import collections
def snakesAndLadders(board):
        rows = len(board)
        total_square = rows*rows

        def next_square(step):
                quot, rem = divmod(step-1, rows)
                row = (rows - 1) - quot
                col = rem if row%2 != rows%2 else (rows - 1) - rem
                return row, col

        dist = {1: 0}#square and step
        queue = collections.deque([1])
        while queue:
            square = queue.popleft()
            if square == total_square:
                return dist[square]
            for new_square in range(square+1, min(square+6, total_square) + 1):
                r, c = next_square(new_square)
                if board[r][c] != -1:
                    new_square = board[r][c]
                if new_square not in dist:
                    dist[new_square] = dist[square] + 1
                    queue.append(new_square)
board=[
[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,35,-1,-1,13,-1],
[-1,-1,-1,-1,-1,-1],
[-1,15,-1,-1,-1,-1]]
print(snakesAndLadders(board))
```

## Find bridge in a graph

```python
from collections import defaultdict

#This class represents an undirected graph using adjacency list representation
class Graph:

	def __init__(self,vertices):
		self.V= vertices #No. of vertices
		self.graph = defaultdict(list) # default dictionary to store graph
		self.Time = 0

	# function to add an edge to graph
	def addEdge(self,u,v):
		self.graph[u].append(v)
		self.graph[v].append(u)

	'''
    A recursive function that finds and prints bridges
	using DFS traversal
	u --> The vertex to be visited next
	visited[] --> keeps track of visited vertices
	disc[] --> Stores discovery times of visited vertices
	parent[] --> Stores parent vertices in DFS tree
    '''
	def bridgeUtil(self, u, visited, parent, low, disc):

		# Mark the current node as visited and print it
		visited[u]= True

		# Initialize discovery time and low value
		disc[u] = self.Time
		low[u] = self.Time
		self.Time += 1

		#Recur for all the vertices adjacent to this vertex
		for v in self.graph[u]:
			# If v is not visited yet, then make it a child of u in DFS tree and recur for it
			if visited[v] == False :
				parent[v] = u
				self.bridgeUtil(v, visited, parent, low, disc)

				# Check if the subtree rooted with v has a connection to one of the ancestors of u
				low[u] = min(low[u], low[v])


				''' If the lowest vertex reachable from subtree
				under v is below u in DFS tree, then u-v is
				a bridge'''
				if low[v] > disc[u]:
					print ("%d %d" %(u,v))
	
					
			elif v != parent[u]: # Update low value of u for parent function calls.
				low[u] = min(low[u], disc[v])


	# DFS based function to find all bridges. It uses recursive function bridgeUtil()
	def bridge(self):

		# Mark all the vertices as not visited and Initialize parent and visited, and ap(articulation point) arrays
		visited = [False] * (self.V)
		disc = [float("Inf")] * (self.V)
		low = [float("Inf")] * (self.V)
		parent = [-1] * (self.V)

		# Call the recursive helper function to find bridges in DFS tree rooted with vertex 'i'
		for i in range(self.V):
			if visited[i] == False:
				self.bridgeUtil(i, visited, parent, low, disc)
		


g1 = Graph(5)
g1.addEdge(1, 0)
g1.addEdge(0, 2)
g1.addEdge(2, 1)
g1.addEdge(0, 3)
g1.addEdge(3, 4)


print ("Bridges in first graph ")
g1.bridge()

g2 = Graph(4)
g2.addEdge(0, 1)
g2.addEdge(1, 2)
g2.addEdge(2, 3)
print ("\nBridges in second graph ")
g2.bridge()


g3 = Graph (7)
g3.addEdge(0, 1)
g3.addEdge(1, 2)
g3.addEdge(2, 0)
g3.addEdge(1, 3)
g3.addEdge(1, 4)
g3.addEdge(1, 6)
g3.addEdge(3, 5)
g3.addEdge(4, 5)
print ("\nBridges in third graph ")
g3.bridge()
```

## Count Strongly connected Components(Kosaraju Algo)

```python
from collections import defaultdict
class Graph:
	def __init__(self,vertices):
		self.V= vertices 
		self.graph = defaultdict(list) 

	def addEdge(self,u,v):
		self.graph[u].append(v)

	# A function used by DFS
	def DFSUtil(self,v,visited):
		# Mark the current node as visited and print it
		visited[v]= True
		print (v)
		#Recur for all the vertices adjacent to this vertex
		for i in self.graph[v]:
			if visited[i]==False:
				self.DFSUtil(i,visited)


	def fillOrder(self,v,visited, stack):
		# Mark the current node as visited
		visited[v]= True
		#Recur for all the vertices adjacent to this vertex
		for i in self.graph[v]:
			if visited[i]==False:
				self.fillOrder(i, visited, stack)
		stack = stack.append(v)
	

	# Function that returns reverse (or transpose) of this graph
	def getTranspose(self):
		g = Graph(self.V)

		# Recur for all the vertices adjacent to this vertex
		for i in self.graph:
			for j in self.graph[i]:
				g.addEdge(j,i)
		return g



	# The main function that finds and prints all strongly connected components
	def printSCCs(self):
		
		stack = []
		# Mark all the vertices as not visited (For first DFS)
		visited =[False]*(self.V)
		# Fill vertices in stack according to their finishing times
		for i in range(self.V):
			if visited[i]==False:
				self.fillOrder(i, visited, stack)

		# Create a reversed graph
		gr = self.getTranspose()
		
		# Mark all the vertices as not visited (For second DFS)
		visited =[False]*(self.V)

		# Now process all vertices in order defined by Stack
		while stack:
			i = stack.pop()
			if visited[i]==False:
				gr.DFSUtil(i, visited)
				print()

# Create a graph given in the above diagram
g = Graph(5)
g.addEdge(1, 0)
g.addEdge(0, 2)
g.addEdge(2, 1)
g.addEdge(0, 3)
g.addEdge(3, 4)
print ("Following are strongly connected components " + "in given graph")
g.printSCCs()
```

## Check whether a graph is Bipartite or Not

```python
V = 4

def colorGraph(G, color, pos, c):
	if color[pos] not in [-1, c]:
		return False

	# color this pos as c and all its neighbours and 1-c
	color[pos] = c
	ans = True
	for i in range(V):
		if G[pos][i]:
			if color[i] == -1:
				ans &= colorGraph(G, color, i, 1-c)
			if color[i] not in [-1, 1 - c]:
				return False
		if not ans:
			return False
	return True

def isBipartite(G):
	color = [-1] * V
	#start is vertex 0
	pos = 0
	# two colors 1 and 0
	return colorGraph(G, color, pos, 1)

G = [[0, 1, 0, 1],
	[1, 0, 1, 0],
	[0, 1, 0, 1],
	[1, 0, 1, 0]]

if isBipartite(G): print("Yes")
else: print("No")
```

## Longest path in a Directed Acyclic Graph

```python
def topologicalSortUtil(v):
	global Stack, visited, adj
	visited[v] = True
	for i in adj[v]:
		if (not visited[i[0]]):
			topologicalSortUtil(i[0])
	Stack.append(v)

# The function to find longest distances from a given vertex. It uses recursive topologicalSortUtil() to get topological sorting.
def longestPath(s):
	global Stack, visited, adj, V
	dist = [-10**9 for _ in range(V)]

	# Call the recursive helper function to store Topological Sort starting from all vertices one by one
	for i in range(V):
		if (visited[i] == False):
			topologicalSortUtil(i)

	# Initialize distances to all vertices as infinite and distance to source as 0
	dist[s] = 0

	# Process vertices in topological order
	while (len(Stack) > 0):

		# Get the next vertex from topological order
		u = Stack[-1]
		del Stack[-1]

		# Update distances of all adjacent vertices
		if (dist[u] != 10**9):
			for i in adj[u]:
				if (dist[i[0]] < dist[u] + i[1]):
					dist[i[0]] = dist[u] + i[1]

	# Print calculated longest distances print(dist)
	for i in range(V):
		print("INF ",end="") if (dist[i] == -10**9) else print(dist[i],end=" ")


V, Stack, visited = 6, [], [False for _ in range(7)]
adj = [[] for _ in range(7)]
# Create a graph given in the above diagram.
# Here vertex numbers are 0, 1, 2, 3, 4, 5 with following mappings:
# 0=r, 1=s, 2=t, 3=x, 4=y, 5=z
adj[0].append([1, 5])
adj[0].append([2, 3])
adj[1].append([3, 6])
adj[1].append([2, 2])
adj[2].append([4, 4])
adj[2].append([5, 2])
adj[2].append([3, 7])
adj[3].append([5, 1])
adj[3].append([4, -1])
adj[4].append([5, -2])
s = 1
print("Following are longest distances from source vertex ",s)
longestPath(s)
```

## Journey to the Moon

```python
TODO
```

## Cheapest Flights Within K Stops

```python
TODO
```

## Oliver and the Game

```python
TODO
```

## Water Jug problem using BFS

```python
"""
You are given an m liter jug and a n liter jug. Both the jugs are initially empty. The jugs don’t have markings to allow measuring smaller quantities. You have to use the jugs to measure d liters of water where d is less than n. 

(X, Y) corresponds to a state where X refers to the amount of water in Jug1 and Y refers to the amount of water in Jug2 
Determine the path from the initial state (xi, yi) to the final state (xf, yf), where (xi, yi) is (0, 0) which indicates both Jugs are initially empty and (xf, yf) indicates a state which could be (0, d) or (d, 0).

The operations you can perform are: 

Empty a Jug, (X, Y)->(0, Y) Empty Jug 1
Fill a Jug, (0, 0)->(X, 0) Fill Jug 1
Pour water from one jug to the other until one of the jugs is either empty or full, (X, Y) -> (X-d, Y+d)
Examples: 

Input : 4 3 2
Output : {(0, 0), (0, 3), (3, 0), (3, 3), (4, 2), (0, 2)}
"""

from collections import deque

def BFS(a, b, target):
	
	# Map is used to store the states, every state is hashed to binary value to indicate either that state is visited before or not
	m = {}
	isSolvable = False
	path = []
	
	# Queue to maintain states
	q = deque()
	
	# Initialing with initial state
	q.append((0, 0))

	while (len(q) > 0):
		# Current state
		u = q.popleft()

		#q.pop() #pop off used state

		# If this state is already visited
		if ((u[0], u[1]) in m):
			continue

		# Doesn't met jug constraints
		if ((u[0] > a or u[1] > b or
			u[0] < 0 or u[1] < 0)):
			continue

		# Filling the vector for constructing the solution path
		path.append([u[0], u[1]])

		# Marking current state as visited
		m[(u[0], u[1])] = 1

		# If we reach solution state, put ans=1
		if (u[0] == target or u[1] == target):
			isSolvable = True
			
			if (u[0] == target):
				if (u[1] != 0):
					
					# Fill final state
					path.append([u[0], 0])
			else:
				if (u[0] != 0):

					# Fill final state
					path.append([0, u[1]])

			# Print the solution path
			sz = len(path)
			for i in range(sz):
				print("(", path[i][0], ",",
						path[i][1], ")")
			break

		# If we have not reached final state then, start developing intermediate states to reach solution state
		q.append([u[0], b]) # Fill Jug2
		q.append([a, u[1]]) # Fill Jug1

		for ap in range(max(a, b) + 1):

			# Pour amount ap from Jug2 to Jug1
			c = u[0] + ap
			d = u[1] - ap

			# Check if this state is possible or not
			if (c == a or (d == 0 and d >= 0)):
				q.append([c, d])

			# Pour amount ap from Jug 1 to Jug2
			c = u[0] - ap
			d = u[1] + ap

			# Check if this state is possible or not
			if ((c == 0 and c >= 0) or d == b):
				q.append([c, d])
		
		# Empty Jug2
		q.append([a, 0])
		
		# Empty Jug1
		q.append([0, b])

	# No, solution exists if ans=0
	if (not isSolvable):
		print ("No solution")


Jug1, Jug2, target = 4, 3, 2
print("Path from initial state to solution state ::")
BFS(Jug1, Jug2, target)
```

## Find if there is a path of more thank length from a source

```python
"""
Given a graph, a source vertex in the graph and a number k, find if there is a simple path (without any cycle) starting from given source and ending at any other vertex such that the distance from source to that vertex is atleast ‘k’ length.

Example:

Input  : Source s = 0, k = 58
Output : True
There exists a simple path 0 -> 7 -> 1
-> 2 -> 8 -> 6 -> 5 -> 3 -> 4
Which has a total distance of 60 km which
is more than 58.

Input  : Source s = 0, k = 62
Output : False

In the above graph, the longest simple
path has distance 61 (0 -> 7 -> 1-> 2
 -> 3 -> 4 -> 5-> 6 -> 8, so output 
should be false for any input greater 
than 61.
"""
# Program to find if there is a simple path with
# weight more than k
	
# This class represents a dipathted graph using
# adjacency list representation
class Graph:
	# Allocates memory for adjacency list
	def __init__(self, V):
		self.V = V
		self.adj = [[] for _ in range(V)]
	
	# Returns true if graph has path more than k length
	def pathMoreThanK(self,src, k):
		# Create a path array with nothing included in path
		path = [False]*self.V
		
		# Add source vertex to path
		path[src] = 1
		
		return self.pathMoreThanKUtil(src, k, path)
		
	# Prints shortest paths from src to all other vertices
	def pathMoreThanKUtil(self,src, k, path):
		# If k is 0 or negative, return true
		if (k <= 0):
			return True
		
		# Get all adjacent vertices of source vertex src and recursively explore all paths from src.
		i = 0
		while i != len(self.adj[src]):
			# Get adjacent vertex and weight of edge
			v = self.adj[src][i][0]
			w = self.adj[src][i][1]
			i += 1
		
			# If vertex v is already there in path, then there is a cycle (we ignore this edge)
			if (path[v] == True):
				continue
		
			# If weight of is more than k, return true
			if (w >= k):
				return True
		
			# Else add this vertex to path
			path[v] = True
		
			# If this adjacent can provide a path longer than k, return true.
			if (self.pathMoreThanKUtil(v, k-w, path)):
				return True
		
			# Backtrack
			path[v] = False
		
		# If no adjacent could produce longer path, return false
		return False
	
	# Utility function to an edge (u, v) of weight w
	def addEdge(self,u, v, w):
		self.adj[u].append([v, w])
		self.adj[v].append([u, w])

# create the graph given in above figure
V = 9
g = Graph(V)

# making above shown graph
g.addEdge(0, 1, 4)
g.addEdge(0, 7, 8)
g.addEdge(1, 2, 8)
g.addEdge(1, 7, 11)
g.addEdge(2, 3, 7)
g.addEdge(2, 8, 2)
g.addEdge(2, 5, 4)
g.addEdge(3, 4, 9)
g.addEdge(3, 5, 14)
g.addEdge(4, 5, 10)
g.addEdge(5, 6, 2)
g.addEdge(6, 7, 1)
g.addEdge(6, 8, 6)
g.addEdge(7, 8, 7)

src = 0
k = 62
if g.pathMoreThanK(src, k):
	print("Yes")
else:
	print("No")

k = 60
if g.pathMoreThanK(src, k):
	print("Yes")
else:
	print("No")
```

## Minimum edges to reverse o make path from source to destination

```python
"""
Given a directed graph and a source node and destination node, we need to find how many edges we need to reverse in order to make at least 1 path from the source node to the destination node.
"""

def addEdge(u, v, w):
	global adj
	adj[u].append((v, w))

def shortestPath(src):

	# Create a set to store vertices that are being preprocessed
	setds = {}

	# Create a vector for distances and initialize all distances as infinite (INF)
	dist = [10**18 for _ in range(V)]

	# Insert source itself in Set and initialize its
	global adj
	setds[(0, src)] = 1
	dist[src] = 0

	while setds:

		# The first vertex in Set is the minimum distance vertex, extract it from set.
		tmp = list(setds.keys())[0]
		del setds[tmp]

		# vertex label is stored in second of pair (it has to be done this way to keep the vertices sorted distance (distance must be first item in pair)
		u = tmp[1]

		# 'i' is used to get all adjacent vertices of a vertex
		# list< pair<int, int> >::iterator i;
		for i in adj[u]:

			# Get vertex label and weight of current adjacent
			# of u.
			v = i[0];
			weight = i[1]

			# If there is shorter path to v through u.
			if (dist[v] > dist[u] + weight):

				# /* If distance of v is not INF then it must be in
				#	 our set, so removing it and inserting again
				#	 with updated less distance.
				#	 Note : We extract only those vertices from Set
				#	 for which distance is finalized. So for them,
				#	 we would never reach here. */
				if (dist[v] != 10**18):
					del setds[(dist[v], v)]

				# Updating distance of v
				dist[v] = dist[u] + weight
				setds[(dist[v], v)] = 1

	return dist

# method adds reverse edge of each original edge in the graph. It gives reverse edge a weight = 1 and all original edges a weight of 0. Now, the length of the shortest path will give us the answer. If shortest path is p: it means we used p reverse edges in the shortest path. 
def modelGraphWithEdgeWeight(edge, E, V):
	global adj
	for i in range(E):
		addEdge(edge[i][0], edge[i][1], 0) # original edge : weight 0
		addEdge(edge[i][1], edge[i][0], 1) # reverse edge : weight 1

# Method returns minimum number of edges to be reversed to reach from src to dest
def getMinEdgeReversal(edge, E, V,src, dest):
	# get modified graph with edge weight
	modelGraphWithEdgeWeight(edge, E, V)

	# get shortes path vector
	dist = shortestPath(src)

	# If distance of destination is still INF, not possible
	return -1 if (dist[dest] == 10**18) else dist[dest]


V = 7
edge = [[0, 1], [2, 1], [2, 3], [5, 1],[4, 5], [6, 4], [6, 3]]
E, adj = len(edge), [[] for _ in range(V + 1)]
minEdgeToReverse = getMinEdgeReversal(edge, E, V, 0, 6)
if (minEdgeToReverse != -1):
	print(minEdgeToReverse)
else:
	print("Not possible")
```

## Paths to travel each nodes using each edge(Seven Bridges)

```python
TODO
```

## Vertex Cover Problem

```python
"""
There are n nodes and m bridges in between these nodes. Print the possible path through each node using each edges (if possible), traveling through each edges only once.
"""

from collections import defaultdict

class Graph:
	def __init__(self, vertices):
		self.V = vertices
		self.graph = defaultdict(list)


	def addEdge(self, u, v):
		self.graph[u].append(v)


	def printVertexCover(self):
		# Initialize all vertices as not visited.
		visited = [False] * (self.V)
		
		# Consider all edges one by one
		for u in range(self.V):
			
			# An edge is only picked when both visited[u] and visited[v] are false
			if not visited[u]:
				
				# Go through all adjacents of u and pick the first not yet visited
				# vertex (We are basically picking an edge (u, v) from remaining edges.
				for v in self.graph[u]:
					if not visited[v]:
						
						# Add the vertices (u, v) to the
						# result set. We make the vertex u and v visited so that all
						# edges from/to them would be ignored
						visited[v] = True
						visited[u] = True
						break

		# Print the vertex cover
		for j in range(self.V):
			if visited[j]:
				print(j, end = ' ')
		print()

g = Graph(7)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 3)
g.addEdge(3, 4)
g.addEdge(4, 5)
g.addEdge(5, 6)
g.printVertexCover()
```

## Chinese Postman or Route Inspection

```python
TODO
```

## Number of Triangles in a Directed and Undirected Graph

```python
"""
Given a Graph, count number of triangles in it. The graph is can be directed or undirected.

Example: 

Input: digraph[V][V] = { {0, 0, 1, 0},
                        {1, 0, 0, 1},
                        {0, 1, 0, 0},
                        {0, 0, 1, 0}
                      };
Output: 2
Give adjacency matrix represents following 
directed graph.
"""

# function to calculate the number of triangles in a simple directed/undirected graph.
# isDirected is true if the graph is directed, its false otherwise
def countTriangle(g, isDirected):
    nodes = len(g)
    count_Triangle = 0
    # Consider every possible triplet of edges in graph
    for i in range(nodes):
        for j in range(nodes):
            for k in range(nodes):
                # check the triplet if it satisfies the condition
                if(i != j and i != k and j != k and g[i][j] and g[j][k] and g[k][i]):
                    count_Triangle += 1
          
    # If graph is directed , division is done by 3 else division by 6 is done
    if isDirected:
      return (count_Triangle//3)
    else: 
      return (count_Triangle//6)


# Create adjacency matrix of an undirected graph
graph = [[0, 1, 1, 0],
		[1, 0, 1, 1],
		[1, 1, 0, 1],
		[0, 1, 1, 0]]
# Create adjacency matrix of a directed graph
digraph = [[0, 0, 1, 0],
		[1, 0, 0, 1],
		[0, 1, 0, 0],
		[0, 0, 1, 0]]

print("The Number of triangles in undirected graph : %d" %
	countTriangle(graph, False))

print("The Number of triangles in directed graph : %d" %
	countTriangle(digraph, True))
```

## Minimise the cashflow among a given set of friends who have borrowed money from each other

```python
"""
Given a number of friends who have to give or take some amount of money from one another. Design an algorithm by which the total cash flow among all the friends is minimized. 
"""

# Number of persons(or vertices in graph)
N = 3

# A utility function that returns index of minimum value in arr[]
def getMin(arr):
	minInd = 0
	for i in range(1, N):
		if (arr[i] < arr[minInd]):
			minInd = i
	return minInd

# A utility function that returns index of maximum value in arr[]
def getMax(arr):
	maxInd = 0
	for i in range(1, N):
		if (arr[i] > arr[maxInd]):
			maxInd = i
	return maxInd


def minOf2(x, y):
	return x if x < y else y

# amount[p] indicates the net amount to be credited/debited to/from person 'p' If amount[p] is positive, then i'th person will amount[i] If amount[p] is negative, then i'th person will give -amount[i]
def minCashFlowRec(amount):

	# Find the indexes of minimum and maximum values in amount[] amount[mxCredit] indicates the maximum amount to be given(or credited) to any person. And amount[mxDebit] indicates the maximum amount to be taken (or debited) from any person. So if there is a positive value in amount[], then there must be a negative value
	mxCredit = getMax(amount)
	mxDebit = getMin(amount)

	# If both amounts are 0, then all amounts are settled
	if (amount[mxCredit] == 0 and amount[mxDebit] == 0):
		return 0

	# Find the minimum of two amounts
	min = minOf2(-amount[mxDebit], amount[mxCredit])
	amount[mxCredit] -=min
	amount[mxDebit] += min

	# If minimum is the maximum amount to be
	print("Person " , mxDebit , " pays " , min
		, " to " , "Person " , mxCredit)

	# Recur for the amount array. Note that it is guaranteed that the recursion would terminate as either amount[mxCredit] or amount[mxDebit] becomes 0
	minCashFlowRec(amount)

# Given a set of persons as graph[] where graph[i][j] indicates the amount that person i needs to pay person j, this function finds and prints the minimum cash flow to settle all debts.
def minCashFlow(graph):

	# Create an array amount[], initialize all value in it as 0.
	amount = [0 for _ in range(N)]

	# Calculate the net amount to be paid to person 'p', and stores it in amount[p]. The value of amount[p] can be calculated by subtracting debts of 'p' from credits of 'p'
	for p in range(N):
		for i in range(N):
			amount[p] += (graph[i][p] - graph[p][i])

	minCashFlowRec(amount)


# graph[i][j] indicates the amount that person i needs to pay person j
graph = [ [0, 1000, 2000],
		[0, 0, 5000],
		[0, 0, 0] ]
minCashFlow(graph)
```

## Two Clique Problem

```python
"""
A Clique is a subgraph of graph such that all vertices in subgraph are completely connected with each other. Given a Graph, find if it can be divided into two Cliques.

Examples:

Input : G[][] =   {{0, 1, 1, 0, 0},
                  {1, 0, 1, 1, 0},
                  {1, 1, 0, 0, 0},
                  {0, 1, 0, 0, 1},
                  {0, 0, 0, 1, 0}};
Output : Yes
"""

from queue import Queue

# This function returns true if subgraph reachable from src is Bipartite or not.
def isBipartiteUtil(G, src, colorArr):
	global V
	colorArr[src] = 1

	# Create a queue (FIFO) of vertex numbers and enqueue source vertex for BFS traversal
	q = Queue()
	q.put(src)

	# Run while there are vertices in queue (Similar to BFS)
	while (not q.empty()):
		
		# Dequeue a vertex from queue
		u = q.get()

		# Find all non-colored adjacent vertices
		for v in range(V):
			
			# An edge from u to v exists and destination v is not colored
			if (G[u][v] and colorArr[v] == -1):
				
				# Assign alternate color to this adjacent v of u
				colorArr[v] = 1 - colorArr[u]
				q.put(v)

			# An edge from u to v exists and destination v is colored with same color as u
			elif (G[u][v] and colorArr[v] == colorArr[u]):
				return False

	# If we reach here, then all adjacent vertices can be colored with alternate color
	return True

# Returns true if a Graph G[][] is Bipartite or Note that G may not be connected.
def isBipartite(G):
	global V
	# Create a color array to store colors assigned to all vertices. Vertex number is used as index in this array. The value '-1' of colorArr[i] is used to indicate that no color is assigned to vertex 'i'. The value 1 is used to indicate first color is assigned and value 0 indicates second color is assigned.
	colorArr = [-1] * V

	# One by one check all not yet colored vertices.
	for i in range(V):
		if (colorArr[i] == -1):
			if (isBipartiteUtil(G, i, colorArr) == False):
				return False

	return True

# Returns true if G can be divided into
# two Cliques, else false.
def canBeDividedinTwoCliques(G):
	global V
	# Find complement of G[][] All values are complemented except diagonal ones
	GC = [[None] * V for _ in range(V)]
	for i in range(V):
		for j in range(V):
			GC[i][j] = not G[i][j] if i != j else 0

	# Return true if complement is Bipartite else false.
	return isBipartite(GC)


V = 5
G = [[0, 1, 1, 1, 0],
	[1, 0, 1, 0, 0],
	[1, 1, 0, 0, 0],
	[0, 1, 0, 0, 1],
	[0, 0, 0, 1, 0]]
if canBeDividedinTwoCliques(G):
	print("Yes")
else:
	print("No")

```