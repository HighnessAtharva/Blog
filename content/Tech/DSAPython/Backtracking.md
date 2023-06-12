---
title: "DSA in Python - Backtracking"
date: 2022-07-07T23:18:34+05:30
draft: true
cover: 
    image: blog/dsa/backtracking.jpg
    alt: Backtracking
    caption: Learn Backtracking Algorithms in Python
tags: ["DSA-Python"] 

---

- [Rat in a maze Problem](#rat-in-a-maze-problem)
- [Printing all solutions in N-Queen Problem](#printing-all-solutions-in-n-queen-problem)
- [Word Break Problem using Backtracking](#word-break-problem-using-backtracking)
- [Remove Invalid Parentheses](#remove-invalid-parentheses)
- [Sudoku Solver](#sudoku-solver)
- [m-Colouring Problem](#m-colouring-problem)
- [Print all palindromic partitions of a string](#print-all-palindromic-partitions-of-a-string)
- [Subset Sum Problem](#subset-sum-problem)
- [The Knight’s tour problem](#the-knights-tour-problem)
- [Tug of War](#tug-of-war)
- [Find shortest safe route in a path with landmines](#find-shortest-safe-route-in-a-path-with-landmines)
- [Combinational Sum](#combinational-sum)
- [Find Maximum number possible by doing at-most K swaps](#find-maximum-number-possible-by-doing-at-most-k-swaps)
- [Print all permutations of a string](#print-all-permutations-of-a-string)
- [Find if there is a path of more than k length from a source](#find-if-there-is-a-path-of-more-than-k-length-from-a-source)
- [Longest Possible Route in a Matrix with Hurdles](#longest-possible-route-in-a-matrix-with-hurdles)
- [Print all possible paths from top left to bottom right of a mXn matrix](#print-all-possible-paths-from-top-left-to-bottom-right-of-a-mxn-matrix)
- [Partition of a set intoK subsets with equal sum](#partition-of-a-set-intok-subsets-with-equal-sum)
- [Find the K-th Permutation Sequence of first N natural numbers](#find-the-k-th-permutation-sequence-of-first-n-natural-numbers)

## Rat in a maze Problem

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

## Printing all solutions in N-Queen Problem

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

## Word Break Problem using Backtracking

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

## Remove Invalid Parentheses

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

## Sudoku Solver

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

## m-Colouring Problem

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

## Print all palindromic partitions of a string

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

## Subset Sum Problem

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

## The Knight’s tour problem

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

## Tug of War

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

## Find shortest safe route in a path with landmines

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

## Combinational Sum

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

## Find Maximum number possible by doing at-most K swaps

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

## Print all permutations of a string

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

## Find if there is a path of more than k length from a source

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

## Longest Possible Route in a Matrix with Hurdles

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

## Print all possible paths from top left to bottom right of a mXn matrix

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

## Partition of a set intoK subsets with equal sum

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

"""*
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

## Find the K-th Permutation Sequence of first N natural numbers

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
