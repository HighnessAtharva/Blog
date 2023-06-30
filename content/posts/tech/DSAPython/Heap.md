---
title: "DSA in Python - Heap"
date: 2022-07-09T13:14:34+05:30
draft: false
cover: 
    image: blog/dsa/Heap.webp
    alt: Heap
    caption: Learn Heap Algorithms in Python
description: "Master FAANG Interviews with the most frequently asked Heap problems with solutions and comprehensive explanations. Boost Skills, Get Paid!"
tags: ["python"] 

---

## Free Preview - 5 Heap Problems

### Implement a Maxheap/MinHeap using arrays and recursion. (Heapify)

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

### Sort an Array using heap. (HeapSort)

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

### Maximum of all subarrays of size k.

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

### “k” largest element in an array

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

### Kth smallest and largest element in an unsorted array

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

## Buy the Interview Guide

{{< gumroad "https://highnessatharva.gumroad.com/l/dsa-python-heap" "/blog/gumroad-marketing.webp" >}}