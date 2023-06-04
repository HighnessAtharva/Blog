---
title: "DSA in Python - Dynamic Programming"
date: 2022-07-10T13:11:34+05:30
draft: true
cover: 
    image: blog/dsa/dp.jpg
    alt: Dynamic Programming
    caption: Learn DP Algorithms in Python
tags: ["DSA-Python"] 

---

- [Coin ChangeProblem](#coin-changeproblem)
- [Knapsack Problem](#knapsack-problem)
- [Binomial CoefficientProblem](#binomial-coefficientproblem)
- [Permutation CoefficientProblem](#permutation-coefficientproblem)
- [Program for nth Catalan Number](#program-for-nth-catalan-number)
- [Matrix Chain Multiplication](#matrix-chain-multiplication)
- [Edit Distance](#edit-distance)
- [Subset Sum Problem](#subset-sum-problem)
- [Friends Pairing Problem](#friends-pairing-problem)
- [Gold Mine Problem](#gold-mine-problem)
- [Assembly Line SchedulingProblem](#assembly-line-schedulingproblem)
- [Painting the Fence Problem](#painting-the-fence-problem)
- [Rod Cutting Problem](#rod-cutting-problem)
- [Longest Common Subsequence](#longest-common-subsequence)
- [Longest Repeated Subsequence](#longest-repeated-subsequence)
- [Longest Increasing Subsequence](#longest-increasing-subsequence)
- [Space Optimized Solution of LCS (Print only length)](#space-optimized-solution-of-lcs-print-only-length)
- [LCS (Longest Common Subsequence) of three strings](#lcs-longest-common-subsequence-of-three-strings)
- [Maximum Sum Increasing Subsequence](#maximum-sum-increasing-subsequence)
- [Count all subsequences having product less than K](#count-all-subsequences-having-product-less-than-k)
- [Longest subsequence such that difference between adjacent is one](#longest-subsequence-such-that-difference-between-adjacent-is-one)
- [Maximum subsequence sum such that no three are consecutive](#maximum-subsequence-sum-such-that-no-three-are-consecutive)
- [Egg Dropping Problem](#egg-dropping-problem)
- [Maximum Length Chain of Pairs](#maximum-length-chain-of-pairs)
- [Maximum size square sub-matrix with all 1s](#maximum-size-square-sub-matrix-with-all-1s)
- [Maximum sum of pairs with specific difference](#maximum-sum-of-pairs-with-specific-difference)
- [Min Cost PathProblem](#min-cost-pathproblem)
- [Maximum difference of zeros and ones in binary string](#maximum-difference-of-zeros-and-ones-in-binary-string)
- [Minimum number of jumps to reach end](#minimum-number-of-jumps-to-reach-end)
- [Minimum cost to fill given weight in a bag](#minimum-cost-to-fill-given-weight-in-a-bag)
- [Minimum removals from array to make max –min \<= K](#minimum-removals-from-array-to-make-max-min--k)
- [Longest Common Substring](#longest-common-substring)
- [Count number of ways to reacha given score in a game](#count-number-of-ways-to-reacha-given-score-in-a-game)
- [Count Balanced Binary Trees of Height h](#count-balanced-binary-trees-of-height-h)
- [Smallest sum contiguous subarray](#smallest-sum-contiguous-subarray)
- [Unbounded Knapsack (Repetition of items allowed)](#unbounded-knapsack-repetition-of-items-allowed)
- [Largest Independent Set Problem](#largest-independent-set-problem)
- [Partition problem](#partition-problem)
- [Longest Palindromic Subsequence](#longest-palindromic-subsequence)
- [Count All Palindromic Subsequence in a given String](#count-all-palindromic-subsequence-in-a-given-string)
- [Longest Palindromic Substring](#longest-palindromic-substring)
- [Longest alternating subsequence](#longest-alternating-subsequence)
- [Weighted Job Scheduling](#weighted-job-scheduling)
- [Coin game winner where every player has three choices](#coin-game-winner-where-every-player-has-three-choices)
- [Count Derangements (Permutation such that no element appears in its original position)](#count-derangements-permutation-such-that-no-element-appears-in-its-original-position)
- [Maximum profit by buying and selling a share at most twice](#maximum-profit-by-buying-and-selling-a-share-at-most-twice)
- [Optimal Strategy for a Game](#optimal-strategy-for-a-game)
- [Optimal Binary Search Tree](#optimal-binary-search-tree)
- [Palindrome PartitioningProblem](#palindrome-partitioningproblem)
- [Word Wrap Problem](#word-wrap-problem)
- [Mobile Numeric Keypad Problem](#mobile-numeric-keypad-problem)
- [Boolean Parenthesization Problem](#boolean-parenthesization-problem)
- [Largest rectangular sub-matrix whose sum is 0](#largest-rectangular-sub-matrix-whose-sum-is-0)
- [Maximum sum rectangle in a 2D matrix](#maximum-sum-rectangle-in-a-2d-matrix)
- [Maximum profit by buying and selling a share at most k times](#maximum-profit-by-buying-and-selling-a-share-at-most-k-times)
- [Find if a string is interleaved of two other strings](#find-if-a-string-is-interleaved-of-two-other-strings)

## Coin ChangeProblem

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

## Knapsack Problem

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

## Binomial CoefficientProblem

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

## Permutation CoefficientProblem

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

## Program for nth Catalan Number

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

## Matrix Chain Multiplication

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

## Edit Distance

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

## Subset Sum Problem

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

## Friends Pairing Problem

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

## Gold Mine Problem

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

## Assembly Line SchedulingProblem

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

## Painting the Fence Problem

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

## Longest Common Subsequence

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

## Longest Repeated Subsequence

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

## Longest Increasing Subsequence

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

## Space Optimized Solution of LCS (Print only length)

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

## LCS (Longest Common Subsequence) of three strings

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

## Maximum Sum Increasing Subsequence

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

## Count all subsequences having product less than K

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

## Longest subsequence such that difference between adjacent is one

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

## Maximum subsequence sum such that no three are consecutive

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

## Egg Dropping Problem

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

## Maximum Length Chain of Pairs

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

## Maximum size square sub-matrix with all 1s

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

## Maximum sum of pairs with specific difference

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

## Min Cost PathProblem

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

## Maximum difference of zeros and ones in binary string

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

## Minimum number of jumps to reach end

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

## Minimum cost to fill given weight in a bag

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

## Minimum removals from array to make max –min <= K

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

## Longest Common Substring

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

## Count number of ways to reacha given score in a game

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

## Count Balanced Binary Trees of Height h

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

## Smallest sum contiguous subarray

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

## Unbounded Knapsack (Repetition of items allowed)

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

## Largest Independent Set Problem

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

## Partition problem

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

## Longest Palindromic Subsequence

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

## Count All Palindromic Subsequence in a given String

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

## Longest Palindromic Substring

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

## Longest alternating subsequence

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

## Weighted Job Scheduling

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

## Coin game winner where every player has three choices

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

## Count Derangements (Permutation such that no element appears in its original position)

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

## Maximum profit by buying and selling a share at most twice

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

## Optimal Strategy for a Game

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

## Optimal Binary Search Tree

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

## Palindrome PartitioningProblem

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

## Word Wrap Problem

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

## Mobile Numeric Keypad Problem

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

## Boolean Parenthesization Problem

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

## Largest rectangular sub-matrix whose sum is 0

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

## Maximum sum rectangle in a 2D matrix

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

## Maximum profit by buying and selling a share at most k times

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

## Find if a string is interleaved of two other strings

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
