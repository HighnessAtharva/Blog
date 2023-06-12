---
title: "DSA in Python - Greedy"
date: 2022-07-09T13:14:34+05:30
draft: true
cover: 
    image: blog/dsa/greedy.jpg
    alt: Greedy
    caption: Learn Greedy Algorithms in Python
tags: ["DSA-Python"] 

---

- [Activity Selection Problem](#activity-selection-problem)
- [Huffman Coding](#huffman-coding)
- [Water Connection Problem](#water-connection-problem)
- [Fractional Knapsack Problem](#fractional-knapsack-problem)
- [Greedy Algorithm to find Minimum number of Coins](#greedy-algorithm-to-find-minimum-number-of-coins)
- [Maximum trains for which stoppage can be provided](#maximum-trains-for-which-stoppage-can-be-provided)
- [Minimum Platforms Problem](#minimum-platforms-problem)
- [Buy Maximum Stocks if i stocks can be bought on i-th day](#buy-maximum-stocks-if-i-stocks-can-be-bought-on-i-th-day)
- [Find the minimum and maximum amount to buy all N candies](#find-the-minimum-and-maximum-amount-to-buy-all-n-candies)
- [Minimum Cost to cut a board into squares](#minimum-cost-to-cut-a-board-into-squares)
- [Check if it is possible to survive on Island](#check-if-it-is-possible-to-survive-on-island)
- [Maximum product subset of an array](#maximum-product-subset-of-an-array)
- [Maximize array sum after K negations](#maximize-array-sum-after-k-negations)
- [Maximize the sum of arr i\*i](#maximize-the-sum-of-arr-ii)
- [Maximum sum of absolute difference of an array](#maximum-sum-of-absolute-difference-of-an-array)
- [Maximize sum of consecutive differences in a circular array](#maximize-sum-of-consecutive-differences-in-a-circular-array)
- [Minimum sum of absolute difference of pairs of two arrays](#minimum-sum-of-absolute-difference-of-pairs-of-two-arrays)
- [Program for Shortest Job First (or SJF) CPU Scheduling](#program-for-shortest-job-first-or-sjf-cpu-scheduling)
- [Program for Least Recently Used (LRU) Page Replacement algorithm](#program-for-least-recently-used-lru-page-replacement-algorithm)
- [Smallest subset with sum greater than all other elements](#smallest-subset-with-sum-greater-than-all-other-elements)
- [Chocolate Distribution Problem](#chocolate-distribution-problem)
- [K Centers Problem](#k-centers-problem)
- [Minimum Cost of ropes](#minimum-cost-of-ropes)
- [Find smallest number with given number of digits and sum of digits](#find-smallest-number-with-given-number-of-digits-and-sum-of-digits)
- [Rearrange characters in a string such that no two adjacent are same](#rearrange-characters-in-a-string-such-that-no-two-adjacent-are-same)
- [Find maximum sum possible equal sum of three stacks](#find-maximum-sum-possible-equal-sum-of-three-stacks)

## Activity Selection Problem

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

## Huffman Coding

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

## Water Connection Problem

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

## Fractional Knapsack Problem

```python
TODO
```

## Greedy Algorithm to find Minimum number of Coins

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

## Maximum trains for which stoppage can be provided

```python
TODO
```

## Minimum Platforms Problem

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

## Buy Maximum Stocks if i stocks can be bought on i-th day

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

## Find the minimum and maximum amount to buy all N candies

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


## Minimum Cost to cut a board into squares

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

## Check if it is possible to survive on Island

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

## Maximum product subset of an array

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

## Maximize array sum after K negations

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

## Maximize the sum of arr i*i

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

## Maximum sum of absolute difference of an array

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

## Maximize sum of consecutive differences in a circular array

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

## Minimum sum of absolute difference of pairs of two arrays

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

## Program for Shortest Job First (or SJF) CPU Scheduling

```python
TODO
```

## Program for Least Recently Used (LRU) Page Replacement algorithm

```python
TODO
```

## Smallest subset with sum greater than all other elements

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

## Chocolate Distribution Problem

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

## K Centers Problem

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

## Minimum Cost of ropes

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

## Find smallest number with given number of digits and sum of digits

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

## Rearrange characters in a string such that no two adjacent are same

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

## Find maximum sum possible equal sum of three stacks

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