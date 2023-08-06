---
title: "DSA in Python - Greedy"
date: 2022-07-09T13:14:34+05:30
draft: false
cover: 
    image: blog/dsa/Greedy.webp
    alt: Greedy
    caption: Learn Greedy Algorithms in Python
description: "Master FAANG Interviews with the most frequently asked Greedy problems with solutions and comprehensive explanations. Boost Skills, Get Paid!"
tags: ["python"] 

---

## Free Preview - 5 Greedy Problems

### Activity Selection Problem

```python
"""
There is one meeting room in a firm. There are N meetings in the form of (start[i], end[i]) where start[i] is start time of meeting i and end[i] is finish time of meeting i.
What is the maximum number of meetings that can be accommodated in the meeting room when only one meeting can be held in the meeting room at a particular time?

Note: Start time of one chosen meeting can't be equal to the end time of the other chosen meeting.


Example 1:

Input:
N = 6
start[] = {1,3,0,5,8,5}
end[] =  {2,4,6,7,9,9}
Output: 
4
Explanation:
Maximum four meetings can be held with
given start and end timings.
The meetings are - (1, 2),(3, 4), (5,7) and (8,9)
"""

class meeting:
	def __init__(self, start, end, pos):
		self.start = start
		self.end = end
		self.pos = pos


def maxMeeting(l, n):

	# Sorting of meeting according to heir finish time.
	l.sort(key = lambda x: x.end)

	ans = [l[0].pos]
	# time_limit to check whether new meeting can be conducted or not.
	time_limit = l[0].end

	# Check for all meeting whether it can be selected or not.
	for i in range(1, n):
		if l[i].start > time_limit:
			ans.append(l[i].pos)
			time_limit = l[i].end

	# Print final selected meetings
	for i in ans:
		print(i + 1, end = "")
	print()


s = [ 1, 3, 0, 5, 8, 5 ]	# Starting time
f = [ 2, 4, 6, 7, 9, 9 ]	# Finish time
n = len(s)
l = [meeting(s[i], f[i], i) for i in range(n)]
maxMeeting(l, n)
```

### Huffman Coding

```python
# A Huffman Tree Node
class node:
	def __init__(self, freq, symbol, left=None, right=None):
		# frequency of symbol
		self.freq = freq

		# symbol name (character)
		self.symbol = symbol

		# node left of current node
		self.left = left

		# node right of current node
		self.right = right

		# tree direction (0/1)
		self.huff = ''


def printNodes(node, val=''):
	# huffman code for current node
	newVal = val + str(node.huff)

	# if node is not an edge node then traverse inside it
	if(node.left):
		printNodes(node.left, newVal)
	if(node.right):
		printNodes(node.right, newVal)

		# if node is edge node then display its huffman code
	if(not node.left and not node.right):
		print(f"{node.symbol} -> {newVal}")


# characters for huffman tree
chars = ['a', 'b', 'c', 'd', 'e', 'f']

# frequency of characters
freq = [ 5, 9, 12, 13, 16, 45]

# list containing unused nodes
nodes = [node(freq[x], chars[x]) for x in range(len(chars))]

while len(nodes) > 1:
	# sort all the nodes in ascending order based on theri frequency
	nodes = sorted(nodes, key=lambda x: x.freq)

	# pick 2 smallest nodes
	left = nodes[0]
	right = nodes[1]

	# assign directional value to these nodes
	left.huff = 0
	right.huff = 1

	# combine the 2 smallest nodes to create new node as their parent
	newNode = node(left.freq+right.freq, left.symbol+right.symbol, left, right)

	# remove the 2 nodes and add their parent as new node among others
	nodes.remove(left)
	nodes.remove(right)
	nodes.append(newNode)

# Huffman Tree is ready!
printNodes(nodes[0])
```

### Water Connection Problem

