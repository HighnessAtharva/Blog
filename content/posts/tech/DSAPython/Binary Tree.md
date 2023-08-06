---
title: "DSA in Python - Binary Trees"
date: 2022-07-08T13:18:34+05:30
draft: false
cover: 
    image: blog/dsa/Binary-Tree.webp
    alt: Binary Tree
    caption: Learn Binary Tree Algorithms in Python
description: "Master FAANG Interviews with the most frequently asked Binary Tree problems with solutions and comprehensive explanations. Boost Skills, Get Paid!"
tags: ["python"] 
---

## Free Preview - 5 Binary Tree Problems

### Level order traversal AKA BFS

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

### Reverse Level Order traversal

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

### Height of a tree

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

### Diameter of a tree

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

### Mirror of a tree / Invert Binary Tree

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

## Buy the Interview Guide

{{< gumroad "https://highnessatharva.gumroad.com/l/dsa-python-binary-tree" "/blog/gumroad-marketing.webp" >}}

---