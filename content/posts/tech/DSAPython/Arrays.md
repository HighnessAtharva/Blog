---
title: "DSA in Python - Arrays"
date: 2022-07-07T23:18:34+05:30
draft: false
cover: 
    image: blog/dsa/Array.webp
    alt: Arrays
    caption: Learn Array Algorithms in Python
description: "Master FAANG Interviews with the most frequently asked Array problems with solutions and comprehensive explanations. Boost Skills, Get Paid!"
tags: ["python"] 
---

## Free Preview - 5 Array Problems

### Reverse the array

```python
def reverseArray(A: list):
    start, end= 0, len(A)-1
    while start<end:
        A[start], A[end]= A[end], A[start]
        start+=1
        end-=1
    
    
A=[1,54,21,51,2,353,2,1,99,121,5,5]
reverseArray(A)
print("After reversing:", A)
```

### Find the maximum and minimum element in an array

```python
def getMinMax(arr: list, n: int):
    min = 0
    max = 0
 
    # If there is only one element then return it as min and max both
    if n == 1:
        max = arr[0]
        min = arr[0]
        return min, max
 
    # If there are more than one elements, then initialize min
    # and max
    if arr[0] > arr[1]:
        max = arr[0]
        min = arr[1]
    else:
        max = arr[1]
        min = arr[0]
 
    for i in range(2, n):
        if arr[i] > max:
            max = arr[i]
        elif arr[i] < min:
            min = arr[i]
 
    return min, max
 
# Driver Code
if __name__ == "__main__":
    arr = [1000, 11, 445, 1, 330, 3000]
    arr_size = 6
    min, max = getMinMax(arr, arr_size)
    print("Minimum element is", min)
    print("Maximum element is", max)
 
```

### Find the "Kth" max and min element of an array

```python
import sys
 
# function to calculate number of elements less than equal to mid
def count(nums, mid):
    cnt = 0
    for i in range(len(nums)):
        if nums[i] <= mid:
            cnt += 1
    return cnt
 
def kthSmallest(nums, k):
    low = sys.maxsize
    high = -sys.maxsize 
     
    # calculate minimum and maximum the array.
    for i in range(len(nums)):
        low = min(low, nums[i])
        high = max(high, nums[i])
 
        # Our answer range lies between minimum and maximum element
        # of the array on which Binary Search is Applied
    while low < high:
        mid = low + (high - low) // 2
        # if the count of number of elements in the array less than equal
        # to mid is less than k then increase the number. Otherwise decrement
        # the number and try to find a better answer.
        if count(nums, mid) < k:
            low = mid + 1
        else:
            high = mid
    return low
 
nums = [1, 4, 5, 3, 19, 3]
k = 3
print("K'th smallest element is", kthSmallest(nums, k))
```

### Given an array which consists of only 0, 1 and 2. Sort the array without using any sorting algo

```python
def sort012(arr):
        n=len(arr)
        low=0
        high=n-1
        mid=0
        while mid<=high:
            if arr[mid]==0:
                arr[mid] , arr[low] = arr[low] , arr[mid]
                mid+=1
                low+=1
            
            elif arr[mid]==1:
                mid+=1
            
            else:
                arr[mid] , arr[high] = arr[high] , arr[mid]
                high-=1
                
A=[0,0,0,2,2,2,1,1,1,0,2,1,1,2,0]
sort012(A)
print("After sorting:", A)
```

### Move all the negative elements to one side of the array

```python
def RearrangePosNeg(arr):
 n = len(arr)
 for i in range(1, n):
  key = arr[i]

  # if current element is positive do nothing
  if (key > 0):
   continue

  # if current element is negative, shift positive elements of arr[0..i-1], to one position to their right 
  j = i - 1
  while (j >= 0 and arr[j] > 0):
   arr[j + 1] = arr[j]
   j = j - 1

  # Put negative element at its
  # right position
  arr[j + 1] = key


# Driver Code
if __name__ == "__main__":
 arr = [-12, 11, -13, -5,
  6, -7, 5, -3, -6]
 RearrangePosNeg(arr)
 print(arr)
```

{{< gumroad "https://highnessatharva.gumroad.com/l/dsa-python-array" "/blog/gumroad-marketing.webp" >}}  

---
