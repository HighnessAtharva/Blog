---
title: "DSA in Python - Arrays"
date: 2022-07-07T23:18:34+05:30
draft: false
cover: 
    image: dsa/array.jpg
    alt: Arrays
    caption: Learn Array Algorithms in Python
tags: ["DSA-Python"] 

---

# Array

## Reverse the array

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

## Find the maximum and minimum element in an array

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

## Find the "Kth" max and min element of an array

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

## Given an array which consists of only 0, 1 and 2. Sort the array without using any sorting algo

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

## Move all the negative elements to one side of the array

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

## Find the Union and Intersection of the two sorted arrays.

```python
def printUnion(arr1, arr2, n1, n2):
    hs = set()
    # Insert the elements of arr1[] to set hs
    for i in range(0, n1):
     hs.add(arr1[i]) 
    # Insert the elements of arr2[] to set hs
    for i in range(0, n2):
     hs.add(arr2[i])
    for i in hs:
     print(i, end=" ")
    print("Union Count", len(hs))


def printIntersection(arr1, arr2, n1, n2):
    hs = set()  
    # Insert the elements of arr1[] to set S
    for i in range(0, n1):
     hs.add(arr1[i])
    intersectCount=0
    for i in range(0, n2):  
     # If element is present in set then
     # push it to vector V
     if arr2[i] in hs:
            print(arr2[i], end=" ")
            intersectCount+=1
    print("Intersection Count", intersectCount)

# Driver Program
arr1 = [7, 1, 5, 2, 3, 6]
arr2 = [3, 8, 6, 20, 7]
n1 = len(arr1)
n2 = len(arr2)

# Function call
printUnion(arr1, arr2, n1, n2)
printIntersection(arr1, arr2, n1, n2)

```

## Write a program to cyclically rotate an array by one.

```python
def rotate(arr):
    n = len(arr)
    i = 0
    j = n - 1
    while i != j:
        arr[i], arr[j] = arr[j], arr[i]
        i = i + 1
 
# Driver function
arr= [1, 2, 3, 4, 5]
rotate(arr)
print(arr)
```

## Find Largest sum contiguous Subarray [V. IMP] / Kadne's Algorithm

```python
def maxSubArraySum(a):
    size=len(a)
    max_so_far =a[0]
    curr_max = a[0]
    
    for i in range(1,size):
        curr_max = max(a[i], curr_max + a[i])
        max_so_far = max(max_so_far,curr_max)
    return max_so_far

a = [-2, -3, 4, -1, -2, 1, 5, -3]
print ("Maximum contiguous sum is" , maxSubArraySum(a))
```

## Minimise the maximum difference between heights 

```python
"""

Given heights of n towers and a value k. We need to either increase or decrease the height of every tower by k (only once) where k > 0. The task is to minimize the difference between the heights of the longest and the shortest tower after modifications and output this difference.
Input : arr[] = {1, 5, 15, 10} k = 3   
Output : Maximum difference is 8 arr[] = {4, 8, 12, 7}

"""
def getMinDiff(arr, k):
    arr.sort()
    n=len(arr)
    ans = arr[n - 1] - arr[0]  # Maximum possible height difference

    tempmin = arr[0]
    tempmax = arr[n - 1]

    for i in range(1, n):
        tempmin = min(arr[0] + k, arr[i] - k)  
        
        # Minimum element when we add k to whole array Maximum element when we
        tempmax = max(arr[i - 1] + k, arr[n - 1] - k)
        
        # subtract k from whole array
        ans = min(ans, tempmax - tempmin)

    return ans

# Driver Code Starts
k = 6 # total towers
arr = [7, 4, 8, 8, 8, 9] # height of each array
print("Maximum difference of height between all towers (minimized as much as possible) is", getMinDiff(arr, k))
```

## Minimum no. of Jumps to reach end of an array

