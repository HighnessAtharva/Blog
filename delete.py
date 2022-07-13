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


