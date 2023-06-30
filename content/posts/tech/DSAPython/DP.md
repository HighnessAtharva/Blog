---
title: "DSA in Python - Dynamic Programming"
date: 2022-07-10T13:11:34+05:30
draft: false
cover: 
    image: blog/dsa/DP.webp
    alt: Dynamic Programming
    caption: Learn DP Algorithms in Python
description: "Master FAANG Interviews with the most frequently asked Dynamic Programming solutions and comprehensive explanations. Boost Skills, Get Paid!"
tags: ["python"] 
---
## Free Preview - 5 Dynamic Programming Problems

### Coin ChangeProblem

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

### Knapsack Problem

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

### Binomial CoefficientProblem

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

### Permutation CoefficientProblem

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

### Program for nth Catalan Number

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


## Buy the Interview Guide

{{< gumroad "https://highnessatharva.gumroad.com/l/dsa-python-dynamic-programming" "/blog/gumroad-marketing.webp" >}}