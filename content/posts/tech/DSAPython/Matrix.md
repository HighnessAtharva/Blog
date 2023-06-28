---
title: "DSA in Python - Matrix"
date: 2022-07-09T13:14:34+05:30
draft: true
cover: 
    image: blog/dsa/matrix.jpg
    alt: Matrix
    caption: Learn Matrix Algorithms in Python
tags: ["python"] 

---

- [Spiral traversal on a Matrix](#spiral-traversal-on-a-matrix)
- [Search an element in a matrix](#search-an-element-in-a-matrix)
- [Find median in a row wise sorted matrix](#find-median-in-a-row-wise-sorted-matrix)
- [Find row with maximum no. of 1's](#find-row-with-maximum-no-of-1s)
- [Print elements in sorted order using row-column wise sorted matrix](#print-elements-in-sorted-order-using-row-column-wise-sorted-matrix)
- [Maximum size rectangle](#maximum-size-rectangle)
- [Find a specific pair in matrix](#find-a-specific-pair-in-matrix)
- [Rotate matrix by 90 degrees](#rotate-matrix-by-90-degrees)
- [Kth smallest element in a row-column wise sorted matrix](#kth-smallest-element-in-a-row-column-wise-sorted-matrix)
- [Common elements in all rows of a given matrix](#common-elements-in-all-rows-of-a-given-matrix)

## Spiral traversal on a Matrix

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

## Search an element in a matrix

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

## Find median in a row wise sorted matrix

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

## Find row with maximum no. of 1's

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

## Print elements in sorted order using row-column wise sorted matrix

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

## Maximum size rectangle

```python
class Solution():
	def maxHist(self, row):
		# Create an empty stack. The stack holds indexes of hist array / The bars stored in stack are always in increasing order of their heights.
		result = []
		top_val = 0 # Top of stack
		max_area = 0 # Initialize max area in current
		area = 0 # Initialize area with current top

		# Run through all bars of given histogram (or row)
		i = 0
		while (i < len(row)):

			# If this bar is higher than the bar on top stack, push it to stack
			if not result or row[result[-1]] <= row[i]:
				result.append(i)
				i += 1
			else:

				# If this bar is lower than top of stack, then calculate area of rectangle with stack top as the smallest (or minimum height) bar. 'i' is 'right index' for the top and element before top in stack is 'left index'
				top_val = row[result.pop()]
				area = top_val * i

				if (len(result)):
					area = top_val * (i - result[-1] - 1)
				max_area = max(area, max_area)

		# Now pop the remaining bars from stack and calculate area with every popped bar as the smallest bar
		while (len(result)):
			top_val = row[result.pop()]
			area = top_val * i
			if (len(result)):
				area = top_val * (i - result[-1] - 1)

			max_area = max(area, max_area)

		return max_area

	# Returns area of the largest rectangle with all 1s in A
	def maxRectangle(self, A):

		# Calculate area for first row and initialize it as result
		result = self.maxHist(A[0])

		# iterate over row to find maximum rectangular area considering each row as histogram
		for i in range(1, len(A)):
			for j in range(len(A[i])):

				# if A[i][j] is 1 then add A[i -1][j]
				if (A[i][j]):
					A[i][j] += A[i - 1][j]

			# Update result if area with current row (as last row) of rectangle) is more
			result = max(result, self.maxHist(A[i]))

		return result

A = [[0, 1, 1, 0],
	[1, 1, 1, 1],
	[1, 1, 1, 1],
	[1, 1, 0, 0]]
ans = Solution()
print("Area of maximum rectangle is", ans.maxRectangle(A))
```

## Find a specific pair in matrix

```python
import sys

# The function returns maximum value A(c,d) - A(a,b) over all choices of indexes such that both c > a and d > b.
def findMaxValue(mat):

	# stores maximum value
	maxValue = -sys.maxsize -1

	# maxArr[i][j] stores max of elements in matrix from (i, j) to (N-1, N-1)
	maxArr = [[0 for _ in range(N)] for _ in range(N)]

	# last element of maxArr will be same's as of the input matrix
	maxArr[N - 1][N - 1] = mat[N - 1][N - 1]

	# preprocess last row
	maxv = mat[N - 1][N - 1]
	for j in range (N - 2, -1, -1):

		if (mat[N - 1][j] > maxv):
			maxv = mat[N - 1][j]
		maxArr[N - 1][j] = maxv

	# preprocess last column
	maxv = mat[N - 1][N - 1] # Initialize max
	for i in range (N - 2, -1, -1):

		if (mat[i][N - 1] > maxv):
			maxv = mat[i][N - 1]
		maxArr[i][N - 1] = maxv

	# preprocess rest of the matrix from bottom
	for i in range (N - 2, -1, -1):

		for j in range (N - 2, -1, -1):

			# Update maxValue
			if (maxArr[i + 1][j + 1] -
				mat[i][j] > maxValue):
				maxValue = (maxArr[i + 1][j + 1] - mat[i][j])

			# set maxArr (i, j)
			maxArr[i][j] = max(mat[i][j], max(maxArr[i][j + 1], maxArr[i + 1][j]))

	return maxValue

N = 5
mat = [[ 1, 2, -1, -4, -20 ],
	[-8, -3, 4, 2, 1 ],
	[ 3, 8, 6, 1, 3 ],
	[ -4, -1, 1, 7, -6] ,
	[0, -4, 10, -5, 1 ]]
					
print ("Maximum Value is", findMaxValue(mat))
```

## Rotate matrix by 90 degrees

```python
N = 4
def rotate90Clockwise(arr) :
	global N
	for j in range(N) :
		for i in range(N - 1, -1, -1) :
			print(arr[i][j], end = " ")
		print()
		
# Driver code	
arr = [ [ 1, 2, 3, 4 ],
		[ 5, 6, 7, 8 ],
		[ 9, 10, 11, 12 ],
		[ 13, 14, 15, 16 ] ]
rotate90Clockwise(arr);
```

## Kth smallest element in a row-column wise sorted matrix

```python
def kthSmallest(mat, n, k):
	a = [0 for _ in range(n*n)]
	v=0
	for i in range(n):
		for j in range(n):
			a[v] = mat[i][j]
			v += 1
	a.sort()
	return a[k - 1]

mat = [ [ 10, 20, 30, 40 ],
			[ 15, 25, 35, 45 ],
			[ 25, 29, 37, 48 ],
			[ 32, 33, 39, 50 ] ]
res = kthSmallest(mat, 4, 7)
print(f"7th smallest element is {str(res)}")
```

## Common elements in all rows of a given matrix

```python
def printCommonElements(mat):
	mp = {mat[0][j]: 1 for j in range(N)}

	# traverse the matrix
	for i in range(1, M):
		for j in range(N):

			# If element is present in the map and is not duplicated in current row.
			if mat[i][j] in mp and mp[mat[i][j]] == i:
			# we increment count of the element in map by 1
				mp[mat[i][j]] = i + 1

				# If this is last row
				if i == M - 1:
					print(mat[i][j], end = " ")

# Specify number of rows and columns
M = 4
N = 5
mat = [[1, 2, 1, 4, 8],
	[3, 7, 8, 5, 1],
	[8, 7, 7, 3, 1],
	[8, 1, 2, 7, 9]]
printCommonElements(mat)
```