```python
"""Every house in the colony has at most one pipe going into it and at most one pipe going out of it. Tanks and taps are to be installed in a manner such that every house with one outgoing pipe but no incoming pipe gets a tank installed on its roof and every house with only an incoming pipe and no outgoing pipe gets a tap.

Given two integers n and p denoting the number of houses and the number of pipes. The connections of pipe among the houses contain three input values: a_i, b_i, d_i denoting the pipe of diameter d_i from house a_i to house b_i, find out the efficient solution for the network. 

The output will contain the number of pairs of tanks and taps t installed in first line and the next t lines contain three integers: house number of tank, house number of tap and the minimum diameter of pipe between them.

Examples: 
 

Input:  4 2
        1 2 60
        3 4 50
Output: 2
        1 2 60
        3 4 50
Explanation:
Connected components are: 1->2 and 3->4
Therefore, our answer is 2 followed by 1 2 60 and 3 4 50.

Input: 9 6
       7 4 98
       5 9 72
       4 6 10
       2 8 22
       9 7 17
       3 1 66
Output: 3
        2 8 22
        3 1 66
        5 6 10
Explanation:
Connected components are 3->1, 5->9->7->4->6 and 2->8. 
Therefore, our answer is 3 followed by 2 8 22, 3 1 66, 5 6 10
"""

# number of houses and number of pipes
n = 0
p = 0

# Array rd stores the ending vertex of pipe
rd = [0]*1100

# Array wd stores the value of diameters between two pipes
wt = [0]*1100

# Array cd stores the starting end of pipe
cd = [0]*1100

# List a, b, c are used to store the final output
a = []
b = []
c = []

ans = 0

def dfs(w):
	global ans
	if (cd[w] == 0):
		return w
	if (wt[w] < ans):
		ans = wt[w]
	return dfs(cd[w])

# Function performing calculations.
def solve(arr):
	global ans
	i = 0
	while (i < p):
		q = arr[i][0]
		h = arr[i][1]
		t = arr[i][2]
		cd[q] = h
		wt[q] = t
		rd[h] = q
		i += 1
	a = []
	b = []
	c = []
	
	# If a pipe has no ending vertex but has starting vertex i.e is an outgoing pipe then we need to start DFS with this vertex.
	for j in range(1, n + 1):
		if (rd[j] == 0 and cd[j]):
			ans = 1000000000
			w = dfs(j)
			# We put the details of component in final output array
			a.append(j)
			b.append(w)
			c.append(ans)
	print(len(a))
	for j in range(len(a)):
		print(a[j], b[j], c[j])


n = 9 # number of houses
p = 6 # number of pipes
arr = [[7, 4, 98], [5, 9, 72], [4, 6, 10 ], [2, 8, 22 ], [9, 7, 17], [3, 1, 66]]
solve(arr)
```

### Fractional Knapsack Problem

```python
TODO
```

### Greedy Algorithm to find Minimum number of Coins

```python
"""
Given the weights and values of n items, we need to put these items in a knapsack of capacity W to get the maximum total value in the knapsack.
In Fractional Knapsack, we can break items for maximizing the total value of knapsack. This problem in which we can break an item is also called the fractional knapsack problem. 
Input: 
Items as (value, weight) pairs 
arr[] = {{60, 10}, {100, 20}, {120, 30}} 
Knapsack Capacity, W = 50; 

Output: 
Maximum possible value = 240 
by taking items of weight 10 and 20 kg and 2/3 fraction 
of 30 kg. Hence total price will be 60+100+(2/3)(120) = 240
"""

class ItemValue:
	"""Item Value DataClass"""
	def __init__(self, wt, val, ind):
		self.wt = wt
		self.val = val
		self.ind = ind
		self.cost = val // wt

	def __lt__(self, other):
		return self.cost < other.cost


def getMaxValue(wt, val, capacity):
	"""function to get maximum value """
	iVal = [ItemValue(wt[i], val[i], i) for i in range(len(wt))]
	# sorting items by value
	iVal.sort(reverse=True)
	totalValue = 0
	for i in iVal:
		curWt = int(i.wt)
		curVal = int(i.val)
		if capacity - curWt >= 0:
			capacity -= curWt
			totalValue += curVal
		else:
			fraction = capacity / curWt
			totalValue += curVal * fraction
			capacity = int(capacity - (curWt * fraction))
			break
	return totalValue


wt = [10, 40, 20, 30]
val = [60, 40, 100, 120]
capacity = 50
maxValue = getMaxValue(wt, val, capacity)
print("Maximum value in Knapsack =", maxValue)
```


## Buy the Interview Guide

{{< gumroad "https://highnessatharva.gumroad.com/l/dsa-python-greedy" "/blog/gumroad-marketing.webp" >}}

---