---
title: "DSA in Python - Matrix"
date: 2022-07-09T13:14:34+05:30
draft: false
cover: 
    image: blog/dsa/Matrix.webp
    alt: Matrix
    caption: Learn Matrix Algorithms in Python
tags: ["python"] 

---

## Free Preview - 5 Matrix Problems

### Spiral traversal on a Matrix

```python

def spiralOrder(matrix):
	ans = []
	if (len(matrix) == 0):
		return ans

	m = len(matrix)
	n = len(matrix[0])
	seen = [[0 for _ in range(n)] for _ in range(m)]
	dr = [0, 1, 0, -1]
	dc = [1, 0, -1, 0]
	x = 0
	y = 0
	di = 0

	# Iterate from 0 to R * C - 1
	for _ in range(m * n):
		ans.append(matrix[x][y])
		seen[x][y] = True
		cr = x + dr[di]
		cc = y + dc[di]

		if cr >= 0 and cr < m and cc >= 0 and cc < n and not (seen[cr][cc]):
			x = cr
			y = cc
		else:
			di = (di + 1) % 4
			x += dr[di]
			y += dc[di]
	return ans


a = [[1, 2, 3, 4],
	[5, 6, 7, 8],
	[9, 10, 11, 12],
	[13, 14, 15, 16]]

for x in spiralOrder(a):
	print(x, end=" ")
print()
```

### Search an element in a matrix

```python
def search(mat, n, x):
	if(n == 0):
		return -1
	for i in range(n):
		for j in range(n):
			if(mat[i][j] == x):
				print("Element found at (", i, ",", j, ")")
				return 1
	print(" Element not found")
	return 0


mat = [[10, 20, 30, 40], [15, 25, 35, 45],[27, 29, 37, 48],[32, 33, 39, 50]]
search(mat, 4, 29)
```

### Find median in a row wise sorted matrix

```python
from bisect import bisect_right as upper_bound
MAX = 100;

def binaryMedian(m, r, d):
	mi = m[0][0]
	mx = 0
	for i in range(r):
		if m[i][0] < mi:
			mi = m[i][0]
		if m[i][d-1] > mx :
			mx = m[i][d-1]
	
	desired = (r * d + 1) // 2
	
	while (mi < mx):
		mid = mi + (mx - mi) // 2
		place = [0];
		
		for i in range(r):
			j = upper_bound(m[i], mid)
			place[0] = place[0] + j
		if place[0] < desired:
			mi = mid + 1
		else:
			mx = mid
	print ("Median is", mi)
	return
	
r, d = 3, 3
m = [ [1, 3, 5], [2, 6, 9], [3, 6, 9]]
binaryMedian(m, r, d)
```

### Find row with maximum no. of 1's

```python
def first(arr , low , high):
	if(high >= low):
		# Get the middle index
		mid = low + (high - low)//2
		# Check if the element at middle index is first 1
		if ( ( mid == 0 or arr[mid-1] == 0) and arr[mid] == 1):
			return mid
		# If the element is 0, recur for right side
		elif (arr[mid] == 0):
			return first(arr, (mid + 1), high);
		# If element is not first 1, recur for left side
		else:
			return first(arr, low, (mid -1));
	return -1

def rowWithMax1s(mat):
	# Initialize max values
	max_row_index,Max = 0,-1

	# Traverse for each row and count number of 1s by finding the index of first 1
	for i in range(R):
		index = first (mat[i], 0, C-1)
		if (index != -1 and C-index > Max):
			Max = C - index;
			max_row_index = i
	return max_row_index

R,C = 4,4

mat = [[0, 0, 0, 1],
	[0, 1, 1, 1],
	[1, 1, 1, 1],
	[0, 0, 0, 0]]
print(f"Index of row with maximum 1s is {str(rowWithMax1s(mat))}")

```

### Print elements in sorted order using row-column wise sorted matrix

```python
import sys
INF = sys.maxsize

# A utility function to youngify a Young Tableau. This is different from standard youngify. It assumes that the value at mat[0][0] is infinite.
def youngify(mat, i, j):
	# Find the values at down and right sides of mat[i][j]
	downVal = mat[i + 1][j] if (i + 1 < N) else INF
	rightVal = mat[i][j + 1] if (j + 1 < N) else INF

	# If mat[i][j] is the down right corner element, return
	if (downVal == INF and rightVal == INF):
		return

	# Move the smaller of two values (downVal and rightVal) to mat[i][j] and recur for smaller value
	if (downVal < rightVal):
		mat[i][j] = downVal
		mat[i + 1][j] = INF
		youngify(mat, i + 1, j)
	
	else:
		mat[i][j] = rightVal
		mat[i][j + 1] = INF
		youngify(mat, i, j + 1)

# A utility function to extract minimum element from Young tableau
def extractMin(mat):
	ret = mat[0][0]
	mat[0][0] = INF
	youngify(mat, 0, 0)
	return ret

def printSorted(mat):
	print("Elements of matrix in sorted order n")
	i = 0
	while i < N * N:
		print(extractMin(mat), end = " ")
		i += 1

N = 4
mat = [[10, 20, 30, 40],
	[15, 25, 35, 45],
	[27, 29, 37, 48],
	[32, 33, 39, 50]]
printSorted(mat)
```

## Buy the Interview Guide

{{< gumroad "https://highnessatharva.gumroad.com/l/dsa-python-matrix" "/blog/gumroad-marketing.webp" >}}