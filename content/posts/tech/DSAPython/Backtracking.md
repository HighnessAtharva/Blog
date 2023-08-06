---
title: "DSA in Python - Backtracking"
date: 2022-07-07T23:18:34+05:30
draft: false
cover: 
    image: blog/dsa/Backtracking.webp
    alt: Backtracking
    caption: Learn Backtracking Algorithms in Python
description: "Master FAANG Interviews with the most frequently asked Backtracking problems with solutions and comprehensive explanations. Boost Skills, Get Paid!"
tags: ["python"] 

---

## Free Preview - 5 Backtracking Problems

### Rat in a maze Problem

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

### Printing all solutions in N-Queen Problem

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

### Word Break Problem using Backtracking

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

### Remove Invalid Parentheses

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

### Sudoku Solver

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

## Buy the Interview Guide

{{< gumroad "https://highnessatharva.gumroad.com/l/dsa-python-backtracking" "/blog/gumroad-marketing.webp" >}}  

---