```python
"""
Given an array of integers where each element represents the max number of steps that can be made forward from that element. Write a function to return the minimum number of jumps to reach the end of the array (starting from the first element). If an element is 0, then we cannot move through that element. If we can't reach the end, return -1.

Input:  arr[] = {1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9}
Output: 3 (1-> 3 -> 8 -> 9)
"""
# Returns minimum number of jumps to reach arr[n-1] from arr[0]
def minJumps(arr, n):
    # The number of jumps needed to reach the starting index is 0
    if (n <= 1):
      return 0
    
    # Return -1 if not possible to jump
    if (arr[0] == 0):
      return -1
    
    # initialization
    # stores all time the maximal reachable index in the array
    maxReach = arr[0] 
    # stores the amount of steps we can still take
    step = arr[0]
    # stores the amount of jumps necessary to reach that maximal reachable position
    jump = 1
    
    # Start traversing array
    
    for i in range(1, n):
        # Check if we have reached the end of the array
        if (i == n-1):
          return jump
        
        # updating maxReach
        maxReach = max(maxReach, i + arr[i])
        
        # we use a step to get to the current index
        step -= 1;
        
        # If no further steps left
        if (step == 0):
          # we must have used a jump
            jump += 1
           
          # Check if the current index / position or lesser index
          # is the maximum reach point from the previous indexes
            if(i >= maxReach):
                return -1
        
          # re-initialize the steps to the amount
          # of steps to reach maxReach from position i.
            step = maxReach - i;
    return -1
    
 
arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
size = len(arr)
print("Minimum number of jumps to reach end is: ", minJumps(arr, size))
```

## Find duplicate in an array of N+1 Integers

```python
"""
Given a limited range array of size n containing elements between 1 and n-1 with one element repeating, find the duplicate number in it without using any extra space. NOTE : ARRAY IS LIMITED RANGE
"""
def findDuplicate(nums):
    actual_sum = sum(nums)
    expected_sum = len(nums) * (len(nums) - 1) // 2
    return actual_sum - expected_sum

A=[3,1,2,4,2]
print(findDuplicate(A))
```

## Merge 2 sorted arrays without using Extra space.

```python
def merge(X, Y):
    m = len(X)
    n = len(Y)
 
    # Consider each element `X[i]` of list `X[]` and ignore the element if it is
    # already in the correct order; otherwise, swap it with the next smaller
    # element, which happens to be the first element of `Y[]`.
    for i in range(m):
 
        # compare the current element of `X[]` with the first element of `Y[]`
        if X[i] > Y[0]:
 
            # swap `X[i] with `Y[0]`
            X[i],Y[0]=Y[0], X[i]
 
            first = Y[0]
 
            # move `Y[0]` to its correct position to maintain the sorted
            # order of `Y[]`. Note: `Y[1…n-1]` is already sorted
            k = 1
            while k < n and Y[k] < first:
                Y[k - 1] = Y[k]
                k = k + 1
 
            Y[k - 1] = first
 

X = [1, 4, 7, 8, 10]
Y = [2, 3, 9]
merge(X, Y)
print("X:", X)
print("Y:", Y)
```

## Merge Intervals

```python
def mergeIntervals(arr):
  
    # Sorting based on the increasing order
    # of the start intervals
    arr.sort(key=lambda x: x[0])
  
    # Stores index of last element in output array (modified arr[])
    index = 0
  
    # Traverse all input Intervals starting from second interval
    for i in range(1, len(arr)):
  
        # If this is not first Interval and overlaps with the previous one, Merge previous and current Intervals
        if (arr[index][1] >= arr[i][0]):
            arr[index][1] = max(arr[index][1], arr[i][1])
        else:
            index = index + 1
            arr[index] = arr[i]
  
    print("The Merged Intervals are :", end=" ")
    for i in range(index+1):
        print(arr[i], end=" ")
  
  

