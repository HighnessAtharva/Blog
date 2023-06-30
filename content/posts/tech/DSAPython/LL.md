---
title: "DSA in Python - Linked List"
date: 2022-07-09T13:14:34+05:30
draft: false
cover: 
    image: blog/dsa/Linked-List.webp
    alt: Linked List
    caption: Learn LL Algorithms in Python
tags: ["python"] 
---
## Free Preview - 5 Linked List Problems

### Write a Program to reverse the Linked List. (Both Iterative and recursive)

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

### Reverse a Linked List in group of Given Size. 

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

### Write a program to Detect and Delete loop in a linked list.

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

### Find the starting point of the loop.

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

### Remove Duplicates in a sorted Linked List.

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

## Buy the Interview Guide

{{< gumroad "https://highnessatharva.gumroad.com/l/dsa-python-linked-list" "/blog/gumroad-marketing.webp" >}}