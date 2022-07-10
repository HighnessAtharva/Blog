---
title: "DSA in Python - Binary Search Trees"
date: 2022-07-09T13:10:34+05:30
draft: false
cover: 
    image: blog/dsa/bst.jpg
    alt: Binary Search Trees
    caption: Learn BST Algorithms in Python
tags: ["DSA-Python"] 

---

- [Find a value in a BST](#find-a-value-in-a-bst)
- [Deletion of a node in a BST](#deletion-of-a-node-in-a-bst)
- [Find min and max value in a BST](#find-min-and-max-value-in-a-bst)
- [Find inorder successor and inorder predecessor in a BST](#find-inorder-successor-and-inorder-predecessor-in-a-bst)
- [Check if a tree is a BST or not](#check-if-a-tree-is-a-bst-or-not)
- [Populate Inorder successor of all nodes](#populate-inorder-successor-of-all-nodes)
- [Find LCA  of 2 nodes in a BST](#find-lca--of-2-nodes-in-a-bst)
- [Construct BST from preorder traversal](#construct-bst-from-preorder-traversal)
- [Convert Binary tree into BST](#convert-binary-tree-into-bst)
- [Convert a normal BST into a Balanced BST](#convert-a-normal-bst-into-a-balanced-bst)
- [Merge two BST](#merge-two-bst)
- [Find Kth largest element and Kth smallest element in a BST](#find-kth-largest-element-and-kth-smallest-element-in-a-bst)
- [Count pairs from 2 BST whose sum is equal to given value "X"](#count-pairs-from-2-bst-whose-sum-is-equal-to-given-value-x)
- [Find the median of BST in O(n) time and O(1) space](#find-the-median-of-bst-in-on-time-and-o1-space)
- [Count BST nodes that lie in a given range](#count-bst-nodes-that-lie-in-a-given-range)
- [Replace every element with the least greater element on its right](#replace-every-element-with-the-least-greater-element-on-its-right)
- [Given "n" appointments, find the conflicting appointments](#given-n-appointments-find-the-conflicting-appointments)
- [Preorder to Postorder](#preorder-to-postorder)
- [Check whether BST contains Dead end](#check-whether-bst-contains-dead-end)
- [Largest BST in a Binary Tree](#largest-bst-in-a-binary-tree)
- [Flatten BST to sorted list](#flatten-bst-to-sorted-list)

## Find a value in a BST

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

## Deletion of a node in a BST

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

## Find min and max value in a BST

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

## Find inorder successor and inorder predecessor in a BST

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

## Check if a tree is a BST or not

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

## Populate Inorder successor of all nodes

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

## Find LCA  of 2 nodes in a BST

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

## Construct BST from preorder traversal

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

## Convert Binary tree into BST

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

## Convert a normal BST into a Balanced BST

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

## Merge two BST

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

## Find Kth largest element and Kth smallest element in a BST

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

## Count pairs from 2 BST whose sum is equal to given value "X"

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

## Find the median of BST in O(n) time and O(1) space

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

## Count BST nodes that lie in a given range

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

## Replace every element with the least greater element on its right

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

## Given "n" appointments, find the conflicting appointments

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

## Preorder to Postorder

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

## Check whether BST contains Dead end

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

## Largest BST in a Binary Tree 

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

## Flatten BST to sorted list

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