arr = [[6, 8], [1, 3], [2, 4], [4, 7]]
mergeIntervals(arr)
```

## Next Permutation

```python
"""
If all digits sorted in descending order, then output is always "Not Possible". For example, 4321. 
If all digits are sorted in ascending order, then we need to swap last two digits. For example, 1234. 
For other cases, we need to process the number from rightmost side (why? because we need to find the smallest of all greater numbers)
"""
def nextPermutation(arr):
    N=len(arr)
    ind = 0
    l = []
    l += arr
    for i in range(N-2, -1, -1):
        if l[i]<l[i+1]:
            ind = i
            break
    for i in range(N-1, ind, -1):
        if l[i]>l[ind]:
            l[i], l[ind] = l[ind], l[i]
            ind += 1
            break
    for i in range((N-ind)//2):
        l[i+ind], l[N-i-1] = l[N-i-1], l[i+ind]
    return "".join(l)
    
print(nextPermutation("218765"))
```

## Count Inversion

```python
def mergeSort(arr, n):
    # A temp_arr is created to store sorted array in merge function
    temp_arr = [0]*n
    return _mergeSort(arr, temp_arr, 0, n-1)
  
# This Function will use MergeSort to count inversions
def _mergeSort(arr, temp_arr, left, right):
    inv_count = 0
  
    # We will make a recursive call if and only if we have more than one elements
    if left < right:
  
        # mid is calculated to divide the array into two subarrays Floor division is must in case of python
        mid = (left + right)//2
  
        # It will calculate inversion counts in the left subarray
        inv_count += _mergeSort(arr, temp_arr, left, mid)
  
        # It will calculate inversion counts in right subarray
        inv_count += _mergeSort(arr, temp_arr,mid + 1, right)
  
        # It will merge two subarrays in a sorted subarray
        inv_count += merge(arr, temp_arr, left, mid, right)
    return inv_count
  
# This function will merge two subarrays
# in a single sorted subarray
  
  
def merge(arr, temp_arr, left, mid, right):
    i = left     # Starting index of left subarray
    j = mid + 1  # Starting index of right subarray
    k = left     # Starting index of to be sorted subarray
    inv_count = 0
  
    # Conditions are checked to make sure that i and j don't exceed their subarray limits.
    while i <= mid and j <= right:
        
        # There will be no inversion if arr[i] <= arr[j]
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            k += 1
            i += 1
        else:
            # Inversion will occur.
            temp_arr[k] = arr[j]
            inv_count += (mid-i + 1)
            k += 1
            j += 1
  
    # Copy the remaining elements of left subarray into temporary array
    while i <= mid:
        temp_arr[k] = arr[i]
        k += 1
        i += 1
  
    # Copy the remaining elements of right subarray into temporary array
    while j <= right:
        temp_arr[k] = arr[j]
        k += 1
        j += 1
  
    # Copy the sorted subarray into Original array
    for loop_var in range(left, right + 1):
        arr[loop_var] = temp_arr[loop_var]
  
    return inv_count
  
arr = [1, 20, 6, 4, 5]
n = len(arr)
result = mergeSort(arr, n)
print("Number of inversions are", result)
```

## Best time to buy and Sell stock

```python
"""
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
"""
def maxProfit(prices):
        max_profit = 0
        min_buy = float('inf')
        for price in prices:
            min_buy=min(min_buy, price)
            max_profit=max(max_profit, price-min_buy)
        return max_profit
print(maxProfit([7,1,5,3,6,4]))
```

## Find all pairs on integer array whose sum is equal to given number

```python
"""
An extended version of the two sum problem
"""
# Returns number of pairs in arr[0..n-1] with sum equal to 'sum'
def getPairsCount(arr, n, sum):
  unordered_map = {}
  count = 0
  for i in range(n):
    if sum - arr[i] in unordered_map:
      count += unordered_map[sum - arr[i]]
    if arr[i] in unordered_map:
      unordered_map[arr[i]] += 1
    else:
      unordered_map[arr[i]] = 1
  return count
  
# Driver code
arr = [1, 5, 7, -1, 5]
n = len(arr)
sum = 6
print('Count of pairs is', getPairsCount(arr, n, sum))
```

## Find common elements In 3 sorted arrays

```python
"""
Given three arrays sorted in non-decreasing order, print all common elements in these arrays.
"""
# Python function to print common elements in three sorted arrays
def findCommon(ar1, ar2, ar3, n1, n2, n3):

  # Initialize starting indexes for ar1[], ar2[] and ar3[]
  i, j, k = 0, 0, 0

  # Iterate through three arrays while all arrays have elements
  while (i < n1 and j < n2 and k < n3):

    # If x = y and y = z, print any of them and move ahead
    # in all arrays
    if (ar1[i] == ar2[j] and ar2[j] == ar3[k]):
      print (ar1[i])
      i += 1
      j += 1
      k += 1

    # x < y
    elif ar1[i] < ar2[j]:
      i += 1

    # y < z
    elif ar2[j] < ar3[k]:
      j += 1

    # We reach here when x > y and z < y, i.e., z is smallest
    else:
      k += 1


# Driver program to check above function
ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]
n1 = len(ar1)
n2 = len(ar2)
n3 = len(ar3)

