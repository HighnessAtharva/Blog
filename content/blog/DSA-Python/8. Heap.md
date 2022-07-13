---
title: "DSA in Python - Heap"
date: 2022-07-09T13:14:34+05:30
draft: false
cover: 
    image: blog/dsa/heap.jpg
    alt: Heap
    caption: Learn Heap Algorithms in Python
tags: ["DSA-Python"] 

---

- [Implement a Maxheap/MinHeap using arrays and recursion. (Heapify)](#implement-a-maxheapminheap-using-arrays-and-recursion-heapify)
- [Sort an Array using heap. (HeapSort)](#sort-an-array-using-heap-heapsort)
- [Maximum of all subarrays of size k.](#maximum-of-all-subarrays-of-size-k)
- [“k” largest element in an array](#k-largest-element-in-an-array)
- [Kth smallest and largest element in an unsorted array](#kth-smallest-and-largest-element-in-an-unsorted-array)
- [Merge “K” sorted arrays.](#merge-k-sorted-arrays)
- [Merge 2 Binary Max Heaps](#merge-2-binary-max-heaps)
- [Kth largest sum continuous subarrays](#kth-largest-sum-continuous-subarrays)
- [Merge “K” Sorted Linked Lists](#merge-k-sorted-linked-lists)
- [Smallest range in “K” Lists](#smallest-range-in-k-lists)
- [Median in a stream of Integers](#median-in-a-stream-of-integers)
- [Check if a Binary Tree is Heap](#check-if-a-binary-tree-is-heap)
- [Convert BST to Min Heap](#convert-bst-to-min-heap)
- [Convert min heap to max heap](#convert-min-heap-to-max-heap)
- [Minimum sum of two numbers formed from digits of an array](#minimum-sum-of-two-numbers-formed-from-digits-of-an-array)

## Implement a Maxheap/MinHeap using arrays and recursion. (Heapify)

```python
def heapify(arr, n, i):
	largest = i # Initialize largest as root
	l = 2 * i + 1 # left = 2*i + 1
	r = 2 * i + 2 # right = 2*i + 2

	# If left child is larger than root
	if l < n and arr[l] > arr[largest]:
		largest = l

	# If right child is larger than largest so far
	if r < n and arr[r] > arr[largest]:
		largest = r

	# If largest is not root
	if largest != i:
		arr[i], arr[largest] = arr[largest], arr[i]

		# Recursively heapify the affected sub-tree
		heapify(arr, n, largest)

def buildHeap(arr, n):
	# Index of last non-leaf node
	startIdx = n // 2 - 1
	# Perform reverse level order traversal from last non-leaf node and heapify each node
	for i in range(startIdx, -1, -1):
		heapify(arr, n, i)

def printHeap(arr, n):
	print("Array representation of Heap is:")
	for i in range(n):
		print(arr[i], end=" ")
	print()


# Binary Tree Representation of input array
#			 1
#		 / \
#		 3	 5
#	 / \	 / \
#	 4	 6 13 10
# / \ / \
# 9 8 15 17

arr = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]
n = len(arr)
buildHeap(arr, n)
printHeap(arr, n)

# Final Heap:
#		  17
#		 / \
#	  15	 13
#	 / \	 / \
#	9  6    5 10
#/ \ / \
#4 8 3 1
```

## Sort an Array using heap. (HeapSort)

```python
def heapify(arr, n, i):
	largest = i		 # Initialize largest as root
	l = 2 * i + 1	 # left = 2*i + 1
	r = 2 * i + 2	 # right = 2*i + 2

	# See if left child of root exists and is greater than root
	if l < n and arr[largest] < arr[l]:
		largest = l

	# See if right child of root exists and is greater than root
	if r < n and arr[largest] < arr[r]:
		largest = r

	# Change root, if needed
	if largest != i:
		arr[i], arr[largest] = arr[largest], arr[i] # swap

		# Heapify the root.
		heapify(arr, n, largest)


def heapSort(arr):
	n = len(arr)
	# Build a maxheap.
	for i in range(n//2 - 1, -1, -1):
		heapify(arr, n, i)

	# One by one extract elements
	for i in range(n-1, 0, -1):
		arr[i], arr[0] = arr[0], arr[i] # swap
		heapify(arr, i, 0)

arr = [12, 11, 13, 5, 6, 7]
heapSort(arr)
n = len(arr)
print("Sorted array is")
for i in range(n):
	print("%d" % arr[i],end=" ")
```

## Maximum of all subarrays of size k.

```python
"""
Given an array and an integer K, find the maximum for each and every contiguous subarray of size k.

Examples : 

Input: arr[] = {1, 2, 3, 1, 4, 5, 2, 3, 6}, K = 3 
Output: 3 3 4 5 5 5 6
Explanation: 
Maximum of 1, 2, 3 is 3
Maximum of 2, 3, 1 is 3
Maximum of 3, 1, 4 is 4
Maximum of 1, 4, 5 is 5
Maximum of 4, 5, 2 is 5 
Maximum of 5, 2, 3 is 5
Maximum of 2, 3, 6 is 6

Input: arr[] = {8, 5, 10, 7, 9, 4, 15, 12, 90, 13}, K = 4 
Output: 10 10 10 15 15 90 90
Explanation:
Maximum of first 4 elements is 10, similarly for next 4 
elements (i.e from index 1 to 4) is 10, So the sequence 
generated is 10 10 10 15 15 90 90
"""
# Python program to find the maximum for
# each and every contiguous subarray of
# size k

from collections import deque

# A Deque (Double ended queue) based
# method for printing maximum element
# of all subarrays of size k
def printMax(arr, n, k):
	""" Create a Double Ended Queue, Qi that will store indexes of array elements. The queue will store indexes of useful elements in every window and it will maintain decreasing order of values from front to rear in Qi, i.e., arr[Qi.front[]] to arr[Qi.rear()] are sorted in decreasing order"""
	
	Qi = deque()
	
	# Process first k (or first window) elements of array
	for i in range(k):
		
		# For every element, the previous smaller elements are useless so remove them from Qi
		while Qi and arr[i] >= arr[Qi[-1]] :
			Qi.pop()
		
		# Add new element at rear of queue
		Qi.append(i);
		
	# Process rest of the elements, i.e. from arr[k] to arr[n-1]
	for i in range(k, n):
		
		# The element at the front of the queue is the largest element of previous window, so print it
		print(str(arr[Qi[0]]) + " ")
		
		# Remove the elements which are out of this window
		while Qi and Qi[0] <= i-k:
			
			# remove from front of deque
			Qi.popleft()
		
		# Remove all elements smaller than the currently being added element (Remove useless elements)
		while Qi and arr[i] >= arr[Qi[-1]] :
			Qi.pop()
		
		# Add current element at the rear of Qi
		Qi.append(i)
	
	# Print the maximum element of last window
	print(str(arr[Qi[0]]))
	

arr = [12, 1, 78, 90, 57, 89, 56]
k = 3
printMax(arr, len(arr), k)
```

## “k” largest element in an array

```python

import heapq as hq

def FirstKelements(arr, size, k):
	# Creating Min Heap for given array with only k elements Create min heap using heapq module
	minHeap = [arr[i] for i in range(k)]

	hq.heapify(minHeap)
	# Loop For each element in array after the kth element

	for i in range(k, size):
		if minHeap[0] > arr[i]:
			continue
		#deleting top element of the min heap
		minHeap[0] = minHeap[-1]
		minHeap.pop()
		minHeap.append(arr[i])
		#maintaining heap again using O(n) time operation....
		hq.heapify(minHeap)
	# Now min heap contains k maximum elements, Iterate and print
	for i in minHeap:
		print(i, end=" ")

arr = [11, 3, 2, 1, 15, 5, 4, 45, 88, 96, 50, 45]
size = len(arr)
# Size of Min Heap
k = 3
FirstKelements(arr, size, k)
```

## Kth smallest and largest element in an unsorted array

```python

import heapq
def kthSmallest(arr, n, k):
	pq = []
	for i in range(k):
		# First push first K elememts into heap
		heapq.heappush(pq, arr[i])
		heapq._heapify_max(pq)
		
	# Now check from k to last element
	for i in range(k, n):	
		# If current element is < first that means there are other k-1 lesser elements are present at bottom thus, pop that element and add kth largest element into the heap till curr at last all the greater element than kth element will get pop off and at the top of heap there will be kth smallest element
		if arr[i] < pq[0]:
			heapq.heappop(pq)
			# Push curr element
			heapq.heappush(pq, arr[i])
			heapq._heapify_max(pq)
	# Return first of element
	return pq[0]

n = 10
arr = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10]
k = 4
print("Kth Smallest Element is:", kthSmallest(arr, n, k))
```

## Merge “K” sorted arrays. 

```python
TODO
```

## Merge 2 Binary Max Heaps

```python
"""
Given two binary max heaps as arrays, merge the given heaps.

Examples : 

Input  : a = {10, 5, 6, 2}, 
         b = {12, 7, 9}
Output : {12, 10, 9, 2, 5, 7, 6}
"""

def MaxHeapify(arr, n, idx):
	
	# Find largest of node and its children
	if idx >= n:
		return
	l = 2 * idx + 1
	r = 2 * idx + 2
	Max = 0
	Max = l if l < n and arr[l] > arr[idx] else idx
	if r < n and arr[r] > arr[Max]:
		Max = r

	# Put Maximum value at root and recur for the child with the Maximum value
	if Max != idx:
		arr[Max], arr[idx] = arr[idx], arr[Max]
		MaxHeapify(arr, n, Max)

# Builds a Max heap of given arr[0..n-1]
def buildMaxHeap(arr, n):
	
	# building the heap from first non-leaf node by calling Max heapify function
	for i in range(int(n / 2) - 1, -1, -1):
		MaxHeapify(arr, n, i)

# Merges Max heaps a[] and b[] into merged[]
def mergeHeaps(merged, a, b, n, m):
	
	# Copy elements of a[] and b[] one by one to merged[]
	for i in range(n):
		merged[i] = a[i]
	for i in range(m):
		merged[n + i] = b[i]

	# build heap for the modified array of size n+m
	buildMaxHeap(merged, n + m)


a = [10, 5, 6, 2]
b = [12, 7, 9]
n = len(a)
m = len(b)
merged = [0] * (m + n)
mergeHeaps(merged, a, b, n, m)
for i in range(n + m):
	print(merged[i], end = " ")
```

## Kth largest sum continuous subarrays

```python
"""
Given an array of integers. Write a program to find the K-th largest mySum of contiguous subarray within the array of numbers which has negative and positive numbers.

Examples: 

Input: a[] = {20, -5, -1} 
         k = 3
Output: 14
Explanation: All mySum of contiguous 
subarrays are (20, 15, 14, -5, -6, -1) 
so the 3rd largest mySum is 14.
"""

import heapq

def kthLargestSum(arr, n, k):	
	# array to store prefix sums
	mySum = [0, arr[0]]
	mySum.extend(mySum[i - 1] + arr[i - 1] for i in range(2, n + 1))
	# priority_queue of min heap
	Q = []
	heapq.heapify(Q)

	# loop to calculate the contiguous subarray mySum position-wise
	for i in range(1, n + 1):

		# loop to traverse all positions that form contiguous subarray
		for j in range(i, n + 1):
			x = mySum[j] - mySum[i - 1]

			# if queue has less then k elements, then simply push it
			if len(Q) < k:
				heapq.heappush(Q, x)
			elif Q[0] < x:
				heapq.heappop(Q)
				heapq.heappush(Q, x)

	# the top element will be then kth largest element
	return Q[0]


a = [10,-10,20,-40]
n = len(a)
k = 6
print(kthLargestSum(a,n,k))
```

## Merge “K” Sorted Linked Lists 

```python
"""
Given K sorted linked lists of size N each, merge them and print the sorted output.

Examples: 

Input: k = 3, n =  4
list1 = 1->3->5->7->NULL
list2 = 2->4->6->8->NULL
list3 = 0->9->10->11->NULL

Output: 0->1->2->3->4->5->6->7->8->9->10->11
Merged lists in a sorted order 
where every element is greater 
than the previous element.
"""

class Node:	
	def __init__(self):
		self.data = 0
		self.next = None

# Function to print nodes in a given linked list
def printList(node):
	while (node != None):
		print(node.data, end = ' ')
		node = node.next
	
def SortedMerge(a, b):
	result = None
	if a is None:
		return(b)
	elif b is None:
		return(a)

	# Pick either a or b, and recur
	if (a.data <= b.data):
		result = a
		result.next = SortedMerge(a.next, b)
	else:
		result = b
		result.next = SortedMerge(a, b.next)
	return result


def mergeKLists(arr, last):

	# Repeat until only one list is left
	while (last != 0):
		i = 0
		j = last

		# (i, j) forms a pair
		while (i < j):
			
			# Merge List i with List j and store merged list in List i
			arr[i] = SortedMerge(arr[i], arr[j])

			# Consider next pair
			i += 1
			j -= 1
			
			# If all pairs are merged, update last
			if (i >= j):
				last = j

	return arr[0]

# Utility function to create a new node.
def newNode(data):
	temp = Node()
	temp.data = data
	temp.next = None
	return temp

# Number of linked lists
k = 3
# Number of elements in each list
n = 4
# An array of pointers storing the head nodes of the linked lists
arr = [0 for _ in range(k)]
arr[0] = newNode(1)
arr[0].next = newNode(3)
arr[0].next.next = newNode(5)
arr[0].next.next.next = newNode(7)
arr[1] = newNode(2)
arr[1].next = newNode(4)
arr[1].next.next = newNode(6)
arr[1].next.next.next = newNode(8)
arr[2] = newNode(0)
arr[2].next = newNode(9)
arr[2].next.next = newNode(10)
arr[2].next.next.next = newNode(11)
head = mergeKLists(arr, k - 1)
printList(head)
```

## Smallest range in “K” Lists

```python
"""
Given k sorted lists of integers of size n each, find the smallest range that includes at least one element from each of the k lists. If more than one smallest range is found, print any one of them.

Example: 

Input: K = 3
arr1[] : [4, 7, 9, 12, 15]
arr2[] : [0, 8, 10, 14, 20]
arr3[] : [6, 12, 16, 30, 50]
Output:
The smallest range is [6 8]

Explanation: Smallest range is formed by 
number 7 from the first list, 8 from second
list and 6 from the third list.

Input: k = 3
arr1[] : [4, 7]
arr2[] : [1, 2]
arr3[] : [20, 40]
Output:
The smallest range is [2 20]

"""

def findSmallestRange(arr, n, k):
	i, minval, maxval, minrange, minel, maxel, flag, minind = 0, 0, 0, 0, 0, 0, 0, 0
		
	# initializing to 0 index
	for i in range(k + 1):
		ptr[i] = 0
	minrange = float('inf')
		
	while True:
		# for maintaining the index of list containing the minimum element
		minind = -1
		minval = 10**9
		maxval = -10**9
		flag = 0

		# iterating over all the list
		for i in range(k):
			
			# if every element of list[i] is traversed then break the loop
			if(ptr[i] == n):
				flag = 1
				break

			# find minimum value among all the list elements pointing by the ptr[] array
			if(ptr[i] < n and arr[i][ptr[i]] < minval):
				minind = i # update the index of the list
				minval = arr[i][ptr[i]]
			
			# find maximum value among all the list elements pointing by the ptr[] array
			if(ptr[i] < n and arr[i][ptr[i]] > maxval):
				maxval = arr[i][ptr[i]]
			
		
		# if any list exhaust we will not get any better answer, so break the while loop
		if flag:
			break

		ptr[minind] += 1

		# updating the minrange
		if((maxval-minval) < minrange):
			minel = minval
			maxel = maxval
			minrange = maxel - minel
	
	print("The smallest range is [", minel, maxel, "]")

N = 5
ptr = [0 for _ in range(501)]
arr = [ [4, 7, 9, 12, 15], [0, 8, 10, 14, 20], [6, 12, 16, 30, 50]]
k = len(arr)
findSmallestRange(arr, N, k)
```

## Median in a stream of Integers

```python
"""
Input: 5 10 15 
Output: 5, 7.5, 10 
Explanation: Given the input stream as an array of integers [5,10,15]. Read integers one by one and print the median correspondingly. So, after reading first element 5,median is 5. After reading 10,median is 7.5 After reading 15 ,median is 10.
Input: 1, 2, 3, 4 
Output: 1, 1.5, 2, 2.5 
Explanation: Given the input stream as an array of integers [1, 2, 3, 4]. Read integers one by one and print the median correspondingly. So, after reading first element 1,median is 1. After reading 2,median is 1.5 After reading 3 ,median is 2.After reading 4 ,median is 2.5. 
"""

from heapq import *

def printMedians(arr, n):
	# max heap to store the smaller half elements
	s = []
	# min heap to store the greater half elements
	g = []

	heapify(s)
	heapify(g)
	med = arr[0]
	heappush(s, med)
	print(med)

	# reading elements of stream one by one
	for i in range(1, n):
		x = arr[i]

		# case1(left side heap has more elements)
		if len(s) > len(g):
			if x < med:
				heappush(g, heappop(s))
				heappush(s, x)
			else:
				heappush(g, x)
			med = (nlargest(1, s)[0] + nsmallest(1, g)[0])/2

		# case2(both heaps are balanced)
		elif len(s) == len(g):
			if x < med:
				heappush(s, x)
				med = nlargest(1, s)[0]
			else:
				heappush(g, x)
				med = nsmallest(1, g)[0]

		# case3(right side heap has more elements)
		else:
			if x > med:
				heappush(s, heappop(g))
				heappush(g, x)
			else:
				heappush(s, x)
			med = (nlargest(1, s)[0] + nsmallest(1, g)[0])/2
		print(med)


arr = [5, 15, 10, 20, 3]
printMedians(arr, len(arr))
```

## Check if a Binary Tree is Heap

```python
class GFG:
	def __init__(self, value):
		self.key = value
		self.left = None
		self.right = None

	def count_nodes(self, root):
		if root is None:
			return 0
		else:
			return (1 + self.count_nodes(root.left) +
					self.count_nodes(root.right))

	def heap_property_util(self, root):
		if (root.left is None and
				root.right is None):
			return True
		if root.right is None:
			return root.key >= root.left.key
		if (root.key >= root.left.key and root.key >= root.right.key):
			return (self.heap_property_util(root.left) and
					self.heap_property_util(root.right))
		else:
			return False

	def complete_tree_util(self, root,
						index, node_count):
		if root is None:
			return True
		if index >= node_count:
			return False
		return (self.complete_tree_util(root.left, 2 *
										index + 1, node_count) and
				self.complete_tree_util(root.right, 2 *
										index + 2, node_count))

	def check_if_heap(self):
		node_count = self.count_nodes(self)
		return bool((self.complete_tree_util(self, 0, node_count) and self.heap_property_util(self)))


root = GFG(5)
root.left = GFG(2)
root.right = GFG(3)
root.left.left = GFG(1)

if root.check_if_heap():
	print("Given binary tree is a heap")
else:
	print("Given binary tree is not a Heap")
```

## Convert BST to Min Heap

```python
class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

def inorderTraversal(root, arr):
	if root is None:
		return

	# first recur on left subtree
	inorderTraversal(root.left, arr)

	# then copy the data of the node
	arr.append(root.data)

	# now recur for right subtree
	inorderTraversal(root.right, arr)


def BSTToMinHeap(root, arr, i):
	if root is None:
		return

	# first copy data at index 'i' of 'arr' to the node
	i[0] += 1
	root.data = arr[i[0]]

	# then recur on left subtree
	BSTToMinHeap(root.left, arr, i)

	# now recur on right subtree
	BSTToMinHeap(root.right, arr, i)

def convertToMinHeapUtil(root):
	# vector to store the data of all the nodes of the BST
	arr = []
	i = [-1]

	# inorder traversal to populate 'arr'
	inorderTraversal(root, arr)

	# BST to MIN HEAP conversion
	BSTToMinHeap(root, arr, i)


def preorderTraversal(root):
	if root is None:
		return
	print(root.data, end=" ")
	preorderTraversal(root.left)
	preorderTraversal(root.right)

root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(7)
convertToMinHeapUtil(root)
print("Preorder Traversal:")
preorderTraversal(root)
```

## Convert min heap to max heap

```python
def MaxHeapify(arr, i, n):
	l = 2 * i + 1
	r = 2 * i + 2
	largest = i
	if l < n and arr[l] > arr[i]:
		largest = l
	if r < n and arr[r] > arr[largest]:
		largest = r
	if largest != i:
		arr[i], arr[largest] = arr[largest], arr[i]
		MaxHeapify(arr, largest, n)

def convertMaxHeap(arr, n):
	# Start from bottommost and rightmost internal mode and heapify all internal modes in bottom up way
	for i in range(int((n - 2) / 2), -1, -1):
		MaxHeapify(arr, i, n)



# array representing Min Heap
arr = [3, 5, 9, 6, 8, 20, 10, 12, 18, 9]
n = len(arr)
print("Min Heap array : ")
print(arr)
convertMaxHeap(arr, n)
print("Max Heap array : ")
print(arr)
```


## Minimum sum of two numbers formed from digits of an array

```python
"""
Given an array of digits (values are from 0 to 9), find the minimum possible sum of two numbers formed from digits of the array. All digits of given array must be used to form the two numbers. 
Examples : 
 

Input: [6, 8, 4, 5, 2, 3]
Output: 604
The minimum sum is formed by numbers 
358 and 246

Input: [5, 3, 0, 7, 4]
Output: 82
The minimum sum is formed by numbers 
35 and 047 
"""

def solve(arr, n):
	# sort the array
	arr.sort()

	# let two numbers be a and b
	a = 0; b = 0
	
	for i in range(n):
		# Fill a and b with every alternate digit of input array
		if (i % 2 != 0):
			a = a * 10 + arr[i]
		else:
			b = b * 10 + arr[i]
	return a + b


arr = [6, 8, 4, 5, 2, 3]
n = len(arr)
print("Sum is ", solve(arr, n))

```