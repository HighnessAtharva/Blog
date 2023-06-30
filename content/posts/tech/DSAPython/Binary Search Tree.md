---
title: "DSA in Python - Binary Search Trees"
date: 2022-07-09T13:10:34+05:30
draft: false
cover: 
    image: blog/dsa/BST.webp
    alt: Binary Search Trees
    caption: Learn BST Algorithms in Python
description: "Master FAANG Interviews with the most frequently asked Binary Search Tree solutions and comprehensive explanations. Boost Skills, Get Paid!"
tags: ["python"] 
---

## Free Preview - 5 Binary Search Tree Problems

### Find a value in a BST

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

### Deletion of a node in a BST

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

### Find min and max value in a BST

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

### Find inorder successor and inorder predecessor in a BST

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

### Check if a tree is a BST or not

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

## Buy the Interview Guide

{{< gumroad "https://highnessatharva.gumroad.com/l/dsa-python-binary-search-tree" "/blog/gumroad-marketing.webp" >}}
