---
title: "DSA in Python - Search and Sort"
date: 2022-07-09T13:14:34+05:30
draft: true
cover: 
    image: blog/dsa/search-sort.jpg
    alt: Search and Sort
    caption: Learn Searching & Sorting Algorithms in Python
tags: ["python"] 

---
- [Bubble Sort](#bubble-sort)
- [Selection Sort](#selection-sort)
- [Insertion Sort](#insertion-sort)
- [Merge Sort](#merge-sort)
- [Quick Sort](#quick-sort)
- [Counting Sort](#counting-sort)
- [Heap Sort](#heap-sort)
- [Radix Sort](#radix-sort)
- [Linear Search](#linear-search)
- [Binary Search](#binary-search)
- [Interpolation Search](#interpolation-search)
- [Find first and last positions of an element in a sorted array](#find-first-and-last-positions-of-an-element-in-a-sorted-array)
- [Find a Fixed Point (Value equal to index) in a given array](#find-a-fixed-point-value-equal-to-index-in-a-given-array)
- [Search in a rotated sorted array](#search-in-a-rotated-sorted-array)
- [square root of an integer](#square-root-of-an-integer)
- [Find the repeating and the missing](#find-the-repeating-and-the-missing)
- [Searching in an array where adjacent differ by at most k](#searching-in-an-array-where-adjacent-differ-by-at-most-k)
- [find a pair with a given difference](#find-a-pair-with-a-given-difference)
- [find two elements that sum to a given value - TwoSum](#find-two-elements-that-sum-to-a-given-value---twosum)
- [find four elements that sum to a given value - ThreeSum](#find-four-elements-that-sum-to-a-given-value---threesum)
- [find four elements that sum to a given value - FourSum](#find-four-elements-that-sum-to-a-given-value---foursum)
- [maximum sum such that no 2 elements are adjacent](#maximum-sum-such-that-no-2-elements-are-adjacent)
- [Count triplet with sum smaller than a given value](#count-triplet-with-sum-smaller-than-a-given-value)
- [print all subarrays with 0 sum](#print-all-subarrays-with-0-sum)
- [Product array Puzzle](#product-array-puzzle)
- [Sort array according to count of set bits](#sort-array-according-to-count-of-set-bits)
- [minimum no. of swaps required to sort the array](#minimum-no-of-swaps-required-to-sort-the-array)
- [Find pivot element in a sorted array](#find-pivot-element-in-a-sorted-array)
- [K-th Element of Two Sorted Arrays](#k-th-element-of-two-sorted-arrays)
- [Aggressive cows](#aggressive-cows)
- [Book Allocation Problem](#book-allocation-problem)
- [EKOSPOJ](#ekospoj)
- [Missing Number in AP](#missing-number-in-ap)
- [Smallest number with atleastn trailing zeroes infactorial](#smallest-number-with-atleastn-trailing-zeroes-infactorial)
- [ROTI-Prata SPOJ](#roti-prata-spoj)
- [DoubleHelix SPOJ](#doublehelix-spoj)
- [Subset Sums](#subset-sums)
- [Implement Merge-sort in-place](#implement-merge-sort-in-place)

## Bubble Sort

```python
def bubble_sort(array):
    n=len(array)
    for i in range(n):
        for j in range(n-i-1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j] 


array=[5,2,3,1,4, -99, 0]
bubble_sort(array)
print(array)
```

## Selection Sort

```python
def selection_sort(array):
    global iterations
    iterations = 0
    for i in range(len(array)):
        minimum_index = i
        for j in range(i + 1, len(array)):
            iterations += 1
            if array[minimum_index] > array[j]:
                minimum_index = j
        
        # Swap the found minimum element with  the first element
        if minimum_index != i:
            array[i], array[minimum_index] = array[minimum_index], array[i]

array=[5,2,3,1,4, -99, 0]
selection_sort(array)
print(array)
```

## Insertion Sort

```python
def insertion_sort(array):
    global iterations
    iterations = 0
    for i in range(1, len(array)):
        current_value = array[i]
        for j in range(i - 1, -1, -1):
            iterations += 1
            if array[j] > current_value:
                array[j], array[j + 1] = array[j + 1], array[j] # swap
            else:
                array[j + 1] = current_value
                break

array=[5,2,3,1,4, -99, 0]
insertion_sort(array)
print(array)
```

## Merge Sort

```python
def merge_sort(array):
    if len(array) < 2:
        return array
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) or j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        if i == len(left) or j == len(right):
            result.extend(left[i:] or right[j:])
            break
    return result

array=[5,2,3,1,4, -99, 0]
print(merge_sort(array))
```

## Quick Sort

```python
def partition(array, low, high):
    i = low - 1            # index of smaller element
    pivot = array[high]    # pivot 
    
    for j in range(low, high):
        # If current element is smaller than the pivot
        
        if array[j] < pivot:
        # increment index of smaller element
        
            i += 1
            array[i], array[j] = array[j], array[i]
            
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

def quick_sort(array, low, high):
    if low < high:
        # pi is partitioning index, arr[p] is now at right place 
        temp = partition(array, low, high)
        
        # Separately sort elements before partition and after partition 
        quick_sort(array, low, temp - 1)
        quick_sort(array, temp + 1, high)

array=[5,2,3,1,4, -99, 0]
quick_sort(array, 0, len(array)-1)
print(array)
```

## Counting Sort

```python
# Counting sort in Python programming


def countingSort(array):
    size = len(array)
    output = [0] * size

    # Initialize count array
    count = [0] * 10

    # Store the count of each elements in count array
    for i in range(size):
        count[array[i]] += 1

    # Store the cummulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Find the index of each element of the original array in count array
    # place the elements in output array
    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1

    # Copy the sorted elements into original array
    for i in range(size):
        array[i] = output[i]


array = [4,0,2, 2, 8, 3, 3, 1]
countingSort(array)
print(array)
```

## Heap Sort

```python
def heapify(nums, heap_size, root_index):
    # Assume the index of the largest element is the root index
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child

    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        # Heapify the new root element to ensure it's the largest
        heapify(nums, heap_size, largest)


def heap_sort(nums):
    n = len(nums)
    
    for i in range(n, -1, -1):
        heapify(nums, n, i)

    # Move the root of the max heap to the end of
    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)

random_list_of_nums = [35, 12, 43, 8, 51]
heap_sort(random_list_of_nums)
print(random_list_of_nums)
```

## Radix Sort

```python
from math import log10
from random import randint

def get_num(num, base, pos):
  return (num // base ** pos) % base

def prefix_sum(array):
  for i in range(1, len(array)):
    array[i] = array[i] + array[i-1]
  return array

def radixsort(l, base=10):
  passes = int(log10(max(l))+1)
  output = [0] * len(l)

  for pos in range(passes):
    count = [0] * base

    for i in l:
      digit = get_num(i, base, pos)
      count[digit] +=1

    count = prefix_sum(count)

    for i in reversed(l):
      digit = get_num(i, base, pos)
      count[digit] -= 1
      new_pos = count[digit]
      output[new_pos] = i

    l = list(output)
  return output

l = [randint(1, 99999) for _ in range(100)]
sortedarr = radixsort(l)
print(sortedarr)
```

## Linear Search

```python
def linearSearch(array, n, x):
    for i in range(n):
        if (array[i] == x):
            return i
    return -1

array = [2, 4, 0, 1, 9]
x = 1
n = len(array)
result = linearSearch(array, n, x)
if(result == -1):
    print("Element not found")
else:
    print("Element found at index: ", result)
```

## Binary Search

```python
def binarySearch(array, x, low, high):
    while low <= high:
        mid = low + (high - low)//2
        if array[mid] == x:
            return mid
        elif array[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

array = [3, 4, 5, 6, 7, 8, 9]
x = 4
result = binarySearch(array, x, 0, len(array)-1)
if result != -1:
    print(f"Element is present at index {str(result)}")
else:
    print("Not found")

```

## Interpolation Search

```python
# Function to determine if target exists in the sorted list `A` or not
# using an interpolation search algorithm
def interpolationSearch(A, target):
    if not A:
        return -1
    (left, right) = (0, len(A) - 1)
    while A[right] != A[left] and A[left] <= target <= A[right]:
        mid = left + (target - A[left]) * (right - left) // (A[right] - A[left])
        if target == A[mid]:
            return mid
        elif target < A[mid]:
            right = mid - 1
        else:
            left = mid + 1
    if target == A[left]:
        return left
    return -1
 
A = [2, 5, 6, 8, 9, 10]
key = 5
index = interpolationSearch(A, key)
if index != -1:
    print('Element found at index', index)
else:
    print('Element found not in the list')
```

## Find first and last positions of an element in a sorted array

```python
def first(arr, x, n):
	low = 0
	high = n - 1
	res = -1
	
	while (low <= high):
		mid = (low + high) // 2		
		if arr[mid] > x:
			high = mid - 1
		elif arr[mid] < x:
			low = mid + 1
		else:
			res = mid
			high = mid - 1

	return res

# If x is present in arr[] then returns the index of FIRST occurrence of x in arr[0..n-1], otherwise returns -1
def last(arr, x, n):
	low = 0
	high = n - 1
	res = -1
	while(low <= high):
		mid = (low + high) // 2
		if arr[mid] > x:
			high = mid - 1
		elif arr[mid] < x:
			low = mid + 1
		else:
			res = mid
			low = mid + 1
	return res

arr = [ 1, 2, 2, 2, 2, 3, 4, 7, 8, 8 ]
n = len(arr)
x = 8
print("First Occurrence =", first(arr, x, n))
print("Last Occurrence =", last(arr, x, n))
```

## Find a Fixed Point (Value equal to index) in a given array

```python
"""
  Input: arr[] = {-10, -5, 0, 3, 7}
  Output: 3  // arr[3] == 3 

  Input: arr[] = {0, 2, 5, 8, 17}
  Output: 0  // arr[0] == 0 


  Input: arr[] = {-10, -5, 3, 4, 7, 9}
  Output: -1  // No Fixed Point
"""

def binarySearch(arr, low, high):
	if high >= low :
		
		mid = low + (high - low)//2
		if mid == arr[mid]:
			return mid
		res = -1
		if mid + 1 <= arr[high]:
			res = binarySearch(arr, (mid + 1), high)
		if res !=-1:
			return res
		if mid-1 >= arr[low]:
			return binarySearch(arr, low, (mid -1))
	return -1

arr = [-10, -1, 0, 3, 10, 11, 30, 50, 100] # NOTE: ARRAY WILL BE SORTED
n = len(arr)
print(f"Fixed Point is {str(binarySearch(arr, 0, n-1))}")

```

## Search in a rotated sorted array

```python
def search(nums, target):
    low, high = 0, len(nums)-1
    while low<=high:
        mid = low + ((high - low))//2
        if nums[mid]==target:
            return mid
        elif nums[low] <= nums[mid]:
            if nums[low] <= target < nums[mid]:
                high = mid-1
            else:
                low = mid+1
        elif nums[mid] < target <= nums[high]:
            low = mid+1
        else:
            high = mid-1
    return -1
    
target=5
nums=[5,6,1,2,3,4]
print(target, "found at index: ",search(nums,target))
```

## square root of an integer

```python
def floorSqrt(x):
	if x in [0, 1]:
		return x
	i = 1
	result = 1
	while (result <= x):
		i += 1
		result = i**2
	return i - 1
x = 11
print(floorSqrt(x))
```

## Find the repeating and the missing

```python
def missandrepeat():	
	arr = [ 4, 3, 6, 2, 1, 1 ]
	numberMap = {}
	max = len(arr)
	for i in arr:
		if i not in numberMap:
			numberMap[i] = True
		else:
			print("Repeating =", i)
	for i in range(1, max + 1):
		if i not in numberMap:
			print("Missing =", i)
missandrepeat()

```


## Searching in an array where adjacent differ by at most k

```python
"""
Input : arr[] = {4, 5, 6, 7, 6}
           k = 1
           x = 6
Output : 2
The first index of 6 is 2.

Input : arr[] = {20, 40, 50, 70, 70, 60}  
          k = 20
          x = 60
Output : 5
The index of 60 is 5
"""

def search(arr, n, x, k):
	# Traverse the given array starting from leftmost element
	i = 0
	while (i < n):
		if (arr[i] == x):
			return i
		# Jump the difference between current array element and x divided by k
		# We use max here to make sure that i moves at-least one step ahead.
		i += max(1, int(abs(arr[i] - x) / k))
	print("number is not present!")
	return -1

arr = [2, 4, 5, 7, 7, 6]
x = 6
k = 2
n = len(arr)
print("Element", x, "is present at index",search(arr, n, x, k))
```

## find a pair with a given difference

```python
"""
Input : arr[] = {4, 5, 6, 7, 6}
           k = 1
           x = 6
Output : 2
The first index of 6 is 2.

Input : arr[] = {20, 40, 50, 70, 70, 60}  
          k = 20
          x = 60
Output : 5
The index of 60 is 5
"""
def findPair(arr,n):
	size = len(arr)
	i,j = 0,1
	while i < size and j < size:
		if i != j and arr[j]-arr[i] == n:
			print (f"Pair found ({arr[i]} ,{arr[j]})")
			return True

		elif arr[j] - arr[i] < n:
			j+=1
		else:
			i+=1
	print ("No pair found")
	return False

arr = [1, 8, 30, 40, 100]
n = 60
findPair(arr, n)
```

## find two elements that sum to a given value - TwoSum

```python
def findPair(nums, target):
    d = {}
    for i, e in enumerate(nums):
        if target - e in d:
            print('Pair found', (nums[d.get(target - e)], nums[i]))
            return
        d[e] = i
    print('Pair not found')

nums = [8, 7, 2, 5, 3, 1]
target = 10
findPair(nums, target)
```

## find four elements that sum to a given value - ThreeSum

```python
def isTripletExist(nums, target):
    d = {e: i for i, e in enumerate(nums)}
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            val = target - (nums[i] + nums[j])
            if val in d and d[val] not in [i, j]:
                return True
    return False
 
nums = [2, 7, 4, 0, 9, 5, 1, 3]
target = 6
if isTripletExist(nums, target):
    print('Triplet exists')
else:
    print('Triplet doesn\'t exist')
```

## find four elements that sum to a given value - FourSum

```python
def hasQuadruplet(nums, target):
    # create an empty dictionary
    # key —> target of a pair in the list
    # value —> list storing an index of every pair having that sum
    d = {}
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            val = target - (nums[i] + nums[j])
            if val in d:
                for pair in d[val]:
                    x, y = pair
                    if x not in [i, j] and y not in [i, j]:
                        print('Quadruplet Found', (nums[i], nums[j], nums[x], nums[y]))
                        return True
            d.setdefault(nums[i] + nums[j], []).append((i, j))
    return False
 
nums = [2, 7, 4, 0, 9, 5, 1, 3]
target = 20
if not hasQuadruplet(nums, target):
    print('Quadruplet doesn\'t exist')
 
```

## maximum sum such that no 2 elements are adjacent

```python
"""
Input: arr[] = {5, 5, 10, 100, 10, 5}
Output: 110
Explanation: Pick the subsequence {5, 100, 5}.
The sum is 110 and no two elements are adjacent. This is the highest possible sum.

Input: arr[] = {3, 2, 7, 10}
Output: 13
Explanation: The subsequence is {3, 10}. This gives sum = 13.
This is the highest possible sum of a subsequence following the given criteria

Input: arr[] = {3, 2, 5, 10, 7}
Output: 15
Explanation: Pick the subsequence {3, 5, 7}. The sum is 15.
"""

def findMaxSum(arr, n):
    incl = 0
    excl = 0   
    for i in arr:
        new_excl = max (excl, incl)
        incl = excl + i
        excl = new_excl
    return max(excl, incl)

arr = [5, 5, 10, 100, 10, 5]
N = 6
print (findMaxSum(arr, N))
```

## Count triplet with sum smaller than a given value

```python
def countTriplets(arr,n,sum):
	arr.sort()
	ans = 0
	# Every iteration of loop counts triplet with first element as arr[i].
	for i in range(n-2):

		# Initialize other two elements as corner elements of subarray arr[j+1..k]
		j = i + 1
		k = n-1

		while(j < k):
			# If sum of current triplet is more or equal, move right corner to look for smaller values
			if (arr[i]+arr[j]+arr[k] >=sum):
				k = k-1
			# Else move left corner
			else:
				# This is important. For current i and j, there can be total k-j third elements.
				ans += (k - j)
				j = j+1
	return ans

arr = [5, 1, 3, 4, 7]
n = len(arr)
target = 12
print(countTriplets(arr, n, target))
```

## print all subarrays with 0 sum

```python
def findSubArrays(arr,n):
	# create a python dict
	hashMap = {}
	# create a python list equivalent to ArrayList
	out = []
	# tracker for sum of elements
	sum1 = 0
	for i in range(n):
		sum1 += arr[i]
		if sum1 == 0:
			out.append((0, i))
		al = []
		if sum1 in hashMap:
			al = hashMap.get(sum1)
			for it in range(len(al)):
				out.append((al[it] + 1, i))
		al.append(i)
		hashMap[sum1] = al
	return out

def printOutput(output):
	for i in output:
		print(f"Subarray found from Index {str(i[0])} to {str(i[1])}")

arr = [6, 3, -1, -3, 4, -2,
		2, 4, 6, -12, -7]
n = len(arr)
out = findSubArrays(arr, n)
# if we did not find any subarray with 0 sum, then subarray does not exists
if (len(out) == 0):
	print ("No subarray exists")
else:
	printOutput (out)
```

## Product array Puzzle

```python
""" 
Given an array arr[] of n integers, construct a Product Array prod[] (of same size) such that prod[i] is equal to the product of all the elements of arr[] except arr[i]. Solve it without division operator and in O(n).
Example: 

Input: arr[] = {10, 3, 5, 6, 2}
Output: prod[] = {180, 600, 360, 300, 900}
The elements of output array are 
{3*5*6*2, 10*5*6*2, 10*3*6*2, 
10*3*5*2, 10*3*5*6}

Input: arr[] = {1, 2, 1, 3, 4}
Output: prod[] = {24, 12, 24, 8, 6}
The elements of output array are 
{3*4*1*2, 1*1*3*4, 4*3*2*1, 
1*1*4*2, 1*1*3*2}
"""
def solve(arr, n):
	# Initialize a variable to store the total product of the array elements
	prod = 1
	for i in arr:
		prod *= i

	# we know x / y mathematically is same as x*(y to power -1)
	for i in arr:
		print(int(prod*(i**-1)), end =" ")

arr = [10, 3, 5, 6, 2]
n = len(arr)
solve(arr, n)
```

## Sort array according to count of set bits

```python
""" 
Input: arr[] = {5, 2, 3, 9, 4, 6, 7, 15, 32};
Output: 15 7 5 3 9 6 2 4 32
Explanation:
The integers in their binary representation are:
    15 -1111
    7  -0111
    5  -0101
    3  -0011
    9  -1001
    6  -0110
    2  -0010
    4- -0100
    32 -10000
hence the non-increasing sorted order is:
{15}, {7}, {5, 3, 9, 6}, {2, 4, 32}
"""

def countSetBits(val):
	cnt = 0
	while val:
		cnt += val % 2
		val = val//2
	return cnt

# Using custom comparator lambda function
arr = [1, 2, 3, 4, 5, 6]

# form a tuple with val, index
n = len(arr)
arr = [(arr[i], i) for i in range(n)]

# first criteria to sort is number of set bits, then the index
sorted_arr = sorted(arr, key=lambda val: (
	countSetBits(val[0]), n-val[1]), reverse=True)
sorted_arr = [val[0] for val in sorted_arr]
print(sorted_arr)
```

## minimum no. of swaps required to sort the array

```python
""" 
Given an array of n distinct elements, find the minimum number of swaps required to sort the array.
Input: {4, 3, 2, 1}
Output: 2
Explanation: Swap index 0 with 3 and 1 with 2 to 
              form the sorted array {1, 2, 3, 4}.	
"""

def minSwaps(arr, N):
	ans = 0
	temp = arr.copy()
	temp.sort()
	for i in range(N):
		# This is checking whether the current element is at the right place or not
		if (arr[i] != temp[i]):
			ans += 1
			# Swap the current element with the right index so that arr[0] to arr[i] is sorted
			swap(arr, i,
				indexOf(arr, temp[i]))
	return ans

def swap(arr, i, j):
	arr[i], arr[j]= arr[j], arr[i]


def indexOf(arr, ele):
	for i in range(len(arr)):	
		if (arr[i] == ele):
				return i
	return -1

a = [101, 758, 315, 730, 472, 619, 460, 479]
n = len(a)
print(minSwaps(a, n))
```


## Find pivot element in a sorted array

```python
def findPivot(arr, left, right):
	if right< left:
		return -1
	if right == left:
		return left
	mid = (left+right)//2
	if mid<right and arr[mid]>arr[mid+1]:
		return mid
	if mid>left and arr[mid]<arr[mid-1]:
		return mid-1
	if arr[left]<arr[mid]:
		return findPivot(arr, mid+1, right)
	else:
		return findPivot(arr, left, mid-1)

arr=[14, 23, 7, 9, 3, 6, 18, 22, 16, 36]
start=0
n=len(arr)-1
pivot=findPivot(arr, start, n)
pivot+=1 # pivot is the index of the first element in the right subarray
print(f'Pivot is {arr[pivot]}')
```

## K-th Element of Two Sorted Arrays

```python
"""Given two sorted arrays of size m and n respectively, you are tasked with finding the element that would be at the k’th position of the final sorted array.

Examples: 

Input : Array 1 - 2 3 6 7 9
        Array 2 - 1 4 8 10
        k = 5
Output : 6
Explanation: The final sorted array would be -
1, 2, 3, 4, 6, 7, 8, 9, 10
The 5th element of this array is 6.
"""

def find(A, B, m, n, k_req):   
    i, j, k = 0, 0, 0
    # Keep taking smaller of the current elements of two sorted arrays and keep incrementing k
    while i < len(A) and j < len(B):
        k += 1
        if A[i] < B[j]:
            if k == k_req:
                return A[i]
            i += 1
        elif k == k_req:
            return B[j]
        else:
            j += 1

    # If array B[] is completely traversed
    while i < len(A):
        k += 1
        if k == k_req:
                return A[i]
        i += 1

    # If array A[] is completely traversed
    while j < len(B):
        k += 1
        if k == k_req:
                return B[j]
        j += 1
 
A = [2, 3, 6, 7, 9]
B = [1, 4, 8, 10]
k = 5;
print(find(A, B, 5, 4, k))
```

## Aggressive cows

```python
"""
Problem Statement: There is a new barn with N stalls and C cows. The stalls are located on a straight line at positions x1,….,xN (0 <= xi <= 1,000,000,000). We want to assign the cows to the stalls, such that the minimum distance between any two of them is as large as possible. What is the largest minimum distance?

Examples:

Input: No of stalls = 5 
       Array: {1,2,8,4,9}
       And number of cows: 3

Output: One integer, the largest minimum distance 3
"""

def isPossible(a, n, cows, mid):
	CntCows = 1
	lastPlacedCow=a[0]
	for i in range(1, n):
		if a[i] -lastPlacedCow >= mid:
			CntCows+=1
			lastPlacedCow=a[i]
	return CntCows >= cows

n = 5
cows = 3;
a=[1,2,8,4,9]
a.sort()
low = 1
high = a[n - 1] - a[0]
while low< high:
	mid = (low + high)//2
	if isPossible(a, n, cows, mid):
		low=mid+1
	else:
		high=mid-1
print(f'Largest minimum distance is: {high}')
```

## Book Allocation Problem

```python
"""
Given number of pages in n different books and m students. The books are arranged in ascending order of number of pages. Every student is assigned to read some consecutive books. The task is to assign books in such a way that the maximum number of pages assigned to a student is minimum. 
Example : 
 

Input : pages[] = {12, 34, 67, 90} , m = 2
Output : 113
Explanation:
There are 2 number of students. Books can be distributed 
in following fashion : 
  1) [12] and [34, 67, 90]
      Max number of pages is allocated to student 
      '2' with 34 + 67 + 90 = 191 pages
  2) [12, 34] and [67, 90]
      Max number of pages is allocated to student
      '2' with 67 + 90 = 157 pages 
  3) [12, 34, 67] and [90]
      Max number of pages is allocated to student 
      '1' with 12 + 34 + 67 = 113 pages

Of the 3 cases, Option 3 has the minimum pages = 113.
"""

def isPossible(arr, n, m, curr_min):
	studentsRequired = 1
	curr_sum = 0
	for i in range(n):

		# check if current number of pages are greater than curr_min that means we will get the result after mid no. of pages
		if (arr[i] > curr_min):
			return False

		# count how many students are required to distribute curr_min pages
		if (curr_sum + arr[i] > curr_min):

			# increment student count
			studentsRequired += 1

			# update curr_sum
			curr_sum = arr[i]

			# if students required becomes greater than given no. of students, return False
			if (studentsRequired > m):
				return False

		# else update curr_sum
		else:
			curr_sum += arr[i]

	return True

# function to find minimum pages
def findPages(arr, n, m):
	# return -1 if no. of books is less than no. of students
	if (n < m):
		return -1

	mysum = sum(arr[i] for i in range(n))
	# initialize start as 0 pages and end as total pages
	start, end = 0, mysum
	result = 10**9

	# traverse until start <= end
	while (start <= end):

		# check if it is possible to distribute books by using mid as current minimum
		mid = (start + end) // 2
		if (isPossible(arr, n, m, mid)):

			# update result to current distribution as it's the best we have found till now.
			result = mid

			# as we are finding minimum and books are sorted so reduce end = mid -1 that means
			end = mid - 1

		else:
			# if not possible means pages should be increased so update start = mid + 1
			start = mid + 1

	# at-last return minimum no. of pages
	return result

arr = [12, 34, 67, 90]  # Number of pages in books
n = len(arr)
m = 2 # No. of students
print("Minimum number of pages = ",findPages(arr, n, m))
```

## EKOSPOJ

```python
TODO
```

## Missing Number in AP

```python
"""
Given an array that represents elements of arithmetic progression in order. One element is missing in the progression, find the missing number. 

Examples: 

Input: arr[]  = {2, 4, 8, 10, 12, 14}
Output: 6

Input: arr[]  = {1, 6, 11, 16, 21, 31};
Output: 26
"""

def find_missing(arr, n):
	first = arr[0]
	last = arr[-1]

	if (first + last) % 2:
		s = (n + 1) / 2
		s *= (first + last)
	else:
		s = (first + last) / 2
		s *= (n + 1)

	return s - sum(arr)

arr = [2, 4, 8, 10, 12, 14]
n = len(arr)
missing = find_missing(arr, n)
print(missing)
```

## Smallest number with atleastn trailing zeroes infactorial

```python
"""
Given a number n. The task is to find the smallest number whose factorial contains at least n trailing zeroes.
Examples : 
 

Input : n = 1
Output : 5 
1!, 2!, 3!, 4! does not contain trailing zero.
5! = 120, which contains one trailing zero.

Input : n = 6
Output : 25
"""

def check(p,n):
    temp = p
    count = 0
    f = 5
    while (f <= temp):
        count += temp//f
        f *= 5
    return (count >= n)
 
# Return smallest number whose factorial contains at least n trailing zeroes
def findNum(n):
    # If n equal to 1, return 5. since 5! = 120.
    if (n==1):
        return 5
    # Initializing low and high for binary search.
    low = 0
    high = 5*n
  
    while (low <high):
        mid = (low + high) >> 1
        # Checking if mid's factorial contains n trailing zeroes.
        if (check(mid, n)):
            high = mid
        else:
            low = mid+1
    return low
 
n = 6
print(findNum(n))
```

## ROTI-Prata SPOJ

```python
TODO
```

## DoubleHelix SPOJ

```python
TODO
```

## Subset Sums

```python
"""
Given an array of integers, print sums of all subsets in it. Output sums can be printed in any order.

Examples : 
Input : arr[] = {2, 3}
Output: 0 2 3 5

Input : arr[] = {2, 4, 5}
Output : 0 2 4 5 6 7 9 11
"""

def subsetSums(arr, l, r, sum=0):
    # Print current subset
    if l > r:
        print(sum, end=" ")
        return
    # Subset including arr[l]
    subsetSums(arr, l + 1, r, sum + arr[l])
    # Subset excluding arr[l]
    subsetSums(arr, l + 1, r, sum)
 
arr = [5, 4, 3]
n = len(arr)
subsetSums(arr, 0, n - 1)
```

## Implement Merge-sort in-place

```python
"""
NOTE: TIME COMPLEXITY IS HIGHER THAN STANDARD MERGE SORT BUT SPACE COMPLEXITY IS O(1)
"""
def merge(arr, start, mid, end):
	start2 = mid + 1
	# If the direct merge is already sorted
	if (arr[mid] <= arr[start2]):
		return
	# Two pointers to maintain start of both arrays to merge
	while (start <= mid and start2 <= end):
		# If element 1 is in right place
		if arr[start] > arr[start2]:
			value = arr[start2]
			index = start2
			# Shift all the elements between element 1 element 2, right by 1.
			while (index != start):
				arr[index] = arr[index - 1]
				index -= 1
			arr[start] = value
			mid += 1
			start2 += 1
		start += 1


def mergeSort(arr, l, r):
	if (l < r):
		# Same as (l + r) / 2, but avoids overflow for large l and r
		m = l + (r - l) // 2
		# Sort first and second halves
		mergeSort(arr, l, m)
		mergeSort(arr, m + 1, r)
		merge(arr, l, m, r)

arr = [12, 11, 13, 5, 6, 7]
arr_size = len(arr)
mergeSort(arr, 0, arr_size - 1)
print(arr)
```
