<!-- - [x] Array
- [x] Backtracking
- [x] Binary Trees
- [x] Bit Manipulation
- [x] Binary Search Trees
- [x] Dynamic Programming
- [x] Graph
- [x] Greedy
- [x] Heap
- [x] LinkedList
- [x] Matrix
- [x] Searching & Sorting
- [x] Stacks & Queues
- [x] String
- [x] Trie
- [x] Elementary Problems  -->
  
[toc]

<hr>

# Array

## [Reverse the array](https://practice.geeksforgeeks.org/problems/reverse-an-array/0)

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

## [Find the maximum and minimum element in an array](https://practice.geeksforgeeks.org/problems/find-minimum-and-maximum-element-in-an-array4428/1)

```python
def getMinMax(arr):
    min = arr[0]
    max = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < min:
            min = arr[i]
        if arr[i] > max:
            max = arr[i]
    return min, max

arr = [1000, 11, 445, 1, 330, 3000]
min, max = getMinMax(arr)
print("Minimum element is", min)
print("Maximum element is", max)
 
```

## [Find the "Kth" max and min element of an array](https://practice.geeksforgeeks.org/problems/kth-smallest-element/0)

```python
def kthSmallest(arr, k):
    return sorted(arr)[k-1]

def kthLargest(arr, k):
    return sorted(arr, reverse=True)[k-1]
 
nums = [1, 4, 5, 3, 19, 1, 90, 99, 100]
k = 3
print("K'th smallest element is", kthSmallest(nums, k))
print("K'th largest element is", kthLargest(nums, k))
```

## [Given an array which consists of only 0, 1 and 2. Sort the array without using any sorting algo](https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s/0)

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

## [Move all the negative elements to one side of the array](https://practice.geeksforgeeks.org/problems/move-all-negative-elements-to-end1813/1)

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

## [Find the Union and Intersection of the two sorted arrays.](https://practice.geeksforgeeks.org/problems/union-of-two-arrays/0)

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

## [Write a program to cyclically rotate an array by one.](https://practice.geeksforgeeks.org/problems/cyclically-rotate-an-array-by-one/0)

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

## [Find Largest sum contiguous Subarray [V. IMP] / Kadne's Algorithm](https://practice.geeksforgeeks.org/problems/kadanes-algorithm/0)

## <img src="https://media.geeksforgeeks.org/wp-content/cdn-uploads/kadane-Algorithm.png" style="zoom: 50%;" />

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

## [Minimise the maximum difference between heights [V.IMP]](https://practice.geeksforgeeks.org/problems/minimize-the-heights3351/1)

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
k = 6 # permissible increase or decrease in the height of each tower. 
arr = [7, 4, 8, 8, 8, 9] # height of each array
print("Maximum difference of height between all towers (minimized as much as possible) is", getMinDiff(arr, k))
```

## [Minimum no. of Jumps to reach end of an array](https://practice.geeksforgeeks.org/problems/minimum-number-of-jumps/0)

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
    
    for start in range(1, n):
        # Check if we have reached the end of the array
        if (start == n-1):
          return jump
        
        # updating maxReach
        maxReach = max(maxReach, start + arr[start])
        
        # we use a step to get to the current index
        step -= 1;
        
        # If no further steps left
        if (step == 0):
          # we must have used a jump
            jump += 1
           
          # Check if the current index / position or lesser index
          # is the maximum reach point from the previous indexes
            if(start >= maxReach):
                return -1
        
          # re-initialize the steps to the amount
          # of steps to reach maxReach from position i.
            step = maxReach - start;
    return -1
    
 
arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
size = len(arr)
print("Minimum number of jumps to reach end is: ", minJumps(arr, size))
```

## [Find duplicate in an array of N+1 Integers](https://leetcode.com/problems/find-the-duplicate-number/)

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

## [Merge 2 sorted arrays without using Extra space.](https://practice.geeksforgeeks.org/problems/merge-two-sorted-arrays5135/1)

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

## [Merge Intervals](https://leetcode.com/problems/merge-intervals/)

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

## [Next Permutation](https://leetcode.com/problems/next-permutation/)

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

## [Count Inversion](https://practice.geeksforgeeks.org/problems/inversion-of-array/0)

```python
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
    for x in range(left, right + 1):
        arr[x] = temp_arr[x]
  
    return inv_count
  
arr = [1, 20, 6, 4, 5]
n = len(arr)
temp_arr = [0]*n
result = _mergeSort(arr, temp_arr, 0, n-1)
print("Number of inversions are", result)
```

## [Best time to buy and Sell stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

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

## [Find all pairs on integer array whose sum is equal to given number](https://practice.geeksforgeeks.org/problems/count-pairs-with-given-sum5022/1)

```python
"""
An extended version of the two sum problem
"""
# Returns number of pairs in arr[0..n-1] with sum equal to 'sum'
def getPairsCount(arr, n, sum):
  seen = {}
  count = 0
  for i in range(n):
    if sum - arr[i] in seen:
      count += seen[sum - arr[i]]
    if arr[i] in seen:
      seen[arr[i]] += 1
    else:
      seen[arr[i]] = 1
  return count
  
# Driver code
arr = [1, 5, 7, -1, 5]
n = len(arr)
sum = 6
print('Count of pairs is', getPairsCount(arr, n, sum))
```

## [Find common elements In 3 sorted arrays](https://practice.geeksforgeeks.org/problems/common-elements1132/1)

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

## [Rearrange the array in alternating positive and negative items with O(1) extra space](https://practice.geeksforgeeks.org/problems/array-of-alternate-ve-and-ve-nos1401/1)

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

## [Find if there is any subarray with sum equal to 0](https://practice.geeksforgeeks.org/problems/subarray-with-0-sum/0)

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

## [Find factorial of a large number](https://practice.geeksforgeeks.org/problems/factorials-of-large-numbers/0)

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

## [Find maximum product subarray](https://practice.geeksforgeeks.org/problems/maximum-product-subarray3604/1)

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

## [Find longest consecutive subsequence](https://practice.geeksforgeeks.org/problems/longest-consecutive-subsequence/0)

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

## [Given an array of size n and a number k, find all elements that appear more than " n/k " times.](https://leetcode.com/problems/majority-element-ii/)

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

## [Maximum profit by buying and selling a share atmost twice](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/)

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

## [Find whether an array is a subset of another array](https://practice.geeksforgeeks.org/problems/array-subset-of-another-array/0)

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

## [Find the triplet that sum to a given value](https://practice.geeksforgeeks.org/problems/triplet-sum-in-array/0)

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

## [Trapping Rain water problem](https://practice.geeksforgeeks.org/problems/trapping-rain-water/0)

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

## [Chocolate Distribution problem](https://practice.geeksforgeeks.org/problems/chocolate-distribution-problem/0)

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

## [Smallest Subarray with sum greater than a given value](https://leetcode.com/problems/minimum-size-subarray-sum/)

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

## [Three way partitioning of an array around a given value](https://practice.geeksforgeeks.org/problems/three-way-partitioning/1)

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

## [Minimum swaps required bring elements less equal K together](https://practice.geeksforgeeks.org/problems/minimum-swaps-required-to-bring-all-elements-less-than-or-equal-to-k-together/0)

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

## [Minimum no. of operations required to make an array palindrome](https://app.glider.ai/practice/problem/basic-programming/make-array-palindrome/problem)

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

## [Median of 2 sorted arrays of different size](https://leetcode.com/problems/median-of-two-sorted-arrays/)

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

# BackTracking

## [Rat in a maze Problem](https://practice.geeksforgeeks.org/problems/rat-in-a-maze-problem/1)

```python
"""
N = 4
m[][] = {{1, 0, 0, 0},
         {1, 1, 0, 1}, 
         {1, 1, 0, 0},
         {0, 1, 1, 1}}
Output:
DDRDRR DRDDRR
Explanation:
The rat can reach the destination at 
(3, 3) from (0, 0) by two paths - DRDDRR 
and DDRDRR, when printed in sorted order 
we get DDRDRR DRDDRR.
"""
def setup():
    global v
    v = [[0 for i in range(100)] for j in range(100)]
    global ans
    ans = []
    
def path(arr, x, y, pth, n):
    if x==n-1 and y==n-1:
        global ans
        ans.append(pth)
        return
    global v
    if arr[x][y]==0 or v[x][y]==1:
        return
    v[x][y]=1
    if x>0:
        path(arr, x-1, y, pth+'U', n)
    if y>0:
        path(arr, x, y-1, pth+'L', n)
    if x<n-1:
        path(arr, x+1, y, pth+'D', n)
    if y<n-1:
        path(arr, x, y+1, pth+'R', n)
    v[x][y]=0

def findPath(m, n):
    global ans
    ans= []
    if m[0][0] == 0 or m[n-1][n-1]==0 :
        return ans
    setup()
    path(m, 0, 0, "", n)
    ans.sort()
    return ans

m = [ [ 1, 0, 0, 0, 0 ], [ 1, 1, 1, 1, 1 ], [ 1, 1, 1, 0, 1 ], [ 0, 0, 0, 0, 1 ],[ 0, 0, 0, 0, 1 ] ]
n = len(m)
print(findPath(m, n))
```

## [Printing all solutions in N-Queen Problem](https://www.geeksforgeeks.org/printing-solutions-n-queen-problem/)

```python

def isSafe(mat, r, c):
 
    # return false if two queens share the same column
    for i in range(r):
        if mat[i][c] == 'Q':
            return False
 
    # return false if two queens share the same `` diagonal
    (i, j) = (r, c)
    while i >= 0 and j >= 0:
        if mat[i][j] == 'Q':
            return False
        i = i - 1
        j = j - 1
 
    # return false if two queens share the same `/` diagonal
    (i, j) = (r, c)
    while i >= 0 and j < len(mat):
        if mat[i][j] == 'Q':
            return False
        i = i - 1
        j = j + 1
 
    return True
 
 
def printSolution(mat):
    for r in mat:
        print(str(r).replace(',', '').replace('\'', ''))
    print()
 
 
def nQueen(mat, r):
 
    # if `N` queens are placed successfully, print the solution
    if r == len(mat):
        printSolution(mat)
        return
 
    # place queen at every square in the current row `r`
    # and recur for each valid movement
    for i in range(len(mat)):
 
        # if no two queens threaten each other
        if isSafe(mat, r, i):
            # place queen on the current square
            mat[r][i] = 'Q'
 
            # recur for the next row
            nQueen(mat, r + 1)
 
            # backtrack and remove the queen from the current square
            mat[r][i] = '–'
 
 
# `N × N` chessboard
N = 8

# `mat[][]` keeps track of the position of queens in
# the current configuration
mat = [['–' for x in range(N)] for y in range(N)]

nQueen(mat, 0)
```

## [Word Break Problem using Backtracking](https://practice.geeksforgeeks.org/problems/word-break-part-2/0)

```python
# A recursive program to print all possible partitions of a given string into dictionary words
 
# A utility function to check whether a word is present in dictionary or not.  An array of strings is used for dictionary.  Using array of strings for dictionary is definitely not a good idea. We have used for simplicity of the program
def dictionaryContains(word):
    dictionary = {"mobile", "samsung", "sam", "sung", "man",
                  "mango", "icecream", "and", "go", "i", "love", "ice", "cream"}
    return word in dictionary
 
# Prints all possible word breaks of given string
def wordBreak(string):
   
    # Last argument is prefix
    wordBreakUtil(string, len(string), "")
 
# Result store the current prefix with spaces
# between words
def wordBreakUtil(string, n, result):
 
    # Process all prefixes one by one
    for i in range(1, n + 1):
       
        # Extract substring from 0 to i in prefix
        prefix = string[:i]
         
        # If dictionary contains this prefix, then
        # we check for remaining string. Otherwise
        # we ignore this prefix (there is no else for
        # this if) and try next
        if dictionaryContains(prefix):
           
            # If no more elements are there, print it
            if i == n:
 
                # Add this element to previous prefix
                result += prefix
                print(result)
                return
            wordBreakUtil(string[i:], n - i, result+prefix+" ")
 

print("First Test:")
wordBreak("iloveicecreamandmango")

print("\nSecond Test:")
wordBreak("ilovesamsungmobile")
 
```

## [Remove Invalid Parentheses](https://leetcode.com/problems/remove-invalid-parentheses/)

```python

from collections import deque

def isValidString(string):
    left = 0
    right = 0
    index = 0
    
    while index < len(string):
        if string[index] == '(':
            left += 1
            
        elif string[index] == ')':
            if left > 0:
                left -= 1
                
            else:
                right += 1
                
            if right > left:
                return False
                
        index += 1
        
    return left == right
    
def removeInvalidParentheses(string):
    
    visited = set()
    result = []
    q = deque()
    valid = False
    
    visited.add(string)
    q.append(string)
    # BFS.
    while len(q) > 0:
        possibleAnswer = q.popleft()
        
        # Check whether 'possibleAnswer' is valid or not.
        if isValidString(possibleAnswer):
            result.append(possibleAnswer)
            valid = True
            
        # If true, then the solution exists at current level. No need to move at next state.
        if valid == True:
            continue
        
        # Generate all possible next state of Strings from current String.
        for i in range(len(possibleAnswer)):
            if possibleAnswer[i] == '(' or possibleAnswer[i] == ')':
                temp = possibleAnswer[0 : i] + possibleAnswer[i + 1 : len(possibleAnswer)]
                
                if temp not in visited:
                    q.append(temp)
                    visited.add(temp)
                    
    return sorted(result)
    
print(removeInvalidParentheses(')(()))'))
print(removeInvalidParentheses('(((a))) ((a))()'))

```

## [Sudoku Solver](https://practice.geeksforgeeks.org/problems/solve-the-sudoku/0)

```python

# N is the size of the 2D matrix N*N
N = 9
 
# A utility function to print grid
def printing(arr):
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end = " ")
        print()
 
# Checks whether it will be legal to assign num to the given row, col
def isSafe(grid, row, col, num):
 
    # Check if we find the same num in the similar row , we return false
    for x in range(9):
        if grid[row][x] == num:
            return False
 
    # Check if we find the same num in the similar column , we return false
    for x in range(9):
        if grid[x][col] == num:
            return False
 
    # Check if we find the same num in the particular 3*3 matrix, we return false
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True
 
# Takes a partially filled-in grid and attempts to assign values to all unassigned locations in
# such a way to meet the requirements for Sudoku solution (non-duplication across rows, columns, and boxes) 
def solveSudoku(grid, row, col):
 
    # Check if we have reached the 8th row and 9th column (0 indexed matrix) , we are
    # returning true to avoid further backtracking
    if (row == N - 1 and col == N):
        return True
     
    # Check if column value becomes 9 , we move to next row and column start from 0
    if col == N:
        row += 1
        col = 0
 
    # Check if the current position of the grid already contains value >0, we iterate for next column
    if grid[row][col] > 0:
        return solveSudoku(grid, row, col + 1)
    for num in range(1, N + 1, 1):
     
        # Check if it is safe to place the num (1-9) in the given row ,col ->we
        # move to next column
        if isSafe(grid, row, col, num):
         
            # Assigning the num in the current (row,col) position of the grid and assuming our assigned
            # num in the position is correct
            grid[row][col] = num
 
            # Checking for next possibility with next column
            if solveSudoku(grid, row, col + 1):
                return True
 
        # Removing the assigned num , since our assumption was wrong , and we go for next assumption with 
     #diff num value
        grid[row][col] = 0
    return False

 
# 0 means unassigned cells
grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]
 
if (solveSudoku(grid, 0, 0)):
    printing(grid)
else:
    print("no solution exists ")
```

## [m-Colouring Problem](https://practice.geeksforgeeks.org/problems/m-coloring-problem/0)

```python
"""
An array color[V] that should have numbers from 1 to m. color[i] should represent the color assigned to the ith vertex. 
The code should also return false if the graph cannot be colored with m colors.
"""

from queue import Queue
 
class node(object):
    color = 1
    edges = set()
 
def canPaint(nodes, n, m):
 
    # Create a visited array of n nodes, initialized to zero
    visited = [0 for _ in range(n+1)]
 
    # maxColors used till now are 1 as all nodes are painted color 1
    maxColors = 1
 
    # Do a full BFS traversal from all unvisited starting points
    for _ in range(1, n + 1):
        if visited[_]:
            continue
 
        # If the starting point is unvisited, mark it visited and push it in queue
        visited[_] = 1
        q = Queue()
        q.put(_)
 
        # BFS Travel starts here
        while not q.empty():
            top = q.get()
 
            # Checking all adjacent nodes to "top" edge in our queue
            for _ in nodes[top].edges:
 
                # IMPORTANT: If the color of the adjacent node is same, increase it by 1
 
                if nodes[top].color == nodes[_].color:
                    nodes[_].color += 1
 
                # If number of colors used shoots m, return 0
                maxColors = max(maxColors, max(
                    nodes[top].color, nodes[_].color))
                     
                if maxColors > m:
                    print(maxColors)
                    return 0
 
                # If the adjacent node is not visited, mark it visited and push it in queue
                if not visited[_]:
                    visited[_] = 1
                    q.put(_)
                     
    return 1
 

n = 4
graph = [ [ 0, 1, 1, 1 ],
          [ 1, 0, 1, 0 ],
          [ 1, 1, 0, 1 ],
          [ 1, 0, 1, 0 ] ]
           
# Number of colors
m = 3 

# Create a vector of n+1 nodes of type "node" The zeroth position is just dummy (1 to n to be used)
nodes = []
for _ in range(n+1):
    nodes.append(node())

# Add edges to each node as per given input
for _ in range(n):
    for __ in range(n):
        if graph[_][__]:
             
            # Connect the undirected graph
            nodes[_].edges.add(_)
            nodes[__].edges.add(__)

# Display final answer
print(canPaint(nodes, n, m))
```

## [Print all palindromic partitions of a string](https://www.geeksforgeeks.org/given-a-string-print-all-possible-palindromic-partition/)

```python
def isPalindrome(string: str,
                 low: int, high: int):
    while low < high:
        if string[low] != string[high]:
            return False
        low += 1
        high -= 1
    return True
 
# Recursive function to find all palindromic partitions of str[start..n-1]
# allPart --> A vector of vector of strings.
#             Every vector inside it stores a partition
# currPart --> A vector of strings to store current partition
def allPalPartUtil(allPart: list, currPart: list,
                   start: int, n: int, string: str):
 
    # If 'start' has reached len
    if start >= n:
         
        # In Python list are passed by reference that is why it is needed to copy first and then append
        x = currPart.copy()
 
        allPart.append(x)
        return
 
    # Pick all possible ending points for substrings
    for i in range(start, n):
 
        # If substring str[start..i] is palindrome
        if isPalindrome(string, start, i):
 
            # Add the substring to result
            currPart.append(string[start:i + 1])
 
            # Recur for remaining substring
            allPalPartUtil(allPart, currPart,
                            i + 1, n, string)
 
            # Remove substring str[start..i] from current partition
            currPart.pop()
 
# Function to print all possible palindromic partitions of str.
# It mainly creates vectors and calls allPalPartUtil()
def allPalPartitions(string: str):
 
    n = len(string)
 
    # To Store all palindromic partitions
    allPart = []
 
    # To store current palindromic partition
    currPart = []
 
    # Call recursive function to generate all partitions and store in allPart
    allPalPartUtil(allPart, currPart, 0, n, string)
 
    # Print all partitions generated by above call
    for i in range(len(allPart)):
        for j in range(len(allPart[i])):
            print(allPart[i][j], end = " ")
        print()
 

string = "nitin"
allPalPartitions(string)
```

## [Subset Sum Problem](https://practice.geeksforgeeks.org/problems/subset-sum-problem2014/1)

```python
"""
Input : arr[] = {4, 1, 10, 12, 5, 2}, 
          sum = 9
Output : TRUE
{4, 5} is a subset with sum 9.

Input : arr[] = {1, 8, 2, 5}, 
          sum = 4
Output : FALSE 
There exists no subset with sum 4.
"""
def isPossible(elements, target):
 
    dp = [False]*(target+1)
 
    # initializing with 1 as sum 0 is always possible
    dp[0] = True
 
    # loop to go through every element of the elements array
    for ele in elements:
       
        # to change the value o all possible sum values to True
        for j in range(target, ele - 1, -1):
            if dp[j - ele]:
                dp[j] = True
 
    # If target is possible return True else False
    return dp[target]
 
# Driver code
arr = [6, 2, 5]
target = 7
 
if isPossible(arr, target):
    print("YES")
else:
    print("NO")
```

## [The Knight’s tour problem](https://www.geeksforgeeks.org/the-knights-tour-problem-backtracking-1/)

```python
# Chessboard Size
n = 6

def isSafe(x, y, board):
  '''
    A utility function to check if i,j are valid indexes
    for N*N chessboard
  '''
  if(x >= 0 and y >= 0 and x < n and y < n and board[x][y] == -1):
    return True
  return False


def printSolution(n, board):
  '''
    A utility function to print Chessboard matrix
  '''
  for i in range(n):
    for j in range(n):
      print(board[i][j], end=' ')
    print()


def solveKT(n):
  '''
    This function solves the Knight Tour problem using
    Backtracking. This function mainly uses solveKTUtil()
    to solve the problem. It returns false if no complete
    tour is possible, otherwise return true and prints the
    tour.
    Please note that there may be more than one solutions,
    this function prints one of the feasible solutions.
  '''

  # Initialization of Board matrix
  board = [[-1 for i in range(n)]for i in range(n)]

  # move_x and move_y define next move of Knight.
  # move_x is for next value of x coordinate
  # move_y is for next value of y coordinate
  move_x = [2, 1, -1, -2, -2, -1, 1, 2]
  move_y = [1, 2, 2, 1, -1, -2, -2, -1]

  # Since the Knight is initially at the first block
  board[0][0] = 0

  # Step counter for knight's position
  pos = 1

  # Checking if solution exists or not
  if(not solveKTUtil(n, board, 0, 0, move_x, move_y, pos)):
    print("Solution does not exist")
  else:
    printSolution(n, board)


def solveKTUtil(n, board, curr_x, curr_y, move_x, move_y, pos):
  '''
    A recursive utility function to solve Knight Tour
    problem
  '''

  if(pos == n**2):
    return True

  # Try all next moves from the current coordinate x, y
  for i in range(8):
    new_x = curr_x + move_x[i]
    new_y = curr_y + move_y[i]
    if(isSafe(new_x, new_y, board)):
      board[new_x][new_y] = pos
      if(solveKTUtil(n, board, new_x, new_y, move_x, move_y, pos+1)):
        return True

      # Backtracking
      board[new_x][new_y] = -1
  return False

solveKT(n)
```

## [Tug of War](https://www.geeksforgeeks.org/tug-of-war/)

```python
# function that tries every possible solution by calling itself recursively
def TOWUtil(arr, n, curr_elements, no_of_selected_elements,
      soln, min_diff, Sum, curr_sum, curr_position):
  
  # checks whether the it is going out of bound
  if (curr_position == n):
    return

  # checks that the numbers of elements left are not less than the number of elements required to form the solution
  if ((int(n / 2) - no_of_selected_elements) >(n - curr_position)):
    return

  # consider the cases when current element is not included in the solution
  TOWUtil(arr, n, curr_elements, no_of_selected_elements, soln, min_diff, Sum, curr_sum, curr_position + 1)

  # add the current element to the solution
  no_of_selected_elements += 1
  curr_sum = curr_sum + arr[curr_position]
  curr_elements[curr_position] = True

  # checks if a solution is formed
  if (no_of_selected_elements == int(n / 2)):
    
    # checks if the solution formed is better than the best solution so far
    if (abs(int(Sum / 2) - curr_sum) < min_diff[0]):
      min_diff[0] = abs(int(Sum / 2) - curr_sum)
      for i in range(n):
        soln[i] = curr_elements[i]
  else:
    
    # consider the cases where current element is included in the solution
    TOWUtil(arr, n, curr_elements, no_of_selected_elements, soln, min_diff, Sum, curr_sum, curr_position + 1)

  # removes current element before returning
  # to the caller of this function
  curr_elements[curr_position] = False

# main function that generate an arr
def tugOfWar(arr, n):
  
  # the boolean array that contains the inclusion and exclusion of an element
  # in current set. The number excluded automatically form the other set
  curr_elements = [None] * n

  # The inclusion/exclusion array for final solution
  soln = [None] * n

  min_diff = [999999999999]
  Sum = 0
  
  for i in range(n):
    Sum += arr[i]
    curr_elements[i] = soln[i] = False

  # Find the solution using recursive function TOWUtil()
  TOWUtil(arr, n, curr_elements, 0, soln, min_diff, Sum, 0, 0)

  # Print the solution
  print("The first subset is: ")
  for i in range(n):
    if (soln[i] == True):
      print(arr[i], end = " ")
  print()
  print("The second subset is: ")
  for i in range(n):
    if (soln[i] == False):
      print(arr[i], end = " ")


arr = [23, 45, -34, 12, 0, 98, -99, 4, 189, -1, 4]
n = len(arr)
tugOfWar(arr, n)

```

## [Find shortest safe route in a path with landmines](https://www.geeksforgeeks.org/find-shortest-safe-route-in-a-path-with-landmines/)

```python
# Python3 program to find shortest safe Route
# in the matrix with landmines
import sys

R = 12
C = 10

# These arrays are used to get row and column
# numbers of 4 neighbours of a given cell
rowNum = [ -1, 0, 0, 1 ]
colNum = [ 0, -1, 1, 0 ]

min_dist = sys.maxsize

# A function to check if a given cell (x, y)
# can be visited or not
def isSafe(mat, visited, x, y):

  if (mat[x][y] == 0 or visited[x][y]):
    return False

  return True

# A function to check if a given cell (x, y) is
# a valid cell or not
def isValid(x, y):

  if (x < R and y < C and x >= 0 and y >= 0):
    return True

  return False

# A function to mark all adjacent cells of
# landmines as unsafe. Landmines are shown with
# number 0
def markUnsafeCells(mat):

  for i in range(R):
    for j in range(C):
      # If a landmines is found
      if (mat[i][j] == 0):
        # Mark all adjacent cells
        for k in range(4):
          if (isValid(i + rowNum[k], j + colNum[k])):
            mat[i + rowNum[k]][j + colNum[k]] = -1

  # Mark all found adjacent cells as unsafe
  for i in range(R):
    for j in range(C):
      if (mat[i][j] == -1):
        mat[i][j] = 0

  print(mat)
"""
      for i in range(R):
          for j in range(C):
              print(mat[i][j], end='')
          print()
"""
    
# Function to find shortest safe Route in the matrix with landmines
# mat[][] - binary input matrix with safe cells marked as 1
# visited[][] - store info about cells already visited in current route
# (i, j) are coordinates of the current cell
# min_dist --> stores minimum cost of shortest path so far
# dist --> stores current path cost

def findShortestPathUtil(mat, visited, i, j, dist):
  global min_dist

  # If destination is reached
  if (j == C - 1):
    # Update shortest path found so far
    min_dist = min(dist, min_dist)
    return

  # If current path cost exceeds minimum so far
  if (dist > min_dist):
    return

  # include (i, j) in current path
  visited[i][j] = True

  # Recurse for all safe adjacent neighbours
  for k in range(4):
    if (isValid(i + rowNum[k], j + colNum[k]) and isSafe(mat, visited, i + rowNum[k], j + colNum[k])):
      findShortestPathUtil(mat, visited, i + rowNum[k], j + colNum[k], dist + 1)

  # Backtrack
  visited[i][j] = False

# A wrapper function over findshortestPathUtil()
def findShortestPath(mat):
  
  global min_dist

  # Stores minimum cost of shortest path so far
  min_dist = sys.maxsize

  # Create a boolean matrix to store info about
  # cells already visited in current route
  visited = [[False for i in range(C)] for j in range(R)]

  # Mark adjacent cells of landmines as unsafe
  markUnsafeCells(mat)

  # Start from first column and take minimum
  for i in range(R):
    # If path is safe from current cell
    if (mat[i][0] == 1):
      # Find shortest route from (i, 0) to any
      # cell of last column (x, C - 1) where
      # 0 <= x < R
      findShortestPathUtil(mat, visited, i, 0, 0)

      # If min distance is already found
      if (min_dist == C - 1):
        break

  # If destination can be reached
  if (min_dist != sys.maxsize):
    print("Length of shortest safe route is", min_dist)
  else:
    # If the destination is not reachable
    print("Destination not reachable from given source")
    
mat = [
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 1, 0, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 1, 1, 1, 0, 1, 1, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 1, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 0, 1, 1, 1, 1 ],
    [ 1, 0, 1, 1, 1, 1, 1, 1, 0, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 0, 1, 1, 1, 1, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 1, 1, 1, 0, 1, 1, 1, 1, 1, 1 ] ]

# Find shortest path
findShortestPath(mat)
```

## [Combinational Sum](https://practice.geeksforgeeks.org/problems/combination-sum/0)

```python
"""Find all combinations that sum to a given value.
Input : arr[] = 2, 4, 6, 8 
            x = 8
Output : [2, 2, 2, 2]
         [2, 2, 4]
         [2, 6]
         [4, 4]
         [8]
"""
def combinationSum(arr, sum):
  ans = []
  temp = []

  # first do hashing nothing but set{} since set does not always sort removing the duplicates 
  # using Set and Sorting the List
  arr = sorted(list(set(arr)))
  findNumbers(ans, arr, temp, sum, 0)
  return ans

def findNumbers(ans, arr, temp, sum, index):
  
  if(sum == 0):
    
    # Adding deep copy of list to ans
    ans.append(list(temp))
    return
  
  # Iterate from index to len(arr) - 1
  for i in range(index, len(arr)):

    # checking that sum does not become negative
    if(sum - arr[i]) >= 0:

      # adding element which can contribute to
      # sum
      temp.append(arr[i])
      findNumbers(ans, arr, temp, sum-arr[i], i)

      # removing element from list (backtracking)
      temp.remove(arr[i])


arr = [2, 4, 6, 8]
sum = 8
ans = combinationSum(arr, sum)

# If result is empty, then
if len(ans) <= 0:
  print("empty")
  
# print all combinations stored in ans
for i in range(len(ans)):

  print("(", end=' ')
  for j in range(len(ans[i])):
    print(str(ans[i][j])+" ", end=' ')
  print(")", end=' ')

```

## [Find Maximum number possible by doing at-most K swaps](https://practice.geeksforgeeks.org/problems/largest-number-in-k-swaps/0)

```python
"""
Given a positive integer, find the maximum integer possible by doing at-most K swap operations on its digits.
Examples: 
Input: M = 254, K = 1
Output: 524
Swap 5 with 2 so number becomes 524
"""

# function to find maximum integer possible by doing at-most K swap operations on its digits
def findMaximumNum(string, k, maxm, ctr):
  
  # return if no swaps left
  if k == 0:
    return

  n = len(string)
  # Consider every digit after the cur position
  mx = string[ctr]

  for i in range(ctr+1,n):
    # Find maximum digit greater than at ctr among rest
    if int(string[i]) > int(mx):
      mx=string[i]
      
  # If maxm is not equal to str[ctr], decrement k  
  if(mx!=string[ctr]):
    k=k-1
  
  # search this maximum among the rest from behind first swap the last maximum digit if it occurs more then 1 time
  # example str= 1293498 and k=1 then max string is 9293418 instead of 9213498
  for i in range(ctr,n):
    # If digit equals maxm swap the digit with current digit and recurse for the rest
    if(string[i]==mx):
      # swap str[ctr] with str[j]
      string[ctr], string[i] = string[i], string[ctr]
      new_str = "".join(string)
      # If current num is more than maximum so far
      if int(new_str) > int(maxm[0]):
        maxm[0] = new_str

      # recurse of the other k - 1 swaps
      findMaximumNum(string, k , maxm, ctr+1)

      # backtrack
      string[ctr], string[i] = string[i], string[ctr]


string = "129814999"
k = 4
maxm = [string]
string = [char for char in string]
findMaximumNum(string, k, maxm, 0)
print(maxm[0])
```

## [Print all permutations of a string](https://practice.geeksforgeeks.org/problems/permutations-of-a-given-string/0)

```python
def permute(s, answer):
  if (len(s) == 0):
    print(answer, end = " ")
    return
  
  for i in range(len(s)):
    ch = s[i]
    left_substr = s[0:i]
    right_substr = s[i + 1:]
    rest = left_substr + right_substr
    permute(rest, answer + ch)

answer=""
s = "alex"
print("All possible strings are : ")
permute(s, answer)

```

## [Find if there is a path of more than k length from a source](https://www.geeksforgeeks.org/find-if-there-is-a-path-of-more-than-k-length-from-a-source/)

```python
# Program to find if there is a simple path with weight more than k
  
# This class represents a dipathted graph using adjacency list representation
class Graph:
  # Allocates memory for adjacency list
  def __init__(self, V):
    self.V = V
    self.adj = [[] for i in range(V)]
  
  # Returns true if graph has path more than k length
  def pathMoreThanK(self,src, k):
    # Create a path array with nothing included in path
    path = [False]*self.V
    
    # Add source vertex to path
    path[src] = 1
    
    return self.pathMoreThanKUtil(src, k, path)
    
  # Prints shortest paths from src to all other vertices
  def pathMoreThanKUtil(self,src, k, path):
    # If k is 0 or negative, return true
    if (k <= 0):
      return True
    
    # Get all adjacent vertices of source vertex src and recursively explore all paths from src.
    i = 0
    while i != len(self.adj[src]):
      # Get adjacent vertex and weight of edge
      v = self.adj[src][i][0]
      w = self.adj[src][i][1]
      i += 1
    
      # If vertex v is already there in path, then there is a cycle (we ignore this edge)
      if (path[v] == True):
        continue
    
      # If weight of is more than k, return true
      if (w >= k):
        return True
    
      # Else add this vertex to path
      path[v] = True
    
      # If this adjacent can provide a path longer than k, return true.
      if (self.pathMoreThanKUtil(v, k-w, path)):
        return True
    
      # Backtrack
      path[v] = False
    
    # If no adjacent could produce longer path, return false
    return False
  
  # Utility function to an edge (u, v) of weight w
  def addEdge(self,u, v, w):
    self.adj[u].append([v, w])
    self.adj[v].append([u, w])
  
  
# create the graph given in above figure
V = 9
g = Graph(V)
# making above shown graph
g.addEdge(0, 1, 4)
g.addEdge(0, 7, 8)
g.addEdge(1, 2, 8)
g.addEdge(1, 7, 11)
g.addEdge(2, 3, 7)
g.addEdge(2, 8, 2)
g.addEdge(2, 5, 4)
g.addEdge(3, 4, 9)
g.addEdge(3, 5, 14)
g.addEdge(4, 5, 10)
g.addEdge(5, 6, 2)
g.addEdge(6, 7, 1)
g.addEdge(6, 8, 6)
g.addEdge(7, 8, 7)

#calling in the function
src = 0
k = 62
print("Yes") if g.pathMoreThanK(src, k) else print("No")
k = 60
print("Yes") if g.pathMoreThanK(src, k) else print("No")

```

## [Longest Possible Route in a Matrix with Hurdles](https://www.geeksforgeeks.org/longest-possible-route-in-a-matrix-with-hurdles/)

```python
# Python program to find Longest Possible Route in a matrix with hurdles
import sys
R,C = 3,10

# A Pair to store status of a cell. found is set to True of destination is reachable and value stores
# distance of longest path
class Pair:
  def __init__(self, found, value):
    self.found = found
    self.value = value

# Function to find Longest Possible Route in the matrix with hurdles. If the destination is not reachable
# the function returns false with cost sys.maxsize. (i, j) is source cell and (x, y) is destination cell.
def findLongestPathUtil(mat, i, j, x, y, visited):

  # if (i, j) itself is destination, return True
  if (i == x and j == y):
    p = Pair( True, 0 )
    return p
  
  # if not a valid cell, return false
  if (i < 0 or i >= R or j < 0 or j >= C or mat[i][j] == 0 or visited[i][j]) :
    p = Pair( False, sys.maxsize )
    return p

  # include (i, j) in current path i.e. set visited(i, j) to True
  visited[i][j] = True

  # res stores longest path from current cell (i, j) to destination cell (x, y)
  res = -sys.maxsize -1

  # go left from current cell
  sol = findLongestPathUtil(mat, i, j - 1, x, y, visited)

  # if destination can be reached on going left from current cell, update res
  if (sol.found):
    res = max(res, sol.value)

  # go right from current cell
  sol = findLongestPathUtil(mat, i, j + 1, x, y, visited)

  # if destination can be reached on going right from current cell, update res
  if (sol.found):
    res = max(res, sol.value)

  # go up from current cell
  sol = findLongestPathUtil(mat, i - 1, j, x, y, visited)

  # if destination can be reached on going up from current cell, update res
  if (sol.found):
    res = max(res, sol.value)

  # go down from current cell
  sol = findLongestPathUtil(mat, i + 1, j, x, y, visited)

  # if destination can be reached on going down from current cell, update res
  if (sol.found):
    res = max(res, sol.value)

  # Backtrack
  visited[i][j] = False

  # if destination can be reached from current cell, return True
  if (res != -sys.maxsize -1):
    p = Pair( True, 1 + res )
    return p
  
  # if destination can't be reached from current cell, return false
  else:
    p = Pair( False, sys.maxsize )
    return p

# A wrapper function over findLongestPathUtil()
def findLongestPath(mat, i, j, x,y):

  # create a boolean matrix to store info about cells already visited in current route initialize visited to false
  visited = [[False for i in range(C)]for j in range(R)]

  # find longest route from (i, j) to (x, y) and print its maximum cost
  p = findLongestPathUtil(mat, i, j, x, y, visited)
  if (p.found):
    print("Length of longest possible route is ",str(p.value))

  # If the destination is not reachable
  else:
    print("Destination not reachable from given source")

# input matrix with hurdles shown with number 0
mat = [ [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 1, 1, 0, 1, 1, 0, 1, 1, 0, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ] ]

# find longest path with source (0, 0) and destination (1, 7)
findLongestPath(mat, 0, 0, 1, 7)
```

## [Print all possible paths from top left to bottom right of a mXn matrix](https://www.geeksforgeeks.org/print-all-possible-paths-from-top-left-to-bottom-right-of-a-mxn-matrix/)

```python
"""
The problem is to print all the possible paths from top left to bottom right of a mXn matrix with the constraints that from each cell you can either move only to right or down.

Examples : 

Input : 1 2 3
        4 5 6
Output : 1 4 5 6
         1 2 5 6
         1 2 3 6

Input : 1 2 
        3 4
Output : 1 2 4
         1 3 4
"""

def printAllPaths(M, m, n):
  mapping = {}
  if not mapping.get((m,n)):
    if m == 1 and n == 1:
      return [M[m-1][n-1]]
    else:
      res = []
      if n > 1:
        a = printAllPaths(M, m, n-1)
        for i in a:
          if not isinstance(i, list):
            i = [i]
          res.append(i+[M[m-1][n-1]])
      if m > 1:
        b =printAllPaths(M, m-1, n)
        for i in b:
          if not isinstance(i, list):
            i = [i]
          res.append(i+[M[m-1][n-1]])
    mapping[(m,n)] = res
  return mapping.get((m,n))

M = [[1, 2, 3], [4, 5, 6], [7,8,9]]
m, n = len(M), len(M[0])
res = printAllPaths(M, m, n)
for i in res:
  print(i)

```

## [Partition of a set intoK subsets with equal sum](https://practice.geeksforgeeks.org/problems/partition-array-to-k-subsets/1)

```python
"""
Input : arr = [2, 1, 4, 5, 6], K = 3
Output : Yes
we can divide above array into 3 parts with equal
sum as [[2, 4], [1, 5], [6]]

Input  : arr = [2, 1, 5, 5, 6], K = 3
Output : No
It is not possible to divide above array into 3
parts with equal sum
"""

"""
array   - given input array
subsetSum array - sum to store each subset of the array
taken   -boolean array to check whether element
is taken into sum partition or not
K     - number of partitions needed
N     - total number of element in array
curIdx   - current subsetSum index
limitIdx   - lastIdx from where array element should
be taken """

def isKPartitionPossibleRec(arr, subsetSum, taken, subset, K, N, curIdx, limitIdx):
  if subsetSum[curIdx] == subset:
    
    """ 
    current index (K - 2) represents (K - 1)
    subsets of equal sum last partition will
    already remain with sum 'subset'
    """
    if (curIdx == K - 2):
      return True
    
    # recursive call for next subsetition
    return isKPartitionPossibleRec(arr, subsetSum, taken,
                  subset, K, N, curIdx + 1 , N - 1)
  
  # start from limitIdx and include elements into current partition
  for i in range(limitIdx, -1, -1):
    
    # if already taken, continue
    if (taken[i]):
      continue
    tmp = subsetSum[curIdx] + arr[i]
    
    # if temp is less than subset, then only include the element and call recursively
    if (tmp <= subset):
      
      # mark the element and include into current partition sum
      taken[i] = True
      subsetSum[curIdx] += arr[i]
      nxt = isKPartitionPossibleRec(arr, subsetSum, taken,
                    subset, K, N, curIdx, i - 1)
                    
      # after recursive call unmark the element and remove from subsetition sum
      taken[i] = False
      subsetSum[curIdx] -= arr[i]
      if (nxt):
        return True
  return False

# Method returns True if arr can be partitioned into K subsets with equal sum
def isKPartitionPossible(arr, N, K):
  
  # If K is 1, then complete array will be our answer
  if (K == 1):
    return True
  
  # If total number of partitions are more than N, then division is not possible
  if (N < K):
    return False
    
  # if array sum is not divisible by K then we can't divide array into K partitions
  sum = 0
  for i in range(N):
    sum += arr[i]
  if (sum % K != 0):
    return False
  
  # the sum of each subset should be subset (= sum / K)
  subset = sum // K
  subsetSum = [0] * K
  taken = [0] * N
  
  # Initialize sum of each subset from 0
  for i in range(K):
    subsetSum[i] = 0
    
  # mark all elements as not taken
  for i in range(N):
    taken[i] = False
    
  # initialize first subset sum as last element of array and mark that as taken
  subsetSum[0] = arr[N - 1]
  taken[N - 1] = True
  
  # call recursive method to check K-substitution condition
  return isKPartitionPossibleRec(arr, subsetSum, taken,
                subset, K, N, 0, N - 1)
 
arr = [2, 1, 4, 5, 3, 3 ]
N = len(arr)
K = 3
if (isKPartitionPossible(arr, N, K)):
  print("Partitions into equal sum is possible.\n")
else:
  print("Partitions into equal sum is not possible.\n")
```

## [Find the K-th Permutation Sequence of first N natural numbers](https://www.geeksforgeeks.org/find-the-k-th-permutation-sequence-of-first-n-natural-numbers/)

```python
"""
Input: N = 3, K = 4 
Output: 231 
Explanation: 
The ordered list of permutation sequence from integer 1 to 3 is : 123, 132, 213, 231, 312, 321. So, the 4th permutation sequence is “231”.

Input: N = 2, K = 1 
Output: 12 
Explanation: 
For n = 2, only 2 permutations are possible 12 21. So, the 1st permutation sequence is “12”. 
"""


# Function to find the index of number at first position of kth sequence of set of size n
def findFirstNumIndex(k, n):
  if (n == 1):
    return 0, k
  n -= 1
  first_num_index = 0
  
  # n_actual_fact = n!
  n_partial_fact = n

  while (k >= n_partial_fact and n > 1):
    n_partial_fact = n_partial_fact * (n - 1)
    n -= 1

  # First position of the kth sequence will be occupied by the number present at index = k / (n-1)!
  first_num_index = k // n_partial_fact
  k = k % n_partial_fact
  return first_num_index, k

# Function to find the kth permutation of n numbers
def findKthPermutation(n, k):

  # Store final answer
  ans = ""
  s = set()

  # Insert all natural number upto n in set
  for i in range(1, n + 1):
    s.add(i)

  # Subtract 1 to get 0 based indexing
  k = k - 1

  for i in range(n):

    # Mark the first position
    itr = list(s)

    index, k = findFirstNumIndex(k, n - i)

    # itr now points to the number at index in set s
    ans += str(itr[index])

    # remove current number from the set
    itr.pop(index)
    
    s = set(itr)
    
  return ans

n = 3
k = 4
kth_perm_seq = findKthPermutation(n, k)
print(kth_perm_seq)



```

# Binary Trees

## [level order traversal AKA BFS](https://practice.geeksforgeeks.org/problems/level-order-traversal/1)

```python
class Node:
  def __init__(self, key):
    self.data = key
    self.left = None
    self.right = None
    

def printLevelOrder(root):
  # Base Case
  if root is None:
    return

  # Create an empty queue for level order traversal
  queue = []

  # Enqueue Root and initialize height
  queue.append(root)

  while(len(queue) > 0):

    # Print front of queue and remove it from queue
    print(queue[0].data)
    node = queue.pop(0)

    # Enqueue left child
    if node.left is not None:
      queue.append(node.left)

    # Enqueue right child
    if node.right is not None:
      queue.append(node.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Level Order Traversal of binary tree is -")
printLevelOrder(root)
```

## [Reverse Level Order traversal](https://practice.geeksforgeeks.org/problems/reverse-level-order-traversal/1)

```python
from collections import deque

class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def reverseLevelOrder(root):
  q = deque()
  q.append(root)
  ans = deque()
  while q:
    node = q.popleft()
    if node is None:
      continue
    
    ans.appendleft(node.data)
    
    if node.right:
      q.append(node.right)
      
    if node.left:
      q.append(node.left)
   
  return ans

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print ("Level Order traversal of binary tree is", reverseLevelOrder(root))
```

## [Height of a tree](https://practice.geeksforgeeks.org/problems/height-of-binary-tree/1)

```python
"""
Given a binary tree, find height of it. Height of empty tree is -1, height of tree with one node is 0
"""
class Node:

  # Constructor to create a new node
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

# Compute the "maxDepth" of a tree -- the number of nodes along the longest path from the root node down to the
# farthest leaf node
def maxDepth(node):
  if node is None:
    return 0 ;

  else :

    # Compute the depth of each subtree
    lDepth = maxDepth(node.left)
    rDepth = maxDepth(node.right)

    # Use the larger one
    if (lDepth > rDepth):
      return lDepth+1
    else:
      return rDepth+1


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print ("Height of tree is %d" %(maxDepth(root)))
```

## [Diameter of a tree](https://practice.geeksforgeeks.org/problems/diameter-of-binary-tree/1)

```python
class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def height(node):

  # Base Case : Tree is empty
  if node is None:
    return 0

  # If tree is not empty then height = 1 + max of left
  # height and right heights
  return 1 + max(height(node.left), height(node.right))

# Function to get the diameter of a binary tree
def diameter(root):

  # Base Case when tree is empty
  if root is None:
    return 0

  # Get the height of left and right sub-trees
  lheight = height(root.left)
  rheight = height(root.right)

  # Get the diameter of left and right sub-trees
  ldiameter = diameter(root.left)
  rdiameter = diameter(root.right)

  # Return max of the following tree:
  # 1) Diameter of left subtree
  # 2) Diameter of right subtree
  # 3) Height of left subtree + height of right subtree +1
  return max(lheight + rheight + 1, max(ldiameter, rdiameter))

"""
Constructed binary tree is
      1
    / \
    2   3
  / \
  4   5
"""
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print(diameter(root))
```

## [Mirror of a tree / Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)

```python
from collections import deque
 
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
 
 
# Function to perform preorder traversal on a given binary tree
def preorder(root):
    if root is None:
        return
    print(root.data, end=' ')
    preorder(root.left)
    preorder(root.right)
 
# Utility function to swap left subtree with right subtree
def swap(root):
    if root is None:
        return
    temp = root.left
    root.left = root.right
    root.right = temp
 
 
# Iterative function to invert a given binary tree using a queue
def invertBinaryTree(root):
    # base case: if the tree is empty
    if root is None:
        return
 
    # maintain a queue and push the root node
    q = deque()
    q.append(root)
 
    # loop till queue is empty
    while q:
 
        # dequeue front node
        curr = q.popleft()
 
        # swap the left child with the right child
        swap(curr)
 
        # enqueue left child of the popped node
        if curr.left:
            q.append(curr.left)
 
        # enqueue right child of the popped node
        if curr.right:
            q.append(curr.right)

 
''' 
Construct the following tree
          1
        /   \
       /     \
      2       3
     / \     / \
    4   5   6   7
'''

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

invertBinaryTree(root)
preorder(root)
```

## Inorder, Preorder and Postorder Tree Traversal (Recursive Method)

```python
class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
 
def preorder(root):
    if root is None:
        return
    print(root.data, end=' ')
    preorder(root.left)
    preorder(root.right)
 
def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data, end=' ')
    inorder(root.right)

def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data, end=' ')
 

''' Construct the following tree
           1
         /   \
        /     \
       2       3
      /      /   \
     /      /     \
    4      5       6
          / \
         /   \
        7     8
'''

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.left.left = Node(7)
root.right.left.right = Node(8)

print("Preorder: ",preorder(root))
print("Inorder: ",inorder(root))
print("PostOrder: ",postorder(root))
```

## [Left View of a tree](https://practice.geeksforgeeks.org/problems/left-view-of-binary-tree/1)

```python
class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
 
 
def leftView(root, level=1, last_level=0):
    # base case: empty tree
    if root is None:
        return last_level
 
    # if the current node is the first node of the current level
    if last_level < level:
 
        # print the node's data
        print(root.key, end=' ')
 
        # update the last level to the current level
        last_level = level
 
    # recur for the left and right subtree by increasing the level by 1
    last_level = leftView(root.left, level + 1, last_level)
    last_level = leftView(root.right, level + 1, last_level)
    return last_level
 
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.left.left = Node(7)
root.right.left.right = Node(8)
leftView(root)
```

## [Right View of Tree](https://practice.geeksforgeeks.org/problems/right-view-of-binary-tree/1)

```python
class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
 

def RightView(root, level=1, lastLevel=0):
    if root is None:
        return lastLevel
 
    # if the current node is the last node of the current level
    if lastLevel < level:
 
        # print the node's data
        print(root.key, end=' ')
 
        # update the last level to the current level
        lastLevel = level
 
    # recur for the right and left subtree by increasing level by 1
    lastLevel = RightView(root.right, level + 1, lastLevel)
    lastLevel = RightView(root.left, level + 1, lastLevel)
    return lastLevel
 
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.left.left = Node(7)
root.right.left.right = Node(8)
RightView(root)
```

## [Top View of a tree](https://practice.geeksforgeeks.org/problems/top-view-of-binary-tree/1)

```python
class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
 
# Recursive function to perform preorder traversal on the tree and fill the dictionary.
# Here, the node has `dist` horizontal distance from the tree's root, and the level represents the node's level.
def printTop(root, dist, level, d):
    if root is None:
        return
 
    # if the current level is less than the maximum level seen so far for the same horizontal distance, or if 
    # the horizontal distance is seen for the first time, update the dictionary
    if dist not in d or level < d[dist][1]:
        # update value and level for current distance
        d[dist] = (root.key, level)
 
    # recur for the left subtree by decreasing horizontal distance and increasing level by 1
    printTop(root.left, dist - 1, level + 1, d)
 
    # recur for the right subtree by increasing both level and horizontal distance by 1
    printTop(root.right, dist + 1, level + 1, d)
 

def printTopView(root):
 
    # create a dictionary where
    # key —> relative horizontal distance of the node from the root node, and
    # value —> pair containing the node's value and its level
    d = {}
 
    # perform preorder traversal on the tree and fill the dictionary
    printTop(root, 0, 0, d)
 
    # traverse the dictionary in sorted order of keys and print the top view
    for key in sorted(d.keys()):
        print(d.get(key)[0], end=' ')

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.left.left = Node(7)
root.right.left.right = Node(8)
printTopView(root)
```

## [Bottom View of a tree](https://practice.geeksforgeeks.org/problems/bottom-view-of-binary-tree/1)

```python
class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
 
# Recursive function to perform preorder traversal on the tree and fill the map.
# Here, the node has `dist` horizontal distance from the tree's root, and the `level` represents the node's level.
def printBottom(root, dist, level, d):
 
    # base case: empty tree
    if root is None:
        return
 
    # if the current level is more than or equal to the maximum level seen so far for the same horizontal distance 
    # or horizontal distance is seen for the first time, update the dictionary
    if dist not in d or level >= d[dist][1]:
        # update value and level for the current distance
        d[dist] = (root.key, level)
 
    # recur for the left subtree by decreasing horizontal distance and increasing level by 1
    printBottom(root.left, dist - 1, level + 1, d)
 
    # recur for the right subtree by increasing both level and horizontal distance by 1
    printBottom(root.right, dist + 1, level + 1, d)
 
 
# Function to print the bottom view of a given binary tree
def printBottomView(root):
 
    # create a dictionary where
    # key —> relative horizontal distance of the node from the root node, and
    # value —> pair containing the node's value and its level
    d = {}
 
    # perform preorder traversal on the tree and fill the dictionary
    printBottom(root, 0, 0, d)
 
    # traverse the dictionary in sorted order of their keys and print the bottom view
    for key in sorted(d.keys()):
        print(d.get(key)[0], end=' ')
        
        
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.left.left = Node(7)
root.right.left.right = Node(8)
printBottomView(root)
```

## [Zig-Zag traversal of a binary tree](https://practice.geeksforgeeks.org/problems/zigzag-tree-traversal/1)

```python
from collections import deque
 
class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
 
 
# Traverse the tree in a preorder fashion and store nodes in a dictionary corresponding to their level
def preorder(root, level, d):
    if root is None:
        return
 
    # insert the current node and its level into the dictionary
    # if the level is odd, insert at the back; otherwise, search at front
    if level % 2 == 1:
        d.setdefault(level, deque()).append(root.key)
    else:
        d.setdefault(level, deque()).appendleft(root.key)
 
    # recur for the left and right subtree by increasing the level by 1
    preorder(root.left, level + 1, d)
    preorder(root.right, level + 1, d)
 
 
# Recursive function to print spiral order traversal of a given binary tree
def SpiralOrderTraversal(root):
 
    # create an empty dictionary to store nodes between given levels
    d = {}
 
    # traverse the tree and insert its nodes into the dictionary corresponding to their level
    preorder(root, 1, d)
 
    # iterate through the dictionary and print all nodes present at every level
    for i in range(1, len(d) + 1):
        print(f'Level {i}:', list(d[i]))
 

root = Node(15)
root.left = Node(10)
root.right = Node(20)
root.left.left = Node(8)
root.left.right = Node(12)
root.right.left = Node(16)
root.right.right = Node(25)
root.left.left.left = Node(20)
root.right.right.right = Node(30)
SpiralOrderTraversal(root)
```

## [Check if a tree is balanced or not](https://practice.geeksforgeeks.org/problems/check-for-balanced-tree/1)

```python
"""
Given a binary tree, write an efficient algorithm to check if it is height-balanced or not. In a height-balanced tree, the absolute difference between the height of the left and right subtree for every node is 0 or 1.
"""
class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
 
 
# Recursive function to check if a given binary tree is height-balanced or not
def isHeightBalanced(root, isBalanced=True):
 
    # base case: tree is empty or not balanced
    if root is None or not isBalanced:
        return 0, isBalanced
 
    # get the height of the left subtree
    left_height, isBalanced = isHeightBalanced(root.left, isBalanced)
 
    # get the height of the right subtree
    right_height, isBalanced = isHeightBalanced(root.right, isBalanced)
 
    # tree is unbalanced if the absolute difference between the height of
    # its left and right subtree is more than 1
    if abs(left_height - right_height) > 1:
        isBalanced = False
 
    # return height of subtree rooted at the current node
    return max(left_height, right_height) + 1, isBalanced
 
'''
Construct the following tree
          1
        /   \
       /     \
      2       3
     / \     /
    4   5   6
'''
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
if isHeightBalanced(root)[1]:
    print('Binary tree is balanced')
else:
    print('Binary tree is not balanced')
```

## [Diagonal Traversal of a Binary tree](https://www.geeksforgeeks.org/diagonal-traversal-of-binary-tree/)

```python
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
 
 
# Recursive function to perform preorder traversal on the tree and
# fill the dictionary with diagonal elements
def printDiagonal(node, diagonal, d):
 
    # base case: empty tree
    if node is None:
        return
 
    # insert the current node into the current diagonal
    d.setdefault(diagonal, []).append(node.data)
 
    # recur for the left subtree by increasing diagonal by 1
    printDiagonal(node.left, diagonal + 1, d)
 
    # recur for the right subtree with the same diagonal
    printDiagonal(node.right, diagonal, d)
 
 
# Function to print the diagonal elements of a given binary tree
def printDiagonalElements(root):
 
    # create an empty dictionary to store the diagonal element in every slope
    d = {}
 
    # perform preorder traversal on the tree and fill the dictionary
    printDiagonal(root, 0, d)
 
    # traverse the dictionary and print diagonal elements
    for i in range(len(d)):
        print(d.get(i))
 
''' Construct the following tree
           1
         /   \
        /     \
      2        3
     /        /  \
    /        /    \
   4        5      6
           / \
         /    \
        7      8
'''
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.left.left = Node(7)
root.right.left.right = Node(8)
printDiagonalElements(root)
```

## [Boundary traversal of a Binary tree](https://practice.geeksforgeeks.org/problems/boundary-traversal-of-binary-tree/1)

```python
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
 
    def isLeaf(self):
        return self.left is None and self.right is None
 
# Recursive function to print the left boundary of the given binary tree
# in a top-down fashion, except for the leaf nodes
def printLeftBoundary(root):
    if root is None:
        return
    node = root
 
    while not node.isLeaf():
        print(node.data, end=' ')
 
        # next process, the left child of `root` if it exists; otherwise, move to the right child
        node = node.left if node.left else node.right
 
# Recursive function to print the right boundary of the given binary tree
# in a bottom-up fashion, except for the leaf nodes
def printRightBoundary(root):
    if root is None or root.isLeaf():
        return
 
    # recur for the right child of `root` if it exists; otherwise, recur for the left child
    printRightBoundary(root.right if root.right else root.left)
 
    # To ensure bottom-up order, print the value of the nodes after recursion unfolds
    print(root.data, end=' ')
 
 
# Recursive function to print the leaf nodes of the given binary tree in an inorder fashion
def printLeafNodes(root):
    if root is None:
        return
    printLeafNodes(root.left)
 
    # print only leaf nodes
    if root.isLeaf():
        print(root.data, end=' ')
 
    # recur for the right subtree
    printLeafNodes(root.right)
 
 
# Function to perform the boundary traversal on a given tree
def performBoundaryTraversal(root):
    if root is None:
        return
 
    # print the root node
    print(root.data, end=' ')
 
    # print the left boundary (except leaf nodes)
    printLeftBoundary(root.left)
 
    # print all leaf nodes
    if not root.isLeaf():
        printLeafNodes(root)
 
    # print the right boundary (except leaf nodes)
    printRightBoundary(root.right)
 
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(8)
root.left.left.right = Node(9)
root.left.right.right = Node(10)
root.right.right.left = Node(11)
root.left.left.right.left = Node(12)
root.left.left.right.right = Node(13)
root.right.right.left.left = Node(14)
performBoundaryTraversal(root)
```

## [Construct Binary Tree from String with Bracket Representation](https://www.geeksforgeeks.org/construct-binary-tree-string-bracket-representation/)

```python
class newNode:
  def __init__(self, data):
    self.data = data
    self.left = self.right = None

def preOrder(node):
    if node is None:
        return
    print(node.data, end=" ")
    preOrder(node.left)
    preOrder(node.right)

# function to return the index of close parenthesis
def findIndex(Str, si, ei):
    if (si > ei):
        return -1

    s = []
    for i in range(si, ei + 1):

        # if open parenthesis, push it
        if (Str[i] == '('):
            s.append(Str[i])

        elif (Str[i] == ')'):
            if (s[-1] == '('):
                s.pop(-1)

                # if stack is empty, this is
                # the required index
                if len(s) == 0:
                    return i
    # if not found return -1
    return -1

# function to conStruct tree from String
def treeFromString(Str, si, ei):
    # Base case
    if (si > ei):
        return None

    # new root
    root = newNode(ord(Str[si]) - ord('0'))
    index = -1

    # if next char is '(' find the
    # index of its complement ')'
    if (si + 1 <= ei and Str[si + 1] == '('):
        index = findIndex(Str, si + 1, ei)

    # if index found
    if (index != -1):

        # call for left subtree
        root.left = treeFromString(Str, si + 2, index - 1)

        # call for right subtree
        root.right = treeFromString(Str, index + 2, ei - 1)
    return root


Str = "4(2(3)(1))(6(5))"
root = treeFromString(Str, 0, len(Str) - 1)
preOrder(root)
```

## [Convert Binary tree into Doubly Linked List](https://practice.geeksforgeeks.org/problems/binary-tree-to-dll/1)

<img src="https://media.geeksforgeeks.org/wp-content/cdn-uploads/TreeToList.png" style="zoom:50%;" />

```python
class Node(object):
  def __init__(self, item):
    self.data = item
    self.left = None
    self.right = None

def BTToDLLUtil(root):
    
    """This is a utility function to convert the binary tree to doubly linked list. 
    Most of the core task is done by this function."""
    if root is None:
        return root

    # Convert left subtree and link to root
    if root.left:
        
        # Convert the left subtree
        left = BTToDLLUtil(root.left)

        # Find inorder predecessor, After this loop, left will point to the
        # inorder predecessor of root
        while left.right:
            left = left.right

        # Make root as next of predecessor
        left.right = root
        
        # Make predecessor as previous of root
        root.left = left

    # Convert the right subtree and link to root
    if root.right:
        
        # Convert the right subtree
        right = BTToDLLUtil(root.right)

        # Find inorder successor, After this loop, right will point to the inorder successor of root
        while right.left:
            right = right.left

        # Make root as previous of successor
        right.left = root
        
        # Make successor as next of root
        root.right = right

    return root

def BTToDLL(root):
    if root is None:
        return root

    # Convert to doubly linked list using BLLToDLLUtil
    root = BTToDLLUtil(root)
    
    # We need pointer to left most node which is head of the constructed Doubly Linked list
    while root.left:
        root = root.left
    return root

def print_list(head):
    if head is None:
        return
    while head:
        print(head.data, end = " ")
        head = head.right


root = Node(10)
root.left = Node(12)
root.right = Node(15)
root.left.left = Node(25)
root.left.right = Node(30)
root.right.left = Node(36)
head = BTToDLL(root)
print_list(head)
```

## [Convert Binary tree into Sum tree](https://practice.geeksforgeeks.org/problems/transform-to-sum-tree/1)

```python
# Given a Binary Tree where each node has positive and negative values. Convert this to a tree where each node contains the sum of the left and right sub trees in the original tree. The values of leaf nodes are changed to 0.

class node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

# Convert a given tree to a tree where every node contains sum of values of
# nodes in left and right subtrees in the original tree
def toSumTree(Node) :
    if Node is None:
        return 0

    # Store the old value
    old_val = Node.data

    # Recursively call for left and right subtrees and store the sum as new value of this node
    Node.data = toSumTree(Node.left) + toSumTree(Node.right)

    # Return the sum of values of nodes in left and right subtrees and old_value of this node
    return Node.data + old_val

# A utility function to print inorder traversal of a Binary Tree
def printInorder(Node):
    if Node is None:
        return
    printInorder(Node.left)
    print(Node.data, end = " ")
    printInorder(Node.right)
  
# Utility function to create a new Binary Tree node
def newNode(data) :
    temp = node(0)
    temp.data = data
    temp.left = None
    temp.right = None
    return temp

root = newNode(10)
root.left = newNode(-2)
root.right = newNode(6)
root.left.left = newNode(8)
root.left.right = newNode(-4)
root.right.left = newNode(7)
root.right.right = newNode(5)
toSumTree(root)
print("Inorder Traversal of the resultant tree is: ")
printInorder(root)
```

## [Construct Binary tree from Inorder and preorder traversal](https://practice.geeksforgeeks.org/problems/construct-tree-1/1)

```python
# A class to store a binary tree node
class Node:
    # Constructor
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
 
# Recursive function to perform inorder traversal on a given binary tree
def inorderTraversal(root):
    if root is None:
        return
    inorderTraversal(root.left)
    print(root.data, end=' ')
    inorderTraversal(root.right)
 
# Recursive function to perform postorder traversal on a given binary tree
def preorderTraversal(root):
    if root is None:
        return
    print(root.data, end=' ')
    preorderTraversal(root.left)
    preorderTraversal(root.right)
 
# Recursive function to construct a binary tree from a given inorder and preorder sequence
def construct(start, end, preorder, pIndex, d):
 
    # base case
    if start > end:
        return None, pIndex
 
    # The next element in `preorder[]` will be the root node of subtree
    # formed by sequence represented by `inorder[start, end]`
    root = Node(preorder[pIndex])
    pIndex = pIndex + 1
 
    # get the index of the root node in inorder to determine the
    # left and right subtree boundary
    index = d[root.data]
 
    # recursively construct the left subtree
    root.left, pIndex = construct(start, index - 1, preorder, pIndex, d)
 
    # recursively construct the right subtree
    root.right, pIndex = construct(index + 1, end, preorder, pIndex, d)
 
    # return current node
    return root, pIndex
 
 
# Construct a binary tree from inorder and preorder traversals.
# This function assumes that the input is valid i.e., given inorder and preorder sequence forms a binary tree
def constructTree(inorder, preorder):
 
    # create a dictionary to efficiently find the index of any element in a given inorder sequence
    d = {}
    for i, e in enumerate(inorder):
        d[e] = i
 
    # `pIndex` stores the index of the next unprocessed node in a preorder sequence;
    # start with the root node (present at 0th index)
    pIndex = 0
 
    return construct(0, len(inorder) - 1, preorder, pIndex, d)[0]
 
 
''' Construct the following tree
           1
         /   \
        /     \
       2       3
      /       / \
     /       /   \
    4       5     6
           / \
          /   \
         7     8
'''
inorder = [4, 2, 1, 7, 5, 8, 3, 6]
preorder = [1, 2, 4, 3, 5, 7, 8, 6]
root = constructTree(inorder, preorder)
print('The inorder traversal is ', end='')
inorderTraversal(root)
print('\nThe preorder traversal is ', end='')
preorderTraversal(root)
```

## [Find minimum swaps required to convert a Binary tree into BST](https://www.geeksforgeeks.org/minimum-swap-required-convert-binary-tree-binary-search-tree/)

```python
"""
The idea is to use the fact that inorder traversal of Binary Search Tree is in increasing order of their value. So, find the inorder traversal of the Binary Tree and store it in the array and try to sort the array. The minimum number of swap required to get the array sorted will be the answer.
"""
def inorder(a, n, index):
    global v

    # If index is greater or equal to vector size
    if (index >= n):
        return

    inorder(a, n, 2 * index + 1)

    # Push elements in vector
    v.append(a[index])
    inorder(a, n, 2 * index + 2)

def minSwaps():
    global v
    t = [[0, 0] for _ in range(len(v))]
    ans = -2

    for i in range(len(v)):
        t[i][0], t[i][1] = v[i], i

    t, i = sorted(t), 0

    while i < len(t):
        if (i == t[i][1]):
            i += 1
            continue
        else:
            # Swapping of elements
            t[i][0], t[t[i][1]][0] = t[t[i][1]][0], t[i][0]
            t[i][1], t[t[i][1]][1] = t[t[i][1]][1], t[i][1]

        # Second is not equal to i
        if (i == t[i][1]):
            i -= 1

        i += 1
        ans += 1
    return ans

v = []
a = [5, 6, 7, 8, 9, 10, 11]
n = len(a)
inorder(a, n, 0)
print(minSwaps())
```

## [Check if Binary tree is Sum tree or not](https://practice.geeksforgeeks.org/problems/sum-tree/1)

```python
class node:
  def __init__(self, x):
    self.data = x
    self.left = None
    self.right = None

def isLeaf(node):
  if node is None:
    return 0
  if node.left is None and node.right is None:
    return 1
  return 0

# returns data if SumTree property holds for the given tree else return -1
def isSumTree(node):
  if node is None:
    return 0
  ls = isSumTree(node.left)

  #To stop for further traversal of tree if found not sumTree
  if(ls == -1):     
    return -1

  rs = isSumTree(node.right)
  #To stop for further traversal of tree if found not sumTree
  if(rs == -1):     
    return -1

  return ls + rs + node.data if (isLeaf(node) or ls + rs == node.data) else -1

root = node(26)
root.left = node(10)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(6)
root.right.right = node(3)
if(isSumTree(root)):
  print("The given tree is a SumTree ")
else:
    print("The given tree is not a SumTree ")
```

## [Check if all leaf nodes are at same level or not](https://practice.geeksforgeeks.org/problems/leaf-at-same-level/1)

```python
class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

# Recursive function which check whether all leaves are at same level
def checkUtil(root, level):
  if root is None:
    return True
  
  # If a tree node is encountered
  if root.left is None and root.right is None:
    
    # When a leaf node is found first time
    if check.leafLevel == 0 :
      check.leafLevel = level # Set first leaf found
      return True

    # If this is not first leaf node, compare its level  with first leaf's level
    return level == check.leafLevel

  # If this is not first leaf node, compare its level with first leaf's level
  return (checkUtil(root.left, level+1)and
      checkUtil(root.right, level+1))

def check(root):
  level = 0
  check.leafLevel = 0
  return (checkUtil(root, level))

root = Node(12)
root.left = Node(5)
root.left.left = Node(3)
root.left.right = Node(9)
root.left.left.left = Node(1)
root.left.right.left = Node(2)
if(check(root)):
  print("Leaves are at same level")
else:
  print("Leaves are not at same level")
```

## [Check if a Binary Tree contains duplicate subtrees of size 2 or more [ IMP ]](https://practice.geeksforgeeks.org/problems/duplicate-subtree-in-binary-tree/1)

```python
# Helper function that allocates a new node with the given data and None left and right pointers.
class newNode:
  def __init__(self, data):
    self.data = data
    self.left = self.right = None

def inorder(node, m):
  if (not node):
    return ""

  Str = "("
  Str += inorder(node.left, m)
  Str += str(node.data)
  Str += inorder(node.right, m)
  Str += ")"

  # Subtree already present (Note that we use unordered_map instead of unordered_set because we want to print multiple duplicates only once, consider example of 4 in above subtree, it should be printed only once.
  if (Str in m and m[Str] == 1):
    print(node.data, end = " ")
  if Str in m:
    m[Str] += 1
  else:
    m[Str] = 1

  return Str

# Wrapper over inorder()
def printAllDups(root):
  m = {}
  inorder(root, m)


root = None
root = newNode(1)
root.left = newNode(2)
root.right = newNode(3)
root.left.left = newNode(4)
root.right.left = newNode(2)
root.right.left.left = newNode(4)
root.right.right = newNode(4)
printAllDups(root)
```

## [Check if 2 trees are mirror or not](https://practice.geeksforgeeks.org/problems/check-mirror-in-n-ary-tree/0)

```python
def checkMirrorTree(M, N, u1, v1, u2, v2):
  mp = {}

  # Traverse first tree nodes
  for i in range(N):
    if u1[i] in mp:
      mp[u1[i]].append(v1[i])
    else:
      mp[u1[i]] = []
  
  # Traverse second tree nodes
  for i in range(N):
    if u2[i] in mp and len(mp[u2[i]]) > 0:
      if(mp[u2[i]][-1] != v2[i]):
        return 0
      mp[u2[i]].pop()
  return 1

M, N = 7, 6
  
#Tree 1
u1 = [ 1, 1, 1, 10, 10, 10 ]
v1 = [ 10, 7, 3, 4, 5, 6 ]

#Tree 2
u2 = [ 1, 1, 1, 10, 10, 10 ]
v2 = [ 3, 7, 10, 6, 5, 4 ]

if(checkMirrorTree(M, N, u1, v1, u2, v2)):
    print("Yes")
else:
    print("No")

```

## [Sum of Nodes on the Longest path from root to leaf node](https://practice.geeksforgeeks.org/problems/sum-of-the-longest-bloodline-of-a-tree/1)

```python
"""
Input : Binary tree:
        4        
       / \       
      2   5      
     / \ / \     
    7  1 2  3    
      /
     6
Output : 13

        4        
       / \       
      2   5      
     / \ / \     
    7  1 2  3 
      /
     6

The highlighted nodes (4, 2, 1, 6) above are 
part of the longest root to leaf path having
sum = (4 + 2 + 1 + 6) = 13
"""

class getNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

# function to find the Sum of nodes on the longest path from root to leaf node
def SumOfLongRootToLeafPath(root, Sum, Len, maxLen, maxSum):
                    
    # if true, then we have traversed a root to leaf path
    if (not root):
        
        # update maximum Length and maximum Sum according to the given conditions
        if (maxLen[0] < Len):
            maxLen[0] = Len
            maxSum[0] = Sum
        elif (maxLen[0]== Len and
            maxSum[0] < Sum):
            maxSum[0] = Sum
        return

    # recur for left subtree
    SumOfLongRootToLeafPath(root.left, Sum + root.data, Len + 1, maxLen, maxSum)

    # recur for right subtree
    SumOfLongRootToLeafPath(root.right, Sum + root.data, Len + 1, maxLen, maxSum)

# utility function to find the Sum of nodes on the longest path from root to leaf node
def SumOfLongRootToLeafPathUtil(root):
    # if tree is NULL, then Sum is 0
    if (not root):
        return 0

    maxSum = [-999999999999]
    maxLen = [0]

    # finding the maximum Sum 'maxSum' for the maximum Length root to leaf path
    SumOfLongRootToLeafPath(root, 0, 0, maxLen, maxSum)
    return maxSum[0]

root = getNode(4)       
root.left = getNode(2)   
root.right = getNode(5)  
root.left.left = getNode(7)
root.left.right = getNode(1) 
root.right.left = getNode(2)
root.right.right = getNode(3) 
root.left.right.left = getNode(6)
print("Sum = ", SumOfLongRootToLeafPathUtil(root))
```

## [Check if given graph is tree or not.  [ IMP ]](https://www.geeksforgeeks.org/check-given-graph-tree/)

```python
from collections import defaultdict

class Graph():
  def __init__(self, V):
    self.V = V
    self.graph = defaultdict(list)

  def addEdge(self, v, w):
    self.graph[v].append(w)
    self.graph[w].append(v)

  # A recursive function that uses visited[] and parent to detect cycle in subgraph reachable from vertex v.
  def isCyclicUtil(self, v, visited, parent):

    # Mark current node as visited
    visited[v] = True

    # Recur for all the vertices adjacent for this vertex
    for i in self.graph[v]:
      # If an adjacent is not visited, then recur for that adjacent
      if visited[i] == False:
        if self.isCyclicUtil(i, visited, v) == True:
          return True

      # If an adjacent is visited and not parent of current vertex, then there is a cycle.
      elif i != parent:
        return True

    return False

  # Returns true if the graph is a tree, else false.
  def isTree(self):
    
    # Mark all the vertices as not visited and not part of recursion stack
    visited = [False] * self.V

    # The call to isCyclicUtil serves multiple purposes. It returns true if graph reachable from vertex 0 is cyclic. 
    # It also marks all vertices reachable from 0.
    if self.isCyclicUtil(0, visited, -1) == True:
      return False

    return all(visited[i] != False for i in range(self.V))

# Driver program to test above functions
g1 = Graph(5)
g1.addEdge(1, 0)
g1.addEdge(0, 2)
g1.addEdge(0, 3)
g1.addEdge(3, 4)
print ("Graph is a Tree" if g1.isTree() == True else "Graph is a not a Tree")

g2 = Graph(5)
g2.addEdge(1, 0)
g2.addEdge(0, 2)
g2.addEdge(2, 1)
g2.addEdge(0, 3)
g2.addEdge(3, 4)
print ("Graph is a Tree" if g2.isTree() == True else "Graph is a not a Tree")
```

## [Find Largest subtree sum in a tree](https://www.geeksforgeeks.org/find-largest-subtree-sum-tree/)

```python
# Function to create new tree node.
class newNode:
 def __init__(self, key):
  self.key = key
  self.left = self.right = None

# Helper function to find largest subtree sum recursively.
def findLargestSubtreeSumUtil(root, ans):
 if (root == None):
  return 0
 
 # Subtree sum rooted at current node.
 currSum = (root.key + findLargestSubtreeSumUtil(root.left, ans) + findLargestSubtreeSumUtil(root.right, ans))

 # Update answer if current subtree sum is greater than answer so far.
 ans[0] = max(ans[0], currSum)

 # Return current subtree sum to its parent node.
 return currSum

# Function to find largest subtree sum.
def findLargestSubtreeSum(root):
 if (root == None): 
  return 0
 ans = [float('-inf')]
 findLargestSubtreeSumUtil(root, ans)
 return ans[0]
 
# Constructed Tree
#     1
#    / \
#      /  \
#     -2   3
#     /\   /\
#    / \    / \
#      4  5  -6  2
root = newNode(1)
root.left = newNode(-2)
root.right = newNode(3)
root.left.left = newNode(4)
root.left.right = newNode(5)
root.right.left = newNode(-6)
root.right.right = newNode(2)
print(findLargestSubtreeSum(root))
```

## [Maximum Sum of nodes in Binary tree such that no two are adjacent](https://www.geeksforgeeks.org/maximum-sum-nodes-binary-tree-no-two-adjacent/)

<img src="https://media.geeksforgeeks.org/wp-content/uploads/nodeSubsetWithMaxSum.png" alt="img" style="zoom:50%;" />

```python
"""
Given a binary tree with a value associated with each node, we need to choose a subset of these nodes such that the sum of 
selected nodes is maximum under a constraint that no two chosen nodes in the subset should be directly connected, that is, 
if we have taken a node in our sum then we can’t take any of its children in consideration and vice versa. 
"""

class newNode:
 def __init__(self, key):
  self.data = key
  self.left = None
  self.right = None

def maxSumHelper(root) :
 if (root == None):
  sum = [0, 0]
  return sum
 
 sum1 = maxSumHelper(root.left)
 sum2 = maxSumHelper(root.right)
 sum = [0, 0]

 # This node is included (Left and right children are not included)
 sum[0] = sum1[1] + sum2[1] + root.data

 # This node is excluded (Either left or right child is included)
 sum[1] = (max(sum1[0], sum1[1]) + max(sum2[0], sum2[1]))
 return sum

def maxSum(root) :
 res = maxSumHelper(root)
 return max(res[0], res[1])

root = newNode(10)
root.left = newNode(1)
root.left.left = newNode(2)
root.left.left.left = newNode(1)
root.left.right = newNode(3)
root.left.right.left = newNode(4)
root.left.right.right = newNode(5)
print(maxSum(root))
```

## [Print all "K" Sum paths in a Binary tree](https://www.geeksforgeeks.org/print-k-sum-paths-binary-tree/)

```python
"""
A binary tree and a number k are given. Print every path in the tree with sum of the nodes in the path as k.
A path can start from any node and end at any node and must be downward only,
i.e. they need not be root node and leaf node; and negative numbers can also be there in the tree.
"""
def printVector(v, i):  
    for j in range(i, len(v)): 
        print(v[j], end = " ") 
    print() 
      
class newNode:  
    def __init__(self, key):  
        self.data = key 
        self.left = None
        self.right = None
  
# This function prints all paths   that have sum k  
def printKPathUtil(root, path, k):  
    if (not root) : 
        return
  
    # add current node to the path  
    path.append(root.data)  
  
    # check if there's any k sum path in the left sub-tree.  
    printKPathUtil(root.left, path, k)  
  
    # check if there's any k sum path in the right sub-tree.  
    printKPathUtil(root.right, path, k)  
  
    # check if there's any k sum path that terminates at this node  
    # Traverse the entire path as there can be negative elements too  
    f = 0
    for j in range(len(path) - 1, -1, -1):      
        f += path[j]  
  
        # If path sum is k, prthe path  
        if (f == k) : 
            printVector(path, j)  
      
    # Remove the current element from the path  
    path.pop(-1)  
  
# A wrapper over printKPathUtil()  
def printKPath(root, k): 
    path =[] 
    printKPathUtil(root, path, k)  
  
root = newNode(1)  
root.left = newNode(3)  
root.left.left = newNode(2)  
root.left.right = newNode(1)  
root.left.right.left = newNode(1)  
root.right = newNode(-1)  
root.right.left = newNode(4)  
root.right.left.left = newNode(1)  
root.right.left.right = newNode(2)  
root.right.right = newNode(5)  
root.right.right.right = newNode(2)  
k = 5
printKPath(root, k)
```

## [Find Least Common Ancestor in a Binary tree](https://practice.geeksforgeeks.org/problems/lowest-common-ancestor-in-a-binary-tree/1)

```python
class Node:
 def __init__(self, key):
  self.key = key
  self.left = None
  self.right = None
 
# This function returns pointer to LCA of two given values n1 and n2
# This function assumes that n1 and n2 are present in Binary Tree
def findLCA(root, n1, n2):
 if root is None:
  return None

 # If either n1 or n2 matches with root's key, report the presence by returning root (Note that if a key is
 # ancestor of other, then the ancestor key becomes LCA
 if root.key == n1 or root.key == n2:
  return root

 # Look for keys in left and right subtrees
 left_lca = findLCA(root.left, n1, n2)
 right_lca = findLCA(root.right, n1, n2)

 # If both of the above calls return Non-NULL, then one key is present in once subtree and other is present in other, 
 # So this node is the LCA
 if left_lca and right_lca:
  return root

 # Otherwise check if left subtree or right subtree is LCA
 return left_lca if left_lca is not None else right_lca


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print ("LCA(4,5) = ", findLCA(root, 4, 5).key)
print ("LCA(4,6) = ", findLCA(root, 4, 6).key)
print ("LCA(3,4) = ", findLCA(root, 3, 4).key)
print ("LCA(2,4) = ", findLCA(root, 2, 4).key)
```

## [Find distance between 2 nodes in a Binary tree](https://practice.geeksforgeeks.org/problems/min-distance-between-two-given-nodes-of-a-binary-tree/1)

```python
"""
A python program to find distance between n1 and n2 in binary tree
"""

class Node:
 def __init__(self, data):
  self.data = data
  self.left = self.right = None


# This function returns pointer to LCA of two given values n1 and n2.
def find_least_common_ancestor(root, n1, n2):
 if root is None:
  return root

 # If either n1 or n2 matches with root's key, report the presence by returning root
 if root.data == n1 or root.data == n2:
  return root

 # Look for keys in left and right subtrees
 left = find_least_common_ancestor(root.left, n1, n2)
 right = find_least_common_ancestor(root.right, n1, n2)

 if left and right:
  return root

 # Otherwise check if left subtree or right subtree is Least Common Ancestor
 if left:
  return left
 else:
  return right

# function to find distance of any node from root
def find_distance_from_ancestor_node(root, data):
 # case when we reach a beyond leaf node or when tree is empty
 if root is None:
  return -1

 # Node is found then return 0
 if root.data == data:
  return 0

 left = find_distance_from_ancestor_node(root.left, data)
 right = find_distance_from_ancestor_node(root.right, data)
 distance = max(left, right)
 return distance+1 if distance >= 0 else -1

# function to find distance between two nodes in a binary tree
def find_distance_between_two_nodes(root: Node, n1: int, n2: int):
 lca = find_least_common_ancestor(root, n1, n2)
 return find_distance_from_ancestor_node(lca, n1) + find_distance_from_ancestor_node(lca, n2) if lca else -1

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)
print("Dist(4,5) = ", find_distance_between_two_nodes(root, 4, 5))
print("Dist(4,6) = ", find_distance_between_two_nodes(root, 4, 6))
print("Dist(3,4) = ", find_distance_between_two_nodes(root, 3, 4))
print("Dist(2,4) = ", find_distance_between_two_nodes(root, 2, 4))
print("Dist(8,5) = ", find_distance_between_two_nodes(root, 8, 5))

```

## [Kth Ancestor of node in a Binary tree](https://www.geeksforgeeks.org/kth-ancestor-node-binary-tree-set-2/)

```python
"""
Given a binary tree in which nodes are numbered from 1 to n. Given a node and a positive integer K.
We have to print the Kth ancestor of the given node in the binary tree.
If there does not exist any such ancestor then print -1.
"""

class newNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
# recursive function to calculate Kth ancestor
def kthAncestorDFS(root, node, k):
    if (not root):
        return None
     
    if (root.data == node or
       (kthAncestorDFS(root.left, node, k)) or
       (kthAncestorDFS(root.right, node, k))):
         
        if (k[0] > 0):
            k[0] -= 1
         
        elif (k[0] == 0):
             
            # print the kth ancestor
            print("Kth ancestor is:", root.data)
             
            # return None to stop further backtracking
            return None
             
        # return current node to previous call
        return root
     

root = newNode(1)
root.left = newNode(2)
root.right = newNode(3)
root.left.left = newNode(4)
root.left.right = newNode(5)

k = [2]
node = 5

# print kth ancestor of given node
parent = kthAncestorDFS(root,node,k)
 
# check if parent is not None, it means there is no Kth ancestor of the node
if (parent):
    print("-1")
```

## [Find all Duplicate subtrees in a Binary tree [ IMP ]](https://practice.geeksforgeeks.org/problems/duplicate-subtrees/1)

```python
# Helper function that allocates a new node with the given data and None left and right pointers.
class newNode:
 def __init__(self, data):
  self.data = data
  self.left = self.right = None

def inorder(node, m):
 if (not node):
  return ""

 Str = "("
 Str += inorder(node.left, m)
 Str += str(node.data)
 Str += inorder(node.right, m)
 Str += ")"

 # Subtree already present (Note that we use unordered_map instead of unordered_set because we want to print
 # multiple duplicates only once, consider example of 4 in above subtree, it should be printed only once.
 if (Str in m and m[Str] == 1):
  print(node.data, end = " ")
 if Str in m:
  m[Str] += 1
 else:
  m[Str] = 1

 return Str

# Wrapper over inorder()
def printAllDups(root):
 m = {}
 inorder(root, m)


root = None
root = newNode(1)
root.left = newNode(2)
root.right = newNode(3)
root.left.left = newNode(4)
root.right.left = newNode(2)
root.right.left.left = newNode(4)
root.right.right = newNode(4)
printAllDups(root)
```

## [Tree Isomorphism Problem](https://practice.geeksforgeeks.org/problems/check-if-tree-is-isomorphic/1)

<img src="https://media.geeksforgeeks.org/wp-content/cdn-uploads/ISomorphicTrees-e1368593305854.png" style="zoom: 80%;" />

```python
"""
Write a function to detect if two trees are isomorphic. Two trees are called isomorphic if one of them can be obtained from 
other by a series of flips, i.e. by swapping left and right children of a number of nodes.
Any number of nodes at any level can have their children swapped. Two empty trees are isomorphic.
"""

class Node:
 def __init__(self, data):
  self.data = data
  self.left = None
  self.right = None
 
# Check if the binary tree is isomorphic or not
def isIsomorphic(n1, n2):
 
 # Both roots are None, trees isomorphic by definition
 if n1 is None and n2 is None:
  return True

 # Exactly one of the n1 and n2 is None, trees are not isomorphic
 if n1 is None or n2 is None:
  return False

 if n1.data != n2.data :
  return False
  
 # There are two possible cases for n1 and n2 to be isomorphic
 
 # Case 1: The subtrees rooted at these nodes have NOT been "Flipped". 
     # Both of these subtrees have to be isomorphic, hence the &&
 # Case 2: The subtrees rooted at these nodes have been "Flipped"
 
 return ((isIsomorphic(n1.left, n2.left)and
   isIsomorphic(n1.right, n2.right)) or
   (isIsomorphic(n1.left, n2.right) and
   isIsomorphic(n1.right, n2.left))
   )

n1 = Node(1)
n1.left = Node(2)
n1.right = Node(3)
n1.left.left = Node(4)
n1.left.right = Node(5)
n1.right.left = Node(6)
n1.left.right.left = Node(7)
n1.left.right.right = Node(8)

n2 = Node(1)
n2.left = Node(3)
n2.right = Node(2)
n2.right.left = Node(4)
n2.right.right = Node(5)
n2.left.right = Node(6)
n2.right.right.left = Node(8)
n2.right.right.right = Node(7)

print ("Yes" if (isIsomorphic(n1, n2) == True) else "No")

```

# Bit Manipulation

## [Count set bits in an integer](https://practice.geeksforgeeks.org/problems/set-bits0143/1)

```python
def countSetBits(n):
    if (n == 0):
        return 0
    else:
        return 1 + countSetBits(n & (n - 1))
             
n = 9
print(countSetBits(n))
```

## [Find the two non-repeating elements in an array of repeating elements](https://practice.geeksforgeeks.org/problems/finding-the-numbers0215/1)

```python
def get2NonRepeatingNos(arr, n):
    s = set()
    for i in range(n):
     
        # Iterate through the array and check if each element is present or not in the set. If the
        # element is present, remove it from the array otherwise add it to the set
 
        if (arr[i] in s):
            s.remove(arr[i])
        else:
            s.add(arr[i])
    print("The 2 non repeating numbers are :",end=" ")
    for it in s:
        print(it,end=" ")
    print()

arr = [2, 3, 7, 9, 11, 2, 3, 11]
n = len(arr)
get2NonRepeatingNos(arr, n)
```

## [Count number of bits to be flipped to convert A to B](https://practice.geeksforgeeks.org/problems/bit-difference/0)

```python
def countSetBits( n ):
    count = 0
    while n:
        count += 1
        n &= (n-1)
    return count
     
def FlippedCount(a , b):
    return countSetBits(a^b)

a = 10
b = 20
print(FlippedCount(a, b))
```

## [Count total set bits in all numbers from 1 to n](https://practice.geeksforgeeks.org/problems/count-total-set-bits/0)

```python
# Function to return the sum of the count of set bits in the integers from 1 to n
def countSetBits(n) :
  # Ignore 0 as all the bits are unset
  n += 1;
  # To store the powers of 2
  powerOf2 = 2;

  # To store the result, it is initialized with n/2 because the count of set
  # least significant bits in the integers from 1 to n is n/2
  cnt = n // 2;

  # Loop for every bit required to represent n
  while (powerOf2 <= n) :

    # Total count of pairs of 0s and 1s
    totalPairs = n // powerOf2;

    # totalPairs/2 gives the complete count of the pairs of 1s Multiplying it with the current power of 2 will 
    # give the count of 1s in the current bit
    cnt += (totalPairs // 2) * powerOf2;

    # If the count of pairs was odd then add the remaining 1s which could not be groupped together
    if (totalPairs & 1) :
      cnt += (n % powerOf2)
    else :
      cnt += 0

    # Next power of 2
    powerOf2 <<= 1;
    
  return cnt;

n = 14;
print(countSetBits(n));

```

## [Program to find whether a no is power of two](https://practice.geeksforgeeks.org/problems/power-of-2/0)

```python
def isPowerOfTwo (x):
    # First x in the below expression is for the case when x is 0
    return (x and (not(x & (x - 1))) )
 
print('Yes') if(isPowerOfTwo(31)) else print('No')
print('Yes') if(isPowerOfTwo(64)) else print('No')
```

## [Find position of the only set bit](https://practice.geeksforgeeks.org/problems/find-position-of-set-bit3706/1)

```python
def isPowerOfTwo(n) :
    return (n and ( not (n & (n-1))))
 
# Returns position of the only set bit in 'n'
def findPosition(n) :
    if not isPowerOfTwo(n) :
        return "Invalid Number (has more than one set digits)"
 
    count = 0
 
    # One by one move the only set bit to right till it reaches end
    while (n) :
        n = n >> 1
        # increment count of shifts
        count += 1

    return count
 
n = 0
print(findPosition(n))
n = 12
print(findPosition(n))
n = 128
print(findPosition(n))

```

## [Copy set bits in a range](https://www.geeksforgeeks.org/copy-set-bits-in-a-range/)

```python
"""
Given two numbers x and y, and a range [l, r] where 1 <= l, r <= 32. The task is consider set bits of y in range [l, r] and set these bits in x also.
Examples : 

Input  : x = 10, y = 13, l = 2, r = 3
Output : x = 14
Binary representation of 10 is 1010 and 
that of y is 1101. There is one set bit
in y at 3'rd position (in given range). 
After we copy this bit to x, x becomes 1110
which is binary representation of 14.

Input  : x = 8, y = 7, l = 1, r = 2
Output : x = 11
"""
def copySetBits(x, y, l, r):
   
    # l and r must be between 1 to 3 (assuming ints are stored using 32 bits)
    if (l < 1 or r > 32):
        return x;
 
    # Traverse in given range
    for i in range(l, r + 1):
       
        # Find a mask (A number whose only set bit is at i'th position)
        mask = 1 << (i - 1);
 
        # If i'th bit is set in y, set i'th bit in x also.
        if ((y & mask) != 0):
            x = x | mask;
    return x;
 

x = 10;
y = 13;
l = 1;
r = 32;
x = copySetBits(x, y, l, r);
print("Modified x is ", x);
```

## [Divide two integers without using multiplication, division and mod operator](https://www.geeksforgeeks.org/divide-two-integers-without-using-multiplication-division-mod-operator/)

```python
def divide(dividend, divisor):
 
    # Calculate sign of divisor i.e., sign will be negative only if
    # either one of them is negative otherwise it will be positive
    sign = -1 if ((dividend < 0) ^ (divisor < 0)) else 1
 
    # Update both divisor and dividend positive
    dividend = abs(dividend)
    divisor = abs(divisor)
 
    # Initialize the quotient
    quotient = 0
    while (dividend >= divisor):
        dividend -= divisor
        quotient += 1
 
    # if the sign value computed earlier is -1 then negate the value of quotient
    if sign == -1:
        quotient = -quotient
    return quotient
 
a = 10
b = 3
print(divide(a, b))
a = 43
b = -8
print(divide(a, b))
```

## [Calculate square of a number without using *, / and pow()](https://www.geeksforgeeks.org/calculate-square-of-a-number-without-using-and-pow/)

```python
def square(n):
    # handle negative input
    if (n < 0):
        n = -n
 
    # Initialize result
    res = n
 
    # Add n to res n-1 times
    for i in range(1, n):
        res += n
    return res

for n in range(1, 6):
    print("n =", n, end=", ")
    print("n^2 =", square(n))
```

## [Power Set](https://practice.geeksforgeeks.org/problems/power-set4302/1)

```python
#Python program to find powerset
from itertools import combinations
def print_powerset(string):
 for i in range(0,len(string)+1):
  for element in combinations(string,i):
   print(''.join(element))
string=['a','b','c']
print_powerset(string)
```

# Binary Search Trees

## [Find a value in a BST](https://practice.geeksforgeeks.org/problems/search-a-node-in-bst/1/)

```python
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
 
 
# Recursive function to insert a key into a BST
def insert(root, key):
 
    # if the root is None, create a new node and return it
    if root is None:
        return Node(key)
 
    # if the given key is less than the root node, recur for the left subtree
    if key < root.data:
        root.left = insert(root.left, key)
 
    # if the given key is more than the root node, recur for the right subtree
    else:
        root.right = insert(root.right, key)
 
    return root
 
 
# Recursive function to search in a given BST
def search(root, key, parent):
 
    # if the key is not present in the key
    if root is None:
        print('Key not found')
        return
 
    # if the key is found
    if root.data == key:
 
        if parent is None:
            print(f'The node with key {key} is root node')
        elif key < parent.data:
            print('The given key is the left node of the node with key', parent.data)
        else:
            print('The given key is the right node of the node with key', parent.data)
 
        return
 
    # if the given key is less than the root node, recur for the left subtree;
    # otherwise, recur for the right subtree
    if key < root.data:
        search(root.left, key, root)
    else:
        search(root.right, key, root)

 
keys = [15, 10, 20, 8, 12, 16, 25]
root = None
for key in keys:
    root = insert(root, key)
search(root, 25, None)
```

## [Deletion of a node in a BST](https://leetcode.com/problems/delete-node-in-a-bst/)

```python
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
 
 
# Function to perform inorder traversal on the BST
def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data, end=' ')
    inorder(root.right)
 
 
# Function to find the maximum value node in the subtree rooted at `ptr`
def findMaximumKey(ptr):
    while ptr.right:
        ptr = ptr.right
    return ptr
 
 
# Recursive function to insert a key into a BST
def insert(root, key):
    if root is None:
        return Node(key)
 
    # if the given key is less than the root node, recur for the left subtree
    if key < root.data:
        root.left = insert(root.left, key)
 
    # if the given key is more than the root node, recur for the right subtree
    else:
        root.right = insert(root.right, key)
 
    return root
 
 
# Function to delete a node from a BST
def deleteNode(root, key):
    if root is None:
        return root
 
    # if the given key is less than the root node, recur for the left subtree
    if key < root.data:
        root.left = deleteNode(root.left, key)
 
    # if the given key is more than the root node, recur for the right subtree
    elif key > root.data:
        root.right = deleteNode(root.right, key)
 
    # key found
    else:
        # Case 1: node to be deleted has no children (it is a leaf node)
        if root.left is None and root.right is None:
            # update root to None
            return None
 
        # Case 2: node to be deleted has two children
        elif root.left and root.right:
            # find its inorder predecessor node
            predecessor = findMaximumKey(root.left)
 
            # copy value of the predecessor to the current node
            root.data = predecessor.data
 
            # recursively delete the predecessor. Note that the
            # predecessor will have at most one child (left child)
            root.left = deleteNode(root.left, predecessor.data)
 
        # Case 3: node to be deleted has only one child
        else:
            # choose a child node
            child = root.left if root.left else root.right
            root = child
 
    return root
 
 
keys = [15, 10, 20, 8, 12, 25]
root = None
for key in keys:
    root = insert(root, key)
root = deleteNode(root, 12)
inorder(root)
```

## [Find min and max value in a BST](https://practice.geeksforgeeks.org/problems/minimum-element-in-bst/1)

```python
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
 
# Function to perform inorder traversal on the BST
def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data, end=' ')
    inorder(root.right)
 
# Function to find the maximum value node in the subtree rooted at `ptr`
def findMaximumKey(ptr):
    while ptr.right:
        ptr = ptr.right
    return ptr.data
    
# Function to find the maximum value node in the subtree rooted at `ptr`
def findMinimumKey(ptr):
    while ptr.left:
        ptr = ptr.left
    return ptr.data
 
 
# Recursive function to insert a key into a BST
def insert(root, key):
    if root is None:
        return Node(key)
 
    # if the given key is less than the root node, recur for the left subtree
    if key < root.data:
        root.left = insert(root.left, key)
 
    # if the given key is more than the root node, recur for the right subtree
    else:
        root.right = insert(root.right, key)
    return root
 

keys = [15, 10, 20, 8, 12, 25]
root = None
for key in keys:
    root = insert(root, key)
inorder(root)
print()
print("Minimum: ",findMinimumKey(root))
print("Maximum: ",findMaximumKey(root)) 
```

## [Find inorder successor and inorder predecessor in a BST](https://practice.geeksforgeeks.org/problems/predecessor-and-successor/1)

```python
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
 
def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key) 
    return root

def findMinimum(root):
    while root.left:
        root = root.left
    return root

def findMaximum(root):
    while root.right:
        root = root.right
    return root
 
def findSuccessor(root, succ, key):
    if root is None:
        return succ
 
    # if a node with the desired value is found, the successor is the minimum value
    # node in its right subtree (if any)
    if root.data == key:
        if root.right:
            return findMinimum(root.right)
 
    # if the given key is less than the root node, recur for the left subtree
    elif key < root.data:
 
        # update successor to the current node before recursing in the left subtree
        succ = root
        return findSuccessor(root.left, succ, key)
 
    # if the given key is more than the root node, recur for the right subtree
    else:
        return findSuccessor(root.right, succ, key) 
    return succ
 
def findPredecessor(root, prec, key):
    if root is None:
        return prec
 
    # if a node with the desired value is found, the predecessor is the maximum value
    # node in its left subtree (if any)
    if root.data == key:
        if root.left:
            return findMaximum(root.left)
 
    # if the given key is less than the root node, recur for the left subtree
    elif key < root.data:
        return findPredecessor(root.left, prec, key)
 
    # if the given key is more than the root node, recur for the right subtree
    else:
        # update predecessor to the current node before recursing in the right subtree
        prec = root
        return findPredecessor(root.right, prec, key)
 
    return prec
 
keys = [15, 10, 20, 8, 12, 16, 25]
''' Construct the following BST
           15
         /    \
        /      \
       10       20
      / \      /  \
     /   \    /    \
    8    12  16    25
'''
root = None
for key in keys:
    root = insert(root, key)

print("SUCCESSOR")
# find inorder successor for each key
for key in keys:
    succ = findSuccessor(root, None, key)
    if succ:
        print(f'The successor of node {key} is {succ.data}')
    else:
        print(f'No Successor exists for node {key}')


print("PREDECESSOR")
# find inorder predecessor for each key
for key in keys:
    prec = findPredecessor(root, None, key)
    if prec:
        print(f'Predecessor of node {key} is {prec.data}')
    else:
        print('The predecessor doesn\'t exist for node', key)
```

## [Check if a tree is a BST or not](https://practice.geeksforgeeks.org/problems/check-for-bst/1)

```python
import sys
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
 
 
def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key) 
    return root
 
 
# Function to perform inorder traversal on the given binary tree and
# check if it is a BST or not. Here, `prev` is the previously processed node
def isBST(root, prev):
 
    # base case: empty tree is a BST
    if root is None:
        return True
 
    # check if the left subtree is BST or not
    left = isBST(root.left, prev)
 
    # value of the current node should be more than that of the previous node
    if root.data <= prev.data:
        return False
 
    # update previous node data and check if the right subtree is BST or not
    prev.data = root.data
    return left and isBST(root.right, prev)
 
 
# Function to determine whether a given binary tree is a BST
def checkForBST(node):
 
    # pointer to store previously processed node in the inorder traversal
    prev = Node(-sys.maxsize)
 
    # check if nodes are processed in sorted order
    if isBST(node, prev):
        print('The tree is a BST!')
    else:
        print('The tree is not a BST!')
 
def swap(root): 
    left = root.left
    root.left = root.right
    root.right = left

 
# keys = [15, 10, 20, 8, 12, 16, 25]
keys=[8,3,1,6,7,10,14,4]
root = None
for key in keys:
    root = insert(root, key)
# swap nodes
swap(root)
checkForBST(root)
```

## [Populate Inorder successor of all nodes](https://practice.geeksforgeeks.org/problems/populate-inorder-successor-for-all-nodes/1)

```python
class Node:
    def __init__(self, data, left=None, right=None, next=None):
        self.data = data
        self.left = left
        self.right = right
        self.next = next
 
# Function to set the next pointer of all nodes in a binary tree.
# curr —> current node
# prev —> previously processed node
def setNextNode(curr, prev=None):
    if curr is None:
        return prev
 
    # recur for the left subtree
    prev = setNextNode(curr.left, prev)
 
    # set the previous node's next pointer to the current node
    if prev:
        prev.next = curr
 
    # update the previous node to the current node
    prev = curr
 
    # recur for the right subtree
    return setNextNode(curr.right, prev)
 
 
# Function to print inorder successor of all nodes of binary tree using the next pointer
def printInorderSuccessors(root):
 
    # go to the leftmost node
    curr = root
    while curr.left:
        curr = curr.left
 
    # print inorder successor of all nodes
    while curr.next:
        print(f'The inorder successor of {curr.data} is {curr.next.data}')
        curr = curr.next
 

''' Construct the following tree
          1
        /   \
       /     \
      2       3
     /      /  \
    /      /    \
   4      5      6
         / \
        /   \
       7     8
'''
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.left.left = Node(7)
root.right.left.right = Node(8)
setNextNode(root)
printInorderSuccessors(root)
```

## [Find LCA  of 2 nodes in a BST](https://practice.geeksforgeeks.org/problems/lowest-common-ancestor-in-a-bst/1)

```python
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
 

def insert(root, key):
    if root is None:
        return Node(key)
 
    # if the given key is less than the root node, recur for the left subtree
    if key < root.data:
        root.left = insert(root.left, key)
 
    # if the given key is more than the root node, recur for the right subtree
    else:
        root.right = insert(root.right, key)
 
    return root
 
 
# Iterative function to search a given node in a BST
def search(root, key):
 
    # traverse the tree and search for the key
    while root:
 
        # if the given key is less than the current node, go to the left
        # subtree; otherwise, go to the right subtree
 
        if key.data < root.data:
            root = root.left
        elif key.data > root.data:
            root = root.right
        # if the key is found, return true
        elif key == root:
            return True
        else:
            return False
 
    # we reach here if the key is not present in the BST
    return False
 
 
# Recursive function to find the lowest common ancestor of given nodes
# `x` and `y`, where both `x` and `y` are present in a BST
def LCARecursive(root, x, y):
    if root is None:
        return None
 
    # if both `x` and `y` is smaller than the root, LCA exists in the left subtree
    if root.data > max(x.data, y.data):
        return LCARecursive(root.left, x, y)
 
    # if both `x` and `y` are greater than the root, LCA exists in the right subtree
    elif root.data < min(x.data, y.data):
        return LCARecursive(root.right, x, y)
 
    # if one key is greater (or equal) than the root and one key is smaller
    # (or equal) than the root, then the current node is LCA
    return root
 
 
# Print lowest common ancestor of two nodes in a BST
def LCA(root, x, y):
 
    # return if the tree is empty, or `x` or `y` is not present in the tree
    if not root or not search(root, x) or not search(root, y):
        return
 
    # `lca` stores the lowest common ancestor of `x` and `y`
    lca = LCARecursive(root, x, y)
 
    # if the lowest common ancestor exists, print it
    if lca:
        print('LCA is', lca.data)
    else:
        print('LCA does not exist')
 
keys = [15, 10, 20, 8, 12, 16, 25]
''' Construct the following tree
         15
        /  \
       /    \
      10     20
     / \     / \
    /   \   /   \
   8    12 16   25
'''
root = None
for key in keys:
    root = insert(root, key)
LCA(root, root.left.left, root.left.right)
```

## [Construct BST from preorder traversal](https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/)

```python
import sys

class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

def inorder(root): 
    if root is None:
        return
    inorder(root.left)
    print(root.key, end=' ')
    inorder(root.right)
 
# Recursive function to build a BST from a preorder sequence.
# start from the root node (the first element in a preorder sequence)
# set the root node's range as [-INFINITY, INFINITY]
def buildBST(preorder, pIndex=0, min=-sys.maxsize, max=sys.maxsize):
 
    # Base case
    if pIndex == len(preorder):
        return None, pIndex
 
    # Return if the next element of preorder traversal is not in the valid range
    val = preorder[pIndex]
    if val < min or val > max:
        return None, pIndex
 
    # Construct the root node and increment `pIndex`
    root = Node(val)
    pIndex = pIndex + 1
 
    # Since all elements in the left subtree of a BST must be less
    # than the root node's value, set range as `[min, val-1]` and recur
    root.left, pIndex = buildBST(preorder, pIndex, min, val - 1)
 
    # Since all elements in the right subtree of a BST must be greater
    # than the root node's value, set range as `[val+1…max]` and recur
    root.right, pIndex = buildBST(preorder, pIndex, val + 1, max)
 
    return root, pIndex
 
 
''' Construct the following BST
          15
        /    \
       /      \
      10       20
     /  \     /  \
    /    \   /    \
   8     12 16    25
'''
preorder = [15, 10, 8, 12, 20, 16, 25]
root = buildBST(preorder)[0]
print('Inorder traversal of BST is:', end=' ')
inorder(root)
```

## [Convert Binary tree into BST](https://practice.geeksforgeeks.org/problems/binary-tree-to-bst/1)

```python
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
 
# Function to perform inorder traversal on the tree
def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data, end=' ')
    inorder(root.right)
  
# Function to traverse the binary tree and store its keys in a set
def extractKeys(root, keys):
    # base case
    if root is None:
        return
    extractKeys(root.left, keys)
    keys.append(root.data)
    extractKeys(root.right, keys)
 
 
# Function to put keys back into a set in their correct order in a BST
# by doing inorder traversal
def convertToBST(root, it):
    if root is None:
        return
    convertToBST(root.left, it)
    root.data = next(it)
    convertToBST(root.right, it)
 
 
# Function to convert a binary tree to BST by maintaining its original structure
def convert(root):
    # traverse the binary tree and store its keys in a set
    keys = []
    extractKeys(root, keys)

    # put back keys present in the set to their correct order in the BST
    it = iter(sorted(keys))
    convertToBST(root, it)
 
''' 
Construct the following tree
           8
         /   \
        /     \
       3       5
      / \     / \
     /   \   /   \
    10    2 4     6
'''
root = Node(8)
root.left = Node(3)
root.right = Node(5)
root.left.left = Node(10)
root.left.right = Node(2)
root.right.left = Node(4)
root.right.right = Node(6)
convert(root)
inorder(root)
```

## [Convert a normal BST into a Balanced BST](https://www.geeksforgeeks.org/convert-normal-bst-balanced-bst/)

```python
class Node: 
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
 
 
# Function to perform the preorder traversal on a BST
def preorder(root):
    if root is None:
        return
    print(root.data, end=' ')
    preorder(root.left)
    preorder(root.right)
 
 
# Recursive function to push nodes of a given binary search tree into a
# list in an inorder fashion
def pushTreeNodes(root, nodes):
    if root is None:
        return
 
    pushTreeNodes(root.left, nodes)
    nodes.append(root)
    pushTreeNodes(root.right, nodes)
 
 
# Recursive function to construct a height-balanced BST from
# given nodes in sorted order
def buildBalancedBST(nodes, start, end):
    if start > end:
        return None
 
    # find the middle index
    mid = (start + end) // 2
 
    # The root node will be a node present at the mid-index
    root = nodes[mid]
 
    # recursively construct left and right subtree
    root.left = buildBalancedBST(nodes, start, mid - 1)
    root.right = buildBalancedBST(nodes, mid + 1, end)
 
    # return root node
    return root
 
 
# Function to construct a height-balanced BST from an unbalanced BST
def constructBalancedBST(root):
 
    # Push nodes of a given binary search tree into a list in sorted order
    nodes = []
    pushTreeNodes(root, nodes)
 
    # Construct a height-balanced BST from sorted BST nodes
    return buildBalancedBST(nodes, 0, len(nodes) - 1)
 

root = Node(20)
root.left = Node(15)
root.left.left = Node(10)
root.left.left.left = Node(5)
root.left.left.left.left = Node(2)
root.left.left.left.right = Node(8)
root = constructBalancedBST(root)
print('Preorder traversal of the constructed BST is ', end='')
preorder(root)
```

## [Merge two BST](https://www.geeksforgeeks.org/merge-two-balanced-binary-search-trees/)

```python
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
 
# Function to push a BST node at the front of a doubly linked list
def push(root, head):
    root.right = head
    if head:
        head.left = root
    head = root
    return head
  
# Function to print and count the total number of nodes in a doubly-linked list
def size(node):
    counter = 0
    while node:
        node = node.right
        counter = counter + 1
    return counter
 
# Function to print preorder traversal of the BST
def preorder(root):
    if root is None:
        return
    print(root.data, end=' ')
    preorder(root.left)
    preorder(root.right)
 
# Recursive method to construct a balanced BST from a sorted doubly linked list
def convertSortedDLLToBalancedBST(head, n):
    if n <= 0:
        return None, head
 
    # recursively construct the left subtree
    leftSubTree, head = convertSortedDLLToBalancedBST(head, n // 2)
 
    # `head` now points to the middle node of the sorted DDL 
    # make the middle node of the sorted DDL as the root node of the BST
    root = head
 
    # update left child of the root node
    root.left = leftSubTree
 
    # update the head reference of the doubly linked list
    head = head.right
 
    # recursively construct the right subtree with the remaining nodes
    root.right, head = convertSortedDLLToBalancedBST(head, n - (n // 2 + 1))
    # +1 for the root
    # return the root node
    return root, head
 
 
# Recursive method to convert a BST into a doubly-linked list. It takes
# the BST's root node and the head node of the doubly linked list as an argument
def convertBSTtoSortedDLL(root, head=None):
    if root is None:
        return head
 
    # recursively convert the right subtree
    head = convertBSTtoSortedDLL(root.right, head)
 
    # push the current node at the front of the doubly linked list
    head = push(root, head)
 
    # recursively convert the left subtree
    head = convertBSTtoSortedDLL(root.left, head)
 
    return head
 
 
# Recursive method to merge two doubly-linked lists into a
# single doubly linked list in sorted order
def sortedMerge(first, second):
 
    # if the first list is empty, return the second list
    if first is None:
        return second
 
    # if the second list is empty, return the first list
    if second is None:
        return first
 
    # if the head node of the first list is smaller
    if first.data < second.data:
        first.right = sortedMerge(first.right, second)
        first.right.left = first
        return first
 
    # if the head node of the second list is smaller
    else:
        second.right = sortedMerge(first, second.right)
        second.right.left = second
        return second
 
 
# Function to merge two balanced BSTs into a single balanced BST
def merge(first, second):
 
    # merge both BSTs into a sorted doubly linked list
    head = sortedMerge(convertBSTtoSortedDLL(first), convertBSTtoSortedDLL(second))
 
    # construct a balanced BST from a sorted doubly linked list
    root, head = convertSortedDLLToBalancedBST(head, size(head))
    return root
 

'''
Construct the first BST
      20
     /  \
    10  30
        / \
       25 100
'''
first = Node(20)
first.left = Node(10)
first.right = Node(30)
first.right.left = Node(25)
first.right.right = Node(100)
'''
Construct the second BST
      50
     /  \
    5   70
'''
second = Node(50)
second.left = Node(5)
second.right = Node(70)
# merge both BSTs
root = merge(first, second)
preorder(root)
```

## [Find Kth largest element and Kth smallest element in a BST](https://practice.geeksforgeeks.org/problems/kth-largest-element-in-bst/1)

```python
import sys
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
 
def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
 
    return root
  
# Function to find the k'th largest node in a BST. Here, `i` denotes the total number of nodes processed so far
def kthLargest(root, i, k):
    if root is None:
        return None, i
 
    # search in the right subtree
    left, i = kthLargest(root.right, i, k)
 
    # if k'th largest is found in the left subtree, return it
    if left:
        return left, i
 
    i = i + 1
 
    # if the current node is k'th largest, return its value
    if i == k:
        return root, i
 
    # otherwise, search in the left subtree
    return kthLargest(root.left, i, k)
 
 
def findKthLargest(root, k):
    i = 0
    # traverse the tree in an inorder fashion and return k'th node
    return kthLargest(root, i, k)[0]
 

def kthSmallest(root, counter, k):
    if root is None:
        return None, counter
 
    # recur for the left subtree
    left, counter = kthSmallest(root.left, counter, k)
 
    # if k'th smallest node is found
    if left:
        return left, counter
 
    # if the root is k'th smallest node
    counter = counter + 1
    if counter == k:
        return root, counter
 
    # recur for the right subtree only if k'th smallest node is not found
    # in the right subtree
    ret, counter = kthSmallest(root.right, counter, k)
    return ret, counter
 
def findKthSmallest(root, k):
    counter = 0
    # recursively find the k'th smallest node
    return kthSmallest(root, counter, k)[0]

keys = [15, 10, 20, 8, 12, 16, 25]
root = None
for key in keys:
    root = insert(root, key)

 
k = 2
print(f"{k}th LARGEST NODE")  
result = findKthLargest(root, k)
if result != sys.maxsize:
    print(result.data)
else:
    print('Invalid Input')


k = 4
print(f"{k}th SMALLEST NODE")
result = findKthSmallest(root, k)
if result:
    print(result.data)
else:
    print(f'{k}\'th smallest node does not exist.')
```

## [Count pairs from 2 BST whose sum is equal to given value "X"](https://practice.geeksforgeeks.org/problems/brothers-from-different-root/1)

```python
class Node:
 def __init__(self,data):
  self.data = data
  self.left = None
  self.right = None

root1,root2 = None,None

# def to count pairs from two BSTs whose sum is equal to a given value x
pairCount = 0
def traverseTree(root1, root2, sum):
 if root1 is None or root2 is None:
  return
 traverseTree(root1.left, root2, sum)
 traverseTree(root1.right, root2, sum)
 diff = sum - root1.data
 findPairs(root2, diff)


def findPairs(root2 , diff):
 global pairCount
 if root2 is None:
  return

 if (diff > root2.data) :
  findPairs(root2.right, diff)
 else :
  findPairs(root2.left, diff)
 if (root2.data == diff):
  pairCount += 1

def countPairs(root1, root2, sum):
 global pairCount

 traverseTree(root1, root2, sum)
 return pairCount


root1 = Node(5) 
root1.left = Node(3)
root1.right = Node(7)
root1.left.left = Node(2)
root1.left.right = Node(4)
root1.right.left = Node(6)
root1.right.right = Node(8)

# formation of BST 2
root2 = Node(10)
root2.left = Node(6)
root2.right = Node(15)
root2.left.left = Node(3)
root2.left.right = Node(8)
root2.right.left = Node(11)
root2.right.right = Node(18)

x = 16
print(f"Pairs = {countPairs(root1, root2, x)}")
```

## [Find the median of BST in O(n) time and O(1) space](https://www.geeksforgeeks.org/find-median-bst-time-o1-space/)

```python
_MIN=float('-inf')
_MAX=float('inf')

# Helper function that allocates a new node with the given data and None left and right pointers.         
class newNode:
 def __init__(self, data):
  self.data = data
  self.left = None
  self.right = None

# A utility function to insert a new node with given key in BST 
def insert(node,key):
 if node is None:
  return newNode(key)

 # Otherwise, recur down the tree 
 if (key < node.data):
  node.left = insert(node.left, key)
 elif (key > node.data):
  node.right = insert(node.right, key)

 # return the (unchanged) node pointer 
 return node


#Function to count nodes in a binary search tree using Morris Inorder traversal
def counNodes(root):
 count = 0
 if root is None:
  return count

 current = root
 while (current != None):
  if current.left is None:
   # Count node if its left is None
   count+=1
   # Move to its right
   current = current.right

  else: 
   # Find the inorder predecessor of current 
   pre = current.left

   while pre.right not in [None, current]:
    pre = pre.right

   #Make current as right child of its inorder predecessor 
   if pre.right is None:
    pre.right = current
    current = current.left
   else:
    pre.right = None
    # Increment count if the current node is to be visited
    count += 1
    current = current.right

 return count


def findMedian(root):
 if root is None:
  return 0
 count = counNodes(root)
 currCount = 0
 current = root

 while (current != None):

  if current.left is None:

   # count current node
   currCount += 1

   # check if current node is the median
   # Odd case
   if (count % 2 != 0 and
    currCount == (count + 1)//2):
    return prev.data

   # Even case
   elif (count % 2 == 0 and
     currCount == (count//2)+1):
    return (prev.data + current.data)//2

   # Update prev for even no. of nodes
   prev = current

   #Move to the right
   current = current.right

  else:

   # Find the inorder predecessor of current 
   pre = current.left
   while pre.right not in [None, current]:
    pre = pre.right

   # Make current as right child of its inorder predecessor 
   if pre.right is None:

    pre.right = current
    current = current.left
   else:

    pre.right = None

    prev = pre

    # Count current node
    currCount+= 1

    # Check if the current node is the median
    if (count % 2 != 0 and
     currCount == (count + 1) // 2 ):
     return current.data

    elif (count%2 == 0 and
     currCount == (count // 2) + 1):
     return (prev.data+current.data)//2

    # update prev node for the case of even
    # no. of nodes
    prev = current
    current = current.right

""" 
Constructed binary tree is
 50
 / \
    30 70
    / \ / \
    20 40 60 80
"""
root = newNode(50)
insert(root, 30)
insert(root, 20)
insert(root, 40)
insert(root, 70)
insert(root, 60)
insert(root, 80)
print("Median of BST is ",findMedian(root))

```

## [Count BST nodes that lie in a given range](https://practice.geeksforgeeks.org/problems/count-bst-nodes-that-lie-in-a-given-range/1)

```python
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
 
def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root
 
def countNodes(root, low, high):
    if root is None:
        return 0
 
    # keep track of the total number of nodes in the tree rooted with `root`.
    # that lies within the current range [low, high]
    count = 0
 
    # increment count if the current node lies within the current range
    if low <= root.data <= high:
        count += 1
 
    # recur for the left subtree
    count += countNodes(root.left, low, high)
 
    # recur for the right subtree and return the total count
    return count + countNodes(root.right, low, high)
 
 
low, high = 12, 20
keys = [15, 25, 20, 22, 30, 18, 10, 8, 9, 12, 6]
root = None
for key in keys:
    root = insert(root, key)

print('The total number of nodes is', countNodes(root, low, high))
```

## [Replace every element with the least greater element on its right](https://www.geeksforgeeks.org/replace-every-element-with-the-least-greater-element-on-its-right/)

```python
""" 
Given an array of integers, replace every element with the least greater element on its right side in the array. If there are no greater elements on the right side, replace it with -1.

Examples: 
Input: [8, 58, 71, 18, 31, 32, 63, 92, 
         43, 3, 91, 93, 25, 80, 28]
Output: [18, 63, 80, 25, 32, 43, 80, 93, 
         80, 25, 93, -1, 28, -1, -1]
"""

class Node: 
 def __init__(self, d):
  self.data = d
  self.left = None
  self.right = None

# A utility function to insert a new node with given data in BST and find its successor
def insert(node, data): 
 global succ
 # If the tree is empty, return a new node
 root = node

 if node is None:
  return Node(data)

 # If key is smaller than root's key, go to left subtree and set successor as current node
 if (data < node.data):
  
  #print("1")
  succ = node
  root.left = insert(node.left, data)

 # Go to right subtree
 elif (data > node.data):
  root.right = insert(node.right, data)
  
 return root

# Function to replace every element with the least greater element on its right
def replace(arr, n):
 
 global succ
 root = None

 # Start from right to left
 for i in range(n - 1, -1, -1):
  succ = None

  # Insert current element into BST and find its inorder successor
  root = insert(root, arr[i])

  # Replace element by its inorder successor in BST
  arr[i] = succ.data if succ else -1
 return arr


 
arr = [ 8, 58, 71, 18, 31, 32, 63,
  92, 43, 3, 91, 93, 25, 80, 28 ]
n = len(arr)
succ = None
arr = replace(arr, n)
print(*arr)
```

## [Given "n" appointments, find the conflicting appointments](https://www.geeksforgeeks.org/given-n-appointments-find-conflicting-appointments/)

```python
"""
Input: appointments[] = { {1, 5} {3, 7}, {2, 6}, {10, 15}, {5, 6}, {4, 100}}
Output: Following are conflicting intervals
[3,7] Conflicts with [1,5]
[2,6] Conflicts with [1,5]
[5,6] Conflicts with [3,7]
[4,100] Conflicts with [1,5]
"""


class Interval:
 def __init__(self):
  self.low = None
  self.high = None
  
# Structure to represent a node in Interval Search Tree
class ITNode:
 def __init__(self):
  self.max = None
  self.i = None
  self.left = None
  self.right = None

def newNode(j):
 #print(j)
 temp = ITNode()
 temp.i = j
 temp.max = j[1]
 return temp

# A utility function to check if given two intervals overlap
def doOVerlap(i1, i2):
 if (i1[0] < i2[1] and i2[0] < i1[1]):
  return True
 return False

# Function to create a new node
def insert(node, data):
 global succ

 # If the tree is empty, return a new node
 root = node
 if node is None:
  return newNode(data)

 # If key is smaller than root's key, go to left subtree and set successor as current node print(node)
 if (data[0] < node.i[0]):
  root.left = insert(node.left, data)

 # Go to right subtree
 else:
  root.right = insert(node.right, data)
 if root.max < data[1]:
  root.max = data[1]

 return root

# The main function that searches a given interval i in a given Interval Tree.
def overlapSearch(root, i):
 if root is None:
  return None

 # If given interval overlaps with root
 if (doOVerlap(root.i, i)):
  return root.i

 # If left child of root is present and max of left child is greater than or
 # equal to given interval, then i may overlap with an interval is left subtree
 if (root.left != None and root.left.max >= i[0]):
  return overlapSearch(root.left, i)

 # Else interval can only overlap with right subtree
 return overlapSearch(root.right, i)

# This function prints all conflicting appointments in a given array of appointments.
def printConflicting(appt, n):
 # Create an empty Interval Search Tree, add first appointment
 root = None
 root = insert(root, appt[0])
 
 # Process rest of the intervals
 for i in range(1, n):
  # If current appointment conflicts with any of the existing intervals, print it
  res = overlapSearch(root, appt[i])
  
  if (res != None):
   print("[", appt[i][0], ",", appt[i][1],
    "] Conflicts with [", res[0],
    ",", res[1], "]")

  # Insert this appointment
  root = insert(root, appt[i])



appt = [ [ 1, 5 ], [ 3, 7 ],
  [ 2, 6 ], [ 10, 15 ],
  [ 5, 6 ], [ 4, 100 ] 
    ]
n = len(appt)
print("Following are conflicting intervals")
printConflicting(appt, n)


```

## [Preorder to Postorder](https://practice.geeksforgeeks.org/problems/preorder-to-postorder/0)

```python
#  A class to store a binary tree node
class Node:
    def __init__(self, key):
        self.key = key
 
def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.key, end=' ')
   
 
 
# Recursive function to build a BST from a preorder sequence.
def constructBST(preorder, start, end):
 
    # base case
    if start > end:
        return None
        
    # Construct the root node of the subtree formed by keys of the
    # preorder sequence in range `[start, end]`
    node = Node(preorder[start])
 
    # search the index of the first element in the current range of preorder
    # sequence larger than the root node's value
    i = start
    while i <= end:
        if preorder[i] > node.key:
            break
        i = i + 1
 
    # recursively construct the left subtree
    node.left = constructBST(preorder, start + 1, i - 1)
 
    # recursively construct the right subtree
    node.right = constructBST(preorder, i, end)
 
    # return current node
    return node
 
  
''' 
Construct the following BST
          15
        /    \
       /      \
      10       20
     /  \     /  \
    /    \   /    \
   8     12 16    25
'''

preorder = [15, 10, 8, 12, 20, 16, 25]
root = constructBST(preorder, 0, len(preorder) - 1)
print('Postorder traversal of BST is ', end='')
postorder(root)
```

## [Check whether BST contains Dead end](https://practice.geeksforgeeks.org/problems/check-whether-bst-contains-dead-end/1)

```python
"""
Given a Binary search Tree that contains positive integer values greater than 0. The task is to check whether the BST contains a dead end or not. Here Dead End means, we are not able to insert any element after that node.

Examples:  

Input :        8
             /   \ 
           5      9
         /   \
        2     7
       /
      1               
Output : Yes
Explanation : Node "1" is the dead End because after that we cant insert any element.       

Input :       8
            /   \ 
           7     10
         /      /   \
        2      9     13

Output : Yes
Explanation : We can't insert any element at node 9.  
"""

all_nodes = set()
leaf_nodes = set()

# A BST node
class newNode:

 def __init__(self, data):
 
  self.data = data
  self.left = None
  self.right = None

# A utility function to insert a new Node with given key in BST 
def insert(node, key):
 if node is None:
  return newNode(key)

 # Otherwise, recur down the tree
 if (key < node.data):
  node.left = insert(node.left,
      key)
 elif (key > node.data):
  node.right = insert(node.right,
       key)

 # return the (unchanged) Node pointer
 return node

# Function to store all node of given binary search tree
def storeNodes(root):

 global all_nodes
 global leaf_nodes
 if root is None:
  return

 # store all node of binary search tree
 all_nodes.add(root.data)

 # store leaf node in leaf_hash
 if root.left is None and root.right is None:
  leaf_nodes.add(root.data)
  return

 # recur call rest tree
 storeNodes(root. left)
 storeNodes(root.right)

# Returns true if there is a dead end in tree, else false.
def isDeadEnd(root):

 global all_nodes
 global leaf_nodes

 if root is None:
  return False

 # create two empty hash sets that store all BST elements and leaf nodes respectively.

 # insert 0 in 'all_nodes' for handle case if bst contain value 1
 all_nodes.add(0)

 # Call storeNodes function to store all BST Node
 storeNodes(root)

 return any(((x + 1) in all_nodes and (x - 1) in all_nodes) for x in leaf_nodes)

root = None
root = insert(root, 8)
root = insert(root, 5)
root = insert(root, 2)
root = insert(root, 3)
root = insert(root, 7)
root = insert(root, 11)
root = insert(root, 4)

if(isDeadEnd(root) == True):
 print("Yes")
else:
 print("No")


```

## [Largest BST in a Binary Tree [ V.V.V.V.V IMP ]](https://practice.geeksforgeeks.org/problems/largest-bst/1)

```python
import sys
sys.setrecursionlimit(1000000)
from collections import deque

IMIN = float('-inf')
IMAX = float('inf')

class newNode:
 def __init__(self, val):
  self.right = None
  self.data = val
  self.left = None

def largestBst(root):
 if root is None:
  return IMAX,IMIN,0
 if root.left is None and root.right is None:
  return root.data,root.data,1

 left=largestBst(root.left)
 right=largestBst(root.right)

 ans=[0,0,0]

 if left[1]<root.data and right[0]>root.data:
  ans[0]=min(left[0],right[0],root.data)
  ans[1]=max(right[1],left[1],root.data)
  ans[2]=1+left[2]+right[2]
  return ans

 ans[0]=IMIN
 ans[1]=IMAX
 ans[2]=max(left[2],right[2])
 return ans[2]

 
"""
 50
 / \
  75  45
 /
40 
"""
root = newNode(50)
root.left = newNode(75)
root.right = newNode(45)
root.left.left = newNode(40)
print("Size of the largest BST is",largestBst(root))
```

## [Flatten BST to sorted list](https://www.geeksforgeeks.org/flatten-bst-to-sorted-list-increasing-order/)

```python
global prev
class node :
 def __init__(self, data):
  self.data = data
  self.left = None
  self.right = None

def printTree(parent):
 root = parent
 while root is not None:
  print(root.data,end=' ')
  root = root.right

def inorder(root):
 global prev
 if root is None:
  return
 inorder(root.left)
 print(root.data,end=' ')
 inorder(root.right)


# Function to flatten binary tree using level order traversal BFS
def flatten(parent):
 global prev
    # Dummy node
 dummy = node(-1)

 # Pointer to previous element
 prev = dummy

 # Calling in-order traversal
 inorder(parent)

 prev.left = None
 prev.right = None

 # Delete dummy node
 return dummy.right

root = node(5)
root.left = node(3)
root.right = node(7)
root.left.left = node(2)
root.left.right = node(4)
root.right.left = node(6)
root.right.right = node(8)
printTree(flatten(root))
```

# Dynamic Programming

## [Coin ChangeProblem](https://practice.geeksforgeeks.org/problems/coin-change2448/1)

```python
"""
Given an unlimited supply of coins of given denominations, find the total number of distinct ways to get the desired change.

For example,

Input: S = { 1, 3, 5, 7 }, target = 8
 
The total number of ways is 6
 
{ 1, 7 }
{ 3, 5 }
{ 1, 1, 3, 3 }
{ 1, 1, 1, 5 }
{ 1, 1, 1, 1, 1, 3 }
{ 1, 1, 1, 1, 1, 1, 1, 1 }
 
 
Input: S = { 1, 2, 3 }, target = 4
 
The total number of ways is 4
 
{ 1, 3 }
{ 2, 2 }
{ 1, 1, 2 }
{ 1, 1, 1, 1 }
"""

def count(S, n, target):
    if target == 0:
        return 1
 
    # return 0 (solution does not exist) if total becomes negative, no elements are left
    if target < 0 or n < 0:
        return 0
 
    # Case 1. Include current coin `S[n]` in solution and recur
    # with remaining change `target-S[n]` with the same number of coins
    incl = count(S, n, target - S[n])
 
    # Case 2. Exclude current coin `S[n]` from solution and recur for remaining coins `n-1`
    excl = count(S, n - 1, target)
 
    # return total ways by including or excluding current coin
    return incl + excl
 

# `n` coins of given denominations
S = [1, 2, 3]
# total change required
target = 4
print('The total number of ways to get the desired change is',
    count(S, len(S) - 1, target))
 
```

## [Knapsack Problem](https://practice.geeksforgeeks.org/problems/0-1-knapsack-problem/0)

```python
"""
In the 0–1 Knapsack problem, we are given a set of items, each with a weight and a value, and we need to determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible.

Please note that the items are indivisible; we can either take an item or not (0-1 property). For example,

Input:
 
value = [ 20, 5, 10, 40, 15, 25 ]
weight = [ 1, 2, 3, 8, 7, 4 ]
int W = 10
 
Output: Knapsack value is 60
 
value = 20 + 40 = 60
weight = 1 + 8 = 9 < W
"""

import sys
 
 
# Values (stored in list `v`)
# Weights (stored in list `w`)
# Total number of distinct items `n`
# Knapsack capacity `W`
def knapsack(v, w, n, W):
    if W < 0:
        return -sys.maxsize
 
    # base case: no items left or capacity becomes 0
    if n < 0 or W == 0:
        return 0
 
    # Case 1. Include current item `n` in knapsack `v[n]` and recur for
    # remaining items `n-1` with decreased capacity `W-w[n]`
    include = v[n] + knapsack(v, w, n - 1, W - w[n])
 
    # Case 2. Exclude current item `v[n]` from the knapsack and recur for
    # remaining items `n-1`
    exclude = knapsack(v, w, n - 1, W)
 
    # return maximum value we get by including or excluding the current item
    return max(include, exclude)
 
 

# input: a set of items, each with a weight and a value
v = [20, 5, 10, 40, 15, 25]
w = [1, 2, 3, 8, 7, 4]
# knapsack capacity
W = 10
print('Knapsack value is', knapsack(v, w, len(v) - 1, W))


```

## [Binomial CoefficientProblem](https://practice.geeksforgeeks.org/problems/ncr1019/1)

```python
"""
A binomial coefficient C(n, k) also gives the number of ways, disregarding order, that k objects can be chosen from among n objects more formally, the number of k-element subsets (or k-combinations) of a n-element set.
"""

def binomialCoeff(n, k):
    C = [0 for i in range(k+1)]
    C[0] = 1  # since nC0 is 1
 
    for i in range(1, n+1):
        # Compute next row of pascal triangle using the previous row
        j = min(i, k)
        while (j > 0):
            C[j] = C[j] + C[j-1]
            j -= 1
 
    return C[k]
 

n = 5
k = 2
print ("Value of C(%d,%d) is %d" % (n, k, binomialCoeff(n, k)))
```

## [Permutation CoefficientProblem](https://www.geeksforgeeks.org/permutation-coefficient/)

```python
"""
P(10, 2) = 90
P(10, 3) = 720
P(10, 0) = 1
P(10, 1) = 10   
"""

def permutationCoeff(n, k):
    # P(n,k)=n*(n-1)*(n-2)*....(n-k-1)
    f=1
    for i in range(k): 
        f*=(n-i)     
    return f  
 
n = 10
k = 2
print("Value of P(", n, ",", k, ") is ", permutationCoeff(n, k))
```

## [Program for nth Catalan Number](https://practice.geeksforgeeks.org/problems/geek-and-his-binary-strings1951/1/)

```python
"""
Catalan numbers are a sequence of natural numbers that occurs in many interesting counting problems like the following.
1) Count the number of expressions containing n pairs of parentheses which are correctly matched. For n = 3, possible expressions are ((())), ()(()), ()()(), (())(), (()()).

2) Count the number of possible Binary Search Trees with n keys (See this) 

The first few Catalan numbers for n = 0, 1, 2, 3, … are 1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, …
"""

def catalan(n):
    return 1 if n <= 1 else sum(catalan(i) * catalan(n-i-1) for i in range(n))
 
for i in range(10):
    print(catalan(i), end=' ')
```

## [Matrix Chain Multiplication](https://practice.geeksforgeeks.org/problems/matrix-chain-multiplication0303/1/)

```python
"""
Input: p[] = {40, 20, 30, 10, 30}   
Output: 26000  
There are 4 matrices of dimensions 40x20, 20x30, 30x10 and 10x30.
Let the input 4 matrices be A, B, C and D.  The minimum number of 
multiplications are obtained by putting parenthesis in following way
(A(BC))D --> 20*30*10 + 40*20*10 + 40*10*30

Input: p[] = {10, 20, 30, 40, 30} 
Output: 30000 
There are 4 matrices of dimensions 10x20, 20x30, 30x40 and 40x30. 
Let the input 4 matrices be A, B, C and D.  The minimum number of 
multiplications are obtained by putting parenthesis in following way
((AB)C)D --> 10*20*30 + 10*30*40 + 10*40*30

Input: p[] = {10, 20, 30}  
Output: 6000  
There are only two matrices of dimensions 10x20 and 20x30. So there 
is only one way to multiply the matrices, cost of which is 10*20*30
"""

import sys

# Matrix A[i] has dimension p[i-1] x p[i] for i = 1..n
def MatrixChainOrder(p, i, j):
	if i == j:
		return 0
	_min = sys.maxsize

	# place parenthesis at different places between first and last matrix,
	# recursively calculate count of multiplications for each parenthesis
	# placement and return the minimum count
	for k in range(i, j):
		count = (MatrixChainOrder(p, i, k) + MatrixChainOrder(p, k + 1, j) + p[i-1] * p[k] * p[j])
		if count < _min:
			_min = count
	# Return minimum count
	return _min

arr = [1, 2, 3, 4, 3]
n = len(arr)
print("Minimum number of multiplications is ",
	MatrixChainOrder(arr, 1, n-1))

```

## [Edit Distance](https://practice.geeksforgeeks.org/problems/edit-distance3702/1)

```python
"""
The Levenshtein distance (or Edit distance) is a way of quantifying how different two strings are from one another by counting the minimum number of operations required to transform one string into the other
('ABA', 'ABC') ——> ('ABAC', 'ABC') == ('ABA', 'AB') 
"""

def dist(X, Y):
    # `m` and `n` is the total number of characters in `X` and `Y`, respectively
    (m, n) = (len(X), len(Y))
    # For all pairs of `i` and `j`, `T[i, j]` will hold the Levenshtein distance
    # between the first `i` characters of `X` and the first `j` characters of `Y`.
    # Note that `T` holds `(m+1)×(n+1)` values.
    T = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # we can transform source prefixes into an empty string by dropping all characters
    for i in range(1, m + 1):
        T[i][0] = i                    # (case 1)

    # we can reach target prefixes from empty source prefix by inserting every character
    for j in range(1, n + 1):
        T[0][j] = j                    # (case 1)

    # fill the lookup table in a bottom-up manner
    for i in range(1, m + 1):

        for j in range(1, n + 1):
            cost = 0 if X[i - 1] == Y[j - 1] else 1
            T[i][j] = min(T[i - 1][j] + 1,      # deletion 
                        T[i][j - 1] + 1,        # insertion 
                        T[i - 1][j - 1] + cost) # replace 

    return T[m][n]
 

X = 'kitten'
Y = 'sitting'
print('The Levenshtein distance is', dist(X, Y))
```

## [Subset Sum Problem](https://practice.geeksforgeeks.org/problems/subset-sum-problem2014/1)

```python
"""
Given a set of positive integers and an integer k, check if there is any non-empty subset that sums to k.
A = { 7, 3, 2, 5, 8 }
k = 14

Output: Subset with the given sum exists
Subset { 7, 2, 5 } sums to 14
"""

def subsetSum(A, k):
    n = len(A)
    # `T[i][j]` stores true if subset with sum `j` can be attained
    # using items up to first `i` items
    T = [[False for _ in range(k + 1)] for _ in range(n + 1)]

    # if the sum is zero
    for i in range(n + 1):
        T[i][0] = True

    # do for i'th item
    for i in range(1, n + 1):
        # consider all sum from 1 to sum
        for j in range(1, k + 1):
            # don't include the i'th element if `j-A[i-1]` is negative
            if A[i - 1] > j:
                T[i][j] = T[i - 1][j]
            else:
                # find the subset with sum `j` by excluding or including the i'th item
                T[i][j] = T[i - 1][j] or T[i - 1][j - A[i - 1]]

    # return maximum value
    return T[n][k]
 

# Input: a set of items and a sum
A = [7, 3, 2, 5, 8]
k = 18
if subsetSum(A, k):
    print('Subsequence with the given sum exists')
else:
    print('Subsequence with the given sum does not exist')
```

## [Friends Pairing Problem](https://practice.geeksforgeeks.org/problems/friends-pairing-problem5425/1)

```python
"""
 Input  : n = 3
 Output : 4
 Explanation:
 {1}, {2}, {3} : all single
 {1}, {2, 3} : 2 and 3 paired but 1 is single.
 {1, 2}, {3} : 1 and 2 are paired but 3 is single.
 {1, 3}, {2} : 1 and 3 are paired but 2 is single.
 Note that {1, 2} and {2, 1} are considered same.
 
 Mathematical Explanation:
 The problem is simplified version of how many ways we can divide n elements into multiple groups.
 (here group size will be max of 2 elements).
 In case of n = 3, we have only 2 ways to make a group: 
     1) all elements are individual(1,1,1)
     2) a pair and individual (2,1)
 In case of n = 4, we have 3 ways to form a group:
     1) all elements are individual (1,1,1,1)
     2) 2 individuals and one pair (2,1,1)
     3) 2 separate pairs (2,2)
"""


# Returns count of ways n people can remain single or paired up.
def countFriendsPairings(n):

	dp = [0 for _ in range(n + 1)]

	# Filling dp[] in bottom-up manner using recursive formula explained above.
	for i in range(n + 1):

		dp[i] = i if (i <= 2) else dp[i - 1] + (i - 1) * dp[i - 2]
	return dp[n]

n = 4
print(countFriendsPairings(n))
```

## [Gold Mine Problem](https://practice.geeksforgeeks.org/problems/gold-mine-problem2608/1)

```python
"""
Given a gold mine of n*m dimensions. Each field in this mine contains a positive integer which is the amount of gold in tons. Initially the miner is at first column but can be at any row. He can move only (right->,right up /,right down\) that is from a given cell, the miner can move to the cell diagonally up towards the right or right or diagonally down towards the right. Find out maximum amount of gold he can collect. 
Examples: 
 

Input : mat[][] = {{1, 3, 3},
                   {2, 1, 4},
                  {0, 6, 4}};
Output : 12 
{(1,0)->(2,1)->(1,2)}

Input: mat[][] = { {1, 3, 1, 5},
                   {2, 2, 4, 1},
                   {5, 0, 2, 3},
                   {0, 6, 1, 2}};
Output : 16
(2,0) -> (1,1) -> (1,2) -> (0,3) OR
(2,0) -> (3,1) -> (2,2) -> (2,3)

"""


def collectGold(gold, x, y, n, m):
	if ((x < 0) or (x == n) or (y == m)):
		return 0

	# Right upper diagonal
	rightUpperDiagonal = collectGold(gold, x - 1, y + 1, n, m)

	# right
	right = collectGold(gold, x, y + 1, n, m)

	# Lower right diagonal
	rightLowerDiagonal = collectGold(gold, x + 1, y + 1, n, m)

	# Return the maximum and store the value
	return gold[x][y] + max(max(rightUpperDiagonal, rightLowerDiagonal), right)


def getMaxGold(gold,n,m):
	maxGold = 0
	for i in range(n):
		goldCollected = collectGold(gold, i, 0, n, m)
		maxGold = max(maxGold, goldCollected)
	return maxGold

gold = [[1, 3, 1, 5],
		[2, 2, 4, 1],
		[5, 0, 2, 3],
		[0, 6, 1, 2]
]
m,n = 4,4
print(getMaxGold(gold, n, m))
```

## [Assembly Line SchedulingProblem](https://www.geeksforgeeks.org/assembly-line-scheduling-dp-34/)

```python
def carAssembly(a, t, e, x):
    NUM_STATION = len(a[0])
    T1 = [0 for _ in range(NUM_STATION)]
    T2 = [0 for _ in range(NUM_STATION)]

    # time taken to leave first station in line 1
    T1[0] = e[0] + a[0][0] 
    # time taken to leave first station in line 2
    T2[0] = e[1] + a[1][0] 

    # Fill tables T1[] and T2[] using above given recursive relations
    for i in range(1, NUM_STATION):
        T1[i] = min(T1[i-1] + a[0][i], T2[i-1] + t[1][i] + a[0][i])
        T2[i] = min(T2[i-1] + a[1][i], T1[i-1] + t[0][i] + a[1][i] )

    # consider exit times and return minimum
    return min(T1[NUM_STATION - 1] + x[0], T2[NUM_STATION - 1] + x[1])
  
a = [[4, 5, 3, 2],
     [2, 10, 1, 4]]
t = [[0, 7, 4, 5],
     [0, 9, 2, 8]]
e = [10, 12]
x = [18, 7]
  
print(carAssembly(a, t, e, x))
```

## [Painting the Fence Problem](https://practice.geeksforgeeks.org/problems/painting-the-fence3727/1)

```python
'''  
Given a fence with n posts and k colors, find out the number of ways of painting the fence such that at most 2 adjacent posts have the same color. Since answer can be large return it modulo 10^9 + 7.
Examples:

Input : n = 2 k = 4
Output : 16
We have 4 colors and 2 posts.
Ways when both posts have same color : 4 
Ways when both posts have diff color :
4(choices for 1st post) * 3(choices for 
2nd post) = 12

Input : n = 3 k = 2
Output : 6
'''


# Returns count of ways to color k posts using k colors
def countWays(n, k):
	# There are k ways to color first post
	total = k
	mod = 1000000007

	# There are 0 ways for single post to violate (same color_ and k ways to not violate (different color)
	same, diff = 0, k

	# Fill for 2 posts onwards
	for _ in range(2, n + 1):
		# Current same is same as previous diff
		same = diff

		# We always have k-1 choices for next post
		diff = total * (k - 1)
		diff = diff % mod

		# Total choices till i.
		total = (same + diff) % mod
	return total

n, k = 3, 2
print(countWays(n, k))
```

## Rod Cutting Problem

```python
'''  
Given a rod of length n and a list of rod prices of length i, where 1 <= i <= n, find the optimal way to cut the rod into smaller rods to maximize profit.
For example, consider the following rod lengths and values:
Input:
length[] = [1, 2, 3, 4, 5, 6, 7, 8]
price[] = [1, 5, 8, 9, 10, 17, 17, 20]
Rod length: 4
Best: Cut the rod into two pieces of length 2 each to gain revenue of 5 + 5 = 10
'''

def rodCut(price, n):
 
    # `T[i]` stores the maximum profit achieved from a rod of length `i`
    T = [0] * (n + 1)
 
    # consider a rod of length `i`
    for i in range(1, n + 1):
        # divide the rod of length `i` into two rods of length `j` and `i-j` each and take maximum
        for j in range(1, i + 1):
            T[i] = max(T[i], price[j - 1] + T[i - j])
 
    # `T[n]` stores the maximum profit achieved from a rod of length `n`
    return T[n]
 
price = [1, 5, 8, 9, 10, 17, 17, 20]
n = 4        # rod length
print('Profit is', rodCut(price, n))
 
```

## [Longest Common Subsequence](https://practice.geeksforgeeks.org/problems/longest-common-subsequence/0)

```python
# Function to return all LCS of substrings `X[0…m-1]`, `Y[0…n-1]`
def LCS(X, Y, m, n, lookup):
    # if the end of either sequence is reached
    if m == 0 or n == 0:
        # create a list with one empty string and return
        return ['']
 
    # if the last character of `X` and `Y` matches
    if X[m - 1] == Y[n - 1]:
        # ignore the last characters of `X` and `Y` and find all LCS of substring
        # `X[0…m-2]`, `Y[0…n-2]` and store it in a list
        lcs = LCS(X, Y, m - 1, n - 1, lookup)
 
        # append current character `X[m-1]` or `Y[n-1]`
        # to all LCS of substring `X[0…m-2]` and `Y[0…n-2]`
        for i in range(len(lcs)):
            lcs[i] = lcs[i] + (X[m - 1])
        return lcs
 
    # we reach here when the last character of `X` and `Y` don't match
 
    # if a top cell of the current cell has more value than the left cell,
    # then ignore the current character of string `X` and find all LCS of
    # substring `X[0…m-2]`, `Y[0…n-1]`
    if lookup[m - 1][n] > lookup[m][n - 1]:
        return LCS(X, Y, m - 1, n, lookup)
 
    # if a left cell of the current cell has more value than the top cell,
    # then ignore the current character of string `Y` and find all LCS of
    # substring `X[0…m-1]`, `Y[0…n-2]`
    if lookup[m][n - 1] > lookup[m - 1][n]:
        return LCS(X, Y, m, n - 1, lookup)
 
    # if the top cell has equal value to the left cell, then consider both characters
 
    top = LCS(X, Y, m - 1, n, lookup)
    left = LCS(X, Y, m, n - 1, lookup)
 
    # merge two lists and return
    return top + left
 
 
# Function to fill the lookup table by finding the length of LCS
# of substring `X` and `Y`
def LCSLength(X, Y, lookup):
 
    # fill the lookup table in a bottom-up manner
    for i in range(1, len(X) + 1):
        for j in range(1, len(Y) + 1):
            # if current character of `X` and `Y` matches
            if X[i - 1] == Y[j - 1]:
                lookup[i][j] = lookup[i - 1][j - 1] + 1
 
            # otherwise, if the current character of `X` and `Y` don't match
            else:
                lookup[i][j] = max(lookup[i - 1][j], lookup[i][j - 1])
 
 
# Function to find all LCS of string `X[0…m-1]` and `Y[0…n-1]`
def findLCS(X, Y):
 
    # lookup[i][j] stores the length of LCS of substring `X[0…i-1]` and `Y[0…j-1]`
    lookup = [[0 for _ in range(len(Y) + 1)] for _ in range(len(X) + 1)]

    # fill lookup table
    LCSLength(X, Y, lookup)

    # find all the longest common subsequences
    lcs = LCS(X, Y, len(X), len(Y), lookup)

    # since a list can contain duplicates, "convert" it to a set and return
    return set(lcs)
 
X = 'ABCBDAB'
Y = 'BDCABA'
lcs = findLCS(X, Y)
print(lcs)
```

## [Longest Repeated Subsequence](https://practice.geeksforgeeks.org/problems/longest-repeating-subsequence/0)

```python
def LRS(X, m, n, lookup):
    # if the end of either sequence is reached, return an empty string
    if m == 0 or n == 0:
        return ''
        
    if X[m - 1] == X[n - 1] and m != n:
        return LRS(X, m - 1, n - 1, lookup) + X[m - 1]
    # otherwise, if characters at index `m` and `n` don't match
    if lookup[m - 1][n] > lookup[m][n - 1]:
        return LRS(X, m - 1, n, lookup)
    else:
        return LRS(X, m, n - 1, lookup)
 
 
# Function to fill the lookup table by finding the length of LRS of substring `X[0…n-1]`
def LRSLength(X, lookup):
    # Fill the lookup table in a bottom-up manner.The first row and first column of the lookup table are already 0.
    for i in range(1, len(X) + 1):
        for j in range(1, len(X) + 1):
            # if characters at index `i` and `j` matches and the index are different
            if X[i - 1] == X[j - 1] and i != j:
                lookup[i][j] = lookup[i - 1][j - 1] + 1
            # otherwise, if characters at index `i` and `j` are different
            else:
                lookup[i][j] = max(lookup[i - 1][j], lookup[i][j - 1])

X = 'ATACTCGGA'
# lookup[i][j] stores the length of LRS of substring `X[0…i-1]` and `X[0…j-1]`
lookup = [[0 for _ in range(len(X) + 1)] for _ in range(len(X) + 1)]
# fill lookup table
LRSLength(X, lookup)
# find the longest repeating subsequence
print(LRS(X, len(X), len(X), lookup))
```

## [Longest Increasing Subsequence](https://practice.geeksforgeeks.org/problems/longest-increasing-subsequence/0)

```python
def findLIS(arr):
    if not arr:
        return []
 
    # LIS[i] stores the longest increasing subsequence of sublist `arr[0…i]` that ends with `arr[i]`
    LIS = [[] for _ in range(len(arr))]
 
    # LIS[0] denotes the longest increasing subsequence ending at `arr[0]`
    LIS[0].append(arr[0])
 
    # start from the second element in the list
    for i in range(1, len(arr)):
        # do for each element in sublist `arr[0…i-1]`
        for j in range(i):
 
            # find the longest increasing subsequence that ends with `arr[j]`
            # where `arr[j]` is less than the current element `arr[i]`
            if arr[j] < arr[i] and len(LIS[j]) > len(LIS[i]):
                LIS[i] = LIS[j].copy()
 
        # include `arr[i]` in `LIS[i]`
        LIS[i].append(arr[i])
 
    # `j` will store the index of LIS
    j = 0
    for i in range(len(arr)):
        if len(LIS[j]) < len(LIS[i]):
            j = i
    print(LIS[j])
 
arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
findLIS(arr)
```

## [Space Optimized Solution of LCS (Print only length)](https://www.geeksforgeeks.org/space-optimized-solution-lcs/)

```python
def lcs(text1, text2):
    m, n = len(text1), len(text2)
    if m > n : text1, text2 = text2, text1
    dp = [0] * (n + 1)
    for c in text1:
        prev = 0
        for i, d in enumerate(text2):
            prev, dp[i + 1] = dp[i + 1], prev + 1 if c == d else max(dp[i], dp[i + 1])
    return dp[-1]
X = "AGGTAB"
Y = "GXTXAYB"
  
print("Length of LCS is", lcs(X, Y))
```

## [LCS (Longest Common Subsequence) of three strings](https://practice.geeksforgeeks.org/problems/lcs-of-three-strings/0)

```python
"""
Given 3 strings of all having length < 100,the task is to find the longest common sub-sequence in all three given sequences.

Examples: 

Input : str1 = "geeks"  
        str2 = "geeksfor"  
        str3 = "geeksforgeeks"
Output : 5
Longest common subsequence is "geeks"
i.e., length = 5
"""

X = "AGGT12"
Y = "12TXAYB"
Z = "12XBA"

dp = [[[-1 for _ in range(100)] for _ in range(100)] for _ in range(100)]
         
# Returns length of LCS for X[0..m-1], Y[0..n-1] and Z[0..o-1]
def lcsOf3(i, j, k):
 
    if(i == -1 or j == -1 or k == -1) :
        return 0

    if(dp[i][j][k] != -1) :
        return dp[i][j][k]

    if X[i] == Y[j] == Z[k]:
        dp[i][j][k] = 1 + lcsOf3(i - 1, j - 1, k - 1)
    
    else:
        dp[i][j][k] = max(max(lcsOf3(i - 1, j, k), lcsOf3(i, j - 1, k)), lcsOf3(i, j, k - 1))

    return dp[i][j][k]
 

m = len(X)
n = len(Y)
o = len(Z)
print("Length of LCS is", lcsOf3(m - 1, n - 1, o - 1))
```

## [Maximum Sum Increasing Subsequence](https://practice.geeksforgeeks.org/problems/maximum-sum-increasing-subsequence4749/1)

```python
"""
Given an array of n positive integers. Write a program to find the sum of maximum sum subsequence of the given array such that the integers in the subsequence are sorted in increasing order. For example, if input is {1, 101, 2, 3, 100, 4, 5}, then output should be 106 (1 + 2 + 3 + 100), if the input array is {3, 4, 5, 10}, then output should be 22 (3 + 4 + 5 + 10) and if the input array is {10, 5, 4, 3}, then output should be 10
"""

def maxSumIS(arr, n):
    maxx = 0
    msis = [0 for _ in range(n)]

    # Initialize msis values for all indexes
    for i in range(n):
        msis[i] = arr[i]

    # Compute maximum sum values in bottom up manner
    for i in range(1, n):
        for j in range(i):
            if (arr[i] > arr[j] and
                msis[i] < msis[j] + arr[i]):
                msis[i] = msis[j] + arr[i]

    # Pick maximum of all msis values
    for i in range(n):
        if maxx < msis[i]:
            maxx = msis[i]
    return maxx

arr = [1, 101, 2, 3, 100, 4, 5]
n = len(arr)
print("Sum of maximum sum increasing " + "subsequence is " +str(maxSumIS(arr, n)))
```

## [Count all subsequences having product less than K](https://www.geeksforgeeks.org/count-subsequences-product-less-k/)

```python
"""
Input : [1, 2, 3, 4] 
        k = 10
Output :11 
Explanation: The subsequences are {1}, {2}, {3}, {4}, {1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4}, {1, 2, 3}, {1, 2, 4}

Input  : [4, 8, 7, 2] 
         k = 50
Output : 9
"""

def productSubSeqCount(arr, k):
    n = len(arr)
    dp = [[0 for _ in range(n + 1)] for _ in range(k + 1)]
    for i in range(1, k + 1):
        for j in range(1, n + 1):

            # number of subsequence using j-1 terms
            dp[i][j] = dp[i][j - 1]

            # if arr[j-1] > i it will surely make product greater thus it won't contribute then
            if arr[j - 1] <= i and arr[j - 1] > 0:

                # number of subsequence using 1 to j-1 terms and j-th term
                dp[i][j] += dp[i // arr[j - 1]][j - 1] + 1
    return dp[k][n]
 
A = [1,2,3,4]
k = 10
print(productSubSeqCount(A, k))
```

## [Longest subsequence such that difference between adjacent is one](https://practice.geeksforgeeks.org/problems/longest-subsequence-such-that-difference-between-adjacents-is-one4724/1)

```python
"""
Input :  arr[] = {10, 9, 4, 5, 4, 8, 6}
Output :  3
As longest subsequences with difference 1 are, "10, 9, 8", 
"4, 5, 4" and "4, 5, 6"

Input :  arr[] = {1, 2, 3, 2, 3, 7, 2, 1}
Output :  7
As longest consecutive sequence is "1, 2, 3, 2, 3, 2, 1"
"""

def longestSubseqWithDiffOne(arr, n):
    # Initialize the dp[] array with 1 as a single element will be of 1 length
    dp = [1 for _ in range(n)]

    # Start traversing the given array
    for i in range(n):
        # Compare with all the previous elements
        for j in range(i):
            # If the element is consecutive then consider this subsequence and update dp[i] if required.
            if arr[i] in [arr[j] + 1, arr[j] - 1]:
                dp[i] = max(dp[i], dp[j]+1)

    # Longest length will be the maximum value of dp array.
    result = 1
    for i in range(n):
        if (result < dp[i]):
            result = dp[i]
    return result

arr = [1, 2, 3, 4, 5, 3, 2]
# Longest subsequence with one difference is {1, 2, 3, 4, 3, 2}
n = len(arr)
print (longestSubseqWithDiffOne(arr, n))
```

## [Maximum subsequence sum such that no three are consecutive](https://www.geeksforgeeks.org/maximum-subsequence-sum-such-that-no-three-are-consecutive/)

```python
# sourcery skip: avoid-builtin-shadow
"""
Input: arr[] = {1, 2, 3}
Output: 5
We can't take three of them, so answer is
2 + 3 = 5

Input: arr[] = {3000, 2000, 1000, 3, 10}
Output: 5013 
3000 + 2000 + 3 + 10 = 5013
"""
arr = [100, 1000, 100, 1000, 1]
sum = [-1] * 10000

# Returns maximum subsequence sum such
# that no three elements are consecutive
def maxSumWO3Consec(n) :
	if(sum[n] != -1):
		return sum[n]
	
	# 3 Base cases (process first three elements)
	if(n == 0) :
		sum[n] = 0
		return sum[n]
	
	if(n == 1) :
		sum[n] = arr[0]
		return sum[n]
	
	if(n == 2) :
		sum[n] = arr[1] + arr[0]
		return sum[n]
	
	# Process rest of the elements We have three cases
	sum[n] = max(max(maxSumWO3Consec(n - 1), maxSumWO3Consec(n - 2) + arr[n-1]), arr[n-1] + arr[n - 2] + maxSumWO3Consec(n - 3))
	return sum[n]

n = len(arr)
print(maxSumWO3Consec(n))
```

## [Egg Dropping Problem](https://practice.geeksforgeeks.org/problems/egg-dropping-puzzle/0)

```python
import sys

# Function to get minimum number of trials needed in worst case with n eggs and k floors
def eggDrop(n, k):
	# If there are no floors, then no trials needed. OR if there is one floor, one trial needed.
	if k in [1, 0]:
		return k

	# We need k trials for one egg and k floors
	if (n == 1):
		return k
	min = sys.maxsize

	# Consider all droppings from 1st floor to kth floor and return the minimum of these values plus 1.
	for x in range(1, k + 1):
		res = max(eggDrop(n - 1, x - 1),
				eggDrop(n, k - x))
		if (res < min):
			min = res
	return min + 1

n = 2
k = 10
print("Minimum number of trials in worst case with", n, "eggs and", k, "floors is", eggDrop(n, k))
```

## [Maximum Length Chain of Pairs](https://practice.geeksforgeeks.org/problems/max-length-chain/1)

```python
"""
You are given n pairs of numbers. In every pair, the first number is always smaller than the second number. A pair (c, d) can follow another pair (a, b) if b < c. Chain of pairs can be formed in this fashion. Find the longest chain which can be formed from a given set of pairs. 

For example, if the given pairs are {{5, 24}, {39, 60}, {15, 28}, {27, 40}, {50, 90} }, then the longest chain that can be formed is of length 3, and the chain is {{5, 24}, {27, 40}, {50, 90}}
"""


class Pair(object):
	def __init__(self, a, b):
		self.a = a
		self.b = b

# This function assumes that arr[] is sorted in increasing
# order according the first (or smaller) values in pairs.
def maxChainLength(arr, n):
	max = 0

	# Initialize MCL(max chain length) values for all indices
	mcl = [1 for _ in range(n)]

	# Compute optimized chain length values in bottom up manner
	for i in range(1, n):
		for j in range(i):
			if (arr[i].a > arr[j].b and
				mcl[i] < mcl[j] + 1):
				mcl[i] = mcl[j] + 1

	# mcl[i] now stores the maximum chain length ending with pair i
	# Pick maximum of all MCL values
	for i in range(n):
		if (max < mcl[i]):
			max = mcl[i]
	return max

arr = [Pair(5, 24), Pair(15, 25),
	Pair(27, 40), Pair(50, 60)]
print('Length of maximum size chain is', maxChainLength(arr, len(arr)))
```

## [Maximum size square sub-matrix with all 1s](https://practice.geeksforgeeks.org/problems/largest-square-formed-in-a-matrix/0)

```python
R = 6
C = 5

def printMaxSubSquare(M):
	global R,C
	Max = 0
	# set all elements of S to 0 first
	S = [[0 for _ in range(C)] for _ in range(2)]

	# Construct the entries
	for i in range(R):
		for j in range(C):

			# Compute the entrie at the current position
			Entrie = M[i][j]
			if Entrie and j:
				Entrie = 1 + min(S[1][j - 1],min(S[0][j - 1], S[1][j]))

			# Save the last entrie and add the new one
			S[0][j] = S[1][j]
			S[1][j] = Entrie

			# Keep track of the max square length
			Max = max(Max, Entrie)

	# Print the square
	print("Maximum size sub-matrix is: ")
	for _ in range(Max):
		for _ in range(Max):
			print("1",end=" ")
		print()	

M = [[0, 1, 1, 0, 1],
	[1, 1, 0, 1, 0],
	[0, 1, 1, 1, 0],
	[1, 1, 1, 1, 0],
	[1, 1, 1, 1, 1],
	[0, 0, 0, 0, 0]]			
printMaxSubSquare(M)
```

## [Maximum sum of pairs with specific difference](https://practice.geeksforgeeks.org/problems/pairs-with-specific-difference/0)

```python
"""
Input  : arr[] = {3, 5, 10, 15, 17, 12, 9}, K = 4
Output : 62
Explanation:
Then disjoint pairs with difference less than K are, (3, 5), (10, 12), (15, 17)  
So maximum sum which we can get is 3 + 5 + 12 + 10 + 15 + 17 = 62
Note that an alternate way to form disjoint pairs is, (3, 5), (9, 12), (15, 17), but this pairing produces lesser sum.

Input  : arr[] = {5, 15, 10, 300}, k = 12
Output : 25
"""

def maxSumPairWithDifferenceLessThanK(arr, N, k):
    maxSum = 0

    # Sort elements to ensure every i and i-1 is closest possible pair
    arr.sort()
 
    # To get maximum possible sum, iterate from largest to smallest, giving larger numbers priority over smaller numbers.
    i = N - 1
    while (i > 0):
 
        # Case I: Diff of arr[i] and arr[i-1] is less than K, add to maxSum
        # Case II: Diff between arr[i] and arr[i-1] is not less than K, move to next i since with sorting we know, 
        # arr[i]-arr[i-1] < arr[i]-arr[i-2] and so on.
        
        if (arr[i] - arr[i - 1] < k):
            # Assuming only positive numbers.
            maxSum += arr[i]
            maxSum += arr[i - 1]
 
            # When a match is found skip this pair
            i -= 1
        i -= 1
    return maxSum

arr = [3, 5, 10, 15, 17, 12, 9]
N = len(arr)
K = 4
print(maxSumPairWithDifferenceLessThanK(arr, N, K))
```

## [Min Cost PathProblem](https://practice.geeksforgeeks.org/problems/path-in-matrix3805/1)

```python
"""
Given a n*n matrix where all numbers are distinct, find the maximum length path (starting from any cell) such that all cells along the path are in increasing order with a difference of 1. 
We can move in 4 directions from a given cell (i, j), i.e., we can move to (i+1, j) or (i, j+1) or (i-1, j) or (i, j-1) with the condition that the adjacent cells have a difference of 1.

Example: 

Input:  mat[][] = {{1, 2, 9}
                   {5, 3, 8}
                   {4, 6, 7}}
Output: 4
The longest path is 6-7-8-9. 
"""
n = 3
# Returns length of the longest path beginning with mat[i][j]. This function mainly uses lookup table dp[n][n]
def findLongestFromACell(i, j, mat, dp):
	if (i < 0 or i >= n or j < 0 or j >= n):
		return 0

	# If this subproblem is already solved
	if (dp[i][j] != -1):
		return dp[i][j]

	# To store the path lengths in all the four directions
	x, y, z, w = -1, -1, -1, -1

	# Since all numbers are unique and in range from 1 to n * n,
	# there is atmost one possible direction from any cell
	if (j < n-1 and ((mat[i][j] + 1) == mat[i][j + 1])):
		x = 1 + findLongestFromACell(i, j + 1, mat, dp)

	if (j > 0 and (mat[i][j] + 1 == mat[i][j-1])):
		y = 1 + findLongestFromACell(i, j-1, mat, dp)

	if (i > 0 and (mat[i][j] + 1 == mat[i-1][j])):
		z = 1 + findLongestFromACell(i-1, j, mat, dp)

	if (i < n-1 and (mat[i][j] + 1 == mat[i + 1][j])):
		w = 1 + findLongestFromACell(i + 1, j, mat, dp)

	# If none of the adjacent fours is one greater we will take 1
	# otherwise we will pick maximum from all the four directions
	dp[i][j] = max(x, max(y, max(z, max(w, 1))))
	return dp[i][j]

# Returns length of the longest path beginning with any cell
def finLongestOverAll(mat):
	result = 1 # Initialize result

	# Create a lookup table and fill all entries in it as -1
	dp = [[-1 for _ in range(n)] for _ in range(n)]
    
	# Compute longest path beginning from all cells
	for i in range(n):
		for j in range(n):
			if (dp[i][j] == -1):
				findLongestFromACell(i, j, mat, dp)
			# Update result if needed
			result = max(result, dp[i][j])
	return result

mat = [[1, 2, 9],
	[5, 3, 8],
	[4, 6, 7]]
print("Length of the longest path is ", finLongestOverAll(mat))
```

## [Maximum difference of zeros and ones in binary string](https://practice.geeksforgeeks.org/problems/maximum-difference-of-zeros-and-ones-in-binary-string4111/1)

```python
"""
Given a binary string of 0s and 1s. The task is to find the length of the substring which is having a maximum difference between the number of 0s and the number of 1s (number of 0s – number of 1s). In case of all 1s print -1.

Examples: 

Input : S = "11000010001"
Output : 6
From index 2 to index 9, there are 7
0s and 1 1s, so number of 0s - number
of 1s is 6.
Input : S = "1111"
Output : -1
"""


MAX = 100

# Return true if there all 1s
def allones(s, n):
	# Checking each index is 0 or not.
	co = sum(1 if i == '1' else 0 for i in s)
	return co == n

# Find the length of substring with maximum difference of zeroes and ones in binary string
def findlength(arr, s, n, ind, st, dp):
	
	# If string is over
	if ind >= n:
		return 0

	# If the state is already calculated.
	if dp[ind][st] != -1:
		return dp[ind][st]

	if not st:
		dp[ind][st] = max(arr[ind] +
		findlength(arr, s, n, ind + 1, 1, dp),
			(findlength(arr, s, n, ind + 1, 0, dp)))
	else:
		dp[ind][st] = max(arr[ind] +
		findlength(arr, s, n, ind + 1, 1, dp), 0)
	return dp[ind][st]

# Returns length of substring which is having maximum difference of number of 0s and number of 1s
def maxLen(s, n):
	# If all 1s return -1.
	if allones(s, n):
		return -1

	# Else find the length.
	arr = [0] * MAX
	for i in range(n):
		arr[i] = 1 if s[i] == '0' else -1
	dp = [[-1] * 3 for _ in range(MAX)]
	return findlength(arr, s, n, 0, 0, dp)

s = "11000010001"
n = 11
print(maxLen(s, n))
```

## [Minimum number of jumps to reach end](https://practice.geeksforgeeks.org/problems/minimum-number-of-jumps/0)

```python
"""
Given an array of integers where each element represents the max number of steps that can be made forward from that element. Write a function to return the minimum number of jumps to reach the end of the array (starting from the first element). If an element is 0, then we cannot move through that element. If we can’t reach the end, return -1.

Examples: 
    Input:  arr[] = {1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9}
    Output: 3 (1-> 3 -> 8 -> 9)
    Explanation: Jump from 1st element to 
    2nd element as there is only 1 step, 
    now there are three options 5, 8 or 9. 
    If 8 or 9 is chosen then the end node 9 
    can be reached. So 3 jumps are made.

    Input:  arr[] = {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1}
    Output: 10
    Explanation: In every step a jump is 
    needed so the count of jumps is 10.
"""

def minJumps(arr, n):
  # The number of jumps needed to reach the starting index is 0
  if (n <= 1):
    return 0
  
  # Return -1 if not possible to jump
  if (arr[0] == 0):
    return -1
  
  # initialization
  maxReach = arr[0]    # stores all time the maximal reachable index in the array
  step = arr[0]   # stores the amount of steps we can still take
  jump = 1   # stores the amount of jumps necessary to reach that maximal reachable position
  
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
       
      # Check if the current index / position or lesser index is the maximum reach point from the previous indexes
      if(i >= maxReach):
        return -1
  
      # re-initialize the steps to the amount of steps to reach maxReach from position i.
      step = maxReach - i;
  return -1
  

arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
size = len(arr)
print("Minimum number of jumps to reach end is % d " % minJumps(arr, size))
```

## [Minimum cost to fill given weight in a bag](https://practice.geeksforgeeks.org/problems/minimum-cost-to-fill-given-weight-in-a-bag1956/1)

```python
"""
You are given a bag of size W kg and you are provided costs of packets different weights of oranges in array cost[] where cost[i] is basically the cost of ‘i’ kg packet of oranges. Where cost[i] = -1 means that ‘i’ kg packet of orange is unavailable
Find the minimum total cost to buy exactly W kg oranges and if it is not possible to buy exactly W kg oranges then print -1. It may be assumed that there is an infinite supply of all available packet types.
Note: array starts from index 1. 

Examples: 

Input  : W = 5, cost[] = {20, 10, 4, 50, 100}
Output : 14
We can choose two oranges to minimize cost. First 
orange of 2Kg and cost 10. Second orange of 3Kg
and cost 4. 

Input  : W = 5, cost[] = {1, 10, 4, 50, 100}
Output : 5
We can choose five oranges of weight 1 kg.
"""

import sys

# Returns the best obtainable price for a rod of length n and price[] as prices of different pieces
def minCost(cost, n):
	dp = [0 for _ in range(n + 1)]
	# Build the table val[] in bottom up manner and return the last entry from the table
	for i in range(1, n + 1):
		min_cost = sys.maxsize
		for j in range(i):
			if j<len(cost) and cost[j]!=-1:
				min_cost = min(min_cost, cost[j] + dp[i - j - 1])
		dp[i] = min_cost

	return dp[n]

cost = [ 10,-1,-1,-1,-1 ]
W = len(cost)
print(minCost(cost, W))
```

## [Minimum removals from array to make max –min <= K](https://www.geeksforgeeks.org/minimum-removals-array-make-max-min-k/)

```python
"""
Input : a[] = {1, 3, 4, 9, 10, 11, 12, 17, 20} 
          k = 4 
Output : 5 
Explanation: Remove 1, 3, 4 from beginning 
and 17, 20 from the end.

Input : a[] = {1, 5, 6, 2, 8}  K=2
Output : 3
Explanation: There are multiple ways to 
remove elements in this case.
One among them is to remove 5, 6, 8.
The other is to remove 1, 2, 5
"""
def removal(a, n, k):
    # sort the array
    a.sort()
    # to store the max length of array with difference <= k
    maxLen = 0
    # pointer to keep track of starting of each subarray
    i = 0
    for j in range(i+1, n):
        # if the subarray from i to j index is valid the store it's length
        if a[j]-a[i] <= k:
            maxLen = max(maxLen, j-i+1)
        else:
            i += 1
        if i >= n:
            break
    return n-maxLen
 
a = [1, 3, 4, 9, 10, 11, 12, 17, 20]
n = len(a)
k = 4
print(removal(a, n, k))
```

## [Longest Common Substring](https://practice.geeksforgeeks.org/problems/longest-common-substring/0)

```python
"""
Input : X = “GeeksforGeeks”, y = “GeeksQuiz” 
Output : 5 
Explanation:
The longest common substring is “Geeks” and is of length 5.
"""

def lcs(i, j, count):
    if (i == 0 or j == 0):
        return count
    if (X[i - 1] == Y[j - 1]):
        count = lcs(i - 1, j - 1, count + 1)
    count = max(count, max(lcs(i, j - 1, 0), lcs(i - 1, j, 0)))
    return count
 
X = "abcdxyz"
Y = "xyzabcd"
n = len(X)
m = len(Y)
print(lcs(n, m, 0))
```

## [Count number of ways to reacha given score in a game](https://practice.geeksforgeeks.org/problems/reach-a-given-score/0)

```python
"""
Consider a game where a player can score 3 or 5 or 10 points in a move. Given a total score n, find number of ways to reach the given score.
Examples: 
 
Input: n = 20
Output: 4
There are following 4 ways to reach 20
(10, 10)
(5, 5, 10)
(5, 5, 5, 5)
(3, 3, 3, 3, 3, 5)
"""

def count(n):
    # table[i] will store count of solutions for value i. Initialize all table values as 0.
    table = [0 for _ in range(n+1)]

    # Base case (If given value is 0)
    table[0] = 1

    # One by one consider given 3 moves and update the table[] values after the index greater than 
    # or equal to the value of the picked move.
    for i in range(3, n+1):
        table[i] += table[i-3]
    for i in range(5, n+1):
        table[i] += table[i-5]
    for i in range(10, n+1):
        table[i] += table[i-10]
    return table[n]

n = 20
print('Count for', n, 'is', count(n)) 
n = 13
print('Count for', n, 'is', count(n))
```

## [Count Balanced Binary Trees of Height h](https://practice.geeksforgeeks.org/problems/bbt-counter/0)

```python
"""
Given a height h, count and return the maximum number of balanced binary trees possible with height h. A balanced binary tree is one in which for every node, the difference between heights of left and right subtree is not more than 1.

Input : h = 3
Output : 15

Input : h = 4
Output : 315
"""
def countBT(h) :
    BIG_PRIME = 1000000007
    if h < 2:
          return 1
    dp0 = dp1 = 1
    dp2 = 3
    for _ in range(2,h+1):
        dp2 = (dp1*dp1 + 2*dp1*dp0)%BIG_PRIME
        dp0 = dp1
        dp1 = dp2
    return dp2

h = 3
print(f"No. of balanced binary trees of height {h} is: {str(countBT(h))}")
```

## [Smallest sum contiguous subarray](https://www.geeksforgeeks.org/smallest-sum-contiguous-subarray/)

```python
"""
Given an array containing n integers. The problem is to find the sum of the elements of the contiguous subarray having the smallest(minimum) sum.
Examples: 
Input : arr[] = {3, -4, 2, -3, -1, 7, -5}
Output : -6
Subarray is {-4, 2, -3, -1} = -6
"""

maxsize=float('inf')

def smallestSumSubarr(arr, n):
	# to store the minimum value that is ending up to the current index
	min_ending_here = maxsize
	
	# to store the minimum value encountered so far
	min_so_far = maxsize
	
	# traverse the array elements
	for i in range(n):
		# if min_ending_here > 0, then it could not possibly contribute to the minimum sum further
		if (min_ending_here > 0):
			min_ending_here = arr[i]
		
		# else add the value arr[i] to min_ending_here
		else:
			min_ending_here += arr[i]
		
		# update min_so_far
		min_so_far = min(min_so_far, min_ending_here)
	return min_so_far
	

arr = [3, -4, 2, -3, -1, 7, -5]
n = len(arr)
print ("Smallest sum: ", smallestSumSubarr(arr, n))
```

## [Unbounded Knapsack (Repetition of items allowed)](https://practice.geeksforgeeks.org/problems/knapsack-with-duplicate-items4201/1)

```python
"""
Given a knapsack weight W and a set of n items with certain value vali and weight wti, we need to calculate the maximum amount that could make up this quantity exactly. This is different from classical Knapsack problem, here we are allowed to use unlimited number of instances of an item.
Examples: 

Input : W = 100
       val[]  = {1, 30}
       wt[] = {1, 50}
Output : 100
There are many ways to fill knapsack.
1) 2 instances of 50 unit weight item.
2) 100 instances of 1 unit weight item.
3) 1 instance of 50 unit weight item and 50
   instances of 1 unit weight items.
We get maximum value with option 2.
"""
def unboundedKnapsack(W, n, val, wt):
    # dp[i] is going to store maximum value with knapsack capacity i.
    dp = [0 for _ in range(W + 1)]
    ans = 0

    # Fill dp[] using above recursive formula
    for i in range(W + 1):
        for j in range(n):
            if (wt[j] <= i):
                dp[i] = max(dp[i], dp[i - wt[j]] + val[j])
    return dp[W]
 
W = 100
val = [10, 30, 20]
wt = [5, 10, 15]
n = len(val)
print(unboundedKnapsack(W, n, val, wt))
```

## [Largest Independent Set Problem](https://www.geeksforgeeks.org/largest-independent-set-problem-dp-26/)

```python
"""
Given a Binary Tree, find size of the Largest Independent Set(LIS) in it. A subset of all tree nodes is an independent set if there is no edge between any two nodes of the subset. 

For example, consider the following binary tree. The largest independent set(LIS) is {10, 40, 60, 70, 80} and size of the LIS is 5.
"""

class node:
	def __init__(self, data):
		
		self.data = data
		self.left = self.right = None
		self.liss = 0

# A memoization function returns size of the largest independent set in a given binary tree
def liss(root):
	if root is None:
		return 0
	if root.liss != 0:
		return root.liss
	if root.left is None and root.right is None:
		root.liss = 1
		return root.liss

	# Calculate size excluding the current node
	liss_excl = (liss(root.left) + liss(root.right))

	# Calculate size including the current node
	liss_incl = 1
	if root.left != None:
		liss_incl += (liss(root.left.left) + liss(root.left.right))

	if root.right != None:
		liss_incl += (liss(root.right.left) + liss(root.right.right))

	# Maximum of two sizes is LISS, store it for future uses.
	root.liss = max(liss_excl, liss_incl)
	return root.liss
	
root = node(20)
root.left = node(8)
root.left.left = node(4)
root.left.right = node(12)
root.left.right.left = node(10)
root.left.right.right = node(14)
root.right = node(22)
root.right.right = node(25)
print("Size of the Largest Independent Set is ", liss(root))
```

## [Partition problem](https://practice.geeksforgeeks.org/problems/subset-sum-problem2014/1)

```python
def isPossible(elements, target):
    dp = [False]*(target+1)
    dp[0] = True
    for ele in elements:
        for j in range(target, ele - 1, -1):
            if dp[j - ele]:
                dp[j] = True
    return dp[target]
 
arr = [6, 2, 5]
target = 7
if isPossible(arr, target):
    print("YES")
else:
    print("NO")
```

## [Longest Palindromic Subsequence](https://practice.geeksforgeeks.org/problems/longest-palindromic-subsequence-1612327878/1/)

```python

"""   
As another example, if the given sequence is “BBABCBCAB”, then the output should be 7 as “BABCBAB” is the longest palindromic subsequence in it. “BBBBB” and “BBCBB” are also palindromic subsequences of the given sequence, but not the longest ones.
"""

dp = [[-1 for _ in range(1001)] for _ in range(1001)]
def lps(s1, s2, n1, n2):
	if (n1 == 0 or n2 == 0):
		return 0

	if (dp[n1][n2] != -1):
		return dp[n1][n2]

	if (s1[n1 - 1] == s2[n2 - 1]):
		dp[n1][n2] = 1 + lps(s1, s2, n1 - 1, n2 - 1)
	else:
		dp[n1][n2] = max(lps(s1, s2, n1 - 1, n2), lps(s1, s2, n1, n2 - 1))

	return dp[n1][n2]


seq = "GEEKSFORGEEKS"
n = len(seq)
s2 = seq
s2 = s2[::-1]
print(f"The length of the LPS is {lps(s2, seq, n, n)}")
```

## [Count All Palindromic Subsequence in a given String](https://practice.geeksforgeeks.org/problems/count-palindromic-subsequences/1)

```python
"""   
Input : str = "abcd"
Output : 4
Explanation :- palindromic  subsequence are : "a" ,"b", "c" ,"d" 

Input : str = "aab"
Output : 4
Explanation :- palindromic subsequence are :"a", "a", "b", "aa"

Input : str = "aaaa"
Output : 15
"""

def countPS(i, j):
	if(i > j):
		return 0

	if(dp[i][j] != -1):
		return dp[i][j]

	if (i == j):
		dp[i][j] = 1
	elif str[i] == str[j]:
		dp[i][j] = (countPS(i + 1, j) + countPS(i, j - 1) + 1)
	else:
		dp[i][j] = (countPS(i + 1, j) + countPS(i, j - 1) - countPS(i + 1, j - 1))

	return dp[i][j]

str = "abcb" # remember to use variable name str otherwise program will fail
dp = [[-1 for _ in range(1000)] for _ in range(1000)]
n = len(str)
print("Total palindromic subsequence are :", countPS(0, n - 1))

```

## [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)

```python
"""   
Suppose we have a string S. We have to find the longest palindromic substring in S. We are assuming that the length of the string S is 1000. So if the string is “BABAC”, then the longest palindromic substring is “BAB”.
"""

def longestPalindrome( s):
   dp = [[False for _ in range(len(s))] for _ in range(len(s))]
   for i in range(len(s)):
      dp[i][i] = True
   max_length = 1
   start = 0
   for l in range(2,len(s)+1):
      for i in range(len(s)-l+1):
         end = i+l
         if l==2:
            if s[i] == s[end-1]:
               dp[i][end-1]=True
               max_length = l
               start = i
         elif s[i] == s[end-1] and dp[i+1][end-2]:
            dp[i][end-1]=True
            max_length = l
            start = i
   return s[start:start+max_length]

print(longestPalindrome("ABBABBC"))
```

## [Longest alternating subsequence](https://practice.geeksforgeeks.org/problems/longest-alternating-subsequence/0)

```python
"""   
Input: arr[] = {1, 5, 4}
Output: 3
The whole arrays is of the form  x1 < x2 > x3 

Input: arr[] = {1, 4, 5}
Output: 2
All subsequences of length 2 are either of the form 
x1 < x2; or x1 > x2

Input: arr[] = {10, 22, 9, 33, 49, 50, 31, 60}
Output: 6
The subsequences {10, 22, 9, 33, 31, 60} or
{10, 22, 9, 49, 31, 60} or {10, 22, 9, 50, 31, 60}
are longest subsequence of length 6.
"""

def LAS(arr, n):
	# "inc" and "dec" initialized as 1 as single element is still LAS
	inc = 1
	dec = 1
	
	# Iterate from second element
	for i in range(1,n):
		if (arr[i] > arr[i-1]):
			# "inc" changes iff "dec" changes
			inc = dec + 1
			
		elif (arr[i] < arr[i-1]):
			# "dec" changes iff "inc" changes
			dec = inc + 1
			
	# Return the maximum length
	return max(inc, dec)

arr = [10, 22, 9, 33, 49, 50, 31, 60]
n = len(arr)
print(LAS(arr, n))

```

## [Weighted Job Scheduling](https://www.geeksforgeeks.org/weighted-job-scheduling/)

```python
"""   
Given N jobs where every job is represented by following three elements of it.

Start Time
Finish Time
Profit or Value Associated (>= 0)
Find the maximum profit subset of jobs such that no two jobs in the subset overlap. 

Example: 

Input: Number of Jobs n = 4
       Job Details {Start Time, Finish Time, Profit}
       Job 1:  {1, 2, 50} 
       Job 2:  {3, 5, 20}
       Job 3:  {6, 19, 100}
       Job 4:  {2, 100, 200}
Output: The maximum profit is 250.
We can get the maximum profit by scheduling jobs 1 and 4.
Note that there is longer schedules possible Jobs 1, 2 and 3 
but the profit with this schedule is 20+50+100 which is less than 250.
"""

# Importing the following module to sort array based on our custom comparison function
from functools import cmp_to_key

# A job has start time, finish time and profit
class Job:
	def __init__(self, start, finish, profit):
		self.start = start
		self.finish = finish
		self.profit = profit

# A utility function that is used for sorting events according to finish time
def jobComparator(s1, s2):
	return s1.finish < s2.finish

# Find the latest job (in sorted array) that doesn't conflict with the job[i]. If there is no compatible job, then it returns -1
def latestNonConflict(arr, i):
	for j in range(i - 1, -1, -1):
		if arr[j].finish <= arr[i - 1].start:
			return j
	return -1

# A recursive function that returns the maximum possible profit from given array of jobs. The array of jobs must be sorted according to finish time
def findMaxProfitRec(arr, n):
	# Base case
	if n == 1:
		return arr[n - 1].profit

	# Find profit when current job is included
	inclProf = arr[n - 1].profit
	i = latestNonConflict(arr, n)
	
	if i != -1:
		inclProf += findMaxProfitRec(arr, i + 1)

	# Find profit when current job is excluded
	exclProf = findMaxProfitRec(arr, n - 1)
	return max(inclProf, exclProf)

# The main function that returns the maximum possible profit from given array of jobs
def findMaxProfit(arr, n):
	
	# Sort jobs according to finish time
	arr = sorted(arr, key = cmp_to_key(jobComparator))
	return findMaxProfitRec(arr, n)

values = [ (3, 10, 20), (1, 2, 50), (6, 19, 100), (2, 100, 200) ]
arr = [Job(i[0], i[1], i[2]) for i in values]
n = len(arr)
print("The optimal profit is", findMaxProfit(arr, n))
```

## [Coin game winner where every player has three choices](https://www.geeksforgeeks.org/coin-game-winner-every-player-three-choices/)

```python
"""   
A and B are playing a game. At the beginning there are n coins. Given two more numbers x and y. In each move a player can pick x or y or 1 coins. A always starts the game. The player who picks the last coin wins the game or the person who is not able to pick any coin loses the game. For a given value of n, find whether A will win the game or not if both are playing optimally.

Examples: 

Input :  n = 5, x = 3, y = 4
Output : A
There are 5 coins, every player can pick 1 or
3 or 4 coins on his/her turn.
A can win by picking 3 coins in first chance.
Now 2 coins will be left so B will pick one 
coin and now A can win by picking the last coin.

Input : 2 3 4
Output : B
"""

# To find winner of game
def findWinner(x, y, n):
	
	# To store results
	dp = [0 for _ in range(n + 1)]

	# Initial values
	dp[0] = False
	dp[1] = True

	# Computing other values.
	for i in range(2, n + 1):
		# If A losses any of i-1 or i-x or i-y game then he will definitely win game i
		if i >= 1 and not dp[i - 1]:
			dp[i] = True
		elif (i - x >= 0 and not dp[i - x]):
			dp[i] = True
		elif (i - y >= 0 and not dp[i - y]):
			dp[i] = True
		else:
			dp[i] = False

	# If dp[n] is true then A will game otherwise he losses
	return dp[n]

x = 3; y = 4; n = 5
if (findWinner(x, y, n)):
	print('A')
else:
	print('B')
```

## [Count Derangements (Permutation such that no element appears in its original position) [ IMPORTANT ]](https://www.geeksforgeeks.org/count-derangements-permutation-such-that-no-element-appears-in-its-original-position/)

```python
"""   
A and B are playing a game. At the beginning there are n coins. Given two more numbers x and y. In each move a player can pick x or y or 1 coins. A always starts the game. The player who picks the last coin wins the game or the person who is not able to pick any coin loses the game. For a given value of n, find whether A will win the game or not if both are playing optimally.

Examples: 

A Derangement is a permutation of n elements, such that no element appears in its original position. For example, a derangement of {0, 1, 2, 3} is {2, 3, 1, 0}.
Given a number n, find the total number of Derangements of a set of n elements.

Examples : 

Input: n = 2
Output: 1
For two elements say {0, 1}, there is only one 
possible derangement {1, 0}

Input: n = 3
Output: 2
For three elements say {0, 1, 2}, there are two 
possible derangements {2, 0, 1} and {1, 2, 0}
"""

def countDer(n):
	if n in [1, 2]:
		return n-1
	a = 0
	b = 1
	for i in range(3, n + 1):
		cur = (i-1)*(a+b)
		a = b
		b = cur
	return b

n = 4
print("Count of Derangements is ", countDer(n))
```

## [Maximum profit by buying and selling a share at most twice [ IMP ]](https://www.geeksforgeeks.org/maximum-profit-by-buying-and-selling-a-share-at-most-twice/)

```python
"""   
In daily share trading, a buyer buys shares in the morning and sells them on the same day. If the trader is allowed to make at most 2 transactions in a day, whereas the second transaction can only start after the first one is complete (Buy->sell->Buy->sell). Given stock prices throughout the day, find out the maximum profit that a share trader could have made.

Examples: 

Input:   price[] = {10, 22, 5, 75, 65, 80}
Output:  87
Trader earns 87 as sum of 12, 75 
Buy at 10, sell at 22, 
Buy at 5 and sell at 80
Input:   price[] = {2, 30, 15, 10, 8, 25, 80}
Output:  100
Trader earns 100 as sum of 28 and 72
Buy at price 2, sell at 30, buy at 8 and sell at 80
Input:   price[] = {100, 30, 15, 10, 8, 25, 80};
Output:  72
Buy at price 8 and sell at 80.
Input:   price[] = {90, 80, 70, 60, 50}
Output:  0
Not possible to earn.
"""

import sys
def maxtwobuysell(arr, size):
	first_buy = -sys.maxsize;
	first_sell = 0;
	second_buy = -sys.maxsize;
	second_sell = 0;

	for i in range(size):
		first_buy = max(first_buy, -arr[i]);
		first_sell = max(first_sell, first_buy + arr[i]);
		second_buy = max(second_buy, first_sell - arr[i]);
		second_sell = max(second_sell, second_buy + arr[i]);
	return second_sell;

arr = [ 2, 30, 15, 10, 8, 25, 80 ];
size = len(arr);
print(maxtwobuysell(arr, size));
```

## [Optimal Strategy for a Game](https://practice.geeksforgeeks.org/problems/optimal-strategy-for-a-game/0)

```python
"""   
Consider a row of n coins of values v1 . . . vn, where n is even. We play a game against an opponent by alternating turns. In each turn, a player selects either the first or last coin from the row, removes it from the row permanently, and receives the value of the coin. Determine the maximum possible amount of money we can definitely win if we move first.
Note: The opponent is as clever as the user.

Let us understand the problem with few examples:  

5, 3, 7, 10 : The user collects maximum value as 15(10 + 5)
8, 15, 3, 7 : The user collects maximum value as 22(7 + 15)
Does choosing the best at each move gives an optimal solution? No. 
In the second example, this is how the game can be finished:

> User chooses 8. 
> Opponent chooses 15. 
> User chooses 7. 
> Opponent chooses 3. 
Total value collected by user is 15(8 + 7)
> User chooses 7. 
> Opponent chooses 8. 
> User chooses 15. 
> Opponent chooses 3. 
Total value collected by user is 22(7 + 15)
So if the user follows the second game state, the maximum value can be collected although the first move is not the best. 
"""
def optimalStrategyOfGame(arr, n):
	memo = {}
	# recursive top down memoized solution
	def solve(i, j):
		if i > j or i >= n or j < 0:
			return 0

		k = (i, j)
		if k in memo:
			return memo[k]

		# if the user chooses ith coin, the opponent can choose from i+1th or jth coin.
		# if he chooses i+1th coin, user is left with [i+2,j] range.
		# if opp chooses jth coin, then user is left with [i+1,j-1] range to choose from.
		# Also opponent tries to choose in such a way that the user has minimum value left.
		option1 = arr[i] + min(solve(i+2, j), solve(i+1, j-1))

		# if user chooses jth coin, opponent can choose ith coin or j-1th coin.
		# if opp chooses ith coin, user can choose in range [i+1,j-1].
		# if opp chooses j-1th coin, user can choose in range [i,j-2].
		option2 = arr[j] + min(solve(i+1, j-1), solve(i, j-2))

		# since the user wants to get maximum money
		memo[k] = max(option1, option2)
		return memo[k]

	return solve(0, n-1)

arr1 = [8, 15, 3, 7]
n = len(arr1)
print(optimalStrategyOfGame(arr1, n))
 
arr2 = [2, 2, 2, 2]
n = len(arr2)
print(optimalStrategyOfGame(arr2, n))
 
arr3 = [20, 30, 2, 2, 2, 10]
n = len(arr3)
print(optimalStrategyOfGame(arr3, n))
```

## [Optimal Binary Search Tree](https://www.geeksforgeeks.org/optimal-binary-search-tree-dp-24/)

```python
"""   
Given a sorted array key [0.. n-1] of search keys and an array freq[0.. n-1] of frequency counts, where freq[i] is the number of searches for keys[i]. Construct a binary search tree of all keys such that the total cost of all the searches is as small as possible.
Let us first define the cost of a BST. The cost of a BST node is the level of that node multiplied by its frequency. The level of the root is 1.

Examples:  

Input:  keys[] = {10, 12}, freq[] = {34, 50}
There can be following two possible BSTs 
        10                       12
          \                     / 
           12                 10
          I                     II
Frequency of searches of 10 and 12 are 34 and 50 respectively.
The cost of tree I is 34*1 + 50*2 = 134
The cost of tree II is 50*1 + 34*2 = 118 
"""

def optCost(freq, i, j):
	if j < i:	 # no elements in this subarray
		return 0
	if j == i:	 # one element in this subarray
		return freq[i]
	
	# Get sum of freq[i], freq[i+1], ... freq[j]
	fsum = Sum(freq, i, j)
	
	# Initialize minimum value
	Min = float('inf')
	
	# One by one consider all elements as root and recursively find cost of the BST, compare the cost with min and update min if needed
	for r in range(i, j + 1):
		cost = (optCost(freq, i, r - 1) +
				optCost(freq, r + 1, j))
		if cost < Min:
			Min = cost
	
	# Return minimum value
	return Min + fsum

# The main function that calculates minimum cost of a Binary Search Tree. It mainly uses optCost() to find the optimal cost.
def optimalSearchTree(keys, freq, n):
	
	# Here array keys[] is assumed to be sorted in increasing order. If keys[]
	# is not sorted, then add code to sort keys, and rearrange freq[] accordingly.
	return optCost(freq, 0, n - 1)

# A utility function to get sum of array elements freq[i] to freq[j]
def Sum(freq, i, j):
	return sum(freq[k] for k in range(i, j + 1))

if __name__ == '__main__':
	keys = [10, 12, 20]
	freq = [34, 8, 50]
	n = len(keys)
	print("Cost of Optimal BST is",
		optimalSearchTree(keys, freq, n))
        
```

## [Palindrome PartitioningProblem](https://practice.geeksforgeeks.org/problems/palindromic-patitioning4845/1)

```python
"""   
Input : str = “geek” 
Output : 2 
We need to make minimum 2 cuts, i.e., “g ee k”
Input : str = “aaaa” 
Output : 0 
The string is already a palindrome.
Input : str = “abcde” 
Output : 4
Input : str = “abbac” 
Output : 1 

"""

def isPalindrome(x):
	return x == x[::-1]

def minPalPartion(string, i, j):
	if i >= j or isPalindrome(string[i:j + 1]):
		return 0
	ans = float('inf')
	for k in range(i, j):
		count = (
			1 + minPalPartion(string, i, k)
			+ minPalPartion(string, k + 1, j)
		)
		ans = min(ans, count)
	return ans

string = "ababbbabbababa"
print("Min cuts needed for Palindrome Partitioning is ", minPalPartion(string, 0, len(string) - 1))
```

## [Word Wrap Problem](https://practice.geeksforgeeks.org/problems/word-wrap/0)

```python
"""   
Given a sequence of words, and a limit on the number of characters that can be put in one line (line width). Put line breaks in the given sequence such that the lines are printed neatly. Assume that the length of each word is smaller than the line width.
The word processors like MS Word do task of placing line breaks. The idea is to have balanced lines. In other words, not have few lines with lots of extra spaces and some lines with small amount of extra spaces. 
 

The extra spaces includes spaces put at the end of every line except the last one.  
The problem is to minimize the following total cost.
 Cost of a line = (Number of extra spaces in the line)^3
 Total Cost = Sum of costs for all lines

For example, consider the following string and line width M = 15
 "Geeks for Geeks presents word wrap problem" 
     
Following is the optimized arrangement of words in 3 lines
Geeks for Geeks
presents word
wrap problem 

The total extra spaces in line 1, line 2 and line 3 are 0, 2 and 3 respectively. 
So optimal value of total cost is 0 + 2*2*2 + 3*3*3 = 35
Please note that the total cost function is not sum of extra spaces, but sum of cubes (or square is also used) of extra spaces. 
"""

# A Dynamic programming solution
# for Word Wrap Problem

# A utility function to print
# the solution
# l[] represents lengths of different
# words in input sequence. For example,
# l[] = {3, 2, 2, 5} is for a sentence
# like "aaa bb cc ddddd". n is size of
# l[] and M is line width (maximum no.
# of characters that can fit in a line)
INF = 2147483647
def printSolution(p, n):
	k = 0
	if p[n] == 1:
		k = 1
	else:
		k = printSolution(p, p[n] - 1) + 1
	print('Line number ', k, ': From word no. ',
								p[n], 'to ', n)
	return k

def solveWordWrap(l, n, M):
	# For simplicity, 1 extra space is used in all below arrays
	# extras[i][j] will have number of extra spaces if words from i to j are put in a single line
	extras = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

	# lc[i][j] will have cost of a line which has words from i to j
	lc = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

	# c[i] will have total cost of optimal arrangement of words from 1 to i
	c = [0 for _ in range(n + 1)]

	# p[] is used to print the solution.
	p = [0 for _ in range(n + 1)]

	# calculate extra spaces in a single line. The value extra[i][j] indicates
	# extra spaces if words from word number i to j are placed in a single line
	for i in range(n + 1):
		extras[i][i] = M - l[i - 1]
		for j in range(i + 1, n + 1):
			extras[i][j] = (extras[i][j - 1] -
									l[j - 1] - 1)

	# Calculate line cost corresponding to the above calculated extra
	# spaces. The value lc[i][j] indicates cost of putting words from word number i to j in a single line
	for i in range(n + 1):
		for j in range(i, n + 1):
			if extras[i][j] < 0:
				lc[i][j] = INF;
			elif j == n:
				lc[i][j] = 0
			else:
				lc[i][j] = (extras[i][j] *
							extras[i][j])

	# Calculate minimum cost and find minimum cost arrangement. The value
	# c[j] indicates optimized cost to arrange words from word number 1 to j.
	c[0] = 0
	for j in range(1, n + 1):
		c[j] = INF
		for i in range(1, j + 1):
			if (c[i - 1] != INF and
				lc[i][j] != INF and
				((c[i - 1] + lc[i][j]) < c[j])):
				c[j] = c[i-1] + lc[i][j]
				p[j] = i
	printSolution(p, n)

l = [3, 2, 2, 5]
n = len(l)
M = 6
solveWordWrap(l, n, M)
```

## [Mobile Numeric Keypad Problem [ IMP ]](https://practice.geeksforgeeks.org/problems/mobile-numeric-keypad5456/1)

```python
"""   
Given the mobile numeric keypad. You can only press buttons that are up, left, right or down to the current button. You are not allowed to press bottom row corner buttons (i.e. * and # ).

Mobile-keypad

Given a number N, find out the number of possible numbers of given length. 

Examples: 

For N=1, number of possible numbers would be 10 (0, 1, 2, 3, …., 9) 
For N=2, number of possible numbers would be 36 
Possible numbers: 00,08 11,12,14 22,21,23,25 and so on. 
If we start with 0, valid numbers will be 00, 08 (count: 2) 
If we start with 1, valid numbers will be 11, 12, 14 (count: 3) 
If we start with 2, valid numbers will be 22, 21, 23,25 (count: 4) 
If we start with 3, valid numbers will be 33, 32, 36 (count: 3) 
If we start with 4, valid numbers will be 44,41,45,47 (count: 4) 
If we start with 5, valid numbers will be 55,54,52,56,58 (count: 5) 
.................................... 
....................................
We need to print the count of possible numbers.
"""

# left, up, right, down move from current location
row = [0, 0, -1, 0, 1]
col = [0, -1, 0, 1, 0]

# Returns count of numbers of length n starting from key position (i, j) in a numeric keyboard.
def getCountUtil(keypad, i, j, n):
	if (keypad == None or n <= 0):
		return 0

	# From a given key, only one number is possible of length 1
	if (n == 1):
		return 1
	k = 0
	move = 0
	ro = 0
	co = 0
	totalCount = 0

	# move left, up, right, down from current location and if
	# new location is valid, then get number count of length
	# (n-1) from that new position and add in count obtained so far
	for move in range(5):
		ro = i + row[move]
		co = j + col[move]
		if (ro >= 0 and ro <= 3 and co >= 0 and co <= 2 and
				keypad[ro][co] != '*' and keypad[ro][co] != '#'):
			totalCount += getCountUtil(keypad, ro, co, n - 1)
	return totalCount

# Return count of all possible numbers of length n in a given numeric keyboard
def getCount(keypad, n):
	if keypad is None or n <= 0:
		return 0
	if (n == 1):
		return 10
	i = 0
	j = 0
	totalCount = 0
	for i in range(4): # Loop on keypad row
		for j in range(3): # Loop on keypad column
			# Process for 0 to 9 digits
			if (keypad[i][j] != '*' and keypad[i][j] != '#'):
			# Get count when number is starting from key position (i, j) and add in count obtained so far
				totalCount += getCountUtil(keypad, i, j, n)
	return totalCount

keypad = [['1', '2', '3'],
		['4', '5', '6'],
		['7', '8', '9'],
		['*', '0', '#']]
print("Count for numbers of length 1:", getCount(keypad, 1))
print("Count for numbers of length 2:", getCount(keypad, 2))
print("Count for numbers of length 3:", getCount(keypad, 3))
print("Count for numbers of length 4:", getCount(keypad, 4))
print("Count for numbers of length 5:", getCount(keypad, 5))
```

## [Boolean Parenthesization Problem](https://practice.geeksforgeeks.org/problems/boolean-parenthesization/0)

```python
"""   
Given a boolean expression with the following symbols. 

Symbols
    'T' ---> true 
    'F' ---> false 
And following operators filled between symbols 

Operators
    &   ---> boolean AND
    |   ---> boolean OR
    ^   ---> boolean XOR 
Count the number of ways we can parenthesize the expression so that the value of expression evaluates to true. 
Let the input be in form of two arrays one contains the symbols (T and F) in order and the other contains operators (&, | and ^}

Examples: 

Input: symbol[]    = {T, F, T}
       operator[]  = {^, &}
Output: 2
The given expression is "T ^ F & T", it evaluates true
in two ways "((T ^ F) & T)" and "(T ^ (F & T))"

Input: symbol[]    = {T, F, F}
       operator[]  = {^, |}
Output: 2
The given expression is "T ^ F | F", it evaluates true
in two ways "( (T ^ F) | F )" and "( T ^ (F | F) )". 

Input: symbol[]    = {T, T, F, T}
       operator[]  = {|, &, ^}
"""

def countParenth(symb, oper, n):
	F = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
	T = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

	# Fill diagonal entries first
	# All diagonal entries in T[i][i] are 1 if symbol[i] is T (true). Similarly, all F[i][i] entries are 1 if
	# symbol[i] is F (False)
	for i in range(n):
		F[i][i] = 1 if symb[i] == 'F' else 0
		T[i][i] = 1 if symb[i] == 'T' else 0

	# Now fill T[i][i+1], T[i][i+2],
	# T[i][i+3]... in order And F[i][i+1], F[i][i+2], F[i][i+3]... in order
	for gap in range(1, n):
		for i, j in enumerate(range(gap, n)):
			T[i][j] = F[i][j] = 0
			for g in range(gap):

				# Find place of parenthesization using current value of gap
				k = i + g

				# Store Total[i][k] and Total[k+1][j]
				tik = T[i][k] + F[i][k]
				tkj = T[k + 1][j] + F[k + 1][j]

				# Follow the recursive formulas according to the current operator
				if oper[k] == '&':
					T[i][j] += T[i][k] * T[k + 1][j]
					F[i][j] += (tik * tkj - T[i][k] *
								T[k + 1][j])
				if oper[k] == '|':
					F[i][j] += F[i][k] * F[k + 1][j]
					T[i][j] += (tik * tkj - F[i][k] *
								F[k + 1][j])
				if oper[k] == '^':
					T[i][j] += (F[i][k] * T[k + 1][j] +
								T[i][k] * F[k + 1][j])
					F[i][j] += (T[i][k] * T[k + 1][j] +
								F[i][k] * F[k + 1][j])
	return T[0][n - 1]


symbols = "TTFT"
operators = "|&^"
n = len(symbols)

# There are 4 ways
# ((T|T)&(F^T)), (T|(T&(F^T))),
# (((T|T)&F)^T) and (T|((T&F)^T))
print(countParenth(symbols, operators, n))
```

## [Largest rectangular sub-matrix whose sum is 0](https://www.geeksforgeeks.org/largest-rectangular-sub-matrix-whose-sum-0/)

```python
"""
Given a 2D matrix, find the number non-empty sub matrices, such that the sum of the elements inside the sub matrix is equal to 0. (note:  elements might be negative).
"""
import itertools
def solve(A):
    if not A or not A[0]: return 0  # SC & guard
    cols = len(A[0]) + 1            # pad left to guard [c - 1]
    A = [[0] + row for row in A]
    for row, c in itertools.product(A, range(2, cols)):
        row[c] += row[c - 1]
    zeros = 0
    for c1 in range(cols - 1):                  # each pair of (c, c2]
        for c2 in range(c1 + 1, cols):
            sofar = 0
            seen = {0: 1}                   # {sum : cnt}, dict to cnt dups
            for row in A:                   # scan top-down as 1D sum 0
                sofar += row[c2] - row[c1]
                if sofar-0 in seen:
                    zeros += seen[sofar-0]
                if sofar in seen:
                    seen[sofar] += 1
                else: seen[sofar] = 1
    return zeros

A=[[-8, 5,  7],
[3 , 7, -8],
[5 ,-8,  9]
]
print(solve(A))
```

## [Maximum sum rectangle in a 2D matrix](https://practice.geeksforgeeks.org/problems/maximum-sum-rectangle/0)

```python
# Implementation of Kadane's algorithm for 1D array. The function returns the maximum sum and stores starting
#  and ending indexes of the maximum sum subarray at addresses pointed by start and finish pointers respectively.
def kadane(arr, start, finish, n):
	Sum = 0
	maxSum = -999999999999
	i = None

	# Just some initial value to check for all negative values case
	finish[0] = -1

	# local variable
	local_start = 0

	for i in range(n):
		Sum += arr[i]
		if Sum < 0:
			Sum = 0
			local_start = i + 1
		elif Sum > maxSum:
			maxSum = Sum
			start[0] = local_start
			finish[0] = i

	# There is at-least one non-negative number
	if finish[0] != -1:
		return maxSum

	# Special Case: When all numbers in arr[] are negative
	maxSum = arr[0]
	start[0] = finish[0] = 0

	# Find the maximum element in array
	for i in range(1, n):
		if arr[i] > maxSum:
			maxSum = arr[i]
			start[0] = finish[0] = i
	return maxSum

def findMaxSum(M):
	global ROW, COL

	# Variables to store the final output
	maxSum, finalLeft = -999999999999, None
	finalRight, finalTop, finalBottom = None, None, None
	left, right, i = None, None, None

	temp = [None] * ROW
	Sum = 0
	start = [0]
	finish = [0]

	# Set the left column
	for left in range(COL):

		# Initialize all elements of temp as 0
		temp = [0] * ROW

		# Set the right column for the left column set by outer loop
		for right in range(left, COL):

			# Calculate sum between current left and right for every row 'i'
			for i in range(ROW):
				temp[i] += M[i][right]

			# Find the maximum sum subarray in temp[]. The kadane() function also
			# sets values of start and finish So 'sum' is sum of rectangle between
			# (start, left) and (finish, right) which is the maximum sum with boundary columns
			# strictly as left and right.
			Sum = kadane(temp, start, finish, ROW)

			# Compare sum with maximum sum so far. If sum is more, then update maxSum and other output values
			if Sum > maxSum:
				maxSum = Sum
				finalLeft = left
				finalRight = right
				finalTop = start[0]
				finalBottom = finish[0]

	# Prfinal values
	print("(Top, Left)", "(", finalTop,
		finalLeft, ")")
	print("(Bottom, Right)", "(", finalBottom,
		finalRight, ")")
	print("Max sum is:", maxSum)

ROW = 4
COL = 5
M = [[1, 2, -1, -4, -20],
	[-8, -3, 4, 2, 1],
	[3, 8, 10, 1, 3],
	[-4, -1, 1, 7, -6]]
findMaxSum(M)
```

## [Maximum profit by buying and selling a share at most k times](https://practice.geeksforgeeks.org/problems/maximum-profit4657/1)

```python
"""
Input:  
Price = [10, 22, 5, 75, 65, 80]
    K = 2
Output:  87
Trader earns 87 as sum of 12 and 75
Buy at price 10, sell at 22, buy at 
5 and sell at 80

Input:  
Price = [12, 14, 17, 10, 14, 13, 12, 15]
    K = 3
Output:  12
Trader earns 12 as the sum of 5, 4 and 3
Buy at price 12, sell at 17, buy at 10 
and sell at 14 and buy at 12 and sell
at 15
 
Input:  
Price = [100, 30, 15, 10, 8, 25, 80]
    K = 3
Output:  72
Only one transaction. Buy at price 8 
and sell at 80.

Input:  
Price = [90, 80, 70, 60, 50]
    K = 1
Output:  0
Not possible to earn. 
"""
def maxProfit(prices, n, k):
	profit = [[0 for _ in range(k + 1)] for _ in range(n)]
	# Profit is zero for the first day and for zero transactions
	for i in range(1, n):
		for j in range(1, k + 1):
			max_so_far = 0
			for l in range(i):
				max_so_far = max(max_so_far, prices[i] -
							prices[l] + profit[l][j - 1])
			profit[i][j] = max(profit[i - 1][j], max_so_far)
	return profit[n - 1][k]

k = 2
prices = [10, 22, 5, 75, 65, 80]
n = len(prices)
print("Maximum profit is:",
	maxProfit(prices, n, k))
```

## [Find if a string is interleaved of two other strings](https://practice.geeksforgeeks.org/problems/interleaved-strings/1)

```python
"""
Given three strings A, B and C. Write a function that checks whether C is an interleaving of A and B. C is said to be interleaving A and B, if it contains all and only characters of A and B and order of all characters in individual strings is preserved. 

Example: 

Input: strings: "XXXXZY", "XXY", "XXZ"
Output: XXXXZY is interleaved of XXY and XXZ
The string XXXXZY can be made by 
interleaving XXY and XXZ
String:    XXXXZY
String 1:    XX Y
String 2:  XX  Z

Input: strings: "XXY", "YX", "X"
Output: XXY is not interleaved of YX and X
XXY cannot be formed by interleaving YX and X.
The strings that can be formed are YXX and XYX
"""

dp = [[0]*101]*101
def dfs(i, j, A, B, C):
	
	# If path has already been calculated from this index then return calculated value.
	if(dp[i][j]!=-1):
		return dp[i][j]
		
	# If we reach the destination return 1
	n,m=len(A),len(B)
	if(i==n and j==m):
		return 1
	
	# If C[i+j] matches with both A[i] and B[j] we explore both the paths
	if (i<n and A[i]==C[i + j] and j<m and B[j]==C[i + j]):
		# go down and store the calculated value in x
		# and go right and store the calculated value in y.
		x = dfs(i + 1, j, A, B, C)
		y = dfs(i, j + 1, A, B, C)
		
		# return the best of both.
		dp[i][j] = x|y
		return dp[i][j]
	
	# If C[i+j] matches with A[i].
	if (i < n and A[i] == C[i + j]):
		# go down
		x = dfs(i + 1, j, A, B, C)
		
		# Return the calculated value.
		dp[i][j] = x
		return dp[i][j]
	
	# If C[i+j] matches with B[j].
	if (j < m and B[j] == C[i + j]):
		y = dfs(i, j + 1, A, B, C)
		
		# Return the calculated value.
		dp[i][j] = y
		return dp[i][j]
	
	# if nothing matches we return 0
	dp[i][j] = 0
	return dp[i][j]

# The main function that returns true if C is
# an interleaving of A and B, otherwise false.
def isInterleaved(A, B, C):

	# Storing the length in n,m
	n = len(A)
	m = len(B)

	# C can be an interleaving of A and B only of the sum
	# of lengths of A & B is equal to the length of C.
	if((n+m)!=len(C)):
		return 0
	# initializing dp array with -1
	for i in range(n+1):
		for j in range(m+1):
			dp[i][j]=-1
	# calling and returning the answer
	return dfs(0,0,A,B,C)
	
def test(A, B, C):
	if (isInterleaved(A, B, C)):
		print(C, "is interleaved of", A, "and", B)
	else:
		print(C, "is not interleaved of", A, "and", B)

test("XXY", "XXZ", "XXZXXXY")
test("XY", "WZ", "WZXY")
test("XY", "X", "XXY")
test("YX", "X", "XXY")
test("XXY", "XXZ", "XXXXZY")
test("ACA", "DAS", "DAACSA")
```

# Graph

## Implement Graph

```python
class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]
        for (src, dest) in edges:
            self.adjList[src].append(dest)
 
 
def printGraph(graph):
    for src in range(len(graph.adjList)):
        for dest in graph.adjList[src]:
            print(f'({src} —> {dest}) ', end='')
        print()
 
edges = [(0, 1), (1, 2), (2, 0), (2, 1), (3, 2), (4, 5), (5, 4)]
n = 6
graph = Graph(edges, n)
printGraph(graph)
```

## Implement Weighted Graph

```python
class Graph:
    def __init__(self, edges, n):
        self.adjList = [None] * n
        for i in range(n):
            self.adjList[i] = []
        for (src, dest, weight) in edges:
            self.adjList[src].append((dest, weight))
 
 
def printGraph(graph):
    for src in range(len(graph.adjList)):
        for (dest, weight) in graph.adjList[src]:
            print(f'({src} —> {dest}, {weight}) ', end='')
        print()
 
 
# Input: Edges in a weighted digraph (as per the above diagram)
# Edge (x, y, w) represents an edge from `x` to `y` having weight `w`
edges = [(0, 1, 6), (1, 2, 7), (2, 0, 5), (2, 1, 4), (3, 2, 10),
        (4, 5, 1), (5, 4, 3)]
n = 6
graph = Graph(edges, n)
printGraph(graph)
```

## [Implement BFS algorithm](https://practice.geeksforgeeks.org/problems/bfs-traversal-of-graph/1)

```python
from collections import deque

class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)


def BFS(graph, v, discovered):
    q = deque()
    discovered[v] = True
    q.append(v)
    while q:
        v = q.popleft()
        print(v, end=' ')
        for u in graph.adjList[v]:
            if not discovered[u]:
                discovered[u] = True
                q.append(u)

edges = [
    (1, 2), (1, 3), (1, 4), (2, 5), (2, 6), (5, 9),
    (5, 10), (4, 7), (4, 8), (7, 11), (7, 12)
    # vertex 0, 13, and 14 are single nodes
]
n = 15
graph = Graph(edges, n)
discovered = [False] * n
for i in range(n):
    if not discovered[i]:
        BFS(graph, i, discovered)

```

## [Implement DFS Algo](https://practice.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1)

```python
from collections import deque
class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)
 
def iterativeDFS(graph, v, discovered):
    stack = deque()
    stack.append(v)
    while stack:
        v = stack.pop()
        if discovered[v]:
            continue
        discovered[v] = True
        print(v, end=' ')
        adjList = graph.adjList[v]
        for i in reversed(range(len(adjList))):
            u = adjList[i]
            if not discovered[u]:
                stack.append(u)
 
 
edges = [
    # Notice that node 0 is unconnected
    (1, 2), (1, 7), (1, 8), (2, 3), (2, 6), (3, 4),
    (3, 5), (8, 9), (8, 12), (9, 10), (9, 11)
    # (6, 9) introduces a cycle
]
n = 13
graph = Graph(edges, n)
discovered = [False] * n
for i in range(n):
    if not discovered[i]:
        iterativeDFS(graph, i, discovered)
```

## [Detect Cycle in Directed Graph using BFS/DFS Algo](https://practice.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1)

```python
class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]
        for (src, dest) in edges:
            self.adjList[src].append(dest)
 
 
# Perform DFS on the graph and set the departure time of all vertices of the graph
def DFS(graph, v, discovered, departure, time):
 
    # mark the current node as discovered
    discovered[v] = True
 
    # do for every edge (v, u)
    for u in graph.adjList[v]:
        # if `u` is not yet discovered
        if not discovered[u]:
            time = DFS(graph, u, discovered, departure, time)
 
    # ready to backtrack set departure time of vertex `v`
    departure[v] = time
    time = time + 1
 
    return time
 
 
# Returns true if the given directed graph is DAG
def isDAG(graph, n):
 
    # keep track of whether a vertex is discovered or not
    discovered = [False] * n
 
    # keep track of the departure time of a vertex in DFS
    departure = [None] * n
 
    time = 0
 
    # Perform DFS traversal from all undiscovered vertices to visit all connected components of a graph
    for i in range(n):
        if not discovered[i]:
            time = DFS(graph, i, discovered, departure, time)
 
    # check if the given directed graph is DAG or not
    for u in range(n):
 
        # check if (u, v) forms a back-edge.
        for v in graph.adjList[u]:
 
            # If the departure time of vertex `v` is greater than equal
            # to the departure time of `u`, they form a back edge.
 
            # Note that `departure[u]` will be equal to `departure[v]`
            # only if `u = v`, i.e., vertex contain an edge to itself
            if departure[u] <= departure[v]:
                return False
 
    # no back edges
    return True
 
 

# List of graph edges as per the above diagram
edges = [(0, 1), (0, 3), (1, 2), (1, 3), (3, 2), (3, 4), (3, 0), (5, 6), (6, 3)]
# total number of nodes in the graph (labelled from 0 to 6)
n = 7
graph = Graph(edges, n)
if isDAG(graph, n):
    print('Does not contain a Cycle')
else:
    print('Contains a Cycle')
 
```

## [Detect Cycle in UnDirected Graph using BFS/DFS Algo](https://practice.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1)

```python
class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)
 
 
# Function to perform DFS traversal on the graph on a graph
def DFS(graph, v, discovered, parent=-1):
 
    # mark the current node as discovered
    discovered[v] = True
 
    # do for every edge (v, w)
    for w in graph.adjList[v]:
 
        # if `w` is not discovered
        if not discovered[w]:
            if DFS(graph, w, discovered, v):
                return True
 
        # if `w` is discovered, and `w` is not a parent
        elif w != parent:
            # we found a back-edge (cycle)
            return True
 
    # No back-edges were found in the graph
    return False
 
 

edges = [
    (0, 1), (0, 6), (0, 7), (1, 2), (1, 5), (2, 3),
    (2, 4), (7, 8), (7, 11), (8, 9), (8, 10), (10, 11)
    # edge (10, 11) introduces a cycle in the graph
]

# total number of nodes in the graph (0 to 11)
n = 12

graph = Graph(edges, n)
discovered = [False] * n
if DFS(graph, 0, discovered):
    print('The graph contains a cycle')
else:
    print('The graph doesn\'t contain any cycle')
```


## [Minimum Step by Knight](https://practice.geeksforgeeks.org/problems/steps-by-knight/0)

```python
"""Given a chessboard, find the shortest distance (minimum number of steps) taken by a knight to reach a given destination from a given source.

For example,

Input:
 
N = 8 (8 × 8 board)
Source = (7, 0)
Destination = (0, 7)
 
Output: Minimum number of steps required is 6
"""

import sys
from collections import deque
 
 
class Node:
    # (x, y) represents chessboard coordinates `dist` represents its minimum distance from the source
    def __init__(self, x, y, dist=0):
        self.x = x
        self.y = y
        self.dist = dist
 
    # As we are using `Node` as a key in a dictionary, we need to override the `__hash__()` and `__eq__()` function
    def __hash__(self):
        return hash((self.x, self.y, self.dist))
 
    def __eq__(self, other):
        return (self.x, self.y, self.dist) == (other.x, other.y, other.dist)
 
 
# Below lists detail all eight possible movements for a knight
row = [2, 2, -2, -2, 1, 1, -1, -1]
col = [-1, 1, 1, -1, 2, -2, 2, -2]
 
 
# Check if (x, y) is valid chessboard coordinates.
# Note that a knight cannot go out of the chessboard
def isValid(x, y, N):
    return x >= 0 and y >= 0 and x < N and y < N
 
 
# Find the minimum number of steps taken by the knight
# from the source to reach the destination using BFS
def findShortestDistance(src, dest, N):

    # set to check if the matrix cell is visited before or not
    visited = set()
 
    # create a queue and enqueue the first node
    q = deque()
    q.append(src)
 
    # loop till queue is empty
    while q:
 
        # dequeue front node and process it
        node = q.popleft()
 
        x = node.x
        y = node.y
        dist = node.dist
 
        # if the destination is reached, return distance
        if x == dest.x and y == dest.y:
            return dist
 
        # skip if the location is visited before
        if node not in visited:
            # mark the current node as visited
            visited.add(node)
 
            # check for all eight possible movements for a knight
            # and enqueue each valid movement
            for i in range(len(row)):
                # get the knight's valid position from the current position on
                # the chessboard and enqueue it with +1 distance
                x1 = x + row[i]
                y1 = y + col[i]
 
                if isValid(x1, y1, N):
                    q.append(Node(x1, y1, dist + 1))
 
    # return infinity if the path is not possible
    return sys.maxsize


N = 8               # N x N matrix
src = Node(0, 7)    # source coordinates
dest = Node(7, 0)   # destination coordinates
print("The minimum number of steps required is",findShortestDistance(src, dest, N))
 
```

## [flood fill algo](https://leetcode.com/problems/flood-fill/)

```python
"""Flood fill (also known as seed fill) is an algorithm that determines the area connected to a given node in a multi-dimensional array.
"""

# Below lists detail all eight possible movements
row = [-1, -1, -1, 0, 0, 1, 1, 1]
col = [-1, 0, 1, -1, 1, -1, 0, 1]
 
 
# check if it is possible to go to pixel (x, y) from the
# current pixel. The function returns false if the pixel
# has a different color, or it's not a valid pixel
def isSafe(mat, x, y, target):
    return 0 <= x < len(mat) and 0 <= y < len(mat[0]) and mat[x][y] == target
 
 
# Flood fill using DFS
def floodfill(mat, x, y, replacement):
 
    # base case
    if not mat or not len(mat):
        return
 
    # get the target color
    target = mat[x][y]
 
    # target color is same as replacement
    if target == replacement:
        return
 
    # replace the current pixel color with that of replacement
    mat[x][y] = replacement
 
    # process all eight adjacent pixels of the current pixel and
    # recur for each valid pixel
    for k in range(len(row)):
 
        # if the adjacent pixel at position (x + row[k], y + col[k]) is
        # a valid pixel and has the same color as that of the current pixel
        if isSafe(mat, x + row[k], y + col[k], target):
            floodfill(mat, x + row[k], y + col[k], replacement)
 
 

mat = [
        ['Y', 'Y', 'Y', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],
        ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'G', 'X', 'X', 'X'],
        ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'X', 'X', 'X'],
        ['W', 'W', 'W', 'W', 'W', 'G', 'G', 'G', 'G', 'X'],
        ['W', 'R', 'R', 'R', 'R', 'R', 'G', 'X', 'X', 'X'],
        ['W', 'W', 'W', 'R', 'R', 'G', 'G', 'X', 'X', 'X'],
        ['W', 'B', 'W', 'R', 'R', 'R', 'R', 'R', 'R', 'X'],
        ['W', 'B', 'B', 'B', 'B', 'R', 'R', 'X', 'X', 'X'],
        ['W', 'B', 'B', 'X', 'B', 'B', 'B', 'B', 'X', 'X'],
        ['W', 'B', 'B', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
    ]

# start node
x, y = (3, 9)   # having a target color `X`

# replacement color
replacement = 'C'

# replace the target color with a replacement color using DFS
floodfill(mat, x, y, replacement)

# print the colors after replacement
for r in mat:
    print(r)
```

## [Clone a graph](https://leetcode.com/problems/clone-graph/)

```python
TODO
```

## [Making wired Connections](https://leetcode.com/problems/number-of-operations-to-make-network-connected/)

```python
"""There are n computers numbered from 0 to n-1 connected by ethernet cables connections forming a network where connections[i] = [a, b] represents a connection between computers a and b. Any computer can reach any other computer directly or indirectly through the network.

Given an initial computer network connections. You can extract certain cables between two directly connected computers, and place them between any pair of disconnected computers to make them directly connected. Return the minimum number of times you need to do this in order to make all the computers connected. If it’s not possible, return -1.

Example 1:

Input: n = 4, connections = [[0,1],[0,2],[1,2]]
Output: 1
Explanation: Remove cable between computer 1 and 2 and place between computers 1 and 3.
Example 2:

Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
Output: 2
Example 3:

Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
Output: -1
Explanation: There are not enough cables.
Example 4:

Input: n = 5, connections = [[0,1],[0,2],[3,4],[2,3]]
Output: 0
"""

def makeConnected(n, connections):
    uf = {i: i for i in range(n)}

    def find(x):
        uf.setdefault(x, x)
        if uf[x] != x:
            uf[x] = find(uf[x])
        return uf[x]

    def union(a, b):
        uf[find(a)] = find(b)
    if len(connections) < n - 1:
        return -1
    for a, b in connections:
        union(a, b)
    islands = len({find(x) for x in uf})
    return islands - 1
n = 4

connections = [[0,1],[0,2],[1,2]]
print(makeConnected(n, connections))
```

## [word Ladder](https://leetcode.com/problems/word-ladder/)

```python
"""
Given two words (beginWord and endWord), and a dictionary's word list,
find the length of shortest transformation sequence from beginWord to endWord, such that:
(i) Only one letter can be changed at a time, and (ii) each transformed word must exist in
the word list. Note that beginWord is not a transformed word.

EXAMPLES
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
-> 5 (because "hit" -> "hot" -> "dot" -> "dog" -> "cog")

"""

from collections import deque
def ladderLength(beginWord, endWord, wordList):
    """
    :type beginWord: str
    :type endWord: str
    :type wordList: Set[str]
    :rtype: int
    """

    queue = deque()
    queue.append((beginWord, [beginWord]))
    while queue:
        node, path = queue.popleft()
        for next in next_nodes(node, wordList) - set(path):
            if next == endWord:
                return len(path) + 1
            else:
                queue.append((next, path + [next]))
    return 0

def next_nodes(word, word_list):
    to_return = set()
    for w in word_list:
        mismatch_count, w_length = 0, len(w)
        for i in range(w_length):
            if w[i] != word[i]:
                mismatch_count += 1
        if mismatch_count == 1:
            to_return.add(w)
    return to_return

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(ladderLength(beginWord, endWord, wordList))
```

## [Dijkstra algo](https://practice.geeksforgeeks.org/problems/implementing-dijkstra-set-1-adjacency-matrix/1/)

```python
"""
Given a source vertex s from a set of vertices V in a weighted digraph where all its edge weights w(u, v) are non-negative, find the shortest path weights d(s, v) from source s for all vertices v present in the graph    
"""
import sys
from heapq import heappop, heappush
 
class Node:
    def __init__(self, vertex, weight=0):
        self.vertex = vertex
        self.weight = weight
 
    # Override the __lt__() function to make `Node` class work with a min-heap
    def __lt__(self, other):
        return self.weight < other.weight
 
class Graph:
    def __init__(self, edges, n):
        # allocate memory for the adjacency list
        self.adjList = [[] for _ in range(n)]
 
        # add edges to the directed graph
        for (source, dest, weight) in edges:
            self.adjList[source].append((dest, weight))
 
def get_route(prev, i, route):
    if i >= 0:
        get_route(prev, prev[i], route)
        route.append(i)
 

def findShortestPaths(graph, source, n):
 
    # create a min-heap and push source node having distance 0
    pq = []
    heappush(pq, Node(source))
 
    # set initial distance from the source to `v` as infinity
    dist = [sys.maxsize] * n
 
    # distance from the source to itself is zero
    dist[source] = 0
 
    # list to track vertices for which minimum cost is already found
    done = [False] * n
    done[source] = True
 
    # stores predecessor of a vertex (to a print path)
    prev = [-1] * n
 
    # run till min-heap is empty
    while pq:
 
        node = heappop(pq)      # Remove and return the best vertex
        u = node.vertex         # get the vertex number
 
        # do for each neighbor `v` of `u`
        for (v, weight) in graph.adjList[u]:
            if not done[v] and (dist[u] + weight) < dist[v]:        # Relaxation step
                dist[v] = dist[u] + weight
                prev[v] = u
                heappush(pq, Node(v, dist[v]))
 
        # mark vertex `u` as done so it will not get picked up again
        done[u] = True
 
    route = []
    for i in range(n):
        if i != source and dist[i] != sys.maxsize:
            get_route(prev, i, route)
            print(f'Path ({source} —> {i}): Minimum cost = {dist[i]}, Route = {route}')
            route.clear()

# initialize edges as per the above diagram (u, v, w) represent edge from vertex `u` to vertex `v` having weight `w`
edges = [(0, 1, 10), (0, 4, 3), (1, 2, 2), (1, 4, 4), (2, 3, 9), (3, 2, 7),
        (4, 1, 1), (4, 2, 8), (4, 3, 2)]
# total number of nodes in the graph (labelled from 0 to 4)
n = 5
graph = Graph(edges, n)
for source in range(n):
    findShortestPaths(graph, source, n)
```

## [Implement Topological Sort](https://practice.geeksforgeeks.org/problems/topological-sort/1)

```python
"""
Given a Directed Acyclic Graph (DAG), print it in topological order using topological sort algorithm. If the graph has more than one topological ordering, output any of them. Assume valid Directed Acyclic Graph (DAG).

A Topological sort or Topological ordering of a directed graph is a linear ordering of its vertices such that for every directed edge uv from vertex u to vertex v, u comes before v in the ordering. A topological ordering is possible if and only if the graph has no directed cycles, i.e. if the graph is DAG.

"""
# A class to represent a graph object
class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]
        for (src, dest) in edges:
            self.adjList[src].append(dest)
 
 
# Perform DFS on the graph and set the departure time of all vertices of the graph
def DFS(graph, v, discovered, departure, time):
    discovered[v] = True
    time = time + 1
    for u in graph.adjList[v]:
        if not discovered[u]:
            time = DFS(graph, u, discovered, departure, time)
    departure[time] = v
    time = time + 1
    return time
 
 
# Function to perform a topological sort on a given DAG
def doTopologicalSort(graph, n):
 
    # departure[] stores the vertex number using departure time as an index
    departure = [-1] * 2 * n
 
    ''' If we had done it the other way around, i.e., fill the array
        with departure time using vertex number as an index, we would
        need to sort it later '''
 
    # to keep track of whether a vertex is discovered or not
    discovered = [False] * n
    time = 0
 
    # perform DFS on all undiscovered vertices
    for i in range(n):
        if not discovered[i]:
            time = DFS(graph, i, discovered, departure, time)
 
    # Print the vertices in order of their decreasing
    # departure time in DFS, i.e., in topological order
    for i in reversed(range(2*n)):
        if departure[i] != -1:
            print(departure[i], end=' ')
 

# List of graph edges as per the above diagram
edges = [(0, 6), (1, 2), (1, 4), (1, 6), (3, 0), (3, 4), (5, 1), (7, 0), (7, 1)] 
# total number of nodes in the graph (labelled from 0 to 7)
n = 8
graph = Graph(edges, n) 
doTopologicalSort(graph, n)
```

## [Minimum time taken by each job to be completed given by a Directed Acyclic Graph](https://www.geeksforgeeks.org/minimum-time-taken-by-each-job-to-be-completed-given-by-a-directed-acyclic-graph/)

```python
"""
Given a Directed Acyclic Graph having V vertices and E edges, where each edge {U, V} represents the Jobs U and V such that Job V can only be started only after completion of Job U. The task is to determine the minimum time taken by each job to be completed where each Job takes unit time to get completed.   
"""

from collections import defaultdict

class Graph:
	def __init__(self, vertices, edges):
		self.graph = defaultdict(list)
		self.n = vertices
		self.m = edges
		
	# Function to add an edge to graph
	def addEdge(self, u, v):
		self.graph[u].append(v)
	
	# Function to find the minimum time needed by each node to get the task
	def printOrder(self, n, m):
	
		# Create a vector to store indegrees of all vertices. Initialize all indegrees as 0.
		indegree = [0] * (self.n + 1)
		
		# Traverse adjacency lists to fill indegrees of vertices. This step takes O(V + E) time
		for i in self.graph:
			for j in self.graph[i]:
				indegree[j] += 1
				
		# Array to store the time in which the job i can be done
		job = [0] * (self.n + 1)
		
		# Create an queue and enqueue all vertices with indegree 0
		q = []
		
		# Update the time of the jobs who don't require any job to be completed before this job
		for i in range(1, self.n + 1):
			if indegree[i] == 0:
				q.append(i)
				job[i] = 1
				
		# Iterate until queue is empty
		while q:
			
			# Get front element of queue
			cur = q.pop(0)
			
			for adj in self.graph[cur]:
				
				# Decrease in-degree of the current node
				indegree[adj] -= 1
			
				# Push its adjacent elements
				if (indegree[adj] == 0):
					job[adj] = 1 + job[cur]
					q.append(adj)
					
		# Print the time to complete the job
		for i in range(1, n + 1):
			print(job[i], end = " ")
			
		print()

# Given Nodes N and edges M
n = 10
m = 13
g = Graph(n, m)
g.addEdge(1, 3)
g.addEdge(1, 4)
g.addEdge(1, 5)
g.addEdge(2, 3)
g.addEdge(2, 8)
g.addEdge(2, 9)
g.addEdge(3, 6)
g.addEdge(4, 6)
g.addEdge(4, 8)
g.addEdge(5, 8)
g.addEdge(6, 7)
g.addEdge(7, 8)
g.addEdge(8, 10)
g.printOrder(n, m)

```

## [Find whether it is possible to finish all tasks or not from given dependencies](https://www.geeksforgeeks.org/find-whether-it-is-possible-to-finish-all-tasks-or-not-from-given-dependencies/)

```python
"""
There are a total of n tasks you have to pick, labelled from 0 to n-1. Some tasks may have prerequisites, for example to pick task 0 you have to first pick task 1, which is expressed as a pair: [0, 1]
Given the total number of tasks and a list of prerequisite pairs, is it possible for you to finish all tasks?
Examples:
 

Input: 2, [[1, 0]] 
Output: true 
Explanation: There are a total of 2 tasks to pick. To pick task 1 you should have finished task 0. So it is possible.
Input: 2, [[1, 0], [0, 1]] 
Output: false 
Explanation: There are a total of 2 tasks to pick. To pick task 1 you should have finished task 0, and to pick task 0 you should also have finished task 1. So it is impossible.
Input: 3, [[1, 0], [2, 1], [3, 2]] 
Output: true 
Explanation: There are a total of 3 tasks to pick. To pick tasks 1 you should have finished task 0, and to pick task 2 you should have finished task 1 and to pick task 3 you should have finished task 2. So it is possible. 
"""


class Solution:
	
	arr = []
	# parameterized constructor
	def __init__(self,n):
		# Initially, everyone is their own child
		self.arr = list(range(n))

	def makeParent(self,a, b):
		# find parent of b and make it a's parent
		self.arr[a] = self.findParent(b)

	def findParent(self,c):
		# when an independent task is found
		return c if (c == self.arr) else self.findParent(self.arr)

	def isPossible(self,N , prerequisites):
		# traverse through pre-requisites array
		for i in range(len(prerequisites)):
			# check whether given pre-requisite pair already have a common pre-requisite(parent)
			if (self.findParent(prerequisites[i][0]) == self.findParent(prerequisites[i][1])):
			# tasks cannot be completed because there was a cyclic condition in the tasks
				return False
			# make parent-child relation between pre-requisite task and the task dependent on it
			self.makeParent(prerequisites[i][0], prerequisites[i][1])
		# if there was no cycle found, tasks can be completed
		return True
	

prerequisites = [[1, 0], [2, 1], [3, 2]]
ob = Solution(4)
if ob.isPossible(4,prerequisites ):
	print("Yes")
else:
	print("No")
```

## [Find the no. of Islands](https://practice.geeksforgeeks.org/problems/find-the-number-of-islands/1)

```python
"""
Given a boolean 2D matrix, find the number of islands. A group of connected 1s forms an island. For example, the below matrix contains 5 islands

Example: 

Input : mat[][] = {{1, 1, 0, 0, 0},
                   {0, 1, 0, 0, 1},
                   {1, 0, 0, 1, 1},
                   {0, 0, 0, 0, 0},
                   {1, 0, 1, 0, 1}}
Output : 5
"""


# Program to count islands in boolean 2D matrix
class Graph:
	def __init__(self, row, col, graph):
		self.ROW = row
		self.COL = col
		self.graph = graph

	# A utility function to do DFS for a 2D boolean matrix. It only considers the 8 neighbours as adjacent vertices
	def DFS(self, i, j):
		if i < 0 or i >= len(self.graph) or j < 0 or j >= len(self.graph[0]) or self.graph[i][j] != 1:
			return

		# mark it as visited
		self.graph[i][j] = -1

		# Recur for 8 neighbours
		self.DFS(i - 1, j - 1)
		self.DFS(i - 1, j)
		self.DFS(i - 1, j + 1)
		self.DFS(i, j - 1)
		self.DFS(i, j + 1)
		self.DFS(i + 1, j - 1)
		self.DFS(i + 1, j)
		self.DFS(i + 1, j + 1)

	# The main function that returns count of islands in a given boolean 2D matrix
	def countIslands(self):
		# Initialize count as 0 and traverse through the all cells of given matrix
		count = 0
		for i in range(self.ROW):
			for j in range(self.COL):
				# If a cell with value 1 is not visited yet, then new island found
				if self.graph[i][j] == 1:
					# Visit all cells in this island and increment island count
					self.DFS(i, j)
					count += 1

		return count


graph = [
	[1, 1, 0, 0, 0],
	[0, 1, 0, 0, 1],
	[1, 0, 0, 1, 1],
	[0, 0, 0, 0, 0],
	[1, 0, 1, 0, 1]
]
row = len(graph)
col = len(graph[0])
g = Graph(row, col, graph)
print("Number of islands is:", g.countIslands())

```

## [Given a sorted Dictionary of an Alien Language, find order of characters](https://practice.geeksforgeeks.org/problems/alien-dictionary/1)

```python
"""
Given a dictionary of ancient origin where the words are arranged alphabetically, find the correct order of alphabets in the ancient language.

For example,

Input:  Ancient dictionary { ¥€±, €±€, €±‰ð, ðß, ±±ð, ±ßß }
Output: The correct order of alphabets in the ancient language is {¥ € ‰ ð ± ß}.
 
Since the input is small, more than one ordering is possible. Another such ordering is {¥ € ð ± ß ‰}.
 
 
Input:  Ancient dictionary { ÿ€±š, €€€ß, €€‰ð, ðß, ±ß¥š }
Output: The correct order of alphabets in the ancient language is {ÿ € ‰ ð ±}.
 
The alphabets {š, ß, ¥} are not included in the order as they are not properly defined.
"""


class Graph:
    def __init__(self, N):
        self.adj = [[] for _ in range(N)]
 

def DFS(graph, v, discovered, departure, time):
    discovered[v] = True
    time = time + 1
    for u in graph.adj[v]:
        if not discovered[u]:
            time = DFS(graph, u, discovered, departure, time)
    departure[time] = v
    return time + 1
 
 
# Utility function to performs topological sort on a given DAG
def doTopologicalSort(graph, d):
 
    # `departure[]` stores the vertex number using departure time as an index
    departure = [-1] * (2 * N)
 
    ''' If we had done it the other way around, i.e., fill the array
        with departure time using vertex number as an index, we would
        need to sort it later '''
 
    # to keep track of whether a vertex is discovered or not
    discovered = [False] * N
    time = 0
 
    # perform DFS on all undiscovered connected vertices
    for i in range(N):
        if not discovered[i] and len(graph.adj[i]):
            time = DFS(graph, i, discovered, departure, time)
 
    print('\nThe correct order of alphabets in the ancient language is', end=' ')
 
    # Print the vertices in order of their decreasing
    # departure time in DFS, i.e., in topological order
    for i in reversed(range(2*N)):
        if departure[i] != -1:
            print(d[departure[i]], end=' ')
 
 
# Utility function to print adjacency list representation of a graph
def printGraph(graph, d):
 
    for i in range(N):
        # ignore vertices with no outgoing edges
        if graph.adj[i]:
            # print current vertex and all neighboring vertices of a vertex `i`
            print(d[i], '—>', [d[v] for v in graph.adj[i]])
 
 
# Function to find the correct order of alphabets in a given dictionary of
# ancient origin. This function assumes that the input is correct.
def findAlphabetsOrder(dictionary):
    # create a dictionary to map each non-ASCII character present in the given dictionary with a unique integer
    d = {}
    k = 0
    # do for each word
    for word in dictionary:
        # do for each non-ASCII character of the word
        for s in word:
            # if the current character is not present in the dictionary, insert it
            d.setdefault(s, k)
            k = k + 1
    # create a graph containing `N` nodes
    graph = Graph(N)

    # iterate through the complete dictionary and compare adjacent words for character mismatch
    for i in range(1, len(dictionary)):
        # previous word in the dictionary
        prev = dictionary[i - 1]

        # current word in the dictionary
        curr = dictionary[i]

        # iterate through both `prev` and `curr` simultaneously and find the first mismatching character
        j = 0
        while j < len(prev) and j < len(curr):
            # mismatch found
            if prev[j] is not curr[j]:

                # add an edge from the current character of `prev` to the
                # current character of `curr` in the graph
                graph.adj[d[prev[j]]].append(d[curr[j]])
                break

            j += 1

    # create a reverse dict
    reverse = {v: k for k, v in d.items()}
    printGraph(graph, reverse)
    # perform a topological sort on the above graph
    doTopologicalSort(graph, reverse)
 

# define the maximum number of alphabets in the ancient dictionary
N = 100
dictionary = [
    ["¥", "€", "±"],
    ["€", "±", "€"],
    ["€", "±", "‰", "ð"],
    ["ð", "ß"],
    ["±", "±", "ð"],
    ["±", "ß", "ß"]
]
findAlphabetsOrder(dictionary)
```

## [Implement Kruksal’sAlgorithm](https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/)

```python
"""
Below are the steps for finding MST using Kruskal’s algorithm

1. Sort all the edges in non-decreasing order of their weight. 
2. Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far. If cycle is not formed, include this edge. Else, discard it. 
3. Repeat step#2 until there are (V-1) edges in the spanning tree.
"""

from collections import defaultdict
class Graph:

	def __init__(self, vertices):
		self.V = vertices # No. of vertices
		self.graph = [] # default dictionary
		# to store graph

	# function to add an edge to graph
	def addEdge(self, u, v, w):
		self.graph.append([u, v, w])

	# A utility function to find set of an element i (uses path compression technique)
	def find(self, parent, i):
		return i if parent[i] == i else self.find(parent, parent[i])

	# A function that does union of two sets of x and y (uses union by rank)
	def union(self, parent, rank, x, y):
		xroot = self.find(parent, x)
		yroot = self.find(parent, y)

		# Attach smaller rank tree under root of high rank tree (Union by Rank)
		if rank[xroot] < rank[yroot]:
			parent[xroot] = yroot
		elif rank[xroot] > rank[yroot]:
			parent[yroot] = xroot

		# If ranks are same, then make one as root and increment its rank by one
		else:
			parent[yroot] = xroot
			rank[xroot] += 1

	# The main function to construct MST using Kruskal's algorithm
	def KruskalMST(self):

		result = [] # This will store the resultant MST
		i = 0 # An index variable, used for sorted edges
		e = 0 # An index variable, used for result[]

		# Step 1: Sort all the edges in non-decreasing order of their
		# weight. If we are not allowed to change the given graph, we can create a copy of graph
		self.graph = sorted(self.graph, key=lambda item: item[2])

		parent = []
		rank = []

		# Create V subsets with single elements
		for node in range(self.V):
			parent.append(node)
			rank.append(0)

		# Number of edges to be taken is equal to V-1
		while e < self.V - 1:

			# Step 2: Pick the smallest edge and increment the index for next iteration
			u, v, w = self.graph[i]
			i = i + 1
			x = self.find(parent, u)
			y = self.find(parent, v)

			# If including this edge doesn't cause cycle, include it in result and increment the indexof 
            # result for next edge
			if x != y:
				e += 1
				result.append([u, v, w])
				self.union(parent, rank, x, y)
				# Else discard the edge

		minimumCost = 0
		print ("Edges in the constructed MST")
		for u, v, weight in result:
			minimumCost += weight
			print("%d -- %d == %d" % (u, v, weight))
		print("Minimum Spanning Tree" , minimumCost)

g = Graph(4)
g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)
g.KruskalMST()
```

## [Implement Prim’s Algorithm](https://www.geeksforgeeks.org/prims-minimum-spanning-tree-mst-greedy-algo-5/)

```python
# A Python program for Prim's Minimum Spanning Tree (MST) algorithm.
# The program is for adjacency matrix representation of the graph

import sys # Library for INT_MAX

class Graph():

	def __init__(self, vertices):
		self.V = vertices
		self.graph = [[0 for column in range(vertices)]
					for row in range(vertices)]

	# A utility function to print the constructed MST stored in parent[]
	def printMST(self, parent):
		print ("Edge \tWeight")
		for i in range(1, self.V):
			print (parent[i], "-", i, "\t", self.graph[i][parent[i]])

	# A utility function to find the vertex with minimum distance value, from the set of vertices not yet included in shortest path tree
	def minKey(self, key, mstSet):

		# Initialize minValue value
		minValue = sys.maxsize

		for v in range(self.V):
			if key[v] < minValue and mstSet[v] == False:
				minValue = key[v]
				min_index = v

		return min_index

	# Function to construct and print MST for a graph represented using adjacency matrix representation
	def primMST(self):

		# Key values used to pick minimum weight edge in cut
		key = [sys.maxsize] * self.V
		parent = [None] * self.V # Array to store constructed MST
		# Make key 0 so that this vertex is picked as first vertex
		key[0] = 0
		mstSet = [False] * self.V

		parent[0] = -1 # First node is always the root of

		for cout in range(self.V):

			# Pick the minimum distance vertex from the set of vertices not yet processed. u is always equal to src in first iteration
			u = self.minKey(key, mstSet)

			# Put the minimum distance vertex in the shortest path tree
			mstSet[u] = True

			# Update dist value of the adjacent vertices of the picked vertex only if the current
			# distance is greater than new distance and the vertex in not in the shortest path tree
			for v in range(self.V):

				# graph[u][v] is non zero only for adjacent vertices of m mstSet[v] is false for vertices not yet included in MST
				# Update the key only if graph[u][v] is smaller than key[v]
				if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
						key[v] = self.graph[u][v]
						parent[v] = u
		self.printMST(parent)

g = Graph(5)
g.graph = [ [0, 2, 0, 6, 0],
			[2, 0, 3, 8, 5],
			[0, 3, 0, 0, 7],
			[6, 8, 0, 0, 9],
			[0, 5, 7, 9, 0]]
g.primMST();
```

## [Total no. of Spanning tree in a graph](https://www.geeksforgeeks.org/total-number-spanning-trees-graph/)

```python
TODO
```

## [Implement Bellman Ford Algorithm](https://practice.geeksforgeeks.org/problems/negative-weight-cycle/0)

```python
"""
We are given a directed graph. We need to compute whether the graph has a negative cycle or not. A negative cycle is one in which the overall sum of the cycle becomes negative.
"""

# a structure to represent a weighted edge in graph
class Edge:
	def __init__(self):
		self.src = 0
		self.dest = 0
		self.weight = 0

# a structure to represent a connected, directed and weighted graph
class Graph:
	def __init__(self):
		# V. Number of vertices, E. Number of edges
		self.V = 0
		self.E = 0

		# graph is represented as an array of edges.
		self.edge = None

# Creates a graph with V vertices and E edges
def createGraph(V, E):

	graph = Graph()
	graph.V = V;
	graph.E = E;
	graph.edge = [Edge() for _ in range(graph.E)]
	return graph;

# The main function that finds shortest distances from src to all other vertices using Bellman- Ford algorithm. The function also detects negative weight cycle
def isNegCycleBellmanFord(graph, src):

	V = graph.V;
	E = graph.E;
	dist = [1000000 for _ in range(V)];
	dist[src] = 0;

	# Step 2: Relax all edges |V| - 1 times. 
    # A simple shortest path from src to any other vertex can have at-most |V| - 1 edges
	for _ in range(1, V):
		for j in range(E):

			u = graph.edge[j].src;
			v = graph.edge[j].dest;
			weight = graph.edge[j].weight;
			if (dist[u] != 1000000 and dist[u] + weight < dist[v]):
				dist[v] = dist[u] + weight;

	# Step 3: check for negative-weight cycles.
	# The above step guarantees shortest distances if graph doesn't contain negative weight cycle.
	# If we get a shorter path, then there is a cycle.
	for i in range(E):

		u = graph.edge[i].src;
		v = graph.edge[i].dest;
		weight = graph.edge[i].weight;
		if (dist[u] != 1000000 and dist[u] + weight < dist[v]):
			return True;

	return False;


# Let us create the graph given in above example
V = 5; # Number of vertices in graph
E = 8; # Number of edges in graph
graph = createGraph(V, E)

source= [0,0,1,1,1,3,3,4]
destination= [1,2,2,3,4,2,1,3]
weight=[-1,4,3,2,2,5,1,-3]

for i in range(E):
    graph.edge[i].src=source[i]
    graph.edge[i].dest=destination[i]
    graph.edge[i].weight=weight[i]

if (isNegCycleBellmanFord(graph, 0)):
	print("Yes")
else:
	print("No")

```

## [Implement Floyd warshallAlgorithm](https://practice.geeksforgeeks.org/problems/implementing-floyd-warshall/0)

```python
"""
The Floyd Warshall Algorithm is for solving the All Pairs Shortest Path problem. The problem is to find shortest distances between every pair of vertices in a given edge weighted directed Graph. 
Example: 

Input:
       graph[][] = { {0,   5,  INF, 10},
                    {INF,  0,  3,  INF},
                    {INF, INF, 0,   1},
                    {INF, INF, INF, 0} }
which represents the following graph
             10
       (0)------->(3)
        |         /|\
      5 |          |
        |          | 1
       \|/         |
       (1)------->(2)
            3       
Note that the value of graph[i][j] is 0 if i is equal to j 
And graph[i][j] is INF (infinite) if there is no edge from vertex i to j.

Output:
Shortest distance matrix
      0      5      8      9
    INF      0      3      4
    INF    INF      0      1
    INF    INF    INF      0
"""


def floydWarshall(graph):
	dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
	for k in range(V):
		# pick all vertices as source one by one
		for i in range(V):
			# Pick all vertices as destination for the above picked source
			for j in range(V):

				# If vertex k is on the shortest path from i to j, then update the value of dist[i][j]
				dist[i][j] = min(dist[i][j],dist[i][k] + dist[k][j])
	printSolution(dist)


# A utility function to print the solution
def printSolution(dist):
	print ("Following matrix shows the shortest distances\
between every pair of vertices")
	for i in range(V):
		for j in range(V):
			if(dist[i][j] == INF):
				print ("%7s" % ("INF"),end=" ")
			else:
				print ("%7d\t" % (dist[i][j]),end=' ')
			if j == V-1:
				print ()



# Let us create the following weighted graph
"""
			10
	(0)------->(3)
		|		 /|\
	5 |		 |
		|		 | 1
	\|/		 |
	(1)------->(2)
			3		 
"""
# Number of vertices in the graph
V = 4
INF = 99999

graph = [[0, 5, INF, 10],
		[INF, 0, 3, INF],
		[INF, INF, 0, 1],
		[INF, INF, INF, 0]
		]

floydWarshall(graph)

```

## [Travelling Salesman Problem](https://www.geeksforgeeks.org/travelling-salesman-problem-set-1/)

```python
"""
Travelling Salesman Problem (TSP): 

Given a set of cities and the distance between every pair of cities, the problem is to find the shortest possible route that visits every city exactly once and returns to the starting point.
"""
n = 4 # there are four nodes in example graph (graph is 1-based)

# dist[i][j] represents shortest distance to go from i to  this matrix can be calculated for any given graph usin all-pair shortest path algorithms
dist = [[0, 0, 0, 0, 0], [0, 0, 10, 15, 20], [
	0, 10, 0, 25, 25], [0, 15, 25, 0, 30], [0, 20, 25, 30, 0]]

# memoization for top down recursion
memo = [[-1]*(1 << (n+1)) for _ in range(n+1)]


def fun(i, mask):
	# base case
	# if only ith bit and 1st bit is set in our mask, it implies we have visited all other nodes already
	if mask == ((1 << i) | 3):
		return dist[1][i]

	# memoization
	if memo[i][mask] != -1:
		return memo[i][mask]

	res = 10**9 # result of this sub-problem

	# we have to travel all nodes j in mask and end the path at ith node so for every node j in mask, recursively calculate cost of travelling all nodes in mask except i and then travel back from node j to node i taking
	# the shortest path take the minimum of all possible j nodes
	for j in range(1, n+1):
		if (mask & (1 << j)) != 0 and j != i and j != 1:
			res = min(res, fun(j, mask & (~(1 << i))) + dist[j][i])
	memo[i][mask] = res # storing the minimum value
	return res



ans = 10**9
for i in range(1, n+1):
	# try to go from node 1 visiting all nodes in between to i then return from i taking the shortest route to 1
	ans = min(ans, fun(i, (1 << (n+1))-1) + dist[i][1])
print(f"The cost of most efficient tour = {str(ans)}")
```

## [Graph ColouringProblem](https://www.geeksforgeeks.org/graph-coloring-applications/)

```python
TODO
```

## [Snake and Ladders Problem](https://leetcode.com/problems/snakes-and-ladders/)

```python
"""
On an N x N board, the numbers from 1 to N*N are written boustrophedonically starting from the bottom left of the board, and alternating direction each row. For example, for a 6 x 6 board, the numbers are written as follows:

You start on square 1 of the board (which is always in the last row and first column). Each move, starting from square x, consists of the following:

You choose a destination square S with number x+1, x+2, x+3, x+4, x+5, or x+6, provided this number is <= N*N.
(This choice simulates the result of a standard 6-sided die roll: ie., there are always at most 6 destinations, regardless of the size of the board.)
If S has a snake or ladder, you move to the destination of that snake or ladder. Otherwise, you move to S. A board square on row r and column c has a “snake or ladder” if board[r][c] != -1. The destination of that snake or ladder is board[r][c].
Note that you only take a snake or ladder at most once per move: if the destination to a snake or ladder is the start of another snake or ladder, you do not continue moving. (For example, if the board is [[4,-1],[-1,3]], and on the first move your destination square is 2, then you finish your first move at 3, because you do not continue moving to 4.)

Return the least number of moves required to reach square N*N. If it is not possible, return -1.
"""
import collections
def snakesAndLadders(board):
        rows = len(board)
        total_square = rows*rows

        def next_square(step):
                quot, rem = divmod(step-1, rows)
                row = (rows - 1) - quot
                col = rem if row%2 != rows%2 else (rows - 1) - rem
                return row, col

        dist = {1: 0}#square and step
        queue = collections.deque([1])
        while queue:
            square = queue.popleft()
            if square == total_square:
                return dist[square]
            for new_square in range(square+1, min(square+6, total_square) + 1):
                r, c = next_square(new_square)
                if board[r][c] != -1:
                    new_square = board[r][c]
                if new_square not in dist:
                    dist[new_square] = dist[square] + 1
                    queue.append(new_square)
board=[
[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,35,-1,-1,13,-1],
[-1,-1,-1,-1,-1,-1],
[-1,15,-1,-1,-1,-1]]
print(snakesAndLadders(board))
```

## [Find bridge in a graph](https://www.geeksforgeeks.org/bridge-in-a-graph/)

```python
from collections import defaultdict

#This class represents an undirected graph using adjacency list representation
class Graph:

	def __init__(self,vertices):
		self.V= vertices #No. of vertices
		self.graph = defaultdict(list) # default dictionary to store graph
		self.Time = 0

	# function to add an edge to graph
	def addEdge(self,u,v):
		self.graph[u].append(v)
		self.graph[v].append(u)

	'''
    A recursive function that finds and prints bridges
	using DFS traversal
	u --> The vertex to be visited next
	visited[] --> keeps track of visited vertices
	disc[] --> Stores discovery times of visited vertices
	parent[] --> Stores parent vertices in DFS tree
    '''
	def bridgeUtil(self, u, visited, parent, low, disc):

		# Mark the current node as visited and print it
		visited[u]= True

		# Initialize discovery time and low value
		disc[u] = self.Time
		low[u] = self.Time
		self.Time += 1

		#Recur for all the vertices adjacent to this vertex
		for v in self.graph[u]:
			# If v is not visited yet, then make it a child of u in DFS tree and recur for it
			if visited[v] == False :
				parent[v] = u
				self.bridgeUtil(v, visited, parent, low, disc)

				# Check if the subtree rooted with v has a connection to one of the ancestors of u
				low[u] = min(low[u], low[v])


				''' If the lowest vertex reachable from subtree
				under v is below u in DFS tree, then u-v is
				a bridge'''
				if low[v] > disc[u]:
					print ("%d %d" %(u,v))
	
					
			elif v != parent[u]: # Update low value of u for parent function calls.
				low[u] = min(low[u], disc[v])


	# DFS based function to find all bridges. It uses recursive function bridgeUtil()
	def bridge(self):

		# Mark all the vertices as not visited and Initialize parent and visited, and ap(articulation point) arrays
		visited = [False] * (self.V)
		disc = [float("Inf")] * (self.V)
		low = [float("Inf")] * (self.V)
		parent = [-1] * (self.V)

		# Call the recursive helper function to find bridges in DFS tree rooted with vertex 'i'
		for i in range(self.V):
			if visited[i] == False:
				self.bridgeUtil(i, visited, parent, low, disc)
		


g1 = Graph(5)
g1.addEdge(1, 0)
g1.addEdge(0, 2)
g1.addEdge(2, 1)
g1.addEdge(0, 3)
g1.addEdge(3, 4)


print ("Bridges in first graph ")
g1.bridge()

g2 = Graph(4)
g2.addEdge(0, 1)
g2.addEdge(1, 2)
g2.addEdge(2, 3)
print ("\nBridges in second graph ")
g2.bridge()


g3 = Graph (7)
g3.addEdge(0, 1)
g3.addEdge(1, 2)
g3.addEdge(2, 0)
g3.addEdge(1, 3)
g3.addEdge(1, 4)
g3.addEdge(1, 6)
g3.addEdge(3, 5)
g3.addEdge(4, 5)
print ("\nBridges in third graph ")
g3.bridge()
```

## [Count Strongly connected Components(Kosaraju Algo)](https://practice.geeksforgeeks.org/problems/strongly-connected-components-kosarajus-algo/1)

```python
from collections import defaultdict
class Graph:
	def __init__(self,vertices):
		self.V= vertices 
		self.graph = defaultdict(list) 

	def addEdge(self,u,v):
		self.graph[u].append(v)

	# A function used by DFS
	def DFSUtil(self,v,visited):
		# Mark the current node as visited and print it
		visited[v]= True
		print (v)
		#Recur for all the vertices adjacent to this vertex
		for i in self.graph[v]:
			if visited[i]==False:
				self.DFSUtil(i,visited)


	def fillOrder(self,v,visited, stack):
		# Mark the current node as visited
		visited[v]= True
		#Recur for all the vertices adjacent to this vertex
		for i in self.graph[v]:
			if visited[i]==False:
				self.fillOrder(i, visited, stack)
		stack = stack.append(v)
	

	# Function that returns reverse (or transpose) of this graph
	def getTranspose(self):
		g = Graph(self.V)

		# Recur for all the vertices adjacent to this vertex
		for i in self.graph:
			for j in self.graph[i]:
				g.addEdge(j,i)
		return g



	# The main function that finds and prints all strongly connected components
	def printSCCs(self):
		
		stack = []
		# Mark all the vertices as not visited (For first DFS)
		visited =[False]*(self.V)
		# Fill vertices in stack according to their finishing times
		for i in range(self.V):
			if visited[i]==False:
				self.fillOrder(i, visited, stack)

		# Create a reversed graph
		gr = self.getTranspose()
		
		# Mark all the vertices as not visited (For second DFS)
		visited =[False]*(self.V)

		# Now process all vertices in order defined by Stack
		while stack:
			i = stack.pop()
			if visited[i]==False:
				gr.DFSUtil(i, visited)
				print()

# Create a graph given in the above diagram
g = Graph(5)
g.addEdge(1, 0)
g.addEdge(0, 2)
g.addEdge(2, 1)
g.addEdge(0, 3)
g.addEdge(3, 4)
print ("Following are strongly connected components " + "in given graph")
g.printSCCs()
```

## [Check whether a graph is Bipartite or Not](https://www.geeksforgeeks.org/bipartite-graph/)

```python
V = 4

def colorGraph(G, color, pos, c):
	if color[pos] not in [-1, c]:
		return False

	# color this pos as c and all its neighbours and 1-c
	color[pos] = c
	ans = True
	for i in range(V):
		if G[pos][i]:
			if color[i] == -1:
				ans &= colorGraph(G, color, i, 1-c)
			if color[i] not in [-1, 1 - c]:
				return False
		if not ans:
			return False
	return True

def isBipartite(G):
	color = [-1] * V
	#start is vertex 0
	pos = 0
	# two colors 1 and 0
	return colorGraph(G, color, pos, 1)

G = [[0, 1, 0, 1],
	[1, 0, 1, 0],
	[0, 1, 0, 1],
	[1, 0, 1, 0]]

if isBipartite(G): print("Yes")
else: print("No")
```

## [Longest path in a Directed Acyclic Graph](https://www.geeksforgeeks.org/find-longest-path-directed-acyclic-graph/)

```python
def topologicalSortUtil(v):
	global Stack, visited, adj
	visited[v] = True
	for i in adj[v]:
		if (not visited[i[0]]):
			topologicalSortUtil(i[0])
	Stack.append(v)

# The function to find longest distances from a given vertex. It uses recursive topologicalSortUtil() to get topological sorting.
def longestPath(s):
	global Stack, visited, adj, V
	dist = [-10**9 for _ in range(V)]

	# Call the recursive helper function to store Topological Sort starting from all vertices one by one
	for i in range(V):
		if (visited[i] == False):
			topologicalSortUtil(i)

	# Initialize distances to all vertices as infinite and distance to source as 0
	dist[s] = 0

	# Process vertices in topological order
	while (len(Stack) > 0):

		# Get the next vertex from topological order
		u = Stack[-1]
		del Stack[-1]

		# Update distances of all adjacent vertices
		if (dist[u] != 10**9):
			for i in adj[u]:
				if (dist[i[0]] < dist[u] + i[1]):
					dist[i[0]] = dist[u] + i[1]

	# Print calculated longest distances print(dist)
	for i in range(V):
		print("INF ",end="") if (dist[i] == -10**9) else print(dist[i],end=" ")


V, Stack, visited = 6, [], [False for _ in range(7)]
adj = [[] for _ in range(7)]
# Create a graph given in the above diagram.
# Here vertex numbers are 0, 1, 2, 3, 4, 5 with following mappings:
# 0=r, 1=s, 2=t, 3=x, 4=y, 5=z
adj[0].append([1, 5])
adj[0].append([2, 3])
adj[1].append([3, 6])
adj[1].append([2, 2])
adj[2].append([4, 4])
adj[2].append([5, 2])
adj[2].append([3, 7])
adj[3].append([5, 1])
adj[3].append([4, -1])
adj[4].append([5, -2])
s = 1
print("Following are longest distances from source vertex ",s)
longestPath(s)
```

## [Journey to the Moon](https://www.hackerrank.com/challenges/journey-to-the-moon/problem)

```python
TODO
```

## [Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/description/)

```python
TODO
```

## [Oliver and the Game](https://www.hackerearth.com/practice/algorithms/graphs/topological-sort/practice-problems/algorithm/oliver-and-the-game-3/)

```python
TODO
```

## [Water Jug problem using BFS](https://www.geeksforgeeks.org/water-jug-problem-using-bfs/)

```python
"""
You are given an m liter jug and a n liter jug. Both the jugs are initially empty. The jugs don’t have markings to allow measuring smaller quantities. You have to use the jugs to measure d liters of water where d is less than n. 

(X, Y) corresponds to a state where X refers to the amount of water in Jug1 and Y refers to the amount of water in Jug2 
Determine the path from the initial state (xi, yi) to the final state (xf, yf), where (xi, yi) is (0, 0) which indicates both Jugs are initially empty and (xf, yf) indicates a state which could be (0, d) or (d, 0).

The operations you can perform are: 

Empty a Jug, (X, Y)->(0, Y) Empty Jug 1
Fill a Jug, (0, 0)->(X, 0) Fill Jug 1
Pour water from one jug to the other until one of the jugs is either empty or full, (X, Y) -> (X-d, Y+d)
Examples: 

Input : 4 3 2
Output : {(0, 0), (0, 3), (3, 0), (3, 3), (4, 2), (0, 2)}
"""

from collections import deque

def BFS(a, b, target):
	
	# Map is used to store the states, every state is hashed to binary value to indicate either that state is visited before or not
	m = {}
	isSolvable = False
	path = []
	
	# Queue to maintain states
	q = deque()
	
	# Initialing with initial state
	q.append((0, 0))

	while (len(q) > 0):
		# Current state
		u = q.popleft()

		#q.pop() #pop off used state

		# If this state is already visited
		if ((u[0], u[1]) in m):
			continue

		# Doesn't met jug constraints
		if ((u[0] > a or u[1] > b or
			u[0] < 0 or u[1] < 0)):
			continue

		# Filling the vector for constructing the solution path
		path.append([u[0], u[1]])

		# Marking current state as visited
		m[(u[0], u[1])] = 1

		# If we reach solution state, put ans=1
		if (u[0] == target or u[1] == target):
			isSolvable = True
			
			if (u[0] == target):
				if (u[1] != 0):
					
					# Fill final state
					path.append([u[0], 0])
			else:
				if (u[0] != 0):

					# Fill final state
					path.append([0, u[1]])

			# Print the solution path
			sz = len(path)
			for i in range(sz):
				print("(", path[i][0], ",",
						path[i][1], ")")
			break

		# If we have not reached final state then, start developing intermediate states to reach solution state
		q.append([u[0], b]) # Fill Jug2
		q.append([a, u[1]]) # Fill Jug1

		for ap in range(max(a, b) + 1):

			# Pour amount ap from Jug2 to Jug1
			c = u[0] + ap
			d = u[1] - ap

			# Check if this state is possible or not
			if (c == a or (d == 0 and d >= 0)):
				q.append([c, d])

			# Pour amount ap from Jug 1 to Jug2
			c = u[0] - ap
			d = u[1] + ap

			# Check if this state is possible or not
			if ((c == 0 and c >= 0) or d == b):
				q.append([c, d])
		
		# Empty Jug2
		q.append([a, 0])
		
		# Empty Jug1
		q.append([0, b])

	# No, solution exists if ans=0
	if (not isSolvable):
		print ("No solution")


Jug1, Jug2, target = 4, 3, 2
print("Path from initial state to solution state ::")
BFS(Jug1, Jug2, target)
```

## [Find if there is a path of more thank length from a source](https://www.geeksforgeeks.org/find-if-there-is-a-path-of-more-than-k-length-from-a-source/)

```python
"""
Given a graph, a source vertex in the graph and a number k, find if there is a simple path (without any cycle) starting from given source and ending at any other vertex such that the distance from source to that vertex is atleast ‘k’ length.

Example:

Input  : Source s = 0, k = 58
Output : True
There exists a simple path 0 -> 7 -> 1
-> 2 -> 8 -> 6 -> 5 -> 3 -> 4
Which has a total distance of 60 km which
is more than 58.

Input  : Source s = 0, k = 62
Output : False

In the above graph, the longest simple
path has distance 61 (0 -> 7 -> 1-> 2
 -> 3 -> 4 -> 5-> 6 -> 8, so output 
should be false for any input greater 
than 61.
"""
# Program to find if there is a simple path with
# weight more than k
	
# This class represents a dipathted graph using
# adjacency list representation
class Graph:
	# Allocates memory for adjacency list
	def __init__(self, V):
		self.V = V
		self.adj = [[] for _ in range(V)]
	
	# Returns true if graph has path more than k length
	def pathMoreThanK(self,src, k):
		# Create a path array with nothing included in path
		path = [False]*self.V
		
		# Add source vertex to path
		path[src] = 1
		
		return self.pathMoreThanKUtil(src, k, path)
		
	# Prints shortest paths from src to all other vertices
	def pathMoreThanKUtil(self,src, k, path):
		# If k is 0 or negative, return true
		if (k <= 0):
			return True
		
		# Get all adjacent vertices of source vertex src and recursively explore all paths from src.
		i = 0
		while i != len(self.adj[src]):
			# Get adjacent vertex and weight of edge
			v = self.adj[src][i][0]
			w = self.adj[src][i][1]
			i += 1
		
			# If vertex v is already there in path, then there is a cycle (we ignore this edge)
			if (path[v] == True):
				continue
		
			# If weight of is more than k, return true
			if (w >= k):
				return True
		
			# Else add this vertex to path
			path[v] = True
		
			# If this adjacent can provide a path longer than k, return true.
			if (self.pathMoreThanKUtil(v, k-w, path)):
				return True
		
			# Backtrack
			path[v] = False
		
		# If no adjacent could produce longer path, return false
		return False
	
	# Utility function to an edge (u, v) of weight w
	def addEdge(self,u, v, w):
		self.adj[u].append([v, w])
		self.adj[v].append([u, w])

# create the graph given in above figure
V = 9
g = Graph(V)

# making above shown graph
g.addEdge(0, 1, 4)
g.addEdge(0, 7, 8)
g.addEdge(1, 2, 8)
g.addEdge(1, 7, 11)
g.addEdge(2, 3, 7)
g.addEdge(2, 8, 2)
g.addEdge(2, 5, 4)
g.addEdge(3, 4, 9)
g.addEdge(3, 5, 14)
g.addEdge(4, 5, 10)
g.addEdge(5, 6, 2)
g.addEdge(6, 7, 1)
g.addEdge(6, 8, 6)
g.addEdge(7, 8, 7)

src = 0
k = 62
if g.pathMoreThanK(src, k):
	print("Yes")
else:
	print("No")

k = 60
if g.pathMoreThanK(src, k):
	print("Yes")
else:
	print("No")
```

## [Minimum edges to reverse o make path from source to destination](https://www.geeksforgeeks.org/minimum-edges-reverse-make-path-source-destination/)

```python
"""
Given a directed graph and a source node and destination node, we need to find how many edges we need to reverse in order to make at least 1 path from the source node to the destination node.
"""

def addEdge(u, v, w):
	global adj
	adj[u].append((v, w))

def shortestPath(src):

	# Create a set to store vertices that are being preprocessed
	setds = {}

	# Create a vector for distances and initialize all distances as infinite (INF)
	dist = [10**18 for _ in range(V)]

	# Insert source itself in Set and initialize its
	global adj
	setds[(0, src)] = 1
	dist[src] = 0

	while setds:

		# The first vertex in Set is the minimum distance vertex, extract it from set.
		tmp = list(setds.keys())[0]
		del setds[tmp]

		# vertex label is stored in second of pair (it has to be done this way to keep the vertices sorted distance (distance must be first item in pair)
		u = tmp[1]

		# 'i' is used to get all adjacent vertices of a vertex
		# list< pair<int, int> >::iterator i;
		for i in adj[u]:

			# Get vertex label and weight of current adjacent
			# of u.
			v = i[0];
			weight = i[1]

			# If there is shorter path to v through u.
			if (dist[v] > dist[u] + weight):

				# /* If distance of v is not INF then it must be in
				#	 our set, so removing it and inserting again
				#	 with updated less distance.
				#	 Note : We extract only those vertices from Set
				#	 for which distance is finalized. So for them,
				#	 we would never reach here. */
				if (dist[v] != 10**18):
					del setds[(dist[v], v)]

				# Updating distance of v
				dist[v] = dist[u] + weight
				setds[(dist[v], v)] = 1

	return dist

# method adds reverse edge of each original edge in the graph. It gives reverse edge a weight = 1 and all original edges a weight of 0. Now, the length of the shortest path will give us the answer. If shortest path is p: it means we used p reverse edges in the shortest path. 
def modelGraphWithEdgeWeight(edge, E, V):
	global adj
	for i in range(E):
		addEdge(edge[i][0], edge[i][1], 0) # original edge : weight 0
		addEdge(edge[i][1], edge[i][0], 1) # reverse edge : weight 1

# Method returns minimum number of edges to be reversed to reach from src to dest
def getMinEdgeReversal(edge, E, V,src, dest):
	# get modified graph with edge weight
	modelGraphWithEdgeWeight(edge, E, V)

	# get shortes path vector
	dist = shortestPath(src)

	# If distance of destination is still INF, not possible
	return -1 if (dist[dest] == 10**18) else dist[dest]


V = 7
edge = [[0, 1], [2, 1], [2, 3], [5, 1],[4, 5], [6, 4], [6, 3]]
E, adj = len(edge), [[] for _ in range(V + 1)]
minEdgeToReverse = getMinEdgeReversal(edge, E, V, 0, 6)
if (minEdgeToReverse != -1):
	print(minEdgeToReverse)
else:
	print("Not possible")
```

## [Paths to travel each nodes using each edge(Seven Bridges)](https://www.geeksforgeeks.org/paths-travel-nodes-using-edgeseven-bridges-konigsberg/)

```python
TODO
```

## [Vertex Cover Problem](https://www.geeksforgeeks.org/vertex-cover-problem-set-1-introduction-approximate-algorithm-2/)

```python
"""
There are n nodes and m bridges in between these nodes. Print the possible path through each node using each edges (if possible), traveling through each edges only once.
"""

from collections import defaultdict

class Graph:
	def __init__(self, vertices):
		self.V = vertices
		self.graph = defaultdict(list)


	def addEdge(self, u, v):
		self.graph[u].append(v)


	def printVertexCover(self):
		# Initialize all vertices as not visited.
		visited = [False] * (self.V)
		
		# Consider all edges one by one
		for u in range(self.V):
			
			# An edge is only picked when both visited[u] and visited[v] are false
			if not visited[u]:
				
				# Go through all adjacents of u and pick the first not yet visited
				# vertex (We are basically picking an edge (u, v) from remaining edges.
				for v in self.graph[u]:
					if not visited[v]:
						
						# Add the vertices (u, v) to the
						# result set. We make the vertex u and v visited so that all
						# edges from/to them would be ignored
						visited[v] = True
						visited[u] = True
						break

		# Print the vertex cover
		for j in range(self.V):
			if visited[j]:
				print(j, end = ' ')
		print()

g = Graph(7)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 3)
g.addEdge(3, 4)
g.addEdge(4, 5)
g.addEdge(5, 6)
g.printVertexCover()
```

## [Chinese Postman or Route Inspection](https://www.geeksforgeeks.org/chinese-postman-route-inspection-set-1-introduction/)

```python
TODO
```

## [Number of Triangles in a Directed and Undirected Graph](https://www.geeksforgeeks.org/number-of-triangles-in-directed-and-undirected-graphs/)

```python
"""
Given a Graph, count number of triangles in it. The graph is can be directed or undirected.

Example: 

Input: digraph[V][V] = { {0, 0, 1, 0},
                        {1, 0, 0, 1},
                        {0, 1, 0, 0},
                        {0, 0, 1, 0}
                      };
Output: 2
Give adjacency matrix represents following 
directed graph.
"""

# function to calculate the number of triangles in a simple directed/undirected graph.
# isDirected is true if the graph is directed, its false otherwise
def countTriangle(g, isDirected):
    nodes = len(g)
    count_Triangle = 0
    # Consider every possible triplet of edges in graph
    for i in range(nodes):
        for j in range(nodes):
            for k in range(nodes):
                # check the triplet if it satisfies the condition
                if(i != j and i != k and j != k and g[i][j] and g[j][k] and g[k][i]):
                    count_Triangle += 1
          
    # If graph is directed , division is done by 3 else division by 6 is done
    if isDirected:
      return (count_Triangle//3)
    else: 
      return (count_Triangle//6)


# Create adjacency matrix of an undirected graph
graph = [[0, 1, 1, 0],
		[1, 0, 1, 1],
		[1, 1, 0, 1],
		[0, 1, 1, 0]]
# Create adjacency matrix of a directed graph
digraph = [[0, 0, 1, 0],
		[1, 0, 0, 1],
		[0, 1, 0, 0],
		[0, 0, 1, 0]]

print("The Number of triangles in undirected graph : %d" %
	countTriangle(graph, False))

print("The Number of triangles in directed graph : %d" %
	countTriangle(digraph, True))
```

## [Minimise the cashflow among a given set of friends who have borrowed money from each other](https://www.geeksforgeeks.org/minimize-cash-flow-among-given-set-friends-borrowed-money/)

```python
"""
Given a number of friends who have to give or take some amount of money from one another. Design an algorithm by which the total cash flow among all the friends is minimized. 
"""

# Number of persons(or vertices in graph)
N = 3

# A utility function that returns index of minimum value in arr[]
def getMin(arr):
	minInd = 0
	for i in range(1, N):
		if (arr[i] < arr[minInd]):
			minInd = i
	return minInd

# A utility function that returns index of maximum value in arr[]
def getMax(arr):
	maxInd = 0
	for i in range(1, N):
		if (arr[i] > arr[maxInd]):
			maxInd = i
	return maxInd


def minOf2(x, y):
	return x if x < y else y

# amount[p] indicates the net amount to be credited/debited to/from person 'p' If amount[p] is positive, then i'th person will amount[i] If amount[p] is negative, then i'th person will give -amount[i]
def minCashFlowRec(amount):

	# Find the indexes of minimum and maximum values in amount[] amount[mxCredit] indicates the maximum amount to be given(or credited) to any person. And amount[mxDebit] indicates the maximum amount to be taken (or debited) from any person. So if there is a positive value in amount[], then there must be a negative value
	mxCredit = getMax(amount)
	mxDebit = getMin(amount)

	# If both amounts are 0, then all amounts are settled
	if (amount[mxCredit] == 0 and amount[mxDebit] == 0):
		return 0

	# Find the minimum of two amounts
	min = minOf2(-amount[mxDebit], amount[mxCredit])
	amount[mxCredit] -=min
	amount[mxDebit] += min

	# If minimum is the maximum amount to be
	print("Person " , mxDebit , " pays " , min
		, " to " , "Person " , mxCredit)

	# Recur for the amount array. Note that it is guaranteed that the recursion would terminate as either amount[mxCredit] or amount[mxDebit] becomes 0
	minCashFlowRec(amount)

# Given a set of persons as graph[] where graph[i][j] indicates the amount that person i needs to pay person j, this function finds and prints the minimum cash flow to settle all debts.
def minCashFlow(graph):

	# Create an array amount[], initialize all value in it as 0.
	amount = [0 for _ in range(N)]

	# Calculate the net amount to be paid to person 'p', and stores it in amount[p]. The value of amount[p] can be calculated by subtracting debts of 'p' from credits of 'p'
	for p in range(N):
		for i in range(N):
			amount[p] += (graph[i][p] - graph[p][i])

	minCashFlowRec(amount)


# graph[i][j] indicates the amount that person i needs to pay person j
graph = [ [0, 1000, 2000],
		[0, 0, 5000],
		[0, 0, 0] ]
minCashFlow(graph)
```

## [Two Clique Problem](https://www.geeksforgeeks.org/two-clique-problem-check-graph-can-divided-two-cliques/)

```python
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

```

# Greedy

## [Activity Selection Problem](https://practice.geeksforgeeks.org/problems/n-meetings-in-one-room/0)

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

## [Huffman Coding](https://practice.geeksforgeeks.org/problems/huffman-encoding/0)

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

## [Water Connection Problem](https://practice.geeksforgeeks.org/problems/water-connection-problem/0)

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

## [Fractional Knapsack Problem](https://practice.geeksforgeeks.org/problems/fractional-knapsack/0)

```python

```

## [Greedy Algorithm to find Minimum number of Coins](https://practice.geeksforgeeks.org/problems/coin-piles/0)

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

## [Maximum trains for which stoppage can be provided](https://www.geeksforgeeks.org/maximum-trains-stoppage-can-provided/)

```python
TODO
```

## [Minimum Platforms Problem](https://practice.geeksforgeeks.org/problems/minimum-platforms/0)

```python
"""
Given the arrival and departure times of all trains that reach a railway station, the task is to find the minimum number of platforms required for the railway station so that no train waits. 
We are given two arrays that represent the arrival and departure times of trains that stop.

Examples:  

Input: arr[] = {9:00, 9:40, 9:50, 11:00, 15:00, 18:00} 
dep[] = {9:10, 12:00, 11:20, 11:30, 19:00, 20:00} 
Output: 3 
Explanation: There are at-most three trains at a time (time between 9:40 to 12:00)

Input: arr[] = {9:00, 9:40} 
dep[] = {9:10, 12:00} 
Output: 1 
Explanation: Only one platform is needed.
"""

def findPlatform(arr, dep, n):
	# Sort arrival and departure arrays
	arr.sort()
	dep.sort()

	# plat_needed indicates number of platforms needed at a time
	plat_needed = 1
	result = 1
	i = 1
	j = 0

	# Similar to merge in merge sort to process all events in sorted order
	while (i < n and j < n):
		# If next event in sorted order is arrival, increment count of platforms needed
		if (arr[i] <= dep[j]):
			plat_needed += 1
			i += 1
		else:
			plat_needed -= 1
			j += 1

		# Update result if needed
		if (plat_needed > result):
			result = plat_needed
	return result

arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
n = len(arr)
print("Minimum Number of Platforms Required = ",
	findPlatform(arr, dep, n))
```

## [Buy Maximum Stocks if i stocks can be bought on i-th day](https://www.geeksforgeeks.org/buy-maximum-stocks-stocks-can-bought-th-day/)

```python
"""
In a stock market, there is a product with its infinite stocks. The stock prices are given for N days, where arr[i] denotes the price of the stock on the ith day. There is a rule that a customer can buy at most i stock on the ith day. If the customer has an amount of k amount of money initially, find out the maximum number of stocks a customer can buy. 

For example, for 3 days the price of a stock is given as 7, 10, 4. You can buy 1 stock worth 7 rs on day 1, 2 stocks worth 10 rs each on day 2 and 3 stock worth 4 rs each on day 3.

Examples: 

Input : price[] = { 10, 7, 19 }, 
              k = 45.
Output : 4
A customer purchases 1 stock on day 1, 
2 stocks on day 2 and 1 stock on day 3 for 
10, 7 * 2 = 14 and 19 respectively. Hence, 
total amount is 10 + 14 + 19 = 43 and number 
of stocks purchased is 4.

Input  : price[] = { 7, 10, 4 }, 
               k = 100.
Output : 6
"""

def buyMaximumProducts(n, k, price):
	# Making pair of stock cost and day number
	arr = [[i + 1, price[i]] for i in range(n)]

	# Sort based on the price of stock
	arr.sort(key = lambda x: x[1])

	# Calculating the max stocks purchased
	total_purchase = 0
	for i in range(n):
		P = min(arr[i][0], k//arr[i][1])
		total_purchase += P
		k -= (P * arr[i][1])
	return total_purchase

price = [ 10, 7, 19 ]
n = len(price)
k = 45
print(buyMaximumProducts(n, k, price))
```

## [Find the minimum and maximum amount to buy all N candies](https://practice.geeksforgeeks.org/problems/shop-in-candy-store/0)

```python
"""
In a candy store, there are N different types of candies available and the prices of all the N different types of candies are provided. There is also an attractive offer by the candy store. We can buy a single candy from the store and get at most K other candies (all are different types) for free.

Find the minimum amount of money we have to spend to buy all the N different candies.
Find the maximum amount of money we have to spend to buy all the N different candies.
In both cases, we must utilize the offer and get the maximum possible candies back. If k or more candies are available, we must take k candies for every candy purchase. If less than k candies are available, we must take all candies for a candy purchase.

Examples: 

	Input :  
	price[] = {3, 2, 1, 4}
	k = 2
	Output :  
	Min = 3, Max = 7
	Explanation :
	Since k is 2, if we buy one candy we can take  atmost two more for free. So in the first case we buy the candy which  costs 1 and take candies worth 3 and 4 for  free, also you buy candy worth 2 as well. So min cost = 1 + 2 = 3. In the second case we buy the candy which  costs 4 and take candies worth 1 and 2 for  free, also We buy candy worth 3 as well. So max cost = 3 + 4 = 7.

One important thing to note is, we must use the offer and get maximum candies back for every candy purchase. So if we want to minimize the money, we must buy candies at minimum cost and get candies of maximum costs for free
"""

from math import ceil

# function to find the maximum and the minimum cost required
def find(arr,n,k):
	
	# Sort the array
	arr.sort()
	b = int(ceil(n/k))
	
	# print the minimum cost
	print("minimum ",sum(arr[:b]))
	
	# print the maximum cost
	print("maximum ", sum(arr[-b:]))
	
arr = [3, 2, 1, 4]
n = len(arr)
k = 2
find(arr,n,k)
```


## [Minimum Cost to cut a board into squares](https://www.geeksforgeeks.org/minimum-cost-cut-board-squares/)

```python
"""
A board of length m and width n is given, we need to break this board into m*n squares such that cost of breaking is minimum. cutting cost for each edge will be given for the board. In short, we need to choose such a sequence of cutting such that cost is minimized. 
https://media.geeksforgeeks.org/wp-content/cdn-uploads/board.png
For above board optimal way to cut into square is:
Total minimum cost in above case is 42. It is 
evaluated using following steps.

Initial Value : Total_cost = 0
Total_cost = Total_cost + edge_cost * total_pieces

Cost 4 Horizontal cut         Cost = 0 + 4*1 = 4
Cost 4 Vertical cut        Cost = 4 + 4*2 = 12
Cost 3 Vertical cut        Cost = 12 + 3*2 = 18
Cost 2 Horizontal cut        Cost = 18 + 2*3 = 24
Cost 2 Vertical cut        Cost = 24 + 2*3 = 30
Cost 1 Horizontal cut        Cost = 30 + 1*4 = 34
Cost 1 Vertical cut        Cost = 34 + 1*4 = 38
Cost 1 Vertical cut        Cost = 38 + 1*4 = 42
"""


def minimumCostOfBreaking(X, Y, m, n):
	res = 0
	# sort the horizontal cost in reverse order
	X.sort(reverse = True)
	# sort the vertical cost in reverse order
	Y.sort(reverse = True)
	# initialize current width as 1
	hzntl = 1; vert = 1

	# loop until one or both cost array are processed
	i = 0; j = 0
	while (i < m and j < n):
		if (X[i] > Y[j]):
			res += X[i] * vert
			# increase current horizontal part count by 1
			hzntl += 1
			i += 1
		
		else:
			res += Y[j] * hzntl
			# increase current vertical part count by 1
			vert += 1
			j += 1

	# loop for horizontal array, if remains
	total = 0
	while (i < m):
		total += X[i]
		i += 1
	res += total * vert

	#loop for vertical array, if remains
	total = 0
	while (j < n):
		total += Y[j]
		j += 1
	res += total * hzntl
	return res
	
m = 6; n = 4
X = [2, 1, 3, 1, 4]
Y = [4, 1, 2]
print(minimumCostOfBreaking(X, Y, m-1, n-1))
```

## [Check if it is possible to survive on Island](https://www.geeksforgeeks.org/survival/)

```python
"""
You are a poor person in an island. There is only one shop in this island, this shop is open on all days of the week except for Sunday. Consider following constraints: 

N – Maximum unit of food you can buy each day.
S – Number of days you are required to survive.
M – Unit of food required each day to survive.
Currently, it’s Monday, and you need to survive for the next S days. 
Find the minimum number of days on which you need to buy food from the shop so that you can survive the next S days, or determine that it isn’t possible to survive. 
Examples: 

Input : S = 10 N = 16 M = 2 
Output : Yes 2 
Explanation 1: One possible solution is to buy a box on the first day (Monday), it’s sufficient to eat from this box up to 8th day (Monday) inclusive. Now, on the 9th day (Tuesday), you buy another box and use the chocolates in it to survive the 9th and 10th day.
Input : 10 20 30 
Output : No 
Explanation 2: You can’t survive even if you buy food because the maximum number of units you can buy in one day is less the required food for one day.
"""


def survival(S, N, M):
# If we can not buy at least a week supply of food during the first week OR We can not buy a day supply of food on the first day then we can't survive.
	if (((N * 6) < (M * 7) and S > 6) or M > N):
		print("No")
	else:
	# If we can survive then we can buy ceil(A / N) times where A is total units of food required.
		days = (M * S) / N
		if (((M * S) % N) != 0):
			days += 1
		print("Yes "),
		print(days)


S = 10; N = 16; M = 2
survival(S, N, M)
```

## [Maximum product subset of an array](https://www.geeksforgeeks.org/maximum-product-subset-array/)

```python
"""
Given an array a, we have to find maximum product possible with the subset of elements present in the array. The maximum product can be single element also.
Examples: 

Input: a[] = { -1, -1, -2, 4, 3 }
Output: 24
Explanation : Maximum product will be ( -2 * -1 * 4 * 3 ) = 24

Input: a[] = { -1, 0 }
Output: 0
Explanation: 0(single element) is maximum product possible
 
Input: a[] = { 0, 0, 0 }
Output: 0
"""

def maxProductSubset(a, n):
	if n == 1:
		return a[0]

	# Find count of negative numbers, count of zeros, negative number with least absolute value and product of non-zero numbers
	max_neg = -999999999999
	count_neg = 0
	count_zero = 0
	prod = 1
	for i in range(n):

		# If number is 0, we don't multiply it with product.
		if a[i] == 0:
			count_zero += 1
			continue

		# Count negatives and keep track of negative number with least absolute value.
		if a[i] < 0:
			count_neg += 1
			max_neg = max(max_neg, a[i])
		prod = prod * a[i]

	# If there are all zeros
	if count_zero == n:
		return 0

	# If there are odd number of negative numbers
	if count_neg & 1:
		# Exceptional case: There is only negative and all other are zeros
		if (count_neg == 1 and count_zero > 0 and
			count_zero + count_neg == n):
			return 0
		# Otherwise result is product of all non-zeros divided by negative number with least absolute value
		prod = int(prod / max_neg)
	return prod

a = [ -1, -1, -2, 4, 3 ]
n = len(a)
print(maxProductSubset(a, n))
```

## [Maximize array sum after K negations](https://practice.geeksforgeeks.org/problems/maximize-sum-after-k-negations/0)

```python
"""
Given an array of size n and a number k. We must modify array K a number of times. Here modify array means in each operation we can replace any array element arr[i] by -arr[i]. We need to perform this operation in such a way that after K operations, the sum of the array must be maximum?

Examples : 

Input : arr[] = {-2, 0, 5, -1, 2}, K = 4
Output: 10
Explanation:
1. Replace (-2) by -(-2), array becomes {2, 0, 5, -1, 2}
2. Replace (-1) by -(-1), array becomes {2, 0, 5, 1, 2}
3. Replace (0) by -(0), array becomes {2, 0, 5, 1, 2}
4. Replace (0) by -(0), array becomes {2, 0, 5, 1, 2}

Input : arr[] = {9, 8, 8, 5}, K = 3
Output: 20
"""

def sol(arr, k):
	# Sorting given array using in-built java sort function
	arr.sort()
	i = 0
	while (k > 0):
		# If we find a 0 in our sorted array, we stop
		if (arr[i] >= 0):
			k = 0
		else:
			arr[i] = (-1) * arr[i]
			k = k - 1
		i += 1
	return sum(arr[j] for j in range(len(arr)))

arr = [-2, 0, 5, -1, 2]
print(sol(arr, 4))
```

## [Maximize the sum of arr[i]*i](https://practice.geeksforgeeks.org/problems/maximize-arrii-of-an-array/0)

```python
"""
Given an array of N integers. You are allowed to rearrange the elements of the array. The task is to find the maximum value of Σarr[i]*i, where i = 0, 1, 2,…., n – 1.

Examples:  

Input : N = 4, arr[] = { 3, 5, 6, 1 }
Output : 31
If we arrange arr[] as { 1, 3, 5, 6 }. 
Sum of arr[i]*i is 1*0 + 3*1 + 5*2 + 6*3 
= 31, which is maximum

Input : N = 2, arr[] = { 19, 20 }
Output : 20
"""
def maxSum(arr,n):
    arr.sort()
    return sum(arr[i] * i for i in range(n))

arr = [3,5,6,1]
n = len(arr)
print(maxSum(arr,n))
```

## [Maximum sum of absolute difference of an array](https://www.geeksforgeeks.org/maximum-sum-absolute-difference-array/)

```python
"""
Given an array, we need to find the maximum sum of absolute difference of any permutation of the given array.
Examples: 
 

Input : { 1, 2, 4, 8 }
Output : 18
Explanation : For the given array there are 
several sequence possible
like : {2, 1, 4, 8}
       {4, 2, 1, 8} and some more.
Now, the absolute difference of an array sequence will be
like for this array sequence {1, 2, 4, 8}, the absolute
difference sum is 
= |1-2| + |2-4| + |4-8| + |8-1|
= 14
For the given array, we get the maximum value for
the sequence {1, 8, 2, 4}
= |1-8| + |8-2| + |2-4| + |4-1|
= 18
"""
import numpy as np

def MaxSumDifference(a,n):
	# sort the original array so that we can retrieve the large elements from the end of array elements
	np.sort(a);

	# In this loop first we will insert one smallest element not entered till that time in final sequence and then enter a highest element(not entered till that time) in final sequence so that we have large difference value. This process is repeated till all array has completely entered in sequence. Here, we have loop till n/2 because we are inserting two elements at a time in loop.
	j = 0
	finalSequence = [0 for _ in range(n)]
	for i in range(int(n / 2)):
		finalSequence[j] = a[i]
		finalSequence[j + 1] = a[n - i - 1]
		j = j + 2
		
	# If there are odd elements, push the  middle element at the end.
	if (n % 2 != 0):
		finalSequence[n-1] = a[n//2 + 1]
	# variable to store the maximum sum of absolute difference
	MaximumSum = 0

	# In this loop absolute difference of elements for the final sequence is calculated.
	for i in range(n - 1):
		MaximumSum = (MaximumSum + abs(finalSequence[i] - finalSequence[i + 1]))

	# absolute difference of last element and 1st element
	MaximumSum = (MaximumSum + abs(finalSequence[n - 1] - 	finalSequence[0]));
	print (MaximumSum)

a = [ 1, 2, 4, 8 ]
n = len(a)
MaxSumDifference(a, n);
```

## [Maximize sum of consecutive differences in a circular array](https://practice.geeksforgeeks.org/problems/swap-and-maximize/0)

```python
"""
Given an array of n elements. Consider array as circular array i.e element after an is a1. The task is to find maximum mysum of the difference between consecutive elements with rearrangement of array element allowed i.e after rearrangement of element find |a1 – a2| + |a2 – a3| + …… + |an – 1 – an| + |an – a1|. 

Examples: 

Input : arr[] = { 4, 2, 1, 8 }
Output : 18
Rearrange given array as : { 1, 8, 2, 4 }
mysum of difference between consecutive element
= |1 - 8| + |8 - 2| + |2 - 4| + |4 - 1|
= 7 + 6 + 2 + 3
= 18.

Input : arr[] = { 10, 12, 15 }
Output : 10
"""

def maxSum(arr, n):
    mysum = 0
    arr.sort()
    # Subtracting a1, a2, a3,....., a(n/2)-1, an/2 twice and adding a(n/2)+1, a(n/2)+2, a(n/2)+3,. ...., an - 1, an twice.
    for i in range(int(n / 2)):
        mysum -= (2 * arr[i])
        mysum += (2 * arr[n - i - 1])
    return mysum
 
arr = [4, 2, 1, 8]
n = len(arr)
print (maxSum(arr, n))
```

## [Minimum sum of absolute difference of pairs of two arrays](https://www.geeksforgeeks.org/minimum-sum-absolute-difference-pairs-two-arrays/)

```python
"""
Given two arrays a[] and b[] of equal length n. The task is to pair each element of array a to an element in array b, such that mysum S of absolute differences of all the pairs is minimum.
Suppose, two elements a[i] and a[j] (i != j) of a are paired with elements b[p] and b[q] of b respectively, 
then p should not be equal to q.

Examples: 

Input :  a[] = {3, 2, 1}
         b[] = {2, 1, 3}
Output : 0
Explanation :
 1st pairing: |3 - 2| + |2 - 1| + |1 - 3|
         = 1 + 1 + 2 = 4
 2nd pairing: |3 - 2| + |1 - 1| + |2 - 3|
         = 1 + 0 + 1 = 2
 3rd pairing: |2 - 2| + |3 - 1| + |1 - 3|
         = 0 + 2 + 2 = 4
 4th pairing: |1 - 2| + |2 - 1| + |3 - 3|
         = 1 + 1 + 0 = 2
 5th pairing: |2 - 2| + |1 - 1| + |3 - 3|
         = 0 + 0 + 0 = 0
 6th pairing: |1 - 2| + |3 - 1| + |2 - 3|
         = 1 + 2 + 1 = 4
 Therefore, 5th pairing has minimum mysum of
 absolute difference.

Input :  n = 4
         a[] = {4, 1, 8, 7}
         b[] = {2, 3, 6, 5}
Output : 6
"""

def findMinSum(a, b, n):
	# Sort both arrays
	a.sort()
	b.sort()
	# Find mysum of absolute differences
	mysum = 0
	
	for i in range(n):
		mysum = mysum + abs(a[i] - b[i])
	return mysum

# Both a[] and b[] must be of same size.
a = [4, 1, 8, 7]
b = [2, 3, 6, 5]
n = len(a)
print(findMinSum(a, b, n))

```

## [Program for Shortest Job First (or SJF) CPU Scheduling](https://www.geeksforgeeks.org/program-for-shortest-job-first-or-sjf-cpu-scheduling-set-1-non-preemptive/)

```python
TODO
```

## [Smallest subset with sum greater than all other elements](https://www.geeksforgeeks.org/smallest-subset-sum-greater-elements/)

```python
"""
Given an array of non-negative integers. Our task is to find minimum number of elements such that their sum should be greater than the sum of rest of the elements of the array.
Examples : 
 

Input : arr[] = {3, 1, 7, 1}
Output : 1
Smallest subset is {7}. Sum of
this subset is greater than all
other elements {3, 1, 1}
"""

def minElements(arr , n):
	# calculating HALF of array sum
	halfSum = 0
	for i in range(n):
		halfSum = halfSum + arr[i]
	halfSum = int(halfSum / 2)
	# sort the array in descending order.
	arr.sort(reverse = True)
	
	res = 0
	curr_sum = 0
	for i in range(n):
		
		curr_sum += arr[i]
		res += 1

		# current sum greater than sum
		if curr_sum > halfSum:
			return res
	return res
	

arr = [3, 1, 7, 1]
n = len(arr)
print(minElements(arr, n) )
```

## [Chocolate Distribution Problem](https://practice.geeksforgeeks.org/problems/chocolate-distribution-problem/0)

```python
"""
Given an array of n integers where each value represents the number of chocolates in a packet. Each packet can have a variable number of chocolates. There are m students, the task is to distribute chocolate packets such that: 

Each student gets one packet.
The difference between the number of chocolates in the packet with maximum chocolates and packet with minimum chocolates given to the students is minimum.
Examples:

Input : arr[] = {7, 3, 2, 4, 9, 12, 56} , m = 3 
Output: Minimum Difference is 2 
Explanation:
We have seven packets of chocolates and 
we need to pick three packets for 3 students 
If we pick 2, 3 and 4, we get the minimum 
difference between maximum and minimum packet 
sizes.
"""

# arr[0..n-1] represents sizes of packets m is number of students. Returns minimum difference between maximum and minimum values of distribution.
def findMinDiff(arr, n, m):

	# if there are no chocolates or number of students is 0
	if (m==0 or n==0):
		return 0

	# Sort the given packets
	arr.sort()

	# Number of students cannot be more than number of packets
	if (n < m):
		return -1

	# Largest number of chocolates
	min_diff = arr[n-1] - arr[0]

	# Find the subarray of size m such that difference between last (maximum in case of sorted) and first (minimum in case of sorted) elements of subarray is minimum.
	for i in range(len(arr) - m + 1):
		min_diff = min(min_diff , arr[i + m - 1] - arr[i])
	return min_diff

arr = [12, 4, 7, 9, 2, 23, 25, 41, 30, 40, 28, 42, 30, 44, 48, 43, 50]
m = 7 # Number of students
n = len(arr)
print("Minimum difference is", findMinDiff(arr, n, m))
```

## [DEFKIN -Defense of a Kingdom](https://www.spoj.com/problems/DEFKIN/)

```python
TODO
```

## [DIEHARD -DIE HARD](https://www.spoj.com/problems/DIEHARD/)

```python
TODO
```

## [GERGOVIA -Wine trading in Gergovia](https://www.spoj.com/problems/GERGOVIA/)

```python
TODO
```

## [Picking Up Chicks](https://www.spoj.com/problems/GCJ101BB/)

```python
TODO
```

## [CHOCOLA –Chocolate](https://www.spoj.com/problems/CHOCOLA/)

```python
TODO
```

## [ARRANGE -Arranging Amplifiers](https://www.spoj.com/problems/ARRANGE/)

```python
TODO
```

## [K Centers Problem](https://www.geeksforgeeks.org/k-centers-problem-set-1-greedy-approximate-algorithm/)

```python
def maxindex(dist, n):
	mi = 0
	for i in range(n):
		if (dist[i] > dist[mi]):
			mi = i
	return mi

def selectKcities(n, weights, k):
	dist = [0]*n
	centers = []

	for i in range(n):
		dist[i] = 10**9
	# index of city having the maximum distance to it's closest center
	mymax = 0
	for i in range(k):
		centers.append(mymax)
		for j in range(n):

			# updating the distance of the cities to their closest centers
			dist[j] = min(dist[j], weights[mymax][j])

		# updating the index of the city with the maximum distance to it's closest center
		mymax = maxindex(dist, n)

	# Printing the maximum distance of a city to a center that is our answer print()
	print(dist[mymax])

	# Printing the cities that were chosen to be made centers
	for i in centers:
		print(i, end = " ")


n = 4
weights = [ [ 0, 4, 8, 5 ],
		[ 4, 0, 10, 7 ],
		[ 8, 10, 0, 9 ],
		[ 5, 7, 9, 0 ] ]
k = 2
selectKcities(n, weights, k)
```

## [Minimum Cost of ropes](https://practice.geeksforgeeks.org/problems/minimum-cost-of-ropes/0)

```python
"""There are given n ropes of different lengths, we need to connect these ropes into one rope. The cost to connect two ropes is equal to the sum of their lengths. We need to connect the ropes with minimum cost.

For example, if we are given 4 ropes of lengths 4, 3, 2, and 6. We can connect the ropes in the following ways. 

First, connect ropes of lengths 2 and 3. Now we have three ropes of lengths 4, 6, and 5. 
Now connect ropes of lengths 4 and 5. Now we have two ropes of lengths 6 and 9. 
Finally connect the two ropes and all ropes have connected.
Total cost for connecting all ropes is 5 + 9 + 15 = 29. This is the optimized cost for connecting ropes. Other ways of connecting ropes would always have same or more cost. For example, if we connect 4 and 6 first (we get three strings of 3, 2, and 10), then connect 10 and 3 (we get two strings of 13 and 2). Finally, we connect 13 and 2. Total cost in this way is 10 + 13 + 15 = 38.
"""

import heapq
def minCost(arr, n):
	
	# Create a priority queue out of the given list
	heapq.heapify(arr)
	
	# Initialize result
	res = 0
	
	# While size of priority queue is more than 1
	while(len(arr) > 1):
		
		# Extract shortest two ropes from arr
		first = heapq.heappop(arr)
		second = heapq.heappop(arr)
		
		#Connect the ropes: update result and insert the new rope to arr
		res += first + second
		heapq.heappush(arr, first + second)
	return res

lengths = [ 4, 3, 2, 6 ]
size = len(lengths)
print(f"Total cost for connecting ropes is {str(minCost(lengths, size))}")
```

## [Find smallest number with given number of digits and sum of digits](https://practice.geeksforgeeks.org/problems/smallest-number5829/1)

```python
"""
How to find the smallest number with given digit sum s and number of digits d? 
Examples : 

Input  : s = 9, d = 2
Output : 18
There are many other possible numbers like 45, 54, 90, etc with sum of digit as 9 and number of digits as 2. The smallest of them is 18.

Input  : s = 20, d = 3
Output : 299
"""

def findSmallest(m,s):

	# If sum of digits is 0, then a number is possible only if number of digits is 1.
	if (s == 0):		
		if(m == 1) :
			print("Smallest number is 0")
		else :
			print("Not possible")
		return

	# Sum greater than the maximum possible sum.
	if (s > 9*m):
		print("Not possible")
		return

	# Create an array to store digits of result
	res = [0 for _ in range(m+1)]

	# deduct sum by one to account for cases later (There must be 1 left for the most significant digit)
	s -= 1

	# Fill last m-1 digits (from right to left)
	for i in range(m-1,0,-1):

		# If sum is still greater than 9, digit must be 9.
		if (s > 9):

			res[i] = 9
			s -= 9

		else:

			res[i] = s
			s = 0

	# Whatever is left should be the most significant digit. The initially subtracted 1 is incorporated here.
	res[0] = s + 1
	print("Smallest number is ",end="")
	for i in range(m):
		print(res[i],end="")

s = 9
m = 2
findSmallest(m, s)
```

## [Rearrange characters in a string such that no two adjacent are same](https://practice.geeksforgeeks.org/problems/rearrange-characters/0)

```python
"""
Given a string with repeated characters, the task is to rearrange characters in a string so that no two adjacent characters are same.
Note : It may be assumed that the string has only lowercase English alphabets.

Examples:  

Input: aaabc 
Output: abaca 

Input: aaabb
Output: ababa 

Input: aa 
Output: Not Possible
"""

def getMaxCountChar(count):
  maxCount = 0
  for i in range(26):
    if count[i] > maxCount:
        maxCount = count[i]
        maxChar = chr(i + ord('a'))
 
  return maxCount, maxChar
 
# Main function for rearranging the characters
def rearrangeString(S):
  n = len(S)
   
  # if length of string is None return False
  if not n:
      return False
     
  # create a hashmap for the alphabets
  count = [0] * 26
  for char in S:
      count[ord(char) - ord('a')] += 1
 
 
  maxCount, maxChar = getMaxCountChar(count)
 
  # if the char with maximum frequency is more than the half of the total length of the string than return False
  if maxCount > (n + 1) // 2:
      return False
 
  # create a list for storing the result
  res = [None] * n
  ind = 0
 
  # place all occurrences of the char with maximum frequency in even positions
  while maxCount:
      res[ind] = maxChar
      ind += 2
      maxCount -= 1
       
  # replace the count of the char with maximum frequency to zero as all the maxChar are already placed in the result
  count[ord(maxChar) - ord('a')] = 0
 
  # place all other char in the result starting from remaining even positions and then place in the odd positions
  for i in range(26):
      while count[i] > 0:
          if ind >= n:
              ind = 1
          res[ind] = chr(i + ord('a') )
          ind += 2
          count[i] -= 1
 
 
  # convert the result list to string and return
  return ''.join(res)
 

myStr = 'bbbaa'
if res := rearrangeString(myStr):
  print(res)
else:
  print('Not valid string')
```

## [Find maximum sum possible equal sum of three stacks](https://www.geeksforgeeks.org/find-maximum-sum-possible-equal-sum-three-stacks/)

```python
"""
Given three stacks of the positive numbers, the task is to find the possible equal maximum sum of the stacks with the removal of top elements allowed. Stacks are represented as an array, and the first index of the array represent the top element of the stack.

Examples: 

Input : stack1[] = { 3, 10}
  stack2[] = { 4, 5 }
  stack3[] = { 2, 1 }
Output : 0
Sum can only be equal after removing all elements 
from all stacks.
"""
def maxSum(stack1, stack2, stack3, n1, n2, n3):
	sum1, sum2, sum3 = 0, 0, 0
	
	# Finding the initial sum of stack1.
	for i in range(n1):
		sum1 += stack1[i]
	
	# Finding the initial sum of stack2.
	for i in range(n2):
		sum2 += stack2[i]
	
	# Finding the initial sum of stack3.
	for i in range(n3):
		sum3 += stack3[i]

# As given in question, first element is top of stack..
	top1, top2, top3 = 0, 0, 0
	ans = 0
	
	while True:
	# If any stack is empty
		if (top1 == n1 or top2 == n2 or top3 == n3):
			return 0
	# If sum of all three stack are equal.
		if sum1 == sum2 == sum3:
			return sum1

	# Finding the stack with maximum sum and removing its top element.
		if (sum1 >= sum2 and sum1 >= sum3):
			sum1 -= stack1[top1]
			top1=top1+1
		elif (sum2 >= sum1 and sum2 >= sum3):
			sum2 -= stack2[top2]
			top2=top2+1
		elif (sum3 >= sum2 and sum3 >= sum1):
			sum3 -= stack3[top3]
			top3=top3+1


stack1 = [ 3, 2, 1, 1, 1 ]
stack2 = [ 4, 3, 2 ]
stack3 = [ 1, 1, 4, 1 ]
n1 = len(stack1)
n2 = len(stack2)
n3 = len(stack3)
print (maxSum(stack1, stack2, stack3, n1, n2, n3))
```

# Heap

## [Implement a Maxheap/MinHeap using arrays and recursion. (Heapify)](https://www.geeksforgeeks.org/building-heap-from-array/)

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

## [Sort an Array using heap. (HeapSort)](https://www.geeksforgeeks.org/heap-sort/)

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

## [Maximum of all subarrays of size k.](https://www.geeksforgeeks.org/sliding-window-maximum-maximum-of-all-subarrays-of-size-k/)

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

## [“k” largest element in an array](https://practice.geeksforgeeks.org/problems/k-largest-elements4206/1)

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

## [Kth smallest and largest element in an unsorted array](https://www.geeksforgeeks.org/kth-smallestlargest-element-unsorted-array/)

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

## [Merge “K” sorted arrays. [ IMP ]](https://practice.geeksforgeeks.org/problems/merge-k-sorted-arrays/1)

```python
TODO
```

## [Merge 2 Binary Max Heaps](https://practice.geeksforgeeks.org/problems/merge-two-binary-max-heap/0)

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

## [Kth largest sum continuous subarrays](https://www.geeksforgeeks.org/k-th-largest-sum-contiguous-subarray/)

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

## [Merge “K” Sorted Linked Lists [V.IMP]](https://practice.geeksforgeeks.org/problems/merge-k-sorted-linked-lists/1)

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

## [Smallest range in “K” Lists](https://practice.geeksforgeeks.org/problems/find-smallest-range-containing-elements-from-k-lists/1)

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

## [Median in a stream of Integers](https://practice.geeksforgeeks.org/problems/find-median-in-a-stream/0)

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

## [Check if a Binary Tree is Heap](https://practice.geeksforgeeks.org/problems/is-binary-tree-heap/1)

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

## [Convert BST to Min Heap](https://www.geeksforgeeks.org/convert-bst-min-heap/)

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

## [Convert min heap to max heap](https://www.geeksforgeeks.org/convert-min-heap-to-max-heap/)

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


## [Minimum sum of two numbers formed from digits of an array](https://practice.geeksforgeeks.org/problems/minimum-sum4058/1)

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

# Linked List

## [Write a Program to reverse the Linked List. (Both Iterative and recursive)](https://www.geeksforgeeks.org/reverse-a-linked-list/)

```python
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def reverse(self):
		prev = None
		current = self.head
		while current is not None:
			next = current.next
			current.next = prev
			prev = current
			current = next
		self.head = prev

	# Function to insert a new node at the beginning
	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	# Utility function to print the linked LinkedList
	def printList(self):
		temp = self.head
		while(temp):
			print (temp.data)
			temp = temp.next


llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(85)
print ("Given Linked List")
llist.printList()
llist.reverse()
print ("\nReversed Linked List")
llist.printList()
```

## [Reverse a Linked List in group of Given Size. [Very Imp]](https://practice.geeksforgeeks.org/problems/reverse-a-linked-list-in-groups-of-given-size/1)

```python
class Node(object):
	def __init__(self, data = None, next = None):
		self.data = data
		self.next = next

	def __repr__(self):
		return repr(self.data)

class LinkedList(object):
	def __init__(self):
		self.head = None

	def __repr__(self):
		nodes = []
		curr = self.head
		while curr:
			nodes.append(repr(curr))
			curr = curr.next
		return '[' + ', '.join(nodes) + ']'

	# Function to insert a new node at the beginning
	def prepend(self, data):
		self.head = Node(data = data,
						next = self.head)

	# Reverses the linked list in groups of size k and returns the pointer to the new head node.
	def reverse(self, k = 1):
		if self.head is None:
			return

		curr = self.head
		prev = None
		new_stack = []
		while curr is not None:
			val = 0
			
			# Terminate the loop whichever comes first either current == None or value >= k
			while curr is not None and val < k:
				new_stack.append(curr.data)
				curr = curr.next
				val += 1

			# Now pop the elements of stack one by one
			while new_stack:
				
				# If final list has not been started yet.
				if prev is None:
					prev = Node(new_stack.pop())
					self.head = prev
				else:
					prev.next = Node(new_stack.pop())
					prev = prev.next
					
		# Next of last element will point to None.
		prev.next = None
		return self.head

# Driver Code
llist = LinkedList()
llist.prepend(9)
llist.prepend(8)
llist.prepend(7)
llist.prepend(6)
llist.prepend(5)
llist.prepend(4)
llist.prepend(3)
llist.prepend(2)
llist.prepend(1)

print("Given linked list")
print(llist)
llist.head = llist.reverse(3)

print("Reversed Linked list")
print(llist)

```

## [Write a program to Detect and Delete loop in a linked list.](https://practice.geeksforgeeks.org/problems/remove-loop-in-linked-list/1)

```python
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def detectAndRemoveLoop(self):
		slow_p = fast_p = self.head
		while(slow_p and fast_p and fast_p.next):
			slow_p = slow_p.next
			fast_p = fast_p.next.next

			# If slow_p and fast_p meet at some point then there is a loop
			if slow_p == fast_p:
				self.removeLoop(slow_p)
		
				# Return 1 to indicate that loop is found
				return 1
		
		# Return 0 to indicate that there is no loop
		return 0

	# Function to remove loop
	# loop_node --> pointer to one of the loop nodes
	# head --> Pointer to the start node of the linked list
	def removeLoop(self, loop_node):
		ptr1 = loop_node
		ptr2 = loop_node
		# Count the number of nodes in loop
		k = 1
		while(ptr1.next != ptr2):
			ptr1 = ptr1.next
			k += 1

		# Fix one pointer to head
		ptr1 = self.head
		# And the other pointer to k nodes after head
		ptr2 = self.head
		for _ in range(k):
			ptr2 = ptr2.next

		# Move both pointers at the same place they will meet at loop starting node
		while(ptr2 != ptr1):
			ptr1 = ptr1.next
			ptr2 = ptr2.next

		# Get pointer to the last node
		while(ptr2.next != ptr1):
			ptr2 = ptr2.next

		# Set the next node of the loop ending node to fix the loop
		ptr2.next = None

	# Function to insert a new node at the beginning
	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	# Utility function to print the LinkedList
	def printList(self):
		temp = self.head
		while(temp):
			print(temp.data, end = ' ')
			temp = temp.next


llist = LinkedList()
llist.push(10)
llist.push(4)
llist.push(15)
llist.push(20)
llist.push(50)
llist.head.next.next.next.next.next = llist.head.next.next
llist.detectAndRemoveLoop()
print("Linked List after removing loop")
llist.printList()
```

## [Find the starting point of the loop.](https://www.geeksforgeeks.org/find-first-node-of-loop-in-a-linked-list/)

```python
class Node:
	def __init__(self, key):
		self.key = key
		self.next = None

def newNode(key):  # sourcery skip: inline-immediately-returned-variable
	temp = Node(key)
	return temp

# A utility function to print a linked list
def printList(head):
	while head is not None:
		print(head.key, end = ' ')
		head = head.next
	print()
	
# Function to detect and remove loop in a linked list that may contain loop
def detectAndRemoveLoop(head):
	
	# If list is empty or has only one node without loop
	if head is None or head.next is None:
		return None

	slow = head
	fast = head

	# Move slow and fast 1 and 2 steps ahead respectively.
	slow = slow.next
	fast = fast.next.next

	# Search for loop using slow and fast pointers
	while (fast and fast.next) and slow != fast:
		slow = slow.next
		fast = fast.next.next

	# If loop does not exist
	if (slow != fast):
		return None

	# If loop exists. Start slow from head and fast from meeting point.
	slow = head

	while (slow != fast):
		slow = slow.next
		fast = fast.next

	return slow


	
head = newNode(50)
head.next = newNode(20)
head.next.next = newNode(15)
head.next.next.next = newNode(4)
head.next.next.next.next = newNode(10)
# create a loop for testing
head.next.next.next.next.next = head.next.next
res = detectAndRemoveLoop(head)

if res is None:
	print("Loop does not exist")
else:
	print(f"Loop starting node is {str(res.key)}")
```

## [Remove Duplicates in a sorted Linked List.](https://practice.geeksforgeeks.org/problems/remove-duplicate-element-from-sorted-linked-list/1)

```python
import math

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

# The function removes duplicates from the given linked list
def removeDuplicates(head):
	
	# Do nothing if the list consist of only one element or empty
	if head is None and head.next is None:
		return

	# Construct a pointer pointing towards head
	current = head

	# Initialise a while loop till the second last node of the linkedlist
	while (current.next):

		# If the data of current and next node is equal we will skip the node between them
		if current.data == current.next.data:
			current.next = current.next.next

		# If the data of current and next node is different move the pointer to the next node
		else:
			current = current.next

	return


def push(head_ref, new_data):
	new_node = Node(new_data)
	new_node.data = new_data
	new_node.next = head_ref	
	head_ref = new_node
	return head_ref

def printList(node):
	while (node != None):
		print(node.data, end = " ")
		node = node.next
	

head = None
head = push(head, 20)
head = push(head, 13)
head = push(head, 13)
head = push(head, 11)
head = push(head, 11)
head = push(head, 11)								
print("List before removal of duplicates ", end = "")
printList(head)
removeDuplicates(head)
print("\nList after removal of elements ", end = "")
printList(head)		
```

## [Remove Duplicates in a Un-sorted Linked List.](https://practice.geeksforgeeks.org/problems/remove-duplicates-from-an-unsorted-linked-list/1)

```python
class Node():
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList():
	def __init__(self):
		self.head = None

	def remove_duplicates(self):
		ptr1 = None
		ptr2 = None
		dup = None
		ptr1 = self.head

		# Pick elements one by one
		while (ptr1 != None and ptr1.next != None):
			ptr2 = ptr1
			# Compare the picked element with rest of the elements
			while (ptr2.next != None):
				# If duplicate then delete it
				if (ptr1.data == ptr2.next.data):
					# Sequence of steps is important here
					dup = ptr2.next
					ptr2.next = ptr2.next.next
				else:
					ptr2 = ptr2.next
			ptr1 = ptr1.next


	def printList(self):
		temp = self.head
		while(temp != None):
			print(temp.data, end=" ")
			temp = temp.next
		print()


list1 = LinkedList()
list1.head = Node(10)
list1.head.next = Node(12)
list1.head.next.next = Node(11)
list1.head.next.next.next = Node(11)
list1.head.next.next.next.next = Node(12)
list1.head.next.next.next.next.next = Node(11)
list1.head.next.next.next.next.next.next = Node(10)
print("Linked List before removing duplicates :")
list1.printList()
list1.remove_duplicates()
print()
print("Linked List after removing duplicates :")
list1.printList()
```

## [Write a Program to Move the last element to Front in a Linked List.](https://www.geeksforgeeks.org/move-last-element-to-front-of-a-given-linked-list/)

```python
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def push(self, data):
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node
		

	def printList(self):
		tmp = self.head
		while tmp is not None:
			print(tmp.data, end=", ")
			tmp = tmp.next
		print()

	# Function to bring the last node to the front
	def moveToFront(self):
		tmp = self.head
		sec_last = None # To maintain the track of  the second last node

	# To check whether we have not received the empty list or list with a single node
		if not tmp or not tmp.next:
			return

		# Iterate till the end to get the last and second last node
		while tmp and tmp.next :
			sec_last = tmp
			tmp = tmp.next

		# point the next of the second last node to None
		sec_last.next = None

		# Make the last node as the first Node
		tmp.next = self.head
		self.head = tmp


llist = LinkedList()
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)
print ("Linked List before moving last to front ")
llist.printList()
llist.moveToFront()
print ("Linked List after moving last to front ")
llist.printList()

```

## [Add “1” to a number represented as a Linked List.](https://practice.geeksforgeeks.org/problems/add-1-to-a-number-represented-as-linked-list/1)

```python
import sys
import math

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


def newNode(data):
	return Node(data)

def reverseList(head):
	if not head:
		return
	curNode = head
	prevNode = head
	nextNode = head.next
	curNode.next = None
	while(nextNode):
		curNode = nextNode
		nextNode = nextNode.next
		curNode.next = prevNode
		prevNode = curNode
	return curNode


def addOne(head):
	# Reverse linked list and add one to head
	head = reverseList(head)
	k = head
	carry = 0
	prev = None
	head.data += 1

	# update carry for next calculation
	while (head != None) and (head.data > 9 or carry > 0):
		prev = head
		head.data += carry
		carry = head.data // 10
		head.data %= 10
		head = head.next

	if carry > 0:
		prev.next = Node(carry)
	# Reverse the modified list
	return reverseList(k)

def printList(head):
	if not head:
		return
	while head:
		print(f"{head.data}", end="")
		head = head.next

head = newNode(1)
head.next = newNode(9)
head.next.next = newNode(9)
head.next.next.next = newNode(9)
print("List is: ", end="")
printList(head)
head = addOne(head)
print("\nResultant list is: ", end="")
printList(head)
```

## [Add two numbers represented by linked lists.](https://practice.geeksforgeeks.org/problems/add-two-numbers-represented-by-linked-lists/1)

```python
    class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	# Method to traverse list and return it in a format
	def traverse(self):
		linkedListStr = ""
		temp = self.head
		while temp:
			linkedListStr += f"{str(temp.data)} -> "
			temp = temp.next
		return f"{linkedListStr}NULL"

	# Method to insert data in linked list
	def insert(self, data):
		newNode = Node(data)
		if self.head is not None:
			newNode.next = self.head
		self.head = newNode

# Helper function to reverse the list
def reverse(Head):
	
	if (Head is None and
		Head.next is None):
		return Head
		
	prev = None
	curr = Head
	
	while curr:
		temp = curr.next
		curr.next = prev
		prev = curr
		curr = temp
		
	Head = prev
	return Head

# Function to add two lists
def listSum(l1, l2):

	if l1 is None:
		return l1
	if l2 is None:
		return l2

	# Reverse first list
	l1 = reverse(l1)

	# Reverse second list
	l2 = reverse(l2)

	# Storing head whose reverse is to be returned This is where which will be final node
	head = l1
	prev = None
	c = 0
	sum = 0
	while l1 is not None and l2 is not None:
		sum = c + l1.data + l2.data
		l1.data = sum % 10
		c = int(sum / 10)
		prev = l1
		l1 = l1.next
		l2 = l2.next
		
	if l1 is not None or l2 is not None:
		if l2 is not None:
			prev.next = l2
		l1 = prev.next
		
		while l1 is not None:
			sum = c + l1.data
			l1.data = sum % 10
			c = int(sum / 10)
			prev = l1
			l1 = l1.next	
	if c > 0:
		prev.next = Node(c)
	return reverse(head)
	

linkedList1 = LinkedList()
linkedList1.insert(3)
linkedList1.insert(6)
linkedList1.insert(5)

linkedList2 = LinkedList()
linkedList2.insert(2)
linkedList2.insert(4)
linkedList2.insert(8)

linkedList3 = LinkedList()
linkedList3.head = listSum(linkedList1.head, linkedList2.head)
print(linkedList3.traverse())
```

## [Intersection of two Sorted Linked List.](https://practice.geeksforgeeks.org/problems/intersection-of-two-sorted-linked-lists/1)

```python
class Node:
	def __init__(self):
		self.data = 0
		self.next = None

def printList(node):
	while (node != None):
		print(node.data, end=" ")
		node = node.next

def new_node(data):
	return Node()
	
def push(head_ref, new_data):
	new_node = Node()
	new_node.data = new_data
	new_node.next = head_ref
	head_ref = new_node
	return head_ref


def intersection(tmp1,tmp2,k):
	res = [0]*k
	set1 = set()
	while (tmp1 != None):
		set1.add(tmp1.data)
		tmp1 = tmp1.next
	cnt = 0
	while (tmp2 != None):
		if tmp2.data in set1:
			res[cnt] = tmp2.data
			cnt += 1
		tmp2 = tmp2.next
	return res

def printList(node):
	while (node != None):
		print(node.data, end=" ")
		node = node.next	

# Start with the empty lists
ll = None
ll1 = None
		
ll = push(ll , 7)
ll = push(ll , 6)
ll = push(ll , 5)
ll = push(ll , 4)
ll = push(ll , 3)
ll = push(ll , 2)
ll = push(ll , 1)
ll = push(ll , 0)
		
ll1 = push(ll1 , 7)
ll1 = push(ll1 , 6)
ll1 = push(ll1 , 5)
ll1 = push(ll1 , 4)
ll1 = push(ll1 , 3)
ll1 = push(ll1 , 12)
ll1 = push(ll1 , 0)
ll1 = push(ll1 , 9)

arr = intersection(ll , ll1 , 6)
print(arr)
```

## [Intersection Point of two Linked Lists.](https://practice.geeksforgeeks.org/problems/intersection-point-in-y-shapped-linked-lists/1)

```python
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

# function to get the intersection point of two linked lists head1 and head
def getIntersectionNode(head1, head2):
	while head2:
		temp = head1
		while temp:
			# if both Nodes are same
			if temp == head2:
				return head2
			temp = temp.next
		head2 = head2.next
	# intersection is not present between the lists
	return None

'''
Create two linked lists
1st 3->6->9->15->30
2nd 10->15->30
15 is the intersection point
'''
newNode = Node(10)
head1 = newNode
newNode = Node(3)
head2 = newNode
newNode = Node(6)
head2.next = newNode
newNode = Node(9)
head2.next.next = newNode
newNode = Node(15)
head1.next = newNode
head2.next.next.next = newNode
newNode = Node(30)
head1.next.next = newNode
if intersectionPoint := getIntersectionNode(head1, head2):
	print("Intersection Point:", intersectionPoint.data)
else:
	print(" No Intersection Point ")
```

## [Merge Sort For Linked lists.[Very Important]](https://practice.geeksforgeeks.org/problems/sort-a-linked-list/1)

```python
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None
	
	# push new value to linked list using append method
	def append(self, new_value):
		
		# Allocate new node
		new_node = Node(new_value)
		
		# if head is None, initialize it to new node
		if self.head is None:
			self.head = new_node
			return
		curr_node = self.head
		while curr_node.next is not None:
			curr_node = curr_node.next
			
		# Append the new node at the end of the linked list
		curr_node.next = new_node
		
	def sortedMerge(self, a, b):
		result = None
		
		# Base cases
		if a is None:
			return b
		if b is  None:
			return a
			
		# pick either a or b and recur..
		if a.data <= b.data:
			result = a
			result.next = self.sortedMerge(a.next, b)
		else:
			result = b
			result.next = self.sortedMerge(a, b.next)
		return result
	
	def mergeSort(self, h):
		# Base case if head is None
		if h is None or h.next is None:
			return h

		# get the middle of the list
		middle = self.getMiddle(h)
		nexttomiddle = middle.next

		# set the next of middle node to None
		middle.next = None

		# Apply mergeSort on left list
		left = self.mergeSort(h)

		# Apply mergeSort on right list
		right = self.mergeSort(nexttomiddle)

		return self.sortedMerge(left, right)

	def getMiddle(self, head):
		if head is None:
			return head
		slow = head
		fast = head
		while (fast.next != None and
			fast.next.next != None):
			slow = slow.next
			fast = fast.next.next
		return slow
		
def printList(head):
	if head is None:
		print(' ')
		return
	curr_node = head
	while curr_node:
		print(curr_node.data, end = " ")
		curr_node = curr_node.next
	print(' ')
	

li = LinkedList()
li.append(15)
li.append(10)
li.append(5)
li.append(20)
li.append(3)
li.append(2)
li.head = li.mergeSort(li.head)
print ("Sorted Linked List is:")
printList(li.head)
```

## [Quicksort for Linked Lists.[Very Important]](https://practice.geeksforgeeks.org/problems/quick-sort-on-linked-list/1)

```python
class Node:
	def __init__(self, val):
		self.data = val
		self.next = None

class QuickSortLinkedList:
	def __init__(self):
		self.head=None

	def addNode(self,data):
		if self.head is None:
			self.head = Node(data)
			return
		curr = self.head
		while (curr.next != None):
			curr = curr.next
		newNode = Node(data)
		curr.next = newNode

	def printList(self,n):
		while (n != None):
			print(n.data, end=" ")
			n = n.next

	''' takes first and last node,but do not
	break any links in the whole linked list'''
	def paritionLast(self,start, end):
		if start == end or start is None or end is None:
			return start

		pivot_prev = start
		curr = start
		pivot = end.data

		'''iterate till one before the end,
		no need to iterate till the end because end is pivot'''

		while (start != end):
			if (start.data < pivot):

				# keep tracks of last modified item
				pivot_prev = curr
				temp = curr.data
				curr.data = start.data
				start.data = temp
				curr = curr.next
			start = start.next

		'''swap the position of curr i.e. next suitable index and pivot'''
		temp = curr.data
		curr.data = pivot
		end.data = temp

		''' return one previous to current because current is now pointing to pivot '''
		return pivot_prev

	def sort(self, start, end):
		if start is None or start == end or start == end.next:
			return

		# split list and partition recurse
		pivot_prev = self.paritionLast(start, end)
		self.sort(start, pivot_prev)

		'''
		if pivot is picked and moved to the start, that means start and pivot is same so pick from next of pivot
		'''
		if(pivot_prev != None and pivot_prev == start):
			self.sort(pivot_prev.next, end)

		# if pivot is in between of the list,start from next of pivot, since we have pivot_prev, so we move two nodes
		elif (pivot_prev != None and pivot_prev.next != None):
			self.sort(pivot_prev.next.next, end)


ll = QuickSortLinkedList()
ll.addNode(30)
ll.addNode(3)
ll.addNode(4)
ll.addNode(20)
ll.addNode(5)
n = ll.head
while n.next is not None:
	n = n.next
print("\nLinked List before sorting")
ll.printList(ll.head)
ll.sort(ll.head, n)
print("\nLinked List after sorting");
ll.printList(ll.head)

```

## [Find the middle Element of a linked list.](https://leetcode.com/problems/middle-of-the-linked-list/)

```python
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None 


class LinkedList:
	def __init__(self):
		self.head = None

	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	def printList(self):
		node = self.head
		while node:
			print(f"{str(node.data)}->", end="")
			node = node.next
		print("NULL")


	def printMiddle(self):
		# Initialize two pointers, one will go one step a time (slow), another two at a time (fast)
		slow = self.head
		fast = self.head
		# Iterate till fast's next is null (fast reaches end)
		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next
		# return the slow's data, which would be the middle element.
		print("The middle element is ", slow.data)


# Start with the empty list
llist = LinkedList()
for i in range(5, 0, -1):
	llist.push(i)
llist.printList()
llist.printMiddle()

```

## [Check if a linked list is a circular linked list.](https://practice.geeksforgeeks.org/problems/circular-linked-list/1)

```python
class Node:
	def __init__(self, data):
		self.data = data # Assign data
		self.next = None # Initialize next as null


class LinkedList:
	def __init__(self):
		self.head = None

def Circular(head):
	if head is None:
		return True
	node = head.next
	i = 0
	while((node is not None) and (node is not head)):
		i = i + 1
		node = node.next
	return node==head


llist = LinkedList()
llist.head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)

llist.head.next = second;
second.next = third;
third.next = fourth

if (Circular(llist.head)):
	print('Yes')
else:
	print('No')

fourth.next = llist.head

if (Circular(llist.head)):
	print('Yes')
else:
	print('No')
```

## [Split a Circular linked list into two halves.](https://practice.geeksforgeeks.org/problems/split-a-circular-linked-list-into-two-halves/1)

```python
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class CircularLinkedList:
	def __init__(self):
		self.head = None
	# circular linked list
	def push(self, data):
		ptr1 = Node(data)
		temp = self.head
		
		ptr1.next = self.head

		# If linked list is not None then set the next of last node
		if self.head is not None:
			while(temp.next != self.head):
				temp = temp.next
			temp.next = ptr1

		else:
			ptr1.next = ptr1 # For the first node

		self.head = ptr1


	def printList(self):
		temp = self.head
		if self.head is not None:
			while(True):
				print ("%d" %(temp.data),end=' ')
				temp = temp.next
				if (temp == self.head):
					break


	# Function to split a list (starting with head) into two lists. head1 and head2 are the head nodes of the two resultant linked lists
	def splitList(self, head1, head2):
		slow_ptr = self.head
		fast_ptr = self.head
	
		if self.head is None:
			return
		
		# If there are odd nodes in the circular list then fast_ptr->next becomes head and for even nodes fast_ptr->next->next becomes head
		while(fast_ptr.next != self.head and
			fast_ptr.next.next != self.head ):
			fast_ptr = fast_ptr.next.next
			slow_ptr = slow_ptr.next

		# If there are even elements in list then move fast_ptr
		if fast_ptr.next.next == self.head:
			fast_ptr = fast_ptr.next

		# Set the head pointer of first half
		head1.head = self.head

		# Set the head pointer of second half
		if self.head.next != self.head:
			head2.head = slow_ptr.next

		# Make second half circular
		fast_ptr.next = slow_ptr.next
	
		# Make first half circular
		slow_ptr.next = self.head


# Initialize lists as empty
head = CircularLinkedList()
head1 = CircularLinkedList()
head2 = CircularLinkedList()

head.push(12)
head.push(56)
head.push(2)
head.push(11)

print ("Original Circular Linked List")
head.printList()

# Split the list
head.splitList(head1 , head2)

print ("\nFirst Circular Linked List")
head1.printList()

print ("\nSecond Circular Linked List")
head2.printList()
```

## [Write a Program to check whether the Singly Linked list is a palindrome or not.](https://practice.geeksforgeeks.org/problems/check-if-linked-list-is-pallindrome/1)

```python
class Node:
	def __init__(self,data):
		self.data = data
		self.ptr = None

def ispalindrome(head):
	# Temp pointer
	slow = head

	# Declare a stack
	stack = []
	
	ispalin = True

	# Push all elements of the list to the stack
	while slow != None:
		stack.append(slow.data)
		# Move ahead
		slow = slow.ptr

	# Iterate in the list again and check by popping from the stack
	while head != None:
		# Get the top most element
		i = stack.pop()
		
		# Check if data is not same as popped element
		if head.data == i:
			ispalin = True
		else:
			ispalin = False
			break

		# Move ahead
		head = head.ptr
	return ispalin


# Addition of linked list
one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(3)
six = Node(2)
seven = Node(1)

# Initialize the next pointer of every current pointer
one.ptr = two
two.ptr = three
three.ptr = four
four.ptr = five
five.ptr = six
six.ptr = seven
seven.ptr = None

result = ispalindrome(one)
print("isPalindrome:", result)
```

## [Deletion from a Circular Linked List.](https://practice.geeksforgeeks.org/problems/deletion-and-reverse-in-linked-list/1/)

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def deleteNode(head, key):
    t = head
    while t and t.next != head:
        if t.next.data == key:
            t.next = t.next.next
        t = t.next

def reverse(head):
    arr = []
    t = head
    arr.append(t.data)
    t = t.next
    while t != head:
        arr.append(t.data)
        t = t.next
    arr = arr[::-1]
    t = head
    i = 0 
    while t != None:
        if t.next == head:
            t.data = arr[len(arr)-1]
            break
        else:
            t.data = arr[i]
        t = t.next
        i+=1
def push(data, prev):
    if prev is None:
        prev = Node(data)
        return prev
    tmp = Node(data)
    prev.next = tmp
    return tmp

def printList(head):
    flg = False
    tmp = head
    while flg is False or tmp != head:
        flg = True
        print(tmp.data, end=" ")
        tmp = tmp.next
    print()

n = 5
arr = [1,2,3,4,5]
delNode = 4

head = Node(None)
prev = head
for i in arr:
    prev = push(i, prev)
head = head.next
prev.next = head
deleteNode(head, delNode)
reverse(head)
printList(head)
```

## [Reverse a Doubly Linked list.](https://practice.geeksforgeeks.org/problems/reverse-a-doubly-linked-list/1)

```python
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None


class DoublyLinkedList:
	
	def __init__(self):
		self.head = None
	
	def reverse(self):
		temp = None
		current = self.head

		# Swap next and prev for all nodes of doubly linked list
		while current is not None:
			temp = current.prev
			current.prev = current.next
			current.next = temp
			current = current.prev

		# Before changing head, check for the cases like empty list and list with only one node
		if temp is not None:
			self.head = temp.prev

	# Given a reference to the head of a list and an integer,inserts a new node on the front of list
	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		if self.head is not None:
			self.head.prev = new_node
		self.head = new_node

	def printList(self, node):
		while(node is not None):
			print(node.data,end=' ')
			node = node.next


dll = DoublyLinkedList()
dll.push(2)
dll.push(4)
dll.push(8)
dll.push(10)

print ("\nOriginal Linked List")
dll.printList(dll.head)

dll.reverse()
print ("\nReversed Linked List")
dll.printList(dll.head)

```

## [Find pairs with a given sum in a DLL.](https://www.geeksforgeeks.org/find-pairs-given-sum-doubly-linked-list/)

```python
class Node:
	def __init__(self, x):
		self.data = x
		self.next = None
		self.prev = None


def pairSum(head, x):
	
	# Set two pointers, first to the beginning of DLL and second to the end of DLL.
	first = head
	second = head
	while (second.next != None):
		second = second.next

	# To track if we find a pair or not
	found = False

	# The loop terminates when they cross each other (second.next == first), or they become same (first == second)
	while (first != second and second.next != first):
			
		# Pair found
		if ((first.data + second.data) == x):
			found = True
			print("Pair found: ", first.data, second.data)
			# Move first in forward direction
			first = first.next
			# Move second in backward direction
			second = second.prev
		elif ((first.data + second.data) < x):
			first = first.next
		else:
			second = second.prev

	# If pair is not present
	if not found:
		print("No pair found")

def insert(head, data):
	temp = Node(data)
	if head:
		temp.next = head
		head.prev = temp
	head = temp
	return head


head = None
head = insert(head, 9)
head = insert(head, 8)
head = insert(head, 6)
head = insert(head, 5)
head = insert(head, 4)
head = insert(head, 2)
head = insert(head, 1)
x = 7
pairSum(head, x)
```

## [Count triplets in a sorted DLL whose sum is equal to given value “X”.](https://www.geeksforgeeks.org/count-triplets-sorted-doubly-linked-list-whose-sum-equal-given-value-x/)

```python
class Node:
	def __init__(self, x):
		self.data = x
		self.next = None
		self.prev = None


def countPairs(first, second, value):
	count = 0

	# The loop terminates when either of two pointers become None, or they cross each other (second.next == first), or they become same (first == second)
	while (first != None and second != None and
		first != second and second.next != first):

		# Pair found
		if ((first.data + second.data) == value):
			
			# Increment count
			count += 1

			# Move first in forward direction
			first = first.next

			# Move second in backward direction
			second = second.prev

		# If sum is greater than 'value' move second in backward direction
		elif ((first.data + second.data) > value):
			second = second.prev

		# Else move first in forward direction
		else:
			first = first.next

	# Required count of pairs
	return count


def countTriplets(head, x):
	
	# If list is empty
	if head is None:
		return 0

	current, first, last = head, None, None
	count = 0

	# Get pointer to the last node of the doubly linked list
	last = head

	while (last.next != None):
		last = last.next

	# Traversing the doubly linked list
	while current != None:

		# For each current node
		first = current.next

		# count pairs with sum(x - current.data) in the range first to last and add it to the 'count' of triplets
		count, current = count + countPairs(
			first, last, x - current.data), current.next

	# Required count of triplets
	return count


def insert(head, data):
	temp = Node(data)
	if head != None:
		temp.next = head
		head.prev = temp
	head = temp
	return head


head = None
head = insert(head, 9)
head = insert(head, 8)
head = insert(head, 6)
head = insert(head, 5)
head = insert(head, 4)
head = insert(head, 2)
head = insert(head, 1)
x = 17
print("Count = ", countTriplets(head, x))

```

## [Sort a “k”sorted Doubly Linked list.[Very IMP]](https://www.codingninjas.com/codestudio/problems/sort-a-k-sorted-doubly-linked-list_1118118)

```python
class Node:
	def __init__(self, val):
		self.data = val
		self.prev = None
		self.next = None

# function to sort a k sorted doubly linked list Using Insertion Sort
# Time Complexity: O(n*k)
# Space Complexity: O(1)
def sortAKSortedDLL(head , k):
	if head is None or head.next is None:
		return head

	# perform on all the nodes in list
	i = head.next
	while (i != None):
		j = i

		# There will be atmost k swaps for each element in the list since each node is k steps away from its correct position
		while (j.prev != None and j.data < j.prev.data):

			# swap j and j.prev node
			temp = j.prev.prev
			temp2 = j.prev
			temp3 = j.next
			j.prev.next = temp3
			j.prev.prev = j
			j.prev = temp
			j.next = temp2
			if (temp != None):
				temp.next = j
			if (temp3 != None):
				temp3.prev = temp2

			# if j is now the new head then reset head
		if j.prev is None:
			head = j
		i = i.next

	return head

# Function to insert a node at the beginning of the Doubly Linked List
def push(new_data):
	global head
	new_node = Node(new_data)
	new_node.prev = None
	new_node.next = head
	if (head != None):
		head.prev = new_node
	head = new_node


def printList(node):
	while (node != None):
		print(node.data,end = " ")
		node = node.next


head = None
# Let us create a k sorted doubly linked list to test the functions Created doubly linked list will be 3<->6<->2<->12<->56<->8
push(8)
push(56)
push(12)
push(2)
push(6)
push(3)

k = 2

print("Original Doubly linked list:")
printList(head)
sortedDLL = sortAKSortedDLL(head, k)
print("")
print("Doubly Linked List after sorting:")
printList(sortedDLL)
```

## [Rotate DoublyLinked list by N nodes.](https://www.geeksforgeeks.org/rotate-doubly-linked-list-n-nodes/)

```python
class Node:
	def __init__(self, next = None, prev = None, data = None):
		self.next = next 
		self.prev = prev 
		self.data = data

def push(head, new_data):
	new_node = Node(data = new_data)
	new_node.next = head
	new_node.prev = None
	if head is not None:
		head.prev = new_node
	head = new_node
	return head

def printList(head):
	node = head
	print("Given linked list")
	while(node is not None):
		print(node.data, end = " ")
		last = node
		node = node.next
	
def rotate(start, N):
	if N == 0 :
		return

	# Let us understand the below code for example N = 2 and list = a <-> b <-> c <-> d <-> e.
	current = start

	# current will either point to Nth or None after this loop. Current will point to node 'b' in the above example
	count = 1
	while count < N and current != None :
		current = current.next
		count += 1

	# If current is None, N is greater than or equal to count of nodes in linked list. Don't change the list in this case
	if current is None:
		return

	# current points to Nth node. Store it in a variable. NthNode points to node 'b' in the above example
	NthNode = current

	# current will point to last node after this loop current will point to node 'e' in the above example
	while current.next != None :
		current = current.next

	# Change next of last node to previous head. Next of 'e' is now changed to node 'a'
	current.next = start

	# Change prev of Head node to current Prev of 'a' is now changed to node 'e'
	start.prev = current

	# Change head to (N+1)th node head is now changed to node 'c'
	start = NthNode.next

	# Change prev of New Head node to None Because Prev of Head Node in Doubly linked list is None
	start.prev = None

	# change next of Nth node to None next of 'b' is now None
	NthNode.next = None

	return start


head = None
head = push(head, 'e')
head = push(head, 'd')
head = push(head, 'c')
head = push(head, 'b')
head = push(head, 'a')
printList(head)
print("\n")
N = 2
head = rotate(head, N)
printList(head)
```

## [Rotate a Doubly Linked list in group of Given Size.[Very IMP]](https://www.geeksforgeeks.org/reverse-doubly-linked-list-groups-given-size/)

```python
class Node:
	def __init__(self):
		self.data = 0
		self.next = None
		self.next = None


def insertAtEnd(head, data):
	new_Node = Node()
	new_Node.data = data
	new_Node.next = None
	temp = head
	if head is None:
		new_Node.prev = None
		head = new_Node
		return head
	while (temp.next != None):
		temp = temp.next
	temp.next = new_Node
	new_Node.prev = temp
	return head


def printDLL(head):
	while (head != None):
		print(head.data, end=" ")
		head = head.next
	print()


# Function to Reverse a doubly linked list in groups of given size
def reverseByN(head, k):
	if head is None:
		return None

	head.prev = None
	temp=None
	curr = head
	newHead = None
	count = 0

	while (curr != None and count < k):
		newHead = curr
		temp = curr.prev
		curr.prev = curr.next
		curr.next = temp
		curr = curr.prev
		count += 1

	# Checking if the reversed LinkedList size is equal to K or not. If it is not equal to k that means we have reversed the last set of size K and we don't need to call the recursive function
	if (count >= k):
		rest = reverseByN(curr, k)
		head.next = rest
		if (rest != None):

			# it is required for prev link otherwise u wont be backtrack list due to broken links
			rest.prev = head
	return newHead


head = None
for i in range(1,11):
	head = insertAtEnd(head, i)
printDLL(head)
n = 4
head = reverseByN(head, n)
printDLL(head)
```

## [Can we reverse a linked list in less than O(n) ?](https://www.geeksforgeeks.org/can-we-reverse-a-linked-list-in-less-than-on/)

```python
It is not possible to reverse a simple singly linked list in less than O(n). A simple singly linked list can only be reversed in O(n) time using recursive and iterative methods. 

A doubly linked list with head and tail pointers while only requiring swapping the head and tail pointers which require lesser operations than a singly linked list can also not be done in less than O(n) since we need to traverse till the end of the list anyway to find the tail node.
```

## [Why Quicksort is preferred for. Arrays and Merge Sort for LinkedLists ?](https://www.geeksforgeeks.org/why-quick-sort-preferred-for-arrays-and-merge-sort-for-linked-lists/)

```python
Quick Sort in its general form is an in-place sort (i.e. it doesn’t require any extra storage) whereas merge sort requires O(N) extra storage, N denoting the array size which may be quite expensive. Allocating and de-allocating the extra space used for merge sort increases the running time of the algorithm.
Comparing average complexity we find that both type of sorts have O(NlogN) average complexity but the constants differ. For arrays, merge sort loses due to the use of extra O(N) storage space.
Most practical implementations of Quick Sort use randomized version. The randomized version has expected time complexity of O(nLogn). The worst case is possible in randomized version also, but worst case doesn’t occur for a particular pattern (like sorted array) and randomized Quick Sort works well in practice.
Quick Sort is also a cache friendly sorting algorithm as it has good locality of reference when used for arrays.
Quick Sort is also tail recursive, therefore tail call optimizations is done.

Why is Merge Sort preferred for Linked Lists?
In case of linked lists the case is different mainly due to difference in memory allocation of arrays and linked lists. Unlike arrays, linked list nodes may not be adjacent in memory.
Unlike array, in linked list, we can insert items in the middle in O(1) extra space and O(1) time if we are given reference/pointer to the previous node. Therefore merge operation of merge sort can be implemented without extra space for linked lists.
In arrays, we can do random access as elements are continuous in memory. Let us say we have an integer (4-byte) array A and let the address of A[0] be x then to access A[i], we can directly access the memory at (x + i*4). Unlike arrays, we can not do random access in linked list.
Quick Sort requires a lot of this kind of access. In linked list to access i’th index, we have to travel each and every node from the head to i’th node as we don’t have continuous block of memory. Therefore, the overhead increases for quick sort. Merge sort accesses data sequentially and the need of random access is low.
```

## [Flatten a Linked List](https://practice.geeksforgeeks.org/problems/flattening-a-linked-list/1)

```python
class Node():
	def __init__(self,data):
		self.data = data
		self.right = None
		self.down = None

class LinkedList():
	def __init__(self):
		self.head = None

	def push(self,head_ref,data):
		new_node = Node(data)
		new_node.down = head_ref
		head_ref = new_node
		return head_ref

	def printList(self):
		temp = self.head
		while(temp != None):
			print(temp.data,end=" ")
			temp = temp.down
		print()

	
	def merge(self, a, b):
		# if first linked list is empty then second is the answer
		if a is None:
			return b

		# if second linked list is empty then first is the result
		if b is None:
			return a

		# compare the data members of the two linked lists and put the larger one in the result
		result = None

		if (a.data < b.data):
			result = a
			result.down = self.merge(a.down,b)
		else:
			result = b
			result.down = self.merge(a,b.down)

		result.right = None
		return result

	def flatten(self, root):

		# Base Case
		if root is None or root.right is None:
			return root

		# recur for list on right
		root.right = self.flatten(root.right)

		# now merge
		root = self.merge(root, root.right)

		# return the root it will be in turn merged with its left
		return root




'''
Let us create the following linked list
			5 -> 10 -> 19 -> 28
			| |	 |	 |
			V V	 V	 V
			7 20 22 35
			|		 |	 |
			V		 V	 V
			8		 50 40
			|			 |
			V			 V
			30			 45
'''
L = LinkedList()
L.head = L.push(L.head, 30);
L.head = L.push(L.head, 8);
L.head = L.push(L.head, 7);
L.head = L.push(L.head, 5);

L.head.right = L.push(L.head.right, 20);
L.head.right = L.push(L.head.right, 10);

L.head.right.right = L.push(L.head.right.right, 50);
L.head.right.right = L.push(L.head.right.right, 22);
L.head.right.right = L.push(L.head.right.right, 19);

L.head.right.right.right = L.push(L.head.right.right.right, 45);
L.head.right.right.right = L.push(L.head.right.right.right, 40);
L.head.right.right.right = L.push(L.head.right.right.right, 35);
L.head.right.right.right = L.push(L.head.right.right.right, 20);

L.head = L.flatten(L.head);
L.printList()
```

## [Sort a LL of 0's, 1's and 2's](https://practice.geeksforgeeks.org/problems/given-a-linked-list-of-0s-1s-and-2s-sort-it/1)

```python
import math

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


def sortList(head):
	if head is None or head.next is None:
		return head

	# Create three dummy nodes to point to beginning of three linked lists. These dummy nodes are created to avoid many None checks.
	zeroD = Node(0)
	oneD = Node(0)
	twoD = Node(0)

	# Initialize current pointers for three lists and whole list.
	zero = zeroD
	one = oneD
	two = twoD

	# Traverse list
	curr = head
	while curr:
		if (curr.data == 0):
			zero.next = curr
			zero = zero.next
		elif curr.data == 1:
			one.next = curr
			one = one.next
		else:
			two.next = curr
			two = two.next
		curr = curr.next
	# Attach three lists
	zero.next = oneD.next or twoD.next
	one.next = twoD.next
	two.next = None

	# Updated head
	head = zeroD.next

	# Delete dummy nodes
	return head

# function to create and return a node
def newNode(data):
	newNode = Node(data)
	newNode.data = data
	newNode.next = None
	return newNode

# Function to print linked list
def printList(node):
	while (node != None):
		print(node.data, end = " ")
		node = node.next
	

head = newNode(1)
head.next = newNode(2)
head.next.next = newNode(0)
head.next.next.next = newNode(1)
print("Linked List Before Sorting")
printList(head)
head = sortList(head)
print("\nLinked List After Sorting")
printList(head)
```

## [Clone a linked list with next and random pointer](https://practice.geeksforgeeks.org/problems/clone-a-linked-list-with-next-and-random-pointer/1)

```python
class Node:
	def __init__(self, data):
		self.data = data	
		self.next = None
		self.random = None


class MyDictionary(dict):
	def __init__(self):
		super().__init__()
		self = {}

	def add(self, key, value):
		self[key] = value


class LinkedList:
	def __init__(self, node):
		self.head = node

	def __repr__(self):
		temp = self.head
		while temp is not None:
			random = temp.random
			random_data = (random.data if
						random is not None else -1)
							
			data = temp.data
			print(
				f"Data-{data}, Random data: {random_data}")
			temp = temp.next
			
		return "\n"

	def push(self, data):
		node = Node(data)
		node.next = self.head
		self.head = node


	def clone(self):
		
		# Initialize two references, one with original list's head.
		original = self.head
		clone = None

		# Initialize two references, one with original list's head.
		mp = MyDictionary()

		# Traverse the original list and make a copy of that in the clone linked list
		while original is not None:
			clone = Node(original.data)
			mp.add(original, clone)
			original = original.next

		# Adjusting the original list reference again.
		original = self.head

		# Traversal of original list again to adjust the next and random references of clone list using hash map.
		while original is not None:
			clone = mp.get(original)
			clone.next = mp.get(original.next)
			clone.random = mp.get(original.random)
			original = original.next
			
		# Return the head reference of the clone list.
		return LinkedList(self.head)


l = LinkedList(Node(5))
l.push(4)
l.push(3)
l.push(2)
l.push(1)

l.head.random = l.head.next.next
l.head.next.random = l.head.next.next.next
l.head.next.next.random = l.head.next.next.next.next
l.head.next.next.next.random = (l.head.next.next.next. next.next)
l.head.next.next.next.next.random = l.head.next

clone = l.clone()
print("Original linked list")
print(l)
print("Cloned linked list")
print(clone)
```

## [Merge K sorted Linked list](https://practice.geeksforgeeks.org/problems/merge-k-sorted-linked-lists/1)

```python
class Node:
	def __init__(self):
		self.data = 0
		self.next = None


def printList(node):
	while (node != None):
		print(node.data, end = ' ')
		node = node.next

def SortedMerge(a, b):
	result = None
	# Base cases
	if a is None:
		return b
	elif b is None:
		return a 

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


def newNode(data):
	temp = Node()
	temp.data = data
	temp.next = None
	return temp


k = 3  # Number of linked lists
n = 4  # Number of elements in each list
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

## [Multiply 2 no. represented by LL](https://practice.geeksforgeeks.org/problems/multiply-two-linked-lists/1)

```python
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node
			
	def printList(self):
		ptr = self.head
		while (ptr != None):
			print(ptr.data, end = '')
			if ptr.next != None:
				print('->', end = '')
			ptr = ptr.next	
		print()
	
# Multiply contents of two Linked Lists
def multiplyTwoLists(first, second):
	num1 = 0
	num2 = 0
	first_ptr = first.head
	second_ptr = second.head
	while first_ptr != None or second_ptr != None:
		if first_ptr != None:
			num1 = (num1 * 10) + first_ptr.data
			first_ptr = first_ptr.next
		if second_ptr != None:
			num2 = (num2 * 10) + second_ptr.data
			second_ptr = second_ptr.next
	return num1 * num2
	

first = LinkedList()
second = LinkedList()

# Create first Linked List 9->4->6
first.push(6)
first.push(4)
first.push(9)
print("First list is: ", end = '')
first.printList()

# Create second Linked List 8->4
second.push(4)
second.push(8)
print("Second List is: ", end = '')
second.printList()

result = multiplyTwoLists(first, second)
print("Result is: ", result)
```

## [Delete nodes which have a greater value on right side](https://practice.geeksforgeeks.org/problems/delete-nodes-having-greater-value-on-right/1)

```python
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:

	def __init__(self):
		self.head = None

	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	def printList(self):
		temp = self.head
		while(temp):
			print (temp.data,end=" ")
			temp = temp.next

	def del_gr_right(self):
		i = self.head
		
		while i:
			value = i.data
			found = False
			j = i.next
			
			while j:
				if j.data > value:
					found = True
					break
				j = j.next
			
			if found:
				temp = i.next
				i.data = i.next.data
				i.next = i.next.next
				temp = None
			else:
				i = i.next


llist = LinkedList()
llist.push(11)
llist.push(18)
llist.push(20)
llist.push(14)
llist.push(15)

print ("Given Linked List is:")
llist.printList()
print()

llist.del_gr_right()

print ("\nLinked list after deletion is")
llist.printList()
```

## [Segregate even and odd nodes in a Linked List](https://practice.geeksforgeeks.org/problems/segregate-even-and-odd-nodes-in-a-linked-list/0)

```python

class Node:

	def __init__(self, data):
		self.data = data 
		self.next =None

# Function to segregate even and odd nodes.
def segregateEvenOdd():
	global head
	evenStart = None 	# Starting node of list having even values.
	evenEnd = None 	# Ending node of even values list.	
	oddStart = None 	# Starting node of odd values list.	
	oddEnd = None 	# Ending node of odd values list.		
	currNode = head # Node to traverse the list.

	while (currNode != None):
		val = currNode.data

		# If current value is even, add it to even values list.
		if (val % 2 == 0):
			if evenStart is None:
				evenStart = currNode
				evenEnd = evenStart
			else:
				evenEnd . next = currNode
				evenEnd = evenEnd . next

		elif oddStart is None:
			oddStart = currNode
			oddEnd = oddStart
		else:
			oddEnd . next = currNode
			oddEnd = oddEnd . next

		# Move head pointer one step in forward direction
		currNode = currNode . next

	# If either odd list or even list is empty, no change is required as all elements are either even or odd.
	if oddStart is None or evenStart is None:
		return

	# Add odd list after even list.	
	evenEnd.next = oddStart
	oddEnd.next = None

	# Modify head pointer to starting of even list.
	head = evenStart


def push(new_data):
	global head
	new_node = Node(new_data)
	new_node.next = head
	head = new_node

def printList():
	global head
	node = head
	while (node != None):
		print(node.data, end = " ")
		node = node.next
	print()
	

''' Let us create a sample linked list as following
0.1.4.6.9.10.11 '''

head = None 
push(11)
push(10)
push(9)
push(6)
push(4)
push(1)
push(0)

print("Original Linked list")
printList()
segregateEvenOdd()
print("Modified Linked list")
printList()
```

## [Program for n’th node from the end of a Linked List](https://practice.geeksforgeeks.org/problems/nth-node-from-end-of-linked-list/1)

```python
class Node:
	def __init__(self, new_data):
		self.data = new_data
		self.next = None
	
class LinkedList:
	def __init__(self):
		self.head = None

	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	def printNthFromLast(self, n):
		temp = self.head # used temp variable
		length = 0
		while temp is not None:
			temp = temp.next
			length += 1

		# print count
		if n > length: 
			# if entered location is greater than length of linked list
			print('Location is greater than the length of LinkedList')
			return
		temp = self.head

		for _ in range(length - n):
			temp = temp.next
		print(temp.data)


llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(35)
llist.printNthFromLast(4)
```

## [Find the first non-repeating character from a stream of characters](https://practice.geeksforgeeks.org/problems/first-non-repeating-character-in-a-stream/0)

```python
from queue import Queue

def firstnonrepeating(Str):
	global MAX_CHAR
	q = Queue()
	charCount = [0] * MAX_CHAR
	
	# traverse whole Stream
	for i in range(len(Str)):

		# push each character in queue
		q.put(Str[i])

		# increment the frequency count
		charCount[ord(Str[i]) -
				ord('a')] += 1

		# check for the non repeating character
		while (not q.empty()):
			if (charCount[ord(q.queue[0]) - ord('a')] > 1):
				q.get()
			else:
				print(q.queue[0], end = " ")
				break

		if (q.empty()):
			print(-1, end = " ")
	print()

MAX_CHAR = 26
Str = "aabc"
firstnonrepeating(Str)
```

# Matrix

## [Spiral traversal on a Matrix](https://practice.geeksforgeeks.org/problems/spirally-traversing-a-matrix/0)

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

## [Search an element in a matrix](https://leetcode.com/problems/search-a-2d-matrix/)

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

## [Find median in a row wise sorted matrix](https://practice.geeksforgeeks.org/problems/median-in-a-row-wise-sorted-matrix1527/1)

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

## [Find row with maximum no. of 1's](https://practice.geeksforgeeks.org/problems/row-with-max-1s0023/1)

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

## [Print elements in sorted order using row-column wise sorted matrix](https://practice.geeksforgeeks.org/problems/sorted-matrix/0)

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

## [Maximum size rectangle](https://practice.geeksforgeeks.org/problems/max-rectangle/1)

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

## [Find a specific pair in matrix](https://www.geeksforgeeks.org/find-a-specific-pair-in-matrix/)

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

## [Rotate matrix by 90 degrees](https://www.geeksforgeeks.org/rotate-a-matrix-by-90-degree-in-clockwise-direction-without-using-any-extra-space/)

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

## [Kth smallest element in a row-column wise sorted matrix](https://practice.geeksforgeeks.org/problems/kth-element-in-matrix/1)

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

## [Common elements in all rows of a given matrix](https://www.geeksforgeeks.org/common-elements-in-all-rows-of-a-given-matrix/)

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

# Searching & Sorting

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
# Python program for implementation of MergeSort
def mergeSort(arr):
	if len(arr) > 1:

		# Finding the mid of the array
		mid = len(arr)//2

		# Dividing the array elements
		L = arr[:mid]

		# into 2 halves
		R = arr[mid:]

		# Sorting the first half
		mergeSort(L)

		# Sorting the second half
		mergeSort(R)

		i = j = k = 0

		# Copy data to temp arrays L[] and R[]
		while i < len(L) and j < len(R):
			if L[i] < R[j]:
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j += 1
			k += 1

		# Checking if any element was left
		while i < len(L):
			arr[k] = L[i]
			i += 1
			k += 1

		while j < len(R):
			arr[k] = R[j]
			j += 1
			k += 1


arr = [12, 11, 13, 5, 6, 7]
mergeSort(arr)
print(arr)


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

## [Find first and last positions of an element in a sorted array](https://practice.geeksforgeeks.org/problems/first-and-last-occurrences-of-x/0)

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

## [Find a Fixed Point (Value equal to index) in a given array](https://practice.geeksforgeeks.org/problems/value-equal-to-index-value1330/1)

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

## [Search in a rotated sorted array](https://leetcode.com/problems/search-in-rotated-sorted-array/)

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

## [square root of an integer](https://practice.geeksforgeeks.org/problems/count-squares3649/1)

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

## [Find the repeating and the missing](https://practice.geeksforgeeks.org/problems/find-missing-and-repeating2512/1)

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


## [Searching in an array where adjacent differ by at most k](https://www.geeksforgeeks.org/searching-array-adjacent-differ-k/)

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

## [find a pair with a given difference](https://practice.geeksforgeeks.org/problems/find-pair-given-difference/0)

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

## [find two elements that sum to a given value - TwoSum](https://practice.geeksforgeeks.org/problems/find-all-four-sum-numbers/0)

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

## [find four elements that sum to a given value - ThreeSum](https://practice.geeksforgeeks.org/problems/find-all-four-sum-numbers/0)

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

## [find four elements that sum to a given value - - FourSum](https://practice.geeksforgeeks.org/problems/find-all-four-sum-numbers/0)

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

## [maximum sum such that no 2 elements are adjacent](https://practice.geeksforgeeks.org/problems/stickler-theif/0)

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

## [Count triplet with sum smaller than a given value](https://practice.geeksforgeeks.org/problems/count-triplets-with-sum-smaller-than-x5549/1)

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

## [print all subarrays with 0 sum](https://practice.geeksforgeeks.org/problems/zero-sum-subarrays/0)

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

## [Product array Puzzle](https://practice.geeksforgeeks.org/problems/product-array-puzzle/0)

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

## [Sort array according to count of set bits](https://practice.geeksforgeeks.org/problems/sort-by-set-bit-count/0)

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

## [minimum no. of swaps required to sort the array](https://practice.geeksforgeeks.org/problems/minimum-swaps/1)

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


## [Find pivot element in a sorted array](http://theoryofprogramming.com/2017/12/16/find-pivot-element-sorted-rotated-array/)

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

## [K-th Element of Two Sorted Arrays](https://practice.geeksforgeeks.org/problems/k-th-element-of-two-sorted-array/0)

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

## [Aggressive cows](https://www.spoj.com/problems/AGGRCOW/)

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

## [Book Allocation Problem](https://practice.geeksforgeeks.org/problems/allocate-minimum-number-of-pages/0)

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

## [EKOSPOJ:](https://www.spoj.com/problems/EKO/)

```python
TODO
```

## [Missing Number in AP](https://practice.geeksforgeeks.org/problems/arithmetic-number/0)

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

## [Smallest number with atleastn trailing zeroes infactorial](https://practice.geeksforgeeks.org/problems/smallest-factorial-number5929/1)

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

## [ROTI-Prata SPOJ](https://www.spoj.com/problems/PRATA/)

```python
TODO
```

## [DoubleHelix SPOJ](https://www.spoj.com/problems/ANARC05B/)

```python
TODO
```

## [Subset Sums](https://www.spoj.com/problems/SUBSUMS/)

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

## [Implement Merge-sort in-place](https://www.geeksforgeeks.org/in-place-merge-sort/)

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

# Stacks & Queues

## [Implement Stack from Scratch](https://www.tutorialspoint.com/javaexamples/data_stack.htm)

```python
class Stack:
    def __init__(self, size):
        self.arr = [None] * size
        self.capacity = size
        self.top = -1

    def push(self, val):
        if self.isFull():
            print('Stack Overflow!! Calling exit()…')
            exit(-1)
 
        print(f'Inserting {val} into the stack…')
        self.top = self.top + 1
        self.arr[self.top] = val

    def pop(self):
        if self.isEmpty():
            print('Stack Underflow!! Calling exit()…')
            exit(-1)
 
        print(f'Removing {self.peek()} from the stack')
 
        # decrease stack size by 1 and (optionally) return the popped element
        top = self.arr[self.top]
        self.top = self.top - 1
        return top

    def peek(self):
        if self.isEmpty():
            exit(-1)
        return self.arr[self.top]

    def size(self):
        return self.top + 1

    def isEmpty(self):
        return self.size() == 0

    def isFull(self):
        return self.size() == self.capacity
 

stack = Stack(3)
stack.push(1)       # Inserting 1 in the stack
stack.push(2)       # Inserting 2 in the stack
stack.pop()         # removing the top element (2)
stack.pop()         # removing the top element (1)
stack.push(3)       # Inserting 3 in the stack

print('Top element is', stack.peek())
print('The stack size is', stack.size())

stack.pop()         # removing the top element (3)
if stack.isEmpty():
    print('The stack is empty')
else:
    print('The stack is not empty')
```

## [Implement Queue from Scratch](https://www.geeksforgeeks.org/queue-set-1introduction-and-array-implementation/)

```python
class Queue:
    def __init__(self, size=1000):
        self.q = [None] * size      # list to store queue elements
        self.capacity = size        # maximum capacity of the queue
        self.front = 0              # front points to the front element in the queue
        self.rear = -1              # rear points to the last element in the queue
        self.count = 0              # current size of the queue
 
    def dequeue(self):
        # check for queue underflow
        if self.isEmpty():
            print('Queue Underflow!! Terminating process.')
            exit(-1)
        x = self.q[self.front]
        print('Removing element…', x)
        self.front = (self.front + 1) % self.capacity
        self.count = self.count - 1
        return x
    def enqueue(self, value):
        # check for queue overflow
        if self.isFull():
            print('Overflow!! Terminating process.')
            exit(-1)
        print('Inserting element…', value)
        self.rear = (self.rear + 1) % self.capacity
        self.q[self.rear] = value
        self.count = self.count + 1

    def peek(self):
        if self.isEmpty():
            print('Queue UnderFlow!! Terminating process.')
            exit(-1)
        return self.q[self.front]
 
    def size(self):
        return self.count

    def isEmpty(self):
        return self.size() == 0
 
    def isFull(self):
        return self.size() == self.capacity
 
 
# create a queue of capacity 5
q = Queue(5)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print('The queue size is', q.size())
print('The front element is', q.peek())
q.dequeue()
print('The front element is', q.peek())
q.dequeue()
q.dequeue()
if q.isEmpty():
    print('The queue is empty')
else:
    print('The queue is not empty')
```

## [Implement 2 stack in an array](https://practice.geeksforgeeks.org/problems/implement-two-stacks-in-an-array/1)

```python
class Stack:
    # Constructor
    def __init__(self, n):
        self.capacity = n
        self.A = [None] * n
        self.top1 = -1
        self.top2 = n
 
    # Function to insert a given element into the first stack
    def push_first(self, key):
        # check if the list is full
        if self.top1 + 1 == self.top2:
            print('Stack Overflow')
            exit(-1)
        self.top1 = self.top1 + 1
        self.A[self.top1] = key
 
    # Function to insert a given element into the second stack
    def push_second(self, key):
        # check if the list is full
        if self.top1 + 1 == self.top2:
            print('Stack Overflow')
            exit(-1)
        self.top2 = self.top2 - 1
        self.A[self.top2] = key
 
    # Function to pop an element from the first stack
    def pop_first(self):
        # if no elements are left in the list
        if self.top1 < 0:
            print('Stack Underflow')
            exit(-1)
        top = self.A[self.top1]
        self.top1 = self.top1 - 1
        return top
 
    # Function to pop an element from the second stack
    def pop_second(self):
        # if no elements are left in the list
        if self.top2 >= self.capacity:
            print('Stack Underflow')
            exit(-1)
        top = self.A[self.top2]
        self.top2 = self.top2 + 1
        return top
 

first = [1, 2, 3, 4, 5]
second = [6, 7, 8, 9, 10]
stack = Stack(len(first) + len(second))
[stack.push_first(i) for i in first]
[stack.push_second(j) for j in second]
print('Popping element from the first stack:', stack.pop_first())
print('Popping element from the second stack:', stack.pop_second())
```

## [find the middle element of a stack](https://www.geeksforgeeks.org/design-a-stack-with-find-middle-operation/)

```python
# Recursive function to find the peak element in a list
def findPeak(nums, left=None, right=None):
 
    # Initialize left and right
    if left is None and right is None:
        left, right = 0, len(nums) - 1
 
    # find the middle element. To avoid overflow, use mid = left + (right - left) / 2
    mid = (left + right) // 2
 
    # check if the middle element is greater than its neighbors
    if ((mid == 0 or nums[mid - 1] <= nums[mid]) and (mid == len(nums) - 1 or nums[mid + 1] <= nums[mid])):
        return mid
  
def findMiddleElement(nums):
    if not nums:
        exit(-1)
    index = findPeak(nums)
    return nums[index]
 
nums = [8, 9, 10, 11, 2, 5, 6]
print('The middle element is', findPeakElement(nums))
 
```

## [Implement "N" stacks in an Array](https://www.geeksforgeeks.org/efficiently-implement-k-stacks-single-array/)

```python
class KStacks:	
	def __init__(self, k, n):
		self.k = k # Number of stacks.
		self.n = n # Total size of array holding  all the 'k' stacks.

		# Array which holds 'k' stacks.
		self.arr = [0] * self.n

		# All stacks are empty to begin with (-1 denotes stack is empty).
		self.top = [-1] * self.k

		# Top of the free stack.
		self.free = 0

		# Points to the next element in either 1. One of the 'k' stacks or, 2. The 'free' stack.
		self.next = [i + 1 for i in range(self.n)]
		self.next[self.n - 1] = -1

	# Check whether given stack is empty.
	def isEmpty(self, sn):
		return self.top[sn] == -1

	# Check whether there is space left for pushing new elements or not.
	def isFull(self):
		return self.free == -1

	# Push 'item' onto given stack number 'sn'.
	def push(self, item, sn):
		if self.isFull():
			print("Stack Overflow")
			return

		# Get the first free position to insert at.
		insert_at = self.free

		# Adjust the free position.
		self.free = self.next[self.free]

		# Insert the item at the free position we obtained above.
		self.arr[insert_at] = item

		# Adjust next to point to the old top of stack element.
		self.next[insert_at] = self.top[sn]

		# Set the new top of the stack.
		self.top[sn] = insert_at

	# Pop item from given stack number 'sn'.
	def pop(self, sn):
		if self.isEmpty(sn):
			return None

		# Get the item at the top of the stack.
		top_of_stack = self.top[sn]

		# Set new top of stack.
		self.top[sn] = self.next[self.top[sn]]

		# Push the old top_of_stack to  the 'free' stack.
		self.next[top_of_stack] = self.free
		self.free = top_of_stack
		return self.arr[top_of_stack]

	def printstack(self, sn):
		top_index = self.top[sn]
		while (top_index != -1):
			print(self.arr[top_index])
			top_index = self.next[top_index]


# Create 3 stacks using an array of size 10.
kstacks = KStacks(3, 10)
# Push some items onto stack number 2.
kstacks.push(15, 2)
kstacks.push(45, 2)
# Push some items onto stack number 1.
kstacks.push(17, 1)
kstacks.push(49, 1)
kstacks.push(39, 1)
# Push some items onto stack number 0.
kstacks.push(11, 0)
kstacks.push(9, 0)
kstacks.push(7, 0)
print(f"Popped element from stack 2 is {str(kstacks.pop(2))}")
print(f"Popped element from stack 1 is {str(kstacks.pop(1))}")
print(f"Popped element from stack 0 is {str(kstacks.pop(0))}")
kstacks.printstack(0)
```

## [Check the expression has valid or Balanced parenthesis or not.](https://practice.geeksforgeeks.org/problems/parenthesis-checker/0)

```python
from collections import deque
 
def isBalanced(exp):
    if not exp or len(exp) & 1:
        return False
 
    # take an empty stack of characters
    stack = deque()
 
    # traverse the input expression
    for ch in exp:
 
        # if the current character in the expression is an opening brace, push the corresponding closing brace into the stack.
        if ch == '(':
            stack.append(')')
        elif ch == '{':
            stack.append('}')
        elif ch == '[':
            stack.append(']')
 
        # return false if the popped character is not the same as the current character
        elif not stack or stack.pop() != ch:
            return False
 
    # the expression is only balanced if the stack is empty at this point
    return not stack
 
exp = '{()}[{}]'
if isBalanced(exp):
    print('The expression is balanced')
else:
    print('The expression is not balanced')
```

## [Reverse a String using Stack](https://practice.geeksforgeeks.org/problems/reverse-a-string-using-stack/1)

```python
from collections import deque
 
def reverse(s):
    stack = deque(s)
    return ''.join(stack.pop() for _ in range(len(s)))
 
s = 'Reverse me'
s = reverse(s)
print(s)
 
```

## [Design a Stack that supports getMin() in O(1) time and O(1) extra space.](https://practice.geeksforgeeks.org/problems/special-stack/1)

```python
class stack:
  def __init__(self):
    self.array = []
    self.top = -1
    self.max = 100  
  
  def isEmpty(self):
    return self.top == -1  

  def isFull(self):  
    return self.top == self.max - 1   
  
  def push(self, data):
    if self.isFull():
      print('Stack OverFlow')
      return
    else:
      self.top += 1
      self.array.append(data)     
  
  def pop(self):
    if self.isEmpty():
      print('Stack UnderFlow')
      return
    else: 
      self.top -= 1
      return self.array.pop()
  
# A class that supports all the stack   operations and one additional  operation getMin() that returns the  minimum element from stack at  any time.  This class inherits from the stack class and uses an  auxiliary stack that holds  minimum elements  
class SpecialStack(stack):
  def __init__(self):
    super().__init__()
    self.Min = stack()  

  def push(self, x):
    if self.isEmpty():
      super().push(x)
      self.Min.push(x)
    else:
      super().push(x)
      y = self.Min.pop()
      self.Min.push(y)
      if x <= y:
        self.Min.push(x)
      else:
        self.Min.push(y)  
  
  
  def pop(self):
    x = super().pop()
    self.Min.pop()
    return x  
  
  def getmin(self):
    x = self.Min.pop()
    self.Min.push(x)
    return x
  
s = SpecialStack()
s.push(10)
s.push(20)
s.push(30)
print(s.getmin())
s.push(5)
print(s.getmin())
```

## [Find the next Greater element](https://practice.geeksforgeeks.org/problems/next-larger-element/0)

```python
from collections import deque

def findNextGreaterElements(arr):
    if not arr:
        return
    result = [-1] * len(arr)
    s = deque()
    for i in range(len(arr)):
        # loop till we have a greater element on top or stack becomes empty. Keep popping elements from the stack smaller than the current element, and set their next greater element to the current element
        while s and arr[s[-1]] < arr[i]:
            result[s[-1]] = arr[i]
            s.pop()
 
        # push current "index" into the stack
        s.append(i)
    return result
 
 
arr = [2, 7, 3, 5, 4, 6, 8]
print(findNextGreaterElements(arr))
```

## [The celebrity Problem](https://practice.geeksforgeeks.org/problems/the-celebrity-problem/1)

```python
"""
In a party of N people, only one person is known to everyone. Such a person may be present in the party, if yes, (s)he doesn’t know anyone in the party. We can only ask questions like “does A know B? “. Find the stranger (celebrity) in the minimum number of questions.
We can describe the problem input as an array of numbers/characters representing persons in the party. We also have a hypothetical function HaveAcquaintance(A, B) which returns true if A knows B, false otherwise. How can we solve the problem. 

Examples:  

Input:
MATRIX = { {0, 0, 1, 0},
           {0, 0, 1, 0},
           {0, 0, 0, 0},
           {0, 0, 1, 0} }
Output:id = 2
Explanation: The person with ID 2 does not 
know anyone but everyone knows him

Input:
MATRIX = { {0, 0, 1, 0},
           {0, 0, 1, 0},
           {0, 1, 0, 0},
           {0, 0, 1, 0} }
Output: No celebrity
Explanation: There is no celebrity.
"""


# Max # of persons in the party
N = 8

# Person with 2 is celebrity
MATRIX = [ [ 0, 0, 1, 0 ],
		[ 0, 0, 1, 0 ],
		[ 0, 0, 0, 0 ],
		[ 0, 0, 1, 0 ] ]

def knows(a, b):
	return MATRIX[a][b]


def findCelebrity(n):
	# Handle trivial case of size = 2
	s = list(range(n))

	# Find a potential celebrity
	while (len(s) > 1):

		# Pop out the first two elements from stack
		A = s.pop()
		B = s.pop()

		# if A knows B, we find that B might be the celebrity and vice versa
		if (knows(A, B)):
			s.append(B)
		else:
			s.append(A)

	# If there are only two people and there is no potential candidate
	if not s:
		return -1

	# Potential candidate?
	C = s.pop();

	# Last candidate was not examined, it leads one excess comparison (optimize)
	if (knows(C, B)):
		C = B

	if (knows(C, A)):
		C = A

	# Check if C is actually a celebrity or not
	for i in range(n):

		# If any person doesn't know 'a' or 'a' doesn't know any person, return -1
		if ((i != C) and (knows(C, i) or not(knows(i, C)))):
			return -1
	return C

	
n = 4
id_ = findCelebrity(n)

if id_ == -1:
	print("No celebrity")
else:
	print("Celebrity ID ", id_)
```

## [Evaluation of Postfix expression](https://practice.geeksforgeeks.org/problems/evaluation-of-postfix-expression/0)

```python
from collections import deque
 def evalPostfix(exp):
    if not exp:
        exit(-1)
    stack = deque()
 
    for ch in exp:
 
        # if the current is an operand, push it into the stack
        if ch.isdigit():
            stack.append(int(ch))
 
        # if the current is an operator
        else:
            # remove the top two elements from the stack
            x = stack.pop()
            y = stack.pop()
 
            # evaluate the expression 'x op y', and push the result back to the stack
            if ch == '+':
                stack.append(y + x)
            elif ch == '-':
                stack.append(y - x)
            elif ch == '*':
                stack.append(y * x)
            elif ch == '/':
                stack.append(y // x)
 
    # At this point, the stack is left with only one element, i.e., expression result
    return stack.pop()
  
exp = '138*+'
print(evalPostfix(exp))
```

## [Reverse a stack using recursion](https://www.geeksforgeeks.org/reverse-a-stack-using-recursion/)

```python

from collections import deque
def insertAtBottom(s, item):
    # base case: if the stack is empty, insert the given item at the bottom
    if not s:
        s.append(item)
        return
 
    # Pop all items from the stack and hold them in the call stack
    top = s.pop()
    insertAtBottom(s, item)
 
    # After the recursion unfolds, push each item in the call stack  at the top of the stack
    s.append(top)
 

def reverseStack(s):
    if not s:
        return
    item = s.pop()
    reverseStack(s)
    insertAtBottom(s, item)

s = deque(range(1, 6))
print('Original stack is', s)
reverseStack(s)
print('Reversed stack is', s)
```

## [Sort a Stack using recursion](https://practice.geeksforgeeks.org/problems/sort-a-stack/1)

```python
from collections import deque
 
def sortedInsert(stack, key):
 
    # base case: if the stack is empty or the key is greater than all elements in the stack
    if not stack or key > stack[-1]:
        stack.append(key)
        return
 
    ''' We reach here when the key is smaller than the top element '''
    top = stack.pop()
    sortedInsert(stack, key)
    stack.append(top)
 
def sortStack(stack):
    if not stack:
        return
    top = stack.pop()
    sortStack(stack)
    sortedInsert(stack, top)
 
A = [5, -2, 9, -7, 3] 
stack = deque(A)
print('Stack before sorting:', list(stack))
sortStack(stack)
print('Stack after sorting:', list(stack))
```

## [Merge Overlapping Intervals](https://practice.geeksforgeeks.org/problems/overlapping-intervals/0)

```python
"""
Consider an event where a log register is maintained containing the guest’s arrival and departure times. Given an array of arrival and departure times from entries in the log register, find the point when there were maximum guests present in the event.

Note that if an arrival and departure event coincides, the arrival time is preferred over the departure time.

 
For example,

Input:
 
arrival = { 1, 2, 4, 7, 8, 12 }
departure = { 2, 7, 8, 12, 10, 15 }
 
Output: Maximum number of guests is 3, present at time 7
"""

def findMaxGuests(arrival, departure):
 
    # Find the time when the last guest leaves the event
    t = max(departure)
 
    # create a count array initialized by 0
    count = [0] * (t + 2)
 
    for i in range(len(arrival)):
        count[arrival[i]] += 1
        count[departure[i] + 1] -= 1
 
    # keep track of the time when there are maximum guests
    max_event_tm = count[0]
 
    # perform a prefix sum computation to determine the guest count at each point
    for i in range(1, t + 1):
        count[i] += count[i - 1]
        if count[max_event_tm] < count[i]:
            max_event_tm = i
 
    print("Event Time:", max_event_tm)
    print("The maximum number of guests is", count[max_event_tm])

 
arrival = [1, 2, 4, 7, 8, 12]
departure = [2, 7, 8, 12, 10, 15]
findMaxGuests(arrival, departure)
```

## [Largest rectangular Area in Histogram](https://practice.geeksforgeeks.org/problems/maximum-rectangular-area-in-a-histogram/0)

```python
"""
ind the largest rectangular area possible in a given histogram where the largest rectangle can be made of a number of contiguous bars. For simplicity, assume that all bars have same width and the width is 1 unit. 
For example, consider the following histogram with 7 bars of heights {6, 2, 5, 4, 5, 1, 6}. The largest possible rectangle possible is 12 (see the below figure, the max area rectangle is highlighted in red)
"""

def getMaxArea(arr):
  s = [-1]
  n = len(arr)
  area = 0
  left_smaller = [-1]*n
  right_smaller = [n]*n
  for i in range(n):
    while s and (s[-1] != -1) and (arr[s[-1]] > arr[i]):
        right_smaller[s[-1]] = i
        s.pop()
    if((i > 0) and (arr[i] == arr[i-1])):
        left_smaller[i] = left_smaller[i-1]
    else:
        left_smaller[i] = s[-1]
    s.append(i)
  for j in range(n):
    area = max(area, arr[j]*(right_smaller[j]-left_smaller[j]-1))
  return area

hist = [6, 2, 5, 4, 5, 1, 6]
print("maxArea = ", getMaxArea(hist))
```

## [Length of the Longest Valid Substring](https://practice.geeksforgeeks.org/problems/valid-substring0624/1)

```python

from collections import deque
def findMaxLen(s):
    if not s:
        return 0
 
    # create a stack of integers for storing an index of parenthesis in the string
    stack = deque()
 
    # initialize the stack by -1
    stack.append(-1)
 
    # stores the length of the longest balanced parenthesis
    length = 0
 
    # iterate over the characters of the string
    for i, e in enumerate(s):
 
        # if the current character is an opening parenthesis, push its index in the stack
        if e == '(':
            stack.append(i)
 
        # if the current character is a closing parenthesis
        else:
            # pop the top index from the stack
            stack.pop()
 
            # if the stack becomes empty, push the current index into the stack
            if not stack:
                stack.append(i)
                continue
 
            # get the length of the longest balanced parenthesis ending at the current character
            curr_len = i - stack[-1]
 
            # update the length of the longest balanced parenthesis
            if length < curr_len:
                length = curr_len
    return length

print(findMaxLen('((()()'))         # prints 4
print(findMaxLen('(((()'))          # prints 2
print(findMaxLen('(((('))           # prints 0
print(findMaxLen('()()'))           # prints 4
print(findMaxLen('(()())(()'))      # prints 6
```

## [Expression contains redundant bracket or not](https://www.geeksforgeeks.org/expression-contains-redundant-bracket-not/)

```python

from collections import deque 
def hasDuplicateParenthesis(exp):
    if not exp or len(exp) <= 3:
        return False
    stack = deque()
 
    # traverse the input expression
    for c in exp:
        # if the current char in the expression is not a closing parenthesis
        if c != ')':
            stack.append(c)
        # if the current char in the expression is a closing parenthesis
        else:
            # if the stack's top element is an opening parenthesis, the subexpression of the form ((exp)) is found
            if stack[-1] == '(':
                return True
 
            # pop till '(' is found for current ')'
            while stack[-1] != '(':
                stack.pop()
 
            # pop '('
            stack.pop()
 
    # if we reach here, then the expression does not have any duplicate parenthesis
    return False
 

exp = '((x+y))' # assumes valid expression
if hasDuplicateParenthesis(exp):
    print('The expression has duplicate parenthesis.')
else:
    print('The expression does not have duplicate parenthesis')
```

## [Implement Stack using Queue](https://practice.geeksforgeeks.org/problems/stack-using-two-queues/1)

```python
from collections import deque
 
class Stack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
 
    # Insert an item into the stack
    def add(self, data):
        # Move all elements from the first queue to the second queue
        while len(self.q1):
            self.q2.append(self.q1.pop())
 
        # Push the given item into the first queue
        self.q1.append(data)
 
        # Move all elements back to the first queue from the second queue
        while len(self.q2):
            self.q1.append(self.q2.pop())

    def pop(self):
        # if the first queue is empty
        if not self.q1:
            print('Underflow!!')
            exit(0)
        front = self.q1.popleft()
        return front
 
 
keys = [1, 2, 3, 4, 5]
s = Stack()
for key in keys:
    s.add(key)
while s:
    print(s.pop())
print(s.pop())
```

## [Implement Stack using Deque](https://www.geeksforgeeks.org/implement-stack-queue-using-deque/)

```python

from collections import deque

class Stack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
 
    # Insert an item into the stack
    def add(self, data):
        self.q1.append(data)
 
    # Remove the top item from the stack
    def poll(self):
        # if the first queue is empty
        if not self.q1:
            print('Stack Underflow!!')
            exit(0)
 
        # Move all elements except last from the first queue to the second queue
        front = None
        while self.q1:
            if len(self.q1) == 1:
                front = self.q1.popleft()
            else:
                self.q2.append(self.q1.popleft())
 
        # Return the last element after moving all elements back to the first queue.
        while self.q2:
            self.q1.append(self.q2.popleft())
        return front
 
  
keys = [1, 2, 3, 4, 5]
s = Stack()
for key in keys:
    s.add(key)
while s:
    print(s.poll())
```

## [Stack Permutations (Check if an array is stack permutation of other)](https://www.geeksforgeeks.org/stack-permutations-check-if-an-array-is-stack-permutation-of-other/)

```python
"""
Given two arrays, both of unique elements. One represents the input queue and the other represents the output queue. Our task is to check if the given output is possible through stack permutation.

Examples: 

Input : First array: 1, 2, 3  
        Second array: 2, 1, 3
Output : Yes
Procedure:
push 1 from input to stack
push 2 from input to stack
pop 2 from stack to output
pop 1 from stack to output
push 3 from input to stack
pop 3 from stack to output


Input : First array: 1, 2, 3  
        Second array: 3, 1, 2
Output : Not Possible  
"""

def checkStackPermutation(ip, op, n):
	# we will be appending elements from input array to stack uptill top of our stack matches with first element of output array
	s = []
	# will maintain a variable j to iterate on output array
	j = 0

	# will iterate one by one in input array
	for i in range(n):

		# appended an element from input array to stack
		s.append(ip[i])
		# if our stack isn't empty and top matches with output array then we will keep popping out from stack uptill top matches with output array
		while s and s[-1] == op[j]:
			s.pop()

			# increasing j so next time we can compare next element in output array
			j += 1

	# if output array was a correct permutation of arr array then by now our stack should be empty
	if not s:
		return True

	return False
	

arr = [4,5,6,7,8] # Input Array
output = [8,7,6,5,4] # Output Array
n = 5
if (checkStackPermutation(arr, output, n)):
	print("Yes")
else:
	print("Not Possible")
```

## [Implement Queue using Stack](https://practice.geeksforgeeks.org/problems/queue-using-two-stacks/1)

```python
from collections import deque
 
class Queue:
    def __init__(self):
        self.s1 = deque()
        self.s2 = deque()
 
    def enqueue(self, data):
        self.s1.append(data)
    
    def dequeue(self):
        # if both stacks are empty
        if not self.s1 and not self.s2:
            print('Underflow!!')
            exit(0)
 
        # if the second stack is empty, move elements from the first stack to it
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
 
        # return the top item from the second stack
        return self.s2.pop()
 
 
keys = [1, 2, 3, 4, 5]
q = Queue()
for key in keys:
    q.enqueue(key)
print(q.dequeue())        # 1
print(q.dequeue())        # 2
```

## [Implement "n" queue in an array](https://www.geeksforgeeks.org/efficiently-implement-k-queues-single-array/)

```python
class KQueues:
	def __init__(self, number_of_queues, array_length):
		self.number_of_queues = number_of_queues
		self.array_length = array_length
		self.array = [-1] * array_length
		self.front = [-1] * number_of_queues
		self.rear = [-1] * number_of_queues
		self.next_array = list(range(1, array_length))
		self.next_array.append(-1)
		self.free = 0

	# To check whether the current queue_number is empty or not
	def is_empty(self, queue_number):
		return self.front[queue_number] == -1

	# To check whether the current queue_number is full or not
	def is_full(self, queue_number):
		return self.free == -1

	# To enqueue the given item in the given queue_number where queue_number is from 0 to number_of_queues-1
	def enqueue(self, item, queue_number):
		if self.is_full(queue_number):
			print("Queue FULL")
			return
		next_free = self.next_array[self.free]
		if self.is_empty(queue_number):
			self.front[queue_number] = self.rear[queue_number] = self.free
		else:
			self.next_array[self.rear[queue_number]] = self.free
			self.rear[queue_number] = self.free
		self.next_array[self.free] = -1
		self.array[self.free] = item
		self.free = next_free

	# To dequeue an item from the given queue_number where queue_number is from 0 to number_of_queues-1
	def dequeue(self, queue_number):
		if self.is_empty(queue_number):
			print("Queue EMPTY")
			return

		front_index = self.front[queue_number]
		self.front[queue_number] = self.next_array[front_index]
		self.next_array[front_index] = self.free
		self.free = front_index
		return self.array[front_index]
		
# Let us create 3 queue in an array of size 10
ks = KQueues(3, 10)
	
# Let us put some items in queue number 2
ks.enqueue(15, 2)
ks.enqueue(45, 2)
# Let us put some items in queue number 1
ks.enqueue(17, 1);
ks.enqueue(49, 1);
ks.enqueue(39, 1);
	
# Let us put some items in queue number 0
ks.enqueue(11, 0);
ks.enqueue(9, 0);
ks.enqueue(7, 0);
	
print(f"Dequeued element from queue 2 is {ks.dequeue(2)}")
print(f"Dequeued element from queue 1 is {ks.dequeue(1)}")
print(f"Dequeued element from queue 0 is {ks.dequeue(0)}")
```

## [Implement a Circular queue](https://www.geeksforgeeks.org/circular-queue-set-1-introduction-array-implementation/)

```python
class CircularQueue():
	def __init__(self, size): 
		self.size = size
		self.queue = [None for _ in range(size)]
		self.front = self.rear = -1

	def enqueue(self, data):
		
		# condition if queue is full
		if ((self.rear + 1) % self.size == self.front):
			print(" Queue is Full\n")
			
		# condition for empty queue
		elif (self.front == -1):
			self.front = 0
			self.rear = 0
			self.queue[self.rear] = data
		else:
			
			# next position of rear
			self.rear = (self.rear + 1) % self.size
			self.queue[self.rear] = data
			
	def dequeue(self):
		if (self.front == -1): # condition for empty queue
			print ("Queue is Empty\n")
			
		# condition for only one element
		elif (self.front == self.rear):
			temp=self.queue[self.front]
			self.front = -1
			self.rear = -1
			return temp
		else:
			temp = self.queue[self.front]
			self.front = (self.front + 1) % self.size
			return temp

	def display(self):
		# condition for empty queue
		if (self.front == -1):
			print ("Queue is Empty")

		elif (self.rear >= self.front):
			print("Elements in the circular queue are:",
											end = " ")
			for i in range(self.front, self.rear + 1):
				print(self.queue[i], end = " ")
			print ()

		else:
			print ("Elements in Circular Queue are:",
										end = " ")
			for i in range(self.front, self.size):
				print(self.queue[i], end = " ")
			for i in range(self.rear + 1):
				print(self.queue[i], end = " ")
			print ()

		if ((self.rear + 1) % self.size == self.front):
			print("Queue is Full")

ob = CircularQueue(5)
ob.enqueue(14)
ob.enqueue(22)
ob.enqueue(13)
ob.enqueue(-6)
ob.display()
print ("Deleted value = ", ob.dequeue())
print ("Deleted value = ", ob.dequeue())
ob.display()
ob.enqueue(9)
ob.enqueue(20)
ob.enqueue(5)
ob.display()
```

## [LRU Cache Implementationa](https://practice.geeksforgeeks.org/problems/lru-cache/1)

```python
class DLLNode:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        # capacity:  capacity of cache
        # Initialize all variable
        self.capacity = capacity
        self.map = {}
        self.head = DLLNode(0, 0)
        self.tail = DLLNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.count = 0

    def deleteNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def addToHead(self, node):
        node.next = self.head.next
        node.next.prev = node
        node.prev = self.head
        self.head.next = node

    # This method works in O(1)
    def get(self, key):
        if key in self.map:
            node = self.map[key]
            result = node.val
            self.deleteNode(node)
            self.addToHead(node)
            print(f'Got the value : {result} for the key: {key}')
            return result
        print(f'Did not get any value for the key: {key}')
        return -1

    # This method works in O(1)
    def set(self, key, value):
        print(f'going to set the (key, value) : ( {key}, {value})')
        if key in self.map:
            node = self.map[key]
            node.val = value
            self.deleteNode(node)
        else:
            node = DLLNode(key, value)
            self.map[key] = node
            if self.count < self.capacity:
                self.count += 1
            else:
                del self.map[self.tail.prev.key]
                self.deleteNode(self.tail.prev)

        self.addToHead(node)


print('Going to test the LRU Cache Implementation')
cache = LRUCache(2)
# it will store a key (1) with value 10 in the cache.
cache.set(1, 10)
# it will store a key (1) with value 10 in the cache.
cache.set(2, 20)
print(f'Value for the key: 1 is {cache.get(1)}')
# evicts key 2 and store a key (3) with value 30 in the cache.
cache.set(3, 30)
print(f'Value for the key: 2 is {cache.get(2)}')
# evicts key 1 and store a key (4) with value 40 in the cache.
cache.set(4, 40)
print(f'Value for the key: 1 is {cache.get(1)}')
print(f'Value for the key: 3 is {cache.get(3)}')
print(f'Value for the key: 4 is {cache.get(4)}')

```

## [Reverse a Queue using recursion](https://practice.geeksforgeeks.org/problems/queue-reversal/1)

```python
from queue import Queue
def Print(queue):
	while (not queue.empty()):
		print(queue.queue[0], end=", ")
		queue.get()

def reversequeue(queue):
	Stack = []
	while (not queue.empty()):
		Stack.append(queue.queue[0])
		queue.get()
	while Stack:
		queue.put(Stack[-1])
		Stack.pop()


queue = Queue()
queue.put(10)
queue.put(20)
queue.put(30)
queue.put(40)
queue.put(50)
queue.put(60)
queue.put(70)
queue.put(80)
queue.put(90)
queue.put(100)
reversequeue(queue)
Print(queue)
```

## [Reverse the first “K” elements of a queue](https://practice.geeksforgeeks.org/problems/reverse-first-k-elements-of-queue/1)

```python
from queue import Queue

def reverseQueueFirstKElements(k, Queue):
	if (Queue.empty() == True or
			k > Queue.qsize()):
		return
	if (k <= 0):
		return

	Stack = []

	# put the first K elements into a Stack
	for _ in range(k):
		Stack.append(Queue.queue[0])
		Queue.get()

	# Enqueue the contents of stack at the back of the queue
	while Stack:
		Queue.put(Stack[-1])
		Stack.pop()

	# Remove the remaining elements and enqueue them at the end of the Queue
	for _ in range(Queue.qsize() - k):
		Queue.put(Queue.queue[0])
		Queue.get()


def Print(Queue):
	while (not Queue.empty()):
		print(Queue.queue[0], end =" ")
		Queue.get()


Queue = Queue()
Queue.put(10)
Queue.put(20)
Queue.put(30)
Queue.put(40)
Queue.put(50)
Queue.put(60)
Queue.put(70)
Queue.put(80)
Queue.put(90)
Queue.put(100)
k = 5
reverseQueueFirstKElements(k, Queue)
Print(Queue)
```

## [Interleave the first half of the queue with second half](https://www.geeksforgeeks.org/interleave-first-half-queue-second-half/)

```python
from queue import Queue

def interLeaveQueue(q):
	if (q.qsize() % 2 != 0):
		print("Input even number of integers.")

	# Initialize an empty stack of int type
	s = []
	halfSize = int(q.qsize() / 2)

	# put first half elements into the stack queue:16 17 18 19 20, stack: 15(T) 14 13 12 11
	for _ in range(halfSize):
		s.append(q.queue[0])
		q.get()

	# enqueue back the stack elements queue: 16 17 18 19 20 15 14 13 12 11
	while s:
		q.put(s[-1])
		s.pop()

	# dequeue the first half elements of queue and enqueue them back queue: 15 14 13 12 11 16 17 18 19 20
	for _ in range(halfSize):
		q.put(q.queue[0])
		q.get()

	# Again put the first half elements into the stack queue: 16 17 18 19 20, stack: 11(T) 12 13 14 15
	for _ in range(halfSize):
		s.append(q.queue[0])
		q.get()

	# interleave the elements of queue and stack queue: 11 16 12 17 13 18 14 19 15 20
	while s:
		q.put(s[-1])
		s.pop()
		q.put(q.queue[0])
		q.get()



q = Queue()
q.put(11)
q.put(12)
q.put(13)
q.put(14)
q.put(15)
q.put(16)
q.put(17)
q.put(18)
q.put(19)
q.put(20)
interLeaveQueue(q)
length = q.qsize()
for _ in range(length):
	print(q.queue[0], end=" ")
	q.get()
```

## [Find the first circular tour that visits all Petrol Pumps](https://practice.geeksforgeeks.org/problems/circular-tour/1)

```python
"""
Suppose there is a circle. There are N petrol pumps on that circle. You will be given two sets of data.
1. The amount of petrol that every petrol pump has.
2. Distance from that petrol pump to the next petrol pump.
Find a starting point where the truck can start to get through the complete circle without exhausting its petrol in between.
Note :  Assume for 1 litre petrol, the truck can go 1 unit of distance.

Example 1:

Input:
N = 4
Petrol = 4 6 7 4
Distance = 6 5 3 5
Output: 1
Explanation: There are 4 petrol pumps with
amount of petrol and distance to next
petrol pump value pairs as {4, 6}, {6, 5},
{7, 3} and {4, 5}. The first point from
where truck can make a circular tour is
2nd petrol pump. Output in this case is 1
(index of 2nd petrol pump).
"""

# A petrol pump has petrol and distance to next petrol pump
class petrolPump:
    def __init__(self,a, b):
        self.petrol = a
        self.distance = b
    
# The function returns starting point if there is a possible solution, otherwise returns -1
def printTour( p, n):
    # deficit is used to store the value of the capacity as soon as the value of capacity becomes negative so as not to traverse the array twice in order to get the solution
    start = 0
    deficit = 0
    capacity = 0
    for i in range(n):
        capacity += p[i].petrol - p[i].distance
        if (capacity < 0):
            # If this particular step is not done then the between steps would be redundant
            start = i + 1
            deficit += capacity
            capacity = 0
    return start if (capacity + deficit >= 0) else -1


arr = [petrolPump(6, 4),petrolPump(3, 6),petrolPump(7, 3)] 
n = len(arr)
start = printTour(arr, n)
if (start == -1):
    print("No solution")
else:
    print("Start = " , start)

```

## [Minimum time required to rot all oranges](https://practice.geeksforgeeks.org/problems/rotten-oranges/0)

```python
"""
Given a matrix of dimension m*n where each cell in the matrix can have values 0, 1 or 2 which has the following meaning:  

0: Empty cell
1: Cells have fresh oranges
2: Cells have rotten oranges
Determine what is the minimum time required so that all the oranges become rotten. A rotten orange at index [i,j] can rot other fresh orange at indexes [i-1,j], [i+1,j], [i,j-1], [i,j+1] (up, down, left and right). If it is impossible to rot every orange then simply return -1.

Examples: 

Input:  arr[][C] = { {2, 1, 0, 2, 1},
                     {1, 0, 1, 2, 1},
                     {1, 0, 0, 2, 1}};
Output:
All oranges can become rotten in 2-time frames.
Explanation: 
At 0th time frame:
 {2, 1, 0, 2, 1}
 {1, 0, 1, 2, 1}
 {1, 0, 0, 2, 1}

At 1st time frame:
 {2, 2, 0, 2, 2}
 {2, 0, 2, 2, 2}
 {1, 0, 0, 2, 2}

At 2nd time frame:
 {2, 2, 0, 2, 2}
 {2, 0, 2, 2, 2}
 {2, 0, 0, 2, 2}
"""


from collections import deque

# function to check whether a cell is valid / invalid
def isvalid(i, j):
	return (i >= 0 and j >= 0 and i < 3 and j < 5)

# Function to check whether the cell is delimiter which is (-1, -1)
def isdelim(temp):
	return (temp[0] == -1 and temp[1] == -1)

# Function to check whether there is still a fresh orange remaining
def checkall(arr):
	for i in range(3):
		for j in range(5):
			if (arr[i][j] == 1):
				return True
	return False

# This function finds if it is possible to rot all oranges or not. If possible, then it returns minimum time required to rot all, otherwise returns -1
def rotOranges(arr):

	# Create a queue of cells
	Q = deque()
	temp = [0, 0]
	ans = 1

	# Store all the cells having rotten orange in first time frame
	for i in range(3):
		for j in range(5):
			if (arr[i][j] == 2):
				temp[0]= i
				temp[1] = j
				Q.append([i, j])

	# Separate these rotten oranges from the oranges which will rotten due the oranges in first time frame using delimiter which is (-1, -1)
	temp[0] = -1
	temp[1] = -1
	Q.append([-1, -1])
	# print(Q)

	# Process the grid while there are rotten oranges in the Queue
	while False:
	
		# This flag is used to determine whether even a single fresh orange gets rotten due to rotten oranges in current time frame so we can increase the count of the required time.
		flag = False
		print(len(Q))

		# Process all the rotten oranges in current time frame.
		while not isdelim(Q[0]):
			temp = Q[0]
			print(len(Q))

			# Check right adjacent cell that if it can be rotten
			if (isvalid(temp[0] + 1, temp[1]) and arr[temp[0] + 1][temp[1]] == 1):
				
				# if this is the first orange to get rotten, increase count and set the flag.
				if (not flag):
					ans, flag =ans + 1, True

				# Make the orange rotten
				arr[temp[0] + 1][temp[1]] = 2

				# append the adjacent orange to Queue
				temp[0] += 1
				Q.append(temp)

				temp[0] -= 1 # Move back to current cell

			# Check left adjacent cell that if it can be rotten
			if (isvalid(temp[0] - 1, temp[1]) and arr[temp[0] - 1][temp[1]] == 1):
				if (not flag):
					ans, flag =ans + 1, True
				arr[temp[0] - 1][temp[1]] = 2
				temp[0] -= 1
				Q.append(temp) # append this cell to Queue
				temp[0] += 1

			# Check top adjacent cell that if it can be rotten
			if (isvalid(temp[0], temp[1] + 1) and arr[temp[0]][temp[1] + 1] == 1):
				if (not flag):
					ans, flag = ans + 1, True
				arr[temp[0]][temp[1] + 1] = 2
				temp[1] += 1
				Q.append(temp) # Push this cell to Queue
				temp[1] -= 1

			# Check bottom adjacent cell if it can be rotten
			if (isvalid(temp[0], temp[1] - 1) and arr[temp[0]][temp[1] - 1] == 1):
				if (not flag):
					ans, flag = ans + 1, True
				arr[temp[0]][temp[1] - 1] = 2
				temp[1] -= 1
				Q.append(temp) # append this cell to Queue
			Q.popleft()

		# Pop the delimiter
		Q.popleft()

		# If oranges were rotten in current frame than separate the rotten oranges using delimiter for the next frame for processing.
		if (len(Q) == 0):
			temp[0] = -1
			temp[1] = -1
			Q.append(temp)

		# If Queue was empty than no rotten oranges left to process so exit

	# Return -1 if all arranges could not rot, otherwise return ans.
	return ans + 1 if(checkall(arr)) else -1

arr = [[2, 1, 0, 2, 1],
	[1, 0, 1, 2, 1],
	[1, 0, 0, 2, 1]]
ans = rotOranges(arr)
if (ans == -1):
	print("All oranges cannot rotn")
else:
	print("Time required for all oranges to rot => " , ans)
```

## [Distance of nearest cell having 1 in a binary matrix](https://practice.geeksforgeeks.org/problems/distance-of-nearest-cell-having-1/0)

```python
"""
Given a binary matrix of N x M, containing at least a value 1. The task is to find the distance of nearest 1 in the matrix for each cell. The distance is calculated as |i1 – i2| + |j1 – j2|, where i1, j1 are the row number and column number of the current cell and i2, j2 are the row number and column number of the nearest cell having value 1.

Examples: 

Input : N = 3, M = 4
        mat[][] = { 0, 0, 0, 1,
                    0, 0, 1, 1,
                    0, 1, 1, 0 }
Output : 3 2 1 0
         2 1 0 0
         1 0 0 1
Explanation:
For cell at (0, 0), nearest 1 is at (0, 3),
so distance = (0 - 0) + (3 - 0) = 3.
Similarly, all the distance can be calculated.

"""
import sys
class matrix_element:
	def __init__(self, row, col):
		self.row = row
		self.col = col
		
def printDistance(arr):
	Row_Count = len(arr)
	Col_Count = len(arr[0])	
	q = []

	# Adding all ones in queue
	for i in range(Row_Count):
		for j in range(Col_Count):
			if (arr[i][j] == 1):
				q.append(matrix_element(i, j))
			
	# In order to find min distance we will again traverse all elements in Matrix. If its zero then it will check against all 1's in Queue. Whatever will be dequeued from queued, will be enqueued back again.
	Queue_Size = len(q)
	for i in range(Row_Count):
		for j in range(Col_Count):
			distance = 0
			min_distance = sys.maxsize
			
			if (arr[i][j] == 0):
				for k in range(Queue_Size):
					One_Pos = q[0]
					q = q[1:]
					One_Row = One_Pos.row
					One_Col = One_Pos.col
					distance = abs(One_Row - i) + abs(One_Col - j)
					min_distance = min(min_distance, distance)
					if (min_distance == 1):
						arr[i][j] = 1
						q.append(matrix_element(One_Row, One_Col))
						break
					q.append(matrix_element(One_Row,One_Col))
					arr[i][j] = min_distance
			else:
				arr[i][j] = 0
								

	for i in range(Row_Count):
		for j in range(Col_Count):
			print(arr[i][j] ,end = " ")
		print()
		

arr = [ [ 0, 0, 0, 1 ], [ 0, 0, 1, 1 ], [ 0, 1, 1, 0 ] ]
printDistance(arr)
```

## [First negative integer in every window of size “k”](https://practice.geeksforgeeks.org/problems/first-negative-integer-in-every-window-of-size-k/0)

```python
"""
Given an array and a positive integer k, find the first negative integer for each window(contiguous subarray) of size k. If a window does not contain a negative integer, then print 0 for that window.

Examples:  

Input : arr[] = {-8, 2, 3, -6, 10}, k = 2
Output : -8 0 -6 -6

First negative integer for each window of size k
{-8, 2} = -8
{2, 3} = 0 (does not contain a negative integer)
{3, -6} = -6
{-6, 10} = -6

Input : arr[] = {12, -1, -7, 8, -15, 30, 16, 28} , k = 3
Output : -1 -1 -7 -15 -15 0

"""

def printFirstNegativeInteger(arr, k):
	firstNegativeIndex = 0
	for i in range(k - 1, len(arr)):
		# skip out of window and positive elements
		while firstNegativeIndex < i and (firstNegativeIndex <= i - k or arr[firstNegativeIndex] >= 0):
			firstNegativeIndex += 1
		# check if a negative element is found, otherwise use 0
		firstNegativeElement = min(arr[firstNegativeIndex], 0)
		print(firstNegativeElement, end=' ')

arr = [12, -1, -7, 8, -15, 30, 16, 28]
k = 3
printFirstNegativeInteger(arr, k)

```

## [Check if all levels of two trees are anagrams or not.](https://www.geeksforgeeks.org/check-if-all-levels-of-two-trees-are-anagrams-or-not/)

```python
class newNode:
	def __init__(self, data):
		self.data = data
		self.left = self.right = None
		
# Returns true if trees with root1 and root2 are level by level anagram, else returns false.
def areAnagrams(root1, root2):

	if root1 is None and root2 is None:
		return True
	if root1 is None or root2 is None:
		return False

	q1 = [root1]
	q2 = [root2]
	while (1) :

		# n1 (queue size) indicates number of Nodes at current level in first tree and n2 indicates number of nodes in current level of second tree.
		n1 = len(q1)
		n2 = len(q2)

		# If n1 and n2 are different
		if (n1 != n2):
			return False

		# If level order traversal is over
		if (n1 == 0):
			break

		# Dequeue all Nodes of current level and Enqueue all Nodes of next level
		curr_level1 = []
		curr_level2 = []
		while (n1 > 0):
			node1 = q1[0]
			q1.pop(0)
			if (node1.left != None) :
				q1.append(node1.left)
			if (node1.right != None) :
				q1.append(node1.right)
			n1 -= 1

			node2 = q2[0]
			q2.pop(0)
			if (node2.left != None) :
				q2.append(node2.left)
			if (node2.right != None) :
				q2.append(node2.right)

			curr_level1.append(node1.data)
			curr_level2.append(node2.data)

		# Check if nodes of current levels are anagrams or not.
		curr_level1.sort()
		curr_level2.sort()
		if (curr_level1 != curr_level2) :
			return False
	return True


root1 = newNode(1)
root1.left = newNode(3)
root1.right = newNode(2)
root1.right.left = newNode(5)
root1.right.right = newNode(4)
root2 = newNode(1)
root2.left = newNode(2)
root2.right = newNode(3)
root2.left.left = newNode(4)
root2.left.right = newNode(5)
if areAnagrams(root1, root2):
	print("Yes")
else:
	print("No")
```

## [Sum of minimum and maximum elements of all subarrays of size “k”.](https://www.geeksforgeeks.org/sum-minimum-maximum-elements-subarrays-size-k/)

```python
"""Given an array of both positive and negative integers, the task is to compute sum of minimum and maximum elements of all sub-array of size k.

Examples: 

Input : arr[] = {2, 5, -1, 7, -3, -1, -2}  
        K = 4
Output : 18
Explanation : Subarrays of size 4 are : 
     {2, 5, -1, 7},   min + max = -1 + 7 = 6
     {5, -1, 7, -3},  min + max = -3 + 7 = 4      
     {-1, 7, -3, -1}, min + max = -3 + 7 = 4
     {7, -3, -1, -2}, min + max = -3 + 7 = 4   
     Sum of all min & max = 6 + 4 + 4 + 4 
                          = 18             """


from collections import deque

# Returns Sum of min and max element of all subarrays of size k
def SumOfKsubArray(arr, n , k):

	Sum = 0 # Initialize result

	# The queue will store indexes of useful elements in every window In deque 'G' we maintain decreasing order of values from front to rear In deque 'S' we maintain increasing order of values from front to rear
	S = deque()
	G = deque()

	for i in range(k):
		# Remove all previous greater elements that are useless.
		while ( len(S) > 0 and arr[S[-1]] >= arr[i]):
			S.pop() # Remove from rear

		# Remove all previous smaller that are elements are useless.
		while ( len(G) > 0 and arr[G[-1]] <= arr[i]):
			G.pop() # Remove from rear

		# Add current element at rear of both deque
		G.append(i)
		S.append(i)

	# Process rest of the Array elements
	for i in range(k, n):
		
		# Element at the front of the deque 'G' & 'S' is the largest and smallest element of previous window respectively
		Sum += arr[S[0]] + arr[G[0]]

		# Remove all elements which are out of this window
		while ( len(S) > 0 and S[0] <= i - k):
			S.popleft()
		while ( len(G) > 0 and G[0] <= i - k):
			G.popleft()

		# remove all previous greater element that are useless
		while ( len(S) > 0 and arr[S[-1]] >= arr[i]):
			S.pop() # Remove from rear

		# remove all previous smaller that are elements are useless
		while ( len(G) > 0 and arr[G[-1]] <= arr[i]):
			G.pop() # Remove from rear

		# Add current element at rear of both deque
		G.append(i)
		S.append(i)

	# Sum of minimum and maximum element of last window
	Sum += arr[S[0]] + arr[G[0]]
	return Sum


arr=[2, 5, -1, 7, -3, -1, -2]
n = len(arr)
k = 3
print(SumOfKsubArray(arr, n, k))
```

## [Minimum sum of squares of character counts in a given string after removing “k” characters.](https://practice.geeksforgeeks.org/problems/game-with-string/0)

```python
"""
Given a string of lowercase alphabets and a number k, the task is to print the minimum value of the string after removal of ‘k’ characters. The value of a string is defined as the sum of squares of the count of each distinct character. 
For example consider the string “saideep”, here frequencies of characters are s-1, a-1, i-1, e-2, d-1, p-1 and value of the string is 1^2 + 1^2 + 1^2 + 1^2 + 1^2 + 2^2 = 9.
Expected Time Complexity: O(k*logn)

Examples: 

Input :  str = abccc, K = 1
Output :  6
We remove c to get the value as 12 + 12 + 22

Input :  str = aaab, K = 2
Output :  2
"""

from queue import PriorityQueue
MAX_CHAR = 26

def minStringValue(str, k):
	l = len(str) # find length of string

	# if K is greater than length of string so reduced string will become 0
	if(k >= l):
		return 0
	
	# Else find Frequency of each character and store in an array
	frequency = [0] * MAX_CHAR
	for i in range(0, l):
		frequency[ord(str[i]) - 97] += 1

	# Push each char frequency negative into a priority_queue as the queue by default is minheap
	q = PriorityQueue()
	for i in range(0, MAX_CHAR):
		q.put(-frequency[i])

	# Removal of K characters
	while(k > 0):
		
		# Get top element in priority_queue multiply it by -1 as temp is negative remove it. Increment by 1 and again push into priority_queue
		temp = q.get()
		temp = temp + 1
		q.put(temp, temp)
		k = k - 1

	# After removal of K characters find sum of squares of string Value	
	result = 0; # initialize result
	while not q.empty():
		temp = q.get()
		temp = temp * (-1)
		result += temp * temp
	return result


str1 = "abbccc"
k = 2
print(minStringValue(str1, k))
str2 = "aaab"
k = 2
print(minStringValue(str2, k))

```

## [Next Smaller Element](https://www.geeksforgeeks.org/next-smaller-element/)

```python
"""
Given an array, print the Next Smaller Element (NSE) for every element. The NSE for an element x is the first smaller element on the right side of x in array. Elements for which no smaller element exist (on right side), consider NSE as -1. 
Examples: 
a) For any array, rightmost element always has NSE as -1. 
b) For an array which is sorted in increasing order, all elements have NSE as -1. 
c) For the input array [4, 8, 5, 2, 25}, the NSE for each element are as follows.

Element         NSE
   4      -->    2
   8      -->    5
   5      -->    2
   2      -->   -1
   25     -->   -1
"""

def printNSE(arr, n):
	mp = {}
	s = []
	for i in range(n):
		if not s:
			s.append(arr[i])
			continue

		# if stack is not empty, then pop an element from stack. If the popped element is greater than next, then a) print the pair b) keep popping while elements are greater and stack is not empty 
		while s and s[-1] > arr[i]:
			mp[s[-1]] = arr[i]
			s.pop()

		# push next to stack so that we can find next smaller for it
		s.append(arr[i])

	# After iterating over the loop, the remaining elements in stack do not have the next smaller element, so print -1 for them
	while s:
		mp[s[-1]] = -1
		s.pop()

	for i in range(n):
		print(arr[i], "--->", mp[arr[i]])


arr = [11, 13, 21, 3]
n = len(arr)
printNSE(arr, n)
```

# String

## [Check whether a String is Palindrome or not](https://practice.geeksforgeeks.org/problems/palindrome-string0817/1)

```python
def isPalindrome(s):
    return s == s[::-1]
 
s = "malayalam"
ans = isPalindrome(s)
 
if ans:
    print("Yes")
else:
    print("No")
```

## [Find Duplicate characters in a string](https://www.geeksforgeeks.org/print-all-the-duplicates-in-the-input-string/)

```python
def printDups(Str):
 
    count = {}
    for i in range(len(Str)):
        if(Str[i] in count):
            count[Str[i]] += 1
        else:
            count[Str[i]] = 1
        #increase the count of characters by 1
  
    for it,it2 in count.items():  #iterating through the unordered map
        if (it2 > 1):   #if the count of characters is greater then 1 then duplicate found
            print(str(it) + ", count = "+str(it2))

Str = "test string"
printDups(Str)
```

## [Write a Code to check whether one string is a rotation of another](https://www.geeksforgeeks.org/a-program-to-check-if-strings-are-rotations-of-each-other/)

```python
def check_rotation(s, goal):

	if (len(s) != len(goal)):
		skip

	q1 = []
	for i in range(len(s)):
		q1.insert(0, s[i])

	q2 = []
	for i in range(len(goal)):
		q2.insert(0, goal[i])

	k = len(goal)
	while (k > 0):
		ch = q2[0]
		q2.pop(0)
		q2.append(ch)
		if (q2 == q1):
			return True
		k -= 1
	return False


s1 = "ABCD"
s2 = "CDAB"
if (check_rotation(s1, s2)):
	print(s2, " is a rotated form of ", s1)
else:
	print(s2, " is not a rotated form of ", s1)
s3 = "ACBD"
if (check_rotation(s1, s3)):
	print(s3, " is a rotated form of ", s1)
else:
	print(s3, " is not a rotated form of ", s1)

```

## [Write a Program to check whether a string is a valid shuffle of two strings or not](https://www.programiz.com/java-programming/examples/check-valid-shuffle-of-strings)

```python
MAX = 256

# This function returns true if contents of arr1[] and arr2[] are same otherwise false.
def compare(arr1, arr2):
	
	global MAX

	for i in range(MAX):
		if (arr1[i] != arr2[i]):
			return False
			
	return True

# This function search for all permutations of pat[] in txt[]
def search(pat, txt):
	
	M = len(pat)
	N = len(txt)

	# countP[]: Store count of all characters of pattern
	# countTW[]: Store count of current window of text
	countP = [0 for _ in range(MAX)]
	countTW = [0 for _ in range(MAX)]

	for i in range(M):
		countP[ord(pat[i])] += 1
		countTW[ord(txt[i])] += 1

	# Traverse through remaining characters of pattern
	for i in range(M, N):

		# Compare counts of current window
		# of text with counts of pattern[]
		if (compare(countP, countTW)):
			return True

		# Add current character to current window
		countTW[ord(txt[i])] += 1

		# Remove the first character of previous window
		countTW[ord(txt[i - M])] -= 1

	# Check for the last window in text
	if(compare(countP, countTW)):
		return True
	return False


txt = "BACDGABCDA"
pat = "ABCD"

if (search(pat, txt)):
	print("Yes")
else:
	print("No")
```

## [Count and Say problem](https://leetcode.com/problems/count-and-say/)

```python
def countnndSay(n):
	if (n == 1):
		return "1"
	if (n == 2):
		return "11"

	# Find n'th term by generating all terms from 3 to n-1. Every term is generated using previous term 
	s = "11"
	for _ in range(3, n + 1):
		# In below for loop, previous character is processed in current iteration. That is why a dummy character is added to make sure that loop runs one extra iteration.
		s += '$'
		l = len(s)

		cnt = 1 # Initialize count
		tmp = "" # Initialize i'th
		# Process previous term to find the next term
		for j in range(1 , l):

			# If current character doesn't match
			if (s[j] != s[j - 1]):

				# Append count of str[j-1] to temp
				tmp += str(cnt + 0)

				# Append str[j-1]
				tmp += s[j - 1]

				# Reset count
				cnt = 1

			# If matches, then increment count of matching characters
			else:
				cnt += 1

		# Update str
		s = tmp
	return s;

N = 3
print(countnndSay(N))
```

## [Write a program to find the longest Palindrome in a string.[ Longest palindromic Substring]](https://practice.geeksforgeeks.org/problems/longest-palindrome-in-a-string/0)

```python
def expand(s, low, high):
    length = len(s)
 
    # expand in both directions
    while low >= 0 and high < length and s[low] == s[high]:
        low = low - 1
        high = high + 1
 
    # return palindromic substring
    return s[low + 1:high]
 

def findLongestPalindromicSubstring(s):
    if not s or not len(s):
        return ''
 
    # `max_str` stores the maximum length palindromic substring found so far
    max_str = ''
 
    # `max_length` stores the maximum length of palindromic substring found so far
    max_length = 0
 
    # consider every character of the given string as a midpoint and expand in both directions to find maximum length palindrome
 
    for i in range(len(s)):
 
        # find the longest odd length palindrome with `s[i]` as a midpoint
        curr_str = expand(s, i, i)
        curr_length = len(curr_str)
 
        # update maximum length palindromic substring if the odd length palindrome has a greater length
 
        if curr_length > max_length:
            max_length = curr_length
            max_str = curr_str
 
        # Find the longest even length palindrome with `s[i]` and `s[i+1]` as midpoints. Note that an even length palindrome has two midpoints.
 
        curr_str = expand(s, i, i + 1)
        curr_length = len(curr_str)
 
        # update maximum length palindromic substring if even length palindrome has a greater length
 
        if curr_length > max_length:
            max_length = curr_length
            max_str = curr_str
 
    return max_str
 

s = 'ABDCBCDBDCBBC'
print(f'The longest palindromic substring of {s} is', findLongestPalindromicSubstring(s))
```

## [Find Longest Recurring Subsequence in String](https://practice.geeksforgeeks.org/problems/longest-repeating-subsequence/0)

```python
def findLongestRepeatingSubSeq( str):
    n = len(str)
    # Create and initialize DP table
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

    # Fill dp table (similar to LCS loops)
    for i in range(1,n+1):
        for j in range(1,n+1):
            # If characters match and indexes are not same
            if (str[i-1] == str[j-1] and i != j):
                dp[i][j] = 1 + dp[i-1][j-1]        
            # If characters do not match
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    return dp[n][n]

str1 = "aabb"
print("The length of the largest subsequence that repeats itself is : " ,findLongestRepeatingSubSeq(str1))
 
```

## [Print all Subsequences of a string.](https://www.geeksforgeeks.org/print-subsequences-string/)

```python
# Below is the implementation of the above approach
def printSubsequence(input, output):

	# Base Case if the input is empty print the output string
	if len(input) == 0:
		print(output, end=' ')
		return

	# output is passed with including the 1st character of input string
	printSubsequence(input[1:], output+input[0])

	# output is passed without including the 1st character of input string
	printSubsequence(input[1:], output)


output = ""
str1 = "abcd"
printSubsequence(str1, output)
```

## [Print all the permutations of the given string](https://practice.geeksforgeeks.org/problems/permutations-of-a-given-string/0)

```python
def permute(s, answer):
	if (len(s) == 0):
		print(answer, end = " ")
		return
	for i in range(len(s)):
		ch = s[i]
		left_substr = s[:i]
		right_substr = s[i + 1:]
		rest = left_substr + right_substr
		permute(rest, answer + ch)

answer = ""
s = "alex"
print("All possible strings are : ")
permute(s, answer)
```

## [Split the Binary string into two substring with equal 0’s and 1’s](https://www.geeksforgeeks.org/split-the-binary-string-into-substrings-with-equal-number-of-0s-and-1s/)

```python
def maxSubStr(str, n):
	# To store the count of 0s and 1s
	count0 = 0
	count1 = 0
	
	# To store the count of maximum substrings str can be divided into
	cnt = 0
	
	for i in range(n):
		if str[i] == '0':
			count0 += 1
		else:
			count1 += 1
			
		if count0 == count1:
			cnt += 1

# It is not possible to split the string
	if count0 != count1:
		return -1
			
	return cnt

str1 = "0100110101"
n = len(str1)
print(maxSubStr(str1, n))

```


## [Rabin Karp Algo](https://www.geeksforgeeks.org/rabin-karp-algorithm-for-pattern-searching/)

```python
# d is the number of characters in the input alphabet
d = 256

# pat -> pattern
# txt -> text
# q -> A prime number

def search(pat, txt, q):
	M = len(pat)
	N = len(txt)
	i = 0
	j = 0
	p = 0 # hash value for pattern
	t = 0 # hash value for txt
	h = 1

	# The value of h would be "pow(d, M-1)%q"
	for _ in range(M-1):
		h = (h*d)%q

	# Calculate the hash value of pattern and first window of text
	for i in range(M):
		p = (d*p + ord(pat[i]))%q
		t = (d*t + ord(txt[i]))%q

	# Slide the pattern over text one by one
	for i in range(N-M+1):
		# Check the hash values of current window of text and pattern if the hash values match then only check for characters one by one
		if p==t:
			# Check for characters one by one
			for j in range(M):
				if txt[i+j] != pat[j]:
					break
				else: j+=1

			# if p == t and pat[0...M-1] = txt[i, i+1, ...i+M-1]
			if j==M:
				print(f"Pattern found at index {str(i)}")

		# Calculate hash value for next window of text: Remove leading digit, add trailing digit
		if i < N-M:
			t = (d*(t-ord(txt[i])*h) + ord(txt[i+M]))%q

			# We might get negative values of t, converting it to positive
			if t < 0:
				t = t+q


txt = "GEEKS FOR GEEKS"
pat = "GEEK"
q = 101
search(pat,txt,q)
```

## [KMP Algo](https://practice.geeksforgeeks.org/problems/longest-prefix-suffix2527/1)

```python
def longestPrefixSuffix(s):
	n = len(s)
	lps = [0] * n # lps[0] is always 0

	# length of the previous longest prefix suffix
	l = 0

	# the loop calculates lps[i] for i = 1 to n-1
	i = 1
	while (i < n):
		if (s[i] == s[l]):
			l = l + 1
			lps[i] = l
			i += 1

		elif l == 0:

			# if (len == 0)
			lps[i] = 0
			i += 1

		else:
			l = lps[l-1]
			# Also, note that we do not increment i here

	res = lps[n-1]

	# Since we are looking for non overlapping parts.
	return n//2 if (res > n/2) else res
		

s = "abcab"
print(longestPrefixSuffix(s))
```

## [Convert a Sentence into its equivalent mobile numeric keypad sequence.](https://www.geeksforgeeks.org/convert-sentence-equivalent-mobile-numeric-keypad-sequence/)

```python
"""
Input : GEEKSFORGEEKS
Output : 4333355777733366677743333557777
For obtaining a number, we need to press a
number corresponding to that character for 
number of times equal to position of the 
character. For example, for character C, 
we press number 2 three times and accordingly.

Input : HELLO WORLD
Output : 4433555555666096667775553
"""

def printSequence(arr, mystr):
	n = len(mystr)
	output = ""
	for i in range(n):

		# checking for space
		if (mystr[i] == ' '):
			output = f"{output}0"
		else:
			# calculating index for each
			# character		
			position = ord(mystr[i]) - ord('A')
			output = output + arr[position]
	
	return output
	

str1 = ["2", "22", "222",
	"3", "33", "333",   
	"4", "44", "444",
	"5", "55", "555",
	"6", "66", "666",
	"7", "77", "777", "7777",
	"8", "88", "888",
	"9", "99", "999", "9999" ]

mystr = "GEEKSFORGEEKS";
print( printSequence(str1, mystr))
```

## [Minimum number of bracket reversals needed to make an expression balanced.](https://practice.geeksforgeeks.org/problems/count-the-reversals/0)

```python
"""
Input:  exp = "}{"
Output: 2
We need to change '}' to '{' and '{' to
'}' so that the expression becomes balanced, 
the balanced expression is '{}'

Input:  exp = "{{{"
Output: Can't be made balanced using reversals

Input:  exp = "{{{{"
Output: 2 

Input:  exp = "{{{{}}"
Output: 1 

Input:  exp = "}{{}}{{{"
Output: 3
"""
import math

def countMinReversals(expr):
	length = len(expr)

	# Expressions of odd lengths cannot be balanced
	if (length % 2 != 0):
		return -1

	left_brace = 0
	right_brace = 0

	for i in range(length):
		# If we find a left bracket then we simply increment the left bracket
		if (expr[i] == '{'):
			left_brace += 1
		elif (left_brace == 0):
			right_brace += 1
		else:
			left_brace -= 1

	return math.ceil(left_brace / 2) + math.ceil(right_brace / 2)


expr = "}}{{"
print(countMinReversals(expr))
```

## [Count All Palindromic Subsequence in a given String.](https://practice.geeksforgeeks.org/problems/count-palindromic-subsequences/1)

```python
"""
Input : str = "abcd"
Output : 4
Explanation :- palindromic  subsequence are : "a" ,"b", "c" ,"d" 

Input : str = "aab"
Output : 4
Explanation :- palindromic subsequence are :"a", "a", "b", "aa"

Input : str = "aaaa"
Output : 15
"""
# Python 3 program to counts Palindromic
# Subsequence in a given String using recursion

def countPS(i, j):
	if(i > j):
		return 0

	if(dp[i][j] != -1):
		return dp[i][j]

	if (i == j):
		dp[i][j] = 1
	elif str[i] == str[j]:
		dp[i][j] = (countPS(i + 1, j) + countPS(i, j - 1) + 1)
	else:
		dp[i][j] = (countPS(i + 1, j) + countPS(i, j - 1) - countPS(i + 1, j - 1))
	return dp[i][j]


str = "abcb"
dp = [[-1 for _ in range(1000)] for _ in range(1000)]
n = len(str)
print("Total palindromic subsequence are :", countPS(0, n - 1))

```

## [Count of number of given string in 2D character array](https://www.geeksforgeeks.org/find-count-number-given-string-present-2d-character-array/)

```python
"""
Given a 2-Dimensional character array and a string, we need to find the given string in 2-dimensional character array, such that individual characters can be present left to right, right to left, top to down or down to top.

Examples: 

Input : a ={
            {D,D,D,G,D,D},
            {B,B,D,E,B,S},
            {B,S,K,E,B,K},
            {D,D,D,D,D,E},
            {D,D,D,D,D,E},
            {D,D,D,D,D,G}
           }
        str= "GEEKS"
Output :2
"""


def internalSearch(ii, needle, row, col, hay, row_max, col_max):
	
	found = 0
	if (row >= 0 and row <= row_max and
		col >= 0 and col <= col_max and
		needle[ii] == hay[row][col]):
		match = needle[ii]
		ii += 1
		hay[row][col] = 0
		if (ii == len(needle)):
			found = 1
		else:
			
			# through Backtrack searching in every directions
			found += internalSearch(ii, needle, row, col + 1, hay, row_max, col_max)
			found += internalSearch(ii, needle, row, col - 1, hay, row_max, col_max)
			found += internalSearch(ii, needle, row + 1, col, hay, row_max, col_max)
			found += internalSearch(ii, needle, row - 1, col, hay, row_max, col_max)
		hay[row][col] = match
	return found

# Function to search the string in 2d array
def searchString(needle, row, col,strr, row_count, col_count):
	found = 0
	for r in range(row_count):
		for c in range(col_count):
			found += internalSearch(0, needle, r, c,
						strr, row_count - 1, col_count - 1)		
	return found


needle = "MAGIC"
inputt = ["BBABBM","CBMBBA","IBABBG","GOZBBI","ABBBBC","MCIGAM"]
strr = [0] * len(inputt)
for i in range(len(inputt)):
	strr[i] = list(inputt[i])
print("count: ", searchString(needle, 0, 0, strr, len(strr), len(strr[0])))

```

## [Search a Word in a 2D Grid of characters.](https://practice.geeksforgeeks.org/problems/find-the-string-in-grid/0)

```python
"""
Input:  grid[][] = {"GEEKSFORGEEKS",
                    "GEEKSQUIZGEEK",
                    "IDEQAPRACTICE"};
        word = "GEEKS"

Output: pattern found at 0, 0
        pattern found at 0, 8
        pattern found at 1, 0
Explanation: 'GEEKS' can be found as prefix of
1st 2 rows and suffix of first row

Input:  grid[][] = {"GEEKSFORGEEKS",
                    "GEEKSQUIZGEEK",
                    "IDEQAPRACTICE"};
        word = "EEE"

Output: pattern found at 0, 2
        pattern found at 0, 10
        pattern found at 2, 2
        pattern found at 2, 12
Explanation: EEE can be found in first row 
twice at index 2 and index 10
and in second row at 2 and 12
"""


class GFG:	
	def __init__(self):
		self.R = None
		self.C = None
		self.dir = [[-1, 0], [1, 0], [1, 1],
					[1, -1], [-1, -1], [-1, 1],
					[0, 1], [0, -1]]
					
	def search2D(self, grid, row, col, word):
		# If first character of word doesn't match with the given starting point in grid.
		if grid[row][col] != word[0]:
			return False
			
		# Search word in all 8 directions starting from (row, col)
		for x, y in self.dir:
			
			# Initialize starting point for current direction
			rd, cd = row + x, col + y
			flag = True
			
			# First character is already checked, match remaining characters
			for k in range(1, len(word)):
				
				# If out of bound or not matched, break
				if (0 <= rd <self.R and 0 <= cd < self.C and word[k] == grid[rd][cd]):
					# Moving in particular direction
					rd += x
					cd += y
				else:
					flag = False
					break
			
			# If all character matched, then value of flag must be false	
			if flag:
				return True
		return False
		
	# Searches given word in a given matrix in all 8 directions
	def patternSearch(self, grid, word):
		# Rows and columns in given grid
		self.R = len(grid)
		self.C = len(grid[0])
		# Consider every point as starting point and search given word
		for row in range(self.R):
			for col in range(self.C):
				if self.search2D(grid, row, col, word):
					print("pattern found at ", f'{str(row)}, {str(col)}')
					

grid = ["GEEKSFORGEEKS",
		"GEEKSQUIZGEEK",
		"IDEQAPRACTICE"]
gfg = GFG()
gfg.patternSearch(grid, 'GEEKS')
print('')
gfg.patternSearch(grid, 'EEE')

```

## [Boyer Moore Algorithm for Pattern Searching.](https://www.geeksforgeeks.org/boyer-moore-algorithm-for-pattern-searching/)

```python
"""
Input:  txt[] = "THIS IS A TEST TEXT"
        pat[] = "TEST"
Output: Pattern found at index 10

Input:  txt[] =  "AABAACAADAABAABA"
        pat[] =  "AABA"
Output: Pattern found at index 0
        Pattern found at index 9
        Pattern found at index 12
"""


NO_OF_CHARS = 256

def badCharHeuristic(string, size):

	# Initialize all occurrence as -1
	badChar = [-1]*NO_OF_CHARS

	# Fill the actual value of last occurrence
	for i in range(size):
		badChar[ord(string[i])] = i;

	# return initialized list
	return badChar

def search(txt, pat):
	m = len(pat)
	n = len(txt)

	# create the bad character list by calling the preprocessing function badCharHeuristic() for given pattern
	badChar = badCharHeuristic(pat, m)

	# s is shift of the pattern with respect to text
	s = 0
	while (s <= n-m):
		j = m-1

		# Keep reducing index j of pattern while characters of pattern and text are matching at this shift s
		while j>=0 and pat[j] == txt[s+j]:
			j -= 1

		# If the pattern is present at current shift, then index j will become -1 after the above loop
		if j<0:
			print(f"Pattern occur at shift = {s}")

				# Shift the pattern so that the next character in text 	aligns with the last occurrence of it in pattern. The condition s+m < n is necessary for the case when pattern occurs at the end of text
			
			s += (m-badChar[ord(txt[s+m])] if s+m<n else 1)
		else:

			# Shift the pattern so that the bad character in text aligns with the last occurrence of it in pattern. The max function is used to make sure that we get a positive shift. We may get a negative shift if the last occurrence of bad character in pattern is on the right side of the current character.
			s += max(1, j-badChar[ord(txt[s+j])])


txt = "ABAAABCD"
pat = "ABC"
search(txt, pat)
```

## [Converting Roman Numerals to Decimal](https://practice.geeksforgeeks.org/problems/roman-number-to-integer/0)

```python

def romanToInt(s):
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            number += translations[char]
        print(number)
         
romanToInt('MCMIV')
```

## [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)

```python
def LCP(X, Y):
    i = j = 0
    while i < len(X) and j < len(Y):
        if X[i] != Y[j]:
            break
        i = i + 1
        j = j + 1
    return X[:i]
 
 
# Function to find the longest common prefix (LCP) between a given set of strings
def findLCP(words):
    prefix = words[0]
    for s in words:
        prefix = LCP(prefix, s)
    return prefix
 
  
words = ['techie delight', 'tech', 'techie', 'technology', 'technical']
print('The longest common prefix is', findLCP(words))
```

## [Number of flips to make binary string alternate](https://practice.geeksforgeeks.org/problems/min-number-of-flips/0)

```python
"""
Input : str = “001”
Output : 1
Minimum number of flips required = 1
We can flip 1st bit from 0 to 1 

Input : str = “0001010111”
Output : 2
Minimum number of flips required = 2
We can flip 2nd bit from 0 to 1 and 9th 
bit from 1 to 0 to make alternate 
string “0101010101”.
"""

def flip( ch):
	return '1' if (ch == '0') else '0'

# Utility method to get minimum flips when alternate string starts with expected char
def getFlipWithStartingCharcter(str, expected):
	flipCount = 0
	for i in range(len( str)):
		# if current character is not expected, increase flip count
		if (str[i] != expected):
			flipCount += 1

		# flip expected character each time
		expected = flip(expected)
	return flipCount

def minFlipToMakeStringAlternate(str):	
	return min(getFlipWithStartingCharcter(str, '0'), getFlipWithStartingCharcter(str, '1'))


str1 = "0001010111"
print(minFlipToMakeStringAlternate(str1))
```

## [Find the first repeated word in string.](https://www.geeksforgeeks.org/find-first-repeated-word-string/)

```python

from collections import Counter

def firstRepeatedWord(sentence):
	lis = list(sentence.split(" "))
	frequency = Counter(lis)
	for i in lis:
		if(frequency[i] > 1):
			return i

sentence = "Vikram had been saying that he had been there"
print(firstRepeatedWord(sentence))
```

## [Minimum number of swaps for bracket balancing.](https://practice.geeksforgeeks.org/problems/minimum-swaps-for-bracket-balancing/0)

```python
"""Input  : []][][
Output : 2
First swap: Position 3 and 4
[][]][
Second swap: Position 5 and 6
[][][]

Input  : [[][]]
Output : 0
The string is already balanced.
"""
def swapCount(s):
	swap = 0
	imbalance = 0;
	
	for i in s:
		if i == '[':
			imbalance -= 1
		else:
			imbalance += 1
			if imbalance > 0:
				swap += imbalance
	return swap

s = "[]][][";
print(swapCount(s))
s = "[[][]]";
print(swapCount(s))

```

## [Find the longest common subsequence between two strings.](https://practice.geeksforgeeks.org/problems/longest-common-subsequence/0)

```python
"""
LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH” of length 3. 
LCS for input Sequences “AGGTAB” and “GXTXAYB” is “GTAB” of length 4.
"""

def lcs(X, Y, m, n):
	L = [[0 for _ in range(n+1)] for _ in range(m+1)]
	# Following steps build L[m+1][n+1] in bottom up fashion. Note that L[i][j] contains length of LCS of X[0..i-1] and Y[0..j-1]
	for i in range(m+1):
		for j in range(n+1):
			if i == 0 or j == 0:
				L[i][j] = 0
			elif X[i-1] == Y[j-1]:
				L[i][j] = L[i-1][j-1] + 1
			else:
				L[i][j] = max(L[i-1][j], L[i][j-1])

		# Create a string variable to store the lcs string
	lcs = ""

	# Start from the right-most-bottom-most corner and one by one store characters in lcs[]
	i = m
	j = n
	while i > 0 and j > 0:

		# If current character in X[] and Y are same, then current character is part of LCS
		if X[i-1] == Y[j-1]:
			lcs += X[i-1]
			i -= 1
			j -= 1

		# If not same, then find the larger of two and go in the direction of larger value
		elif L[i-1][j] > L[i][j-1]:
			i -= 1

		else:
			j -= 1

	# We traversed the table in reverse order LCS is the reverse of what we got
	lcs = lcs[::-1]
	print(f"LCS of {X} and {Y} is {lcs}")


X = "AGGTAB"
Y = "GXTXAYB"
m = len(X)
n = len(Y)
lcs(X, Y, m, n)
```

## [Program to generate all possible valid IP addresses from given  string.](https://www.geeksforgeeks.org/program-generate-possible-valid-ip-addresses-given-string/)

```python
"""
Input: 25525511135
Output: [“255.255.11.135”, “255.255.111.35”]
Explanation:
These are the only valid possible
IP addresses.

"""

def solve(s, i, j, level, temp, res):
	if (i == (j + 1) and level == 5):
		res.append(temp[1:])

	# Digits of a number ranging 0-255 can lie only between  0-3
	k = i
	while (k < i + 3 and k <= j):
		ad = s[i: k + 1]

		# Return if string starting with '0' or it is greater than 255.
		if ((s[i] == '0' and len(ad) > 1) or int(ad) > 255):
			return

		# Recursively call for another level.
		solve(s, k + 1, j, level + 1, f'{temp}.{ad}', res)

		k += 1


s = "25525511135"
n = len(s)
ans = []
solve(s, 0, n - 1, 1, "", ans)
for s in ans:
	print(s)
```

## [Write a program to find the smallest window that contains all characters of string itself.](https://practice.geeksforgeeks.org/problems/smallest-distant-window/0)

```python
"""
Input: aabcbcdbca
Output: dbca
Explanation: 
Possible substrings= {aabcbcd, abcbcd, 
bcdbca, dbca....}
Of the set of possible substrings 'dbca' 
is the shortest substring having all the 
distinct characters of given string. 

Input: aaab
Output: ab
Explanation: 
Possible substrings={aaab, aab, ab}
Of the set of possible substrings 'ab' 
is the shortest substring having all 
the distinct characters of given string.    
"""
# Python program to find the smallest
# window containing
# all characters of a pattern
from collections import defaultdict

MAX_CHARS = 256

def findSubString(strr):
	n = len(strr)
	if n <= 1:
		return strr
	dist_count = len(set(list(strr)))
	curr_count = defaultdict(lambda: 0)
	count = 0
	start = 0
	min_len = n

	for j in range(min_len):
		curr_count[strr[j]] += 1

		# If any distinct character matched, then increment count
		if curr_count[strr[j]] == 1:
			count += 1

		# Try to minimize the window i.e., check if any character is occurring more no. of times than its occurrence in pattern, if yes then remove it from starting and also remove the useless characters.
		if count == dist_count:
			while curr_count[strr[start]] > 1:
				curr_count[strr[start]] -= 1
				start += 1

			# Update window size
			len_window = j - start + 1
			if min_len > len_window:
				min_len = len_window
				start_index = start

	return str(strr[start_index: start_index + min_len])


print(f'Smallest window containing all distinct characters is: {findSubString("aabcbcdbca")}')
```

## [Minimum characters to be added at front to make string palindrome](https://www.geeksforgeeks.org/minimum-characters-added-front-make-string-palindrome/)

```python
"""
Input  : str = "ABC"
Output : 2
We can make above string palindrome as "CBABC"
by adding 'B' and 'C' at front.

Input  : str = "AACECAAAA";
Output : 2
We can make above string palindrome as AAAACECAAAA
by adding two A's at front of string.
"""

def ispalindrome(s):
    l = len(s)
    i = 0
    j = l - 1
    while i <= j:
        if(s[i] != s[j]):
            return False
        i += 1
        j -= 1
    return True
 
s = "BABABAA"
cnt = 0
flag = 0
while s != "":
    if(ispalindrome(s)):
        flag = 1
        break
    else:
        cnt += 1
        # erase the last element of the string
        s = s[:-1]

# print the number of insertion at front
if(flag):
    print(cnt)
```

## [Find the smallest window in a string containing all characters of another string](https://practice.geeksforgeeks.org/problems/smallest-window-in-a-string-containing-all-the-characters-of-another-string/0)

```python
"""
nput: string = “this is a test string”, pattern = “tist” 
Output: Minimum window is “t stri” 
Explanation: “t stri” contains all the characters of pattern.

Input: string = “geeksforgeeks”, pattern = “ork” 
Output: Minimum window is “ksfor”
"""


def smallestWindow(s, p):
	n = len(s)
	if n < len(p):
		return -1
	mp = [0]*256
	# Starting index of ans
	start = 0
	# Answer, Length of ans
	ans = n + 1
	cnt = 0
	# creating map
	for i in p:
		mp[ord(i)] += 1
		if mp[ord(i)] == 1:
			cnt += 1
	i = 0

	# Traversing the window
	for j in range(n):
		mp[ord(s[j])] -= 1
		if mp[ord(s[j])] == 0:
			cnt -= 1
			while cnt == 0:
				if ans > j - i + 1:
					ans = j - i + 1
					start = i

				# Sliding I
				# Calculation for removing I
				mp[ord(s[i])] += 1
				if mp[ord(s[i])] > 0:
					cnt += 1
				i += 1
	if ans > n:
		return "-1"
	return s[start:start+ans]


s = "ADOBECODEBANC"
p = "ABC"
result = smallestWindow(s, p)
print("Smallest window that contain all character :", result)
```

## [Recursively remove all adjacent duplicates](https://practice.geeksforgeeks.org/problems/consecutive-elements/0)

```python
def removeDuplicates(S):
	n = len(S)
	# We don't need to do anything for empty or single character string.
	if (n < 2):
		return
	# j is used to store index is result string (or index of current distinct character)
	j = 0
	
	# Traversing string
	for i in range(n):
		# If current character S[i] is different from S[j]
		if (S[j] != S[i]):
			j += 1
			S[j] = S[i]
	
	# Putting string termination character.
	j += 1
	S = S[:j]
	return S
	

S1 = "geeksforgeeks"
S1 = list(S1.rstrip())
S1 = removeDuplicates(S1)
print(*S1, sep = "")

S2 = "aabcca"
S2 = list(S2.rstrip())
S2 = removeDuplicates(S2)
print(*S2, sep = "")
```

## [String matching where one string contains wildcard characters](https://practice.geeksforgeeks.org/problems/wildcard-string-matching/0)

```python
def match(first, second):

	# If we reach at the end of both strings, we are done
	if len(first) == 0 and len(second) == 0:
		return True

	# Make sure to eliminate consecutive '*'
	if len(first) > 1 and first[0] == '*':
		i = 0
		while i+1 < len(first) and first[i+1] == '*':
			i += 1
		first = first[i:]

	# Make sure that the characters after '*' are present
	# in second string. This function assumes that the first
	# string will not contain two consecutive '*'
	if len(first) > 1 and first[0] == '*' and len(second) == 0:
		return False

	# If the first string contains '?', or current characters
	# of both strings match
	if (len(first) > 1 and first[0] == '?') or (len(first) != 0
												and len(second) != 0 and first[0] == second[0]):
		return match(first[1:], second[1:])

	# If there is *, then there are two possibilities
	# a) We consider current character of second string
	# b) We ignore current character of second string.
	if len(first) != 0 and first[0] == '*':
		return match(first[1:], second) or match(first, second[1:])

	return False


def test(first, second):
	if match(first, second):
		print("Yes")
	else:
		print("No")


test("g*ks", "geeks") # Yes
test("ge?ks*", "geeksforgeeks") # Yes
test("g*k", "gee") # No because 'k' is not in second
test("*pqrs", "pqrst") # No because 't' is not in first
test("abc*bcd", "abcdhghgbcd") # Yes
test("abc*c?d", "abcd") # No because second must have 2 instances of 'c'
test("*c*d", "abcd") # Yes
test("*?c*d", "abcd") # Yes
test("geeks**", "geeks") # Yes
```

## [Function to find Number of customers who could not get a computer](https://www.geeksforgeeks.org/function-to-find-number-of-customers-who-could-not-get-a-computer/)

```python
"""
Write a function “runCustomerSimulation” that takes following two inputs 

An integer ‘n’: total number of computers in a cafe and a string: 
A sequence of uppercase letters ‘seq’: Letters in the sequence occur in pairs. The first occurrence indicates the arrival of a customer; the second indicates the departure of that same customer. 
A customer will be serviced if there is an unoccupied computer. No letter will occur more than two times. 
Customers who leave without using a computer always depart before customers who are currently using the computers. There are at most 20 computers per cafe.

For each set of input the function should output a number telling how many customers, if any walked away without using a computer. Return 0 if all the customers were able to use a computer.
runCustomerSimulation (2, “ABBAJJKZKZ”) should return 0
runCustomerSimulation (3, “GACCBDDBAGEE”) should return 1 as ‘D’ was not able to get any computer
runCustomerSimulation (3, “GACCBGDDBAEE”) should return 0
runCustomerSimulation (1, “ABCBCA”) should return 2 as ‘B’ and ‘C’ were not able to get any computer.
runCustomerSimulation(1, “ABCBCADEED”) should return 3 as ‘B’, ‘C’ and ‘E’ were not able to get any computer.
"""

MAX_CHAR = 26

# n is number of computers in cafe.
# 'seq' is given sequence of customer entry, exit events
def runCustomerSimulation(n, seq):

	# seen[i] = 0, indicates that customer 'i' is not in cafe
	# seen[1] = 1, indicates that customer 'i' is in cafe but computer is not assigned yet.
	# seen[2] = 2, indicates that customer 'i' is in cafe and has occupied a computer.
	seen = [0] * MAX_CHAR

	# Initialize result which is number of customers who could not get any computer.
	res = 0
	occupied = 0 # To keep track of occupied

	# Traverse the input sequence
	for i in range(len(seq)):

		# Find index of current character in seen[0...25]
		ind = ord(seq[i]) - ord('A')

		# If first occurrence of 'seq[i]'
		if seen[ind] == 0:

			# set the current character as seen
			seen[ind] = 1

			# If number of occupied computers is less than n, then assign a computer to new customer
			if occupied < n:
				occupied+=1

				# Set the current character as occupying a computer
				seen[ind] = 2

			# Else this customer cannot get a computer, increment
			else:
				res+=1

		# If this is second occurrence of 'seq[i]'
		else:
			# Decrement occupied only if this customer was using a computer
			if seen[ind] == 2:
				occupied-=1
			seen[ind] = 0

	return res


print (runCustomerSimulation(2, "ABBAJJKZKZ"))
print (runCustomerSimulation(3, "GACCBDDBAGEE"))
print (runCustomerSimulation(3, "GACCBGDDBAEE"))
print (runCustomerSimulation(1, "ABCBCA"))
print (runCustomerSimulation(1, "ABCBCADEED"))
```

## [Transform One String to Another using Minimum Number of Given Operation](https://www.geeksforgeeks.org/transform-one-string-to-another-using-minimum-number-of-given-operation/)

```python
"""
Input:  A = "ABD", B = "BAD"
Output: 1
Explanation: Pick B and insert it at front.

Input:  A = "EACBD", B = "EABCD"
Output: 3
Explanation: Pick B and insert at front, EACBD => BEACD
             Pick A and insert at front, BEACD => ABECD
             Pick E and insert at front, ABECD => EABCD
"""

# Function to find minimum number of operations required  transform A to B
def minOps(A, B):
	m = len(A)
	n = len(B)

	# This part checks whether conversion is possible or not
	if n != m:
		return -1

	count = [0] * 256

	for i in range(n):	 # count characters in A
		count[ord(B[i])] += 1
	for i in range(n):	 # subtract count for every char in B
		count[ord(A[i])] -= 1
	for i in range(256): # Check if all counts become 0
		if count[i]:
			return -1

	# This part calculates the number of operations required
	res = 0
	i = n-1
	j = n-1
	while i >= 0:
	
		# if there is a mismatch, then keep incrementing result 'res' until B[j] is not found in A[0..i]
		while i>= 0 and A[i] != B[j]:
			i -= 1
			res += 1

		# if A[i] and B[j] match
		if i >= 0:
			i -= 1
			j -= 1
	return res

A = "EACBD"
B = "EABCD"
print(f"Minimum number of operations required is {str(minOps(A,B))}")
```

## [Check if two given strings are isomorphic to each other](https://practice.geeksforgeeks.org/problems/isomorphic-strings/0)

```python
"""
Input:  str1 = "aab", str2 = "xxy"
Output: True
'a' is mapped to 'x' and 'b' is mapped to 'y'.

Input:  str1 = "aab", str2 = "xyz"
Output: False
One occurrence of 'a' in str1 has 'x' in str2 and 
other occurrence of 'a' has 'y'.
"""

def areIsomorphic(str1, str2):
	#initializing a dictionary to store letters from str1 and str2 as key value pairs
	charCount = {}
	#initially setting c to "a"
	c = "a"
	#iterating over str1 and str2
	for i in range(len(str1)):
		#if str1[i] is a key in charCount
		if str1[i] in charCount:
			c = charCount[str1[i]]
			if c != str2[i]:
				return False
		#if str2[i] is not a value in charCount
		elif str2[i] not in charCount.values():
			charCount[str1[i]] = str2[i]
		else:
			return False
	return True
		

str1 = "aac"
str2 = "xxy"
if (len(str1) == len(str2) and areIsomorphic(str1, str2)):
	print("Is Isomorphic")
else:
	print("Is Not Isomorphic")
```

## [Recursively print all sentences that can be formed from list of word lists](https://www.geeksforgeeks.org/recursively-print-all-sentences-that-can-be-formed-from-list-of-word-lists/)

```python
"""
Input: {{"you", "we"},
        {"have", "are"},
        {"sleep", "eat", "drink"}}

Output:
  you have sleep
  you have eat
  you have drink
  you are sleep
  you are eat
  you are drink
  we have sleep
  we have eat
  we have drink
  we are sleep
  we are eat
  we are drink 
"""

R = 3
C = 3

# A recursive function to print all possible sentences that can be formed from a list of word list
def printUtil(arr, m, n, output):
	# Add current word to output array
	output[m] = arr[m][n]

	# If this is last word of current output sentence, then print the output sentence
	if m==R-1:
		for i in range(R):
			print (output[i],end= " ")
		print()
		return

	# Recur for next row
	for i in range(C):
		if arr[m+1][i] != "":
			printUtil(arr, m+1, i, output)

def printf(arr):

	# Create an array to store sentence
	output = [""] * R

	# Consider all words for first row as starting points and print all sentences
	for i in range(C):
		if arr[0][i] != "":
			printUtil(arr, 0, i, output)


arr = [ ["you", "we",""],
		["have", "are",""],
		["sleep", "eat", "drink"]]
printf(arr)
```

# Trie

## [Construct a trie from scratch](https://www.geeksforgeeks.org/trie-insert-and-search/)

```python
class TrieNode:
    def __init__(self):
        self.children = [None]*26
        # isEndOfWord is True if node represent the end of the word
        self.isEndOfWord = False
  
class Trie:
    def __init__(self):
        self.root = self.getNode()
  
    def getNode(self):
        # Returns new trie node (initialized to NULLs)
        return TrieNode()
  
    def _charToIndex(self,ch):
        # private helper function. 
        # Converts key current character into index use only 'a' through 'z' and lower case
        return ord(ch)-ord('a')
  
  
    def insert(self,key):
        # If not present, inserts key into trie. If the key is prefix of trie node, just marks leaf node
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
  
            # if current character is not present
            if not pCrawl.children[index]:
                pCrawl.children[index] = self.getNode()
            pCrawl = pCrawl.children[index]
  
        # mark last node as leaf
        pCrawl.isEndOfWord = True
  
    def search(self, key):
        # Search key in the trie Returns true if key presents in trie, else false
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not pCrawl.children[index]:
                return False
            pCrawl = pCrawl.children[index]
  
        return pCrawl.isEndOfWord
  

def constructTrie():
    # Input keys (use only 'a' through 'z' and lower case)
    keys = ["the","a","there","answer","any", "by","their", "these"]
    output = ["Not present in trie", "Present in trie"]
  
    # Trie object
    t = Trie()
  
    # Construct trie
    for key in keys:
        t.insert(key)
  
    # Search for different keys
    print("the->",output[t.search("the")])
    print("these->",output[t.search("these")])
    print("their->",output[t.search("their")])
    print("thaw->",output[t.search("thaw")])
  
if __name__ == '__main__':
    constructTrie()
```

## [Find shortest unique prefix for every word in a given list](https://www.geeksforgeeks.org/find-all-shortest-unique-prefixes-to-represent-each-word-in-a-given-list/)

```python
"""
Input:  [AND, BONFIRE, BOOL, CASE, CATCH, CHAR]
Output: [A, BON, BOO, CAS, CAT, CH]
Explanation:
A can uniquely identify AND
BON can uniquely identify BONFIRE
BOO can uniquely identify BOOL
CAS can uniquely identify CASE
CAT can uniquely identify CATCH
CH can uniquely identify CHAR
"""
# A class to store a Trie node
class TrieNode:
    def __init__(self):
        # each node stores a dictionary to its child nodes
        self.child = {}
 
        # keep track of the total number of times the current node is visited while inserting data in Trie
        self.freq = 0
 
 
# Function to insert a given string into a Trie
def insert(root, word): 
    # start from the root node
    curr = root
    for c in word:
        # create a new node if the path doesn't exist
        curr.child.setdefault(c, TrieNode())
 
        # increment frequency
        curr.child[c].freq += 1
 
        # go to the next node
        curr = curr.child[c]
 
 
# Function to recursively traverse the Trie in a preorder fashion and print the shortest unique prefix for each word in the Trie
def printShortestPrefix(root, word_so_far):
    if root is None:
        return
 
    # print `word_so_far` if the current Trie node is visited only once
    if root.freq == 1:
        print(word_so_far)
        return
 
    # recur for all child nodes
    for k, v in root.child.items():
        printShortestPrefix(v, word_so_far + k)
 
 
# Find the shortest unique prefix for every word in a given array
def findShortestPrefix(words):
    # construct a Trie from the given items
    root = TrieNode()
    for s in words:
        insert(root, s)
 
    # Recursively traverse the Trie in a preorder fashion to list all prefixes
    printShortestPrefix(root, '')
 
words = ['AND', 'BONFIRE', 'BOOL', 'CASE', 'CATCH', 'CHAR']
findShortestPrefix(words)

```

## [Word Break Problem | (Trie solution)](https://www.geeksforgeeks.org/word-break-problem-trie-solution/)

```python

# Currently, Trie supports lowercase English characters. So, the character size is 26.
CHAR_SIZE = 26
 
 
class Node:
    next = [None] * CHAR_SIZE
    exist = False       # true when the node is a leaf node
 
 
# Iterative function to insert a string into a Trie
def insertTrie(head, s):
 
    # start from the root node
    node = head
 
    # do for each character in the string
    for c in s:
 
        index = ord(c) - ord('a')
 
        # create a new node if the path doesn't exist
        if node.next[index] is None:
            node.next[index] = Node()
 
        # go to the next node
        node = node.next[index]
 
    # mark the last node as a leaf
    node.exist = True
 
 
# Function to determine if a string can be segmented into space-separated sequence of one or more dictionary words
def wordBreak(head, s):
 
    # get the length of the string
    n = len(s)
 
    # `good[i]` is true if the first `i` characters of `s` can be segmented
    good = [None] * (n + 1)
    good[0] = True      # base case
 
    for i in range(n):
        if good[i]:
            node = head
            for j in range(i, n):
                if node is None:
                    break
 
                index = ord(s[j]) - ord('a')
                node = node.next[index]
 
                # we can make [0, i] using our known decomposition and [i+1, j] using this string in a Trie
                if node and node.exist:
                    good[j + 1] = True
 
    # `good[n]` would be true if all characters of `s` can be segmented
    return good[n]
 
 
# List of strings to represent a dictionary
words = ['self', 'th', 'is', 'famous', 'word', 'break', 'b', 'r', 'e', 'a', 'k', 'br', 'bre', 'brea', 'ak', 'prob', 'lem']

# given string
s = 'wordbreakproblem'

# create a Trie to store the dictionary
t = Node()
for word in words:
    insertTrie(t, word)

# check if the string can be segmented or not
if wordBreak(t, s):
    print('The string can be segmented')
else:
    print('The string can\'t be segmented')
```

## [Given a sequence of words, print all anagrams together](https://practice.geeksforgeeks.org/problems/k-anagrams-1/0)

```python
class TrieNode:
    def __init__(self):
        # each node stores a dictionary to its child nodes
        self.child = {}
 
        # stores anagrams in the leaf node
        self.words = []
 
 
# Function to insert a string into a Trie
def insert(root, word, originalWord):
    curr = root
    for c in word:
        curr.child.setdefault(c, TrieNode())
        curr = curr.child[c]
 
    # anagrams will end up at the same leaf node
    curr.words.append(originalWord)
 

def printAnagrams(root):
    if root is None:
        return
 
    # print the current word
    if len(root.words) > 1:
        print(root.words)
 
    # recur for all child nodes
    for child in root.child.values():
        printAnagrams(child)
 
def groupAnagrams(words):
    root = TrieNode()
    for word in words:
        # Sort the characters of the current word and insert it into the Trie. Note that the original word gets stored on the leaf
        insert(root, ''.join(sorted(word)), word)
    printAnagrams(root)
 
 
words = ['auctioned', 'actors', 'altered', 'streaming', 'related', 'education', 'aspired', 'costar', 'despair', 'mastering', 'act','cat','tac'
]
groupAnagrams(words)
```

## [Print unique rows in a given boolean matrix](https://practice.geeksforgeeks.org/problems/unique-rows-in-boolean-matrix/1)

```python
# Given a binary matrix of M X N of integers, you need to return only unique rows of binary array
ROW = 4
COL = 5

def findUniqueRows(M):
    for i in range(ROW):
        flag = 0
        for j in range(i):
            flag = 1
            for k in range(COL):
                if (M[i][k] != M[j][k]):
                    flag = 0

            if (flag == 1):
                break
        if (flag == 0):
            for j in range(COL):
                print(M[i][j], end = " ")
            print()    


M = [ [ 0, 1, 0, 0, 1 ],
      [ 1, 0, 1, 1, 0 ],
      [ 0, 1, 0, 0, 1 ],
      [ 1, 0, 1, 0, 0 ] ]
findUniqueRows(M)


```

# Elementary Problems

## Check Leap Year

```python
# Python program to check if year is a leap year or not

year = 2000

# divided by 100 means century year (ending with 00) century year divided by 400 is leap year
if (year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year".format(year))

# not divided by 100 means not a century year year divided by 4 is a leap year
elif (year % 4 ==0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))

# if not divided by both 400 (century year) and 4 (not century year) year is not leap year
else:
    print("{0} is not a leap year".format(year))
```

## Generate Random Number

```python
import random
print(random.randint(0,9))
```

## Largest No of 3

```python
num1 = 10
num2 = 14
num3 = 12

if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The largest number is", largest)
```

## Prime Number

```python
num = 29
# define a flag variable
flag = False

# prime numbers are greater than 1
if num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break

# check if flag is True
if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")
```

## Factorial

```python

num = 7
factorial = 1

# check if the number is negative, positive or zero
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)
```

## Prime Number Intervals

```python
lower = 900
upper = 1000

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
```

## Fibonacci Sequence
```python

nterms = int(input("How many terms? "))
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1
```

## Armstrong Number

```python
num = int(input("Enter a number: "))
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
```

## Decimal to Binary/Hexadecimal/Octal

```python
dec = 344

print("The decimal value of", dec, "is:")
print(bin(dec), "in binary.")
print(oct(dec), "in octal.")
print(hex(dec), "in hexadecimal.")

```

## GCD

```python
def compute_hcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i 
    return hcf

num1 = 54 
num2 = 24

print("The H.C.F. is", compute_hcf(num1, num2))
```

## LCM

```python
def compute_gcd(x, y):
   while(y):
       x, y = y, x % y
   return x

def compute_lcm(x, y):
   lcm = (x*y)//compute_gcd(x,y)
   return lcm

num1 = 54
num2 = 24 

print("The L.C.M. is", compute_lcm(num1, num2))
```

## Factorial Using Recursion

```python
def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)

num = 7

if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of", num, "is", recur_factorial(num))

```

## 10 Triange Pattern Programs

```python
"""
*
* *
* * *
* * * *
* * * * *
"""
rows = int(input("Enter number of rows: "))
for i in range(rows):
    for j in range(i+1):
        print("* ", end="")
    print("\n")



"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""

rows = int(input("Enter number of rows: "))
for i in range(rows):
    for j in range(i+1):
        print(j+1, end=" ")
    print("\n")


"""
A
B B
C C C
D D D D
E E E E E
"""
rows = int(input("Enter number of rows: "))
ascii_value = 65
for i in range(rows):
    for j in range(i+1):
        alphabet = chr(ascii_value)
        print(alphabet, end=" ")
    ascii_value += 1
    print("\n")

"""
* * * * *
* * * *
* * *
* *
*
"""
rows = int(input("Enter number of rows: "))
for i in range(rows, 0, -1):
    for j in range(0, i):
        print("* ", end=" ")
    print("\n")


"""
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
"""
rows = int(input("Enter number of rows: "))
for i in range(rows, 0, -1):
    for j in range(1, i+1):
        print(j, end=" ")
    print("\n")

"""
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
"""

rows = int(input("Enter number of rows: "))
k = 0
for i in range(1, rows+1):
    for space in range(1, (rows-i)+1):
        print(end="  ")
    while k!=(2*i-1):
        print("* ", end="")
        k += 1
    k = 0
    print()


"""
        1 
      2 3 2 
    3 4 5 4 3 
  4 5 6 7 6 5 4 
5 6 7 8 9 8 7 6 5
"""

rows = int(input("Enter number of rows: "))

k = 0
count=0
count1=0

for i in range(1, rows+1):
    for space in range(1, (rows-i)+1):
        print("  ", end="")
        count+=1
    
    while k!=((2*i)-1):
        if count<=rows-1:
            print(i+k, end=" ")
            count+=1
        else:
            count1+=1
            print(i+k-(2*count1), end=" ")
        k += 1
    
    count1 = count = k = 0
    print()

"""
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
"""

rows = int(input("Enter number of rows: "))

for i in range(rows, 1, -1):
    for space in range(0, rows-i):
        print("  ", end="")
    for j in range(i, 2*i-1):
        print("* ", end="")
    for j in range(1, i-1):
        print("* ", end="")
    print()


"""
           1
         1   1
       1   2   1
     1   3   3    1
   1  4    6   4   1
 1  5   10   10  5   1
"""

rows = int(input("Enter number of rows: "))
coef = 1

for i in range(1, rows+1):
    for space in range(1, rows-i+1):
        print(" ",end="")
    for j in range(0, i):
        if j==0 or i==0:
            coef = 1
        else:
            coef = coef * (i - j)//j
        print(coef, end = " ")
    print()

"""
1
2 3
4 5 6
7 8 9 10
"""
rows = int(input("Enter number of rows: "))
number = 1

for i in range(1, rows+1):
    for j in range(1, i+1):
        print(number, end=" ")
        number += 1
    print()

```