print ("Common elements are")
findCommon(ar1, ar2, ar3, n1, n2, n3)


```

## Rearrange the array in alternating positive and negative items with O(1) extra space

```python
def rearrange(arr, n):
  i = 0
  j = n - 1

  # shift all negative values to the end
  while (i < j):

    while (i <= n - 1 and arr[i] > 0):
      i += 1
    while (j >= 0 and arr[j] < 0):
      j -= 1

    if (i < j):
      temp = arr[i]
      arr[i] = arr[j]
      arr[j] = temp

  # i has index of leftmost
  # negativ ement
  if (i == 0 or i == n):
    return 0

  # start with first positive element at index 0  array in alternating positive & negative items
  k = 0
  while (k < n and i < n):

    # swap next positive element at even position from next negative element.
    arr[k], arr[i]= arr[i], arr[k]
    i = i + 1
    k = k + 2

arr = [2, 3,-4, -1, 6, -9 ]
n = len(arr)
rearrange(arr, n)
print("Rearranged array is", arr)
```

## Find if there is any subarray with sum equal to 0

```python
"""
Given an array of positive and negative numbers, find if there is a subarray (of size at-least one) with 0 sum.

"""
#Function to check whether there is a subarray present with 0-sum or not.

def subArrayExists(arr):
    n=len(arr)
    #using set to store the prefix sum which has appeared already.
    s = set() 
 
    sum = 0
    #iterating over the array.
    for i in range(n): 
        #storing prefix sum.
        sum += arr[i] 
  
        #if prefix sum is 0 or if it is already present in set then it is
  #repeated which means there is a subarray whose summation was 0, so we return true.
        if sum == 0 or sum in s: 
            return True
            
        #storing every prefix sum obtained in set.
        s.add(sum) 
    
    #returning false if we don't get any subarray with 0 sum.      
    return False

print(subArrayExists([4, 2, -3, 1, 6]))
```

## Find factorial of a large number

```python
def range_prod(low,high):
    if low+1 < high:
        mid = (high+low)//2
        return range_prod(low,mid) * range_prod(mid+1,high)
    if low == high:
        return low
    return low*high

def factorial(n):
    if n < 2:
        return 1
    return range_prod(1,n)
    
print(factorial(12))
```

## Find maximum product subarray

```python
def maxProduct(arr):
    n=len(arr)
    # Variables to store maximum and minimum product till ith index.
    minVal = arr[0]
    maxVal = arr[0]
    maxProduct = arr[0]
    for i in range(1, n):
        # When multiplied by -ve number, maxVal becomes minVal and minVal becomes maxVal.
        if (arr[i] < 0):
            minVal, maxVal = maxVal, minVal
        # maxVal and minVal stores the product of subarray ending at arr[i].
        maxVal = max(arr[i], maxVal * arr[i])
        minVal = min(arr[i], minVal * arr[i])
        # Max Product of array.
        maxProduct = max(maxProduct, maxVal)
    return maxProduct

print(maxProduct([6, -3, -10, 0, 2]))

```

## Find longest consecutive subsequence

```python
"""
Given an array of integers, find the length of the longest sub-sequence such that elements in the subsequence are consecutive integers, the consecutive numbers can be in any order. 
"""
def findLongestConseqSubseq(arr):
    n=len(arr)
    #using a Set to store elements.
    s = set() 
    ans=0
  
    #inserting all the array elements in Set.
    for ele in arr: 
        s.add(ele) 
  
    #checking each possible sequence from the start. 
    for i in range(n): 
  
        #if current element is starting element of a sequence then only we try to find out the length of sequence. 
        if (arr[i]-1) not in s: 
  
            j=arr[i] 
            #then we keep checking whether the next consecutive elements are present in Set and 
         #we keep incrementing the counter. 
            while(j in s): 
                j+=1
  
            #storing the maximum count.
            ans=max(ans, j-arr[i]) 
            
    #returning the length of longest subsequence.       
    return ans 
    
