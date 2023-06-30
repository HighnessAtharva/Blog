---
title: "DSA in Python - Search and Sort"
date: 2022-07-09T13:14:34+05:30
draft: false
cover: 
    image: blog/dsa/Search-Sort.webp
    alt: Search and Sort
    caption: Learn Searching & Sorting Algorithms in Python
tags: ["python"] 
---

## Free Preview - 5 Search and Sort Problems

### Bubble Sort

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

### Selection Sort

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

### Insertion Sort

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

### Merge Sort

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

### Quick Sort

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

## Buy the Interview Guide

{{< gumroad "https://highnessatharva.gumroad.com/l/dsa-python-searching-sorting" "/blog/gumroad-marketing.webp" >}}