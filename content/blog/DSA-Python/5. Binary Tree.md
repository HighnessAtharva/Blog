---
title: "DSA in Python - Binary Trees"
date: 2022-07-08T13:18:34+05:30
draft: false
cover: 
    image: blog/dsa/binary-tree.jpg
    alt: Binary Tree
    caption: Learn Binary Tree Algorithms in Python
tags: ["DSA-Python"] 

---

- [Level order traversal AKA BFS](#level-order-traversal-aka-bfs)
- [Reverse Level Order traversal](#reverse-level-order-traversal)
- [Height of a tree](#height-of-a-tree)
- [Diameter of a tree](#diameter-of-a-tree)
- [Mirror of a tree / Invert Binary Tree](#mirror-of-a-tree--invert-binary-tree)
- [Inorder, Preorder and Postorder Tree Traversal (Recursive Method)](#inorder-preorder-and-postorder-tree-traversal-recursive-method)
- [Left View of a tree](#left-view-of-a-tree)
- [Right View of Tree](#right-view-of-tree)
- [Top View of a tree](#top-view-of-a-tree)
- [Bottom View of a tree](#bottom-view-of-a-tree)
- [Zig-Zag traversal of a binary tree](#zig-zag-traversal-of-a-binary-tree)
- [Check if a tree is balanced or not](#check-if-a-tree-is-balanced-or-not)
- [Diagonal Traversal of a Binary tree](#diagonal-traversal-of-a-binary-tree)
- [Boundary traversal of a Binary tree](#boundary-traversal-of-a-binary-tree)
- [Construct Binary Tree from String with Bracket Representation](#construct-binary-tree-from-string-with-bracket-representation)
- [Convert Binary tree into Doubly Linked List](#convert-binary-tree-into-doubly-linked-list)
- [Convert Binary tree into Sum tree](#convert-binary-tree-into-sum-tree)
- [Construct Binary tree from Inorder and preorder traversal](#construct-binary-tree-from-inorder-and-preorder-traversal)
- [Find minimum swaps required to convert a Binary tree into BST](#find-minimum-swaps-required-to-convert-a-binary-tree-into-bst)
- [Check if Binary tree is Sum tree or not](#check-if-binary-tree-is-sum-tree-or-not)
- [Check if all leaf nodes are at same level or not](#check-if-all-leaf-nodes-are-at-same-level-or-not)
- [Check if a Binary Tree contains duplicate subtrees of size 2 or more](#check-if-a-binary-tree-contains-duplicate-subtrees-of-size-2-or-more)
- [Check if 2 trees are mirror or not](#check-if-2-trees-are-mirror-or-not)
- [Sum of Nodes on the Longest path from root to leaf node](#sum-of-nodes-on-the-longest-path-from-root-to-leaf-node)
- [Check if given graph is tree or not](#check-if-given-graph-is-tree-or-not)
- [Find Largest subtree sum in a tree](#find-largest-subtree-sum-in-a-tree)
- [Maximum Sum of nodes in Binary tree such that no two are adjacent](#maximum-sum-of-nodes-in-binary-tree-such-that-no-two-are-adjacent)
- [Print all "K" Sum paths in a Binary tree](#print-all-k-sum-paths-in-a-binary-tree)
- [Find Least Common Ancestor in a Binary tree](#find-least-common-ancestor-in-a-binary-tree)
- [Find distance between 2 nodes in a Binary tree](#find-distance-between-2-nodes-in-a-binary-tree)
- [Kth Ancestor of node in a Binary tree](#kth-ancestor-of-node-in-a-binary-tree)
- [Find all Duplicate subtrees in a Binary tree](#find-all-duplicate-subtrees-in-a-binary-tree)
- [Tree Isomorphism Problem](#tree-isomorphism-problem)

## Level order traversal AKA BFS

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

## Reverse Level Order traversal

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

## Height of a tree

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

## Diameter of a tree

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

## Mirror of a tree / Invert Binary Tree

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

## Left View of a tree

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

## Right View of Tree

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

## Top View of a tree

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

## Bottom View of a tree

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

## Zig-Zag traversal of a binary tree

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

## Check if a tree is balanced or not

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

## Diagonal Traversal of a Binary tree

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

## Boundary traversal of a Binary tree

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

## Construct Binary Tree from String with Bracket Representation

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

## Convert Binary tree into Doubly Linked List

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

## Convert Binary tree into Sum tree

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

## Construct Binary tree from Inorder and preorder traversal

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

## Find minimum swaps required to convert a Binary tree into BST

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

## Check if Binary tree is Sum tree or not

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

## Check if all leaf nodes are at same level or not

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

## Check if a Binary Tree contains duplicate subtrees of size 2 or more

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

## Check if 2 trees are mirror or not

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

## Sum of Nodes on the Longest path from root to leaf node

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

## Check if given graph is tree or not

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

## Find Largest subtree sum in a tree

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

## Maximum Sum of nodes in Binary tree such that no two are adjacent

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

## Print all "K" Sum paths in a Binary tree

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

## Find Least Common Ancestor in a Binary tree

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

## Find distance between 2 nodes in a Binary tree

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

## Kth Ancestor of node in a Binary tree

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

## Find all Duplicate subtrees in a Binary tree

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

## Tree Isomorphism Problem

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