print(findLongestConseqSubseq([1, 9, 3, 10, 4, 20, 2]))
```

## Given an array of size n and a number k, find all elements that appear more than " n/k " times.

```python
"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
"""
def majorityElement(nums):
    if not nums:
        return []
    count1, count2, candidate1, candidate2 = 0, 0, None, None
    for x in nums:
        if candidate1 == x:
            count1 += 1
        elif candidate2 == x:
            count2 += 1
        elif count1 == 0:
            candidate1 = x
            count1 = 1
        elif count2 == 0:
            candidate2 = x
            count2 = 1
        else:
            count1 -= 1
            count2 -= 1
    res = []
    for c in [candidate1, candidate2]:
        if nums.count(c) > len(nums) // 3:
            res.append(c)
    return res
print(majorityElement([3,2,3]))
```

## Maximum profit by buying and selling a share atmost twice

```python
"""
Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
"""
def maxProfit(prices):
    b1, b2= -float('inf'), -float('inf')
    s1, s2 = 0, 0
    for price in prices:
        s2 = max(s2, b2 + price)
        b2 = max(b2, s1 - price)
        s1 = max(s1, b1 + price)
        b1 = max(b1, -price)
    return s2
    
print(maxProfit([3,3,5,0,0,3,1,4]))
```

## Find whether an array is a subset of another array

```python
def isSubset( a1, a2):
    n,m =len(a1), len(a2)
    s = set()
    for i in range(n) :
        s.add(a1[i])

    p = len(s)
    for i in range(m) :
        s.add(a2[i])
    if (len(s) == p) :
        return "Yes"
    return "No"

a=[11, 1, 13, 21, 3, 7]
b=[11, 3, 7, 1]
print(isSubset(a, b))
```

## Find the triplet that sum to a given value

```python
def findTriplets(arr, X): 
    n=len(arr)
    found = False
    for i in range(0, n-2): 
        for j in range(i+1, n-1): 
            for k in range(j+1, n): 
                if (arr[i] + arr[j] + arr[k] == X): 
                    print(arr[i], arr[j], arr[k]) 
                    found = True
     
    # If no triplet with 0 sum found in array 
    if (found == False): 
        print("Three Sum not exist ") 
   
arr = [0, -1, 2, -3, 1] 
sum= 3
findTriplets(arr, sum) 
```

## Trapping Rain water problem

```python
def trap(heights):
 
    # maintain two pointers left and right, pointing to the leftmost and
    # rightmost index of the input list
    (left, right) = (0, len(heights) - 1)
    water = 0
 
    maxLeft = heights[left]
    maxRight = heights[right]
 
    while left < right:
        if heights[left] <= heights[right]:
            left = left + 1
            maxLeft = max(maxLeft, heights[left])
            water += (maxLeft - heights[left])
        else:
            right = right - 1
            maxRight = max(maxRight, heights[right])
            water += (maxRight - heights[right])
 
    return water
 

heights = [7, 0, 4, 2, 5, 0, 6, 4, 0, 5]
print("The maximum amount of water that can be trapped is", trap(heights))
```

## Chocolate Distribution problem

```python
"""
Input : arr[] = {7, 3, 2, 4, 9, 12, 56} , m = 3 
Output: Minimum Difference is 2 
Explanation: We have seven packets of chocolates and we need to pick three packets for 3 students. If we pick 2, 3 and 4, we get the minimum  difference between maximum and minimum packet sizes.
"""
# arr[0..n-1] represents sizes of packets
# m is number of students.
# Returns minimum difference between maximum
# and minimum values of distribution.
def findMinDiff(arr, m):
    n=len(arr)
    if (m==0 or n==0):
        return 0    
    arr.sort()  
    
    # Number of students cannot be more than number of packets
    if (n < m):
     return -1   
     
    # Largest number of chocolates
    min_diff = arr[n-1] - arr[0]    
    
    # Find the subarray of size m such that difference between last (maximum in case of sorted) and 
    #first (minimum in case of sorted) elements of subarray is minimum.
    for i in range(len(arr) - m + 1):
     min_diff = min(min_diff , arr[i + m - 1] - arr[i])
    
    return min_diff


arr = [12, 4, 7, 9, 2, 23, 25, 41, 30, 40, 28, 42, 30, 44, 48, 43, 50]
m = 7 # Number of students
print("Minimum difference is", findMinDiff(arr, m))
 

```

## Smallest Subarray with sum greater than a given value

```python
"""
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
"""
def minSubArrayLen(nums, target):
    i, j, pres, res = 0 , 0 , 0, len(nums) + 1
    while j < len(nums):
        pres += nums[j]; j += 1
        while pres >= target:
            res = min(res, j - i)
            pres -= nums[i]
            i+= 1
    return res if res != len(nums) + 1 else 0

sum=7
print(minSubArrayLen([2,3,1,2,4,3], sum))
```

## Three way partitioning of an array around a given value

```python
def threeWayPartition(arr, lowVal, highVal):
    n = len(arr)
    # Initialize ext available positions for smaller (than range) and greater elements
    start = 0
    end = n - 1
    i = 0
 
    # Traverse elements from left
    while i <= end:
 
        # If current element is smaller than range, put it on next available smaller position.
        if arr[i] < lowVal:
            arr[i], arr[start] = arr[start], arr[i]
            i += 1
            start += 1
 
        # If current element is greater than range, put it on next available greater position.
        elif arr[i] > highVal:
              arr[i], arr[end] = arr[end], arr[i]
              end -= 1
        else:
            i += 1
 
arr = [1, 14, 5, 20, 4, 2, 54, 20, 87, 98, 3, 1, 32]
"""
1) All elements smaller than lowVal come first. 
2) All elements in range lowVal to highVal come next. 
3) All elements greater than highVal appear in the end.
"""
threeWayPartition(arr, 10, 20)
print(arr)

```

## Minimum swaps required bring elements less equal K together

```python
"""
Find the minimum number of swaps required to bring all the numbers less than or equal to k together, i.e. make them a contiguous subarray.
"""
def minSwap(arr, k) :
    n=len(arr)
    # Find count of elements which are less than equals to k
    count = 0
    for i in range(0, n) :
        if (arr[i] <= k) :
            count = count + 1
     
    # Find unwanted elements in current window of size 'count'
    bad = 0
    for i in range(0, count) :
        if (arr[i] > k) :
            bad = bad + 1
     
    # Initialize answer with 'bad' value of current window
    ans = bad
    j = count
    for i in range(0, n) :
         
        if(j == n) :
            break
             
        # Decrement count of previous window
        if (arr[i] > k) :
            bad = bad - 1
         
        # Increment count of current window
        if (arr[j] > k) :
            bad = bad + 1
         
        # Update ans if count of 'bad' is less in current window
        ans = min(ans, bad)
        j = j + 1
 
    return ans
 

arr = [2, 1, 5, 6, 3]
k = 3
print (minSwap(arr, k))
 
arr1 = [2, 7, 9, 5, 8, 7, 4]
k = 5
print (minSwap(arr1, k))
```

## Minimum no. of operations required to make an array palindrome

```python
"""
Input:  [6, 1, 3, 7]
Output: 1
Explanation: [6, 1, 3, 7] —> Merge 6 and 1 —> [7, 3, 7]
"""
def findMin(arr):
 
    # stores the minimum number of merge operations needed
    count = 0
 
    # `i` and `j` initially points to endpoints of the array
    i = 0
    j = len(arr) - 1
 
    # loop till the search space is exhausted
    while i < j:
        if arr[i] < arr[j]:
            # merge item at i'th index with the item at (i+1)'th index
            arr[i + 1] += arr[i]
            i = i + 1
            count = count + 1
        elif arr[i] > arr[j]:
            # merge item at (j-1)'th index with the item at j'th index
            arr[j - 1] += arr[j]
            j = j - 1
            count = count + 1
        # otherwise, ignore both the elements
        else:
            i = i + 1
            j = j - 1
 
    return count
 

arr = [6, 1, 4, 3, 1, 7]
min = findMin(arr)
print("The minimum number of operations required:", min)
```

## Median of 2 sorted arrays of different size

```python
def Solution(arr1, arr2):
    arr = arr1 + arr2
    arr.sort()
    n = len(arr)
  
    # If length of array is even
    if n % 2 == 0:
        return (arr[n // 2] + arr[n // 2 - 1]) / 2
 
    # If length of array is odd
    else:
        return arr[n//2]
  

arr1 = [ -5, 3, 6, 12, 15]
arr2 = [ -12, -10, -6, -3, 4, 10 ]
print("Median = ", Solution(arr1, arr2))
```
