---
title: "DSA in Python - Linked List"
date: 2022-07-09T13:14:34+05:30
draft: true
cover: 
    image: blog/dsa/ll.jpg
    alt: Linked List
    caption: Learn LL Algorithms in Python
tags: ["python"] 

---
- [Write a Program to reverse the Linked List. (Both Iterative and recursive)](#write-a-program-to-reverse-the-linked-list-both-iterative-and-recursive)
- [Reverse a Linked List in group of Given Size.](#reverse-a-linked-list-in-group-of-given-size)
- [Write a program to Detect and Delete loop in a linked list.](#write-a-program-to-detect-and-delete-loop-in-a-linked-list)
- [Find the starting point of the loop.](#find-the-starting-point-of-the-loop)
- [Remove Duplicates in a sorted Linked List.](#remove-duplicates-in-a-sorted-linked-list)
- [Remove Duplicates in a Un-sorted Linked List.](#remove-duplicates-in-a-un-sorted-linked-list)
- [Write a Program to Move the last element to Front in a Linked List.](#write-a-program-to-move-the-last-element-to-front-in-a-linked-list)
- [Add “1” to a number represented as a Linked List.](#add-1-to-a-number-represented-as-a-linked-list)
- [Add two numbers represented by linked lists.](#add-two-numbers-represented-by-linked-lists)
- [Intersection of two Sorted Linked List](#intersection-of-two-sorted-linked-list)
- [Intersection Point of two Linked Lists](#intersection-point-of-two-linked-lists)
- [Merge Sort For Linked lists](#merge-sort-for-linked-lists)
- [Quicksort for Linked Lists](#quicksort-for-linked-lists)
- [Find the middle Element of a linked list](#find-the-middle-element-of-a-linked-list)
- [Check if a linked list is a circular linked list](#check-if-a-linked-list-is-a-circular-linked-list)
- [Split a Circular linked list into two halves](#split-a-circular-linked-list-into-two-halves)
- [Write a Program to check whether the Singly Linked list is a palindrome or not](#write-a-program-to-check-whether-the-singly-linked-list-is-a-palindrome-or-not)
- [Deletion from a Circular Linked List](#deletion-from-a-circular-linked-list)
- [Reverse a Doubly Linked list](#reverse-a-doubly-linked-list)
- [Find pairs with a given sum in a DLL](#find-pairs-with-a-given-sum-in-a-dll)
- [Count triplets in a sorted DLL whose sum is equal to given value “X”](#count-triplets-in-a-sorted-dll-whose-sum-is-equal-to-given-value-x)
- [Sort a “k”sorted Doubly Linked list](#sort-a-ksorted-doubly-linked-list)
- [Rotate DoublyLinked list by N nodes](#rotate-doublylinked-list-by-n-nodes)
- [Rotate a Doubly Linked list in group of Given Size](#rotate-a-doubly-linked-list-in-group-of-given-size)
- [Can we reverse a linked list in less than O(n) ?](#can-we-reverse-a-linked-list-in-less-than-on-)
- [Why Quicksort is preferred for. Arrays and Merge Sort for LinkedLists ?\]](#why-quicksort-is-preferred-for-arrays-and-merge-sort-for-linkedlists-)
- [Flatten a Linked List](#flatten-a-linked-list)
- [Sort a LL of 0's, 1's and 2's](#sort-a-ll-of-0s-1s-and-2s)
- [Clone a linked list with next and random pointer](#clone-a-linked-list-with-next-and-random-pointer)
- [Merge K sorted Linked list](#merge-k-sorted-linked-list)
- [Multiply 2 no. represented by LL](#multiply-2-no-represented-by-ll)
- [Delete nodes which have a greater value on right side](#delete-nodes-which-have-a-greater-value-on-right-side)
- [Segregate even and odd nodes in a Linked List](#segregate-even-and-odd-nodes-in-a-linked-list)
- [Program for n’th node from the end of a Linked List](#program-for-nth-node-from-the-end-of-a-linked-list)
- [Find the first non-repeating character from a stream of characters](#find-the-first-non-repeating-character-from-a-stream-of-characters)

## Write a Program to reverse the Linked List. (Both Iterative and recursive)

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

## Reverse a Linked List in group of Given Size. 

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

## Write a program to Detect and Delete loop in a linked list.

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

## Find the starting point of the loop.

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

## Remove Duplicates in a sorted Linked List.

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

## Remove Duplicates in a Un-sorted Linked List.

```python
class Node():
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList():
	def __init__(self):
		self.head = None

	def remove_duplicates(self):
		ptr1 = None
		ptr2 = None
		dup = None
		ptr1 = self.head

		# Pick elements one by one
		while (ptr1 != None and ptr1.next != None):
			ptr2 = ptr1
			# Compare the picked element with rest of the elements
			while (ptr2.next != None):
				# If duplicate then delete it
				if (ptr1.data == ptr2.next.data):
					# Sequence of steps is important here
					dup = ptr2.next
					ptr2.next = ptr2.next.next
				else:
					ptr2 = ptr2.next
			ptr1 = ptr1.next


	def printList(self):
		temp = self.head
		while(temp != None):
			print(temp.data, end=" ")
			temp = temp.next
		print()


list1 = LinkedList()
list1.head = Node(10)
list1.head.next = Node(12)
list1.head.next.next = Node(11)
list1.head.next.next.next = Node(11)
list1.head.next.next.next.next = Node(12)
list1.head.next.next.next.next.next = Node(11)
list1.head.next.next.next.next.next.next = Node(10)
print("Linked List before removing duplicates :")
list1.printList()
list1.remove_duplicates()
print()
print("Linked List after removing duplicates :")
list1.printList()
```

## Write a Program to Move the last element to Front in a Linked List.

```python
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def push(self, data):
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node
		

	def printList(self):
		tmp = self.head
		while tmp is not None:
			print(tmp.data, end=", ")
			tmp = tmp.next
		print()

	# Function to bring the last node to the front
	def moveToFront(self):
		tmp = self.head
		sec_last = None # To maintain the track of  the second last node

	# To check whether we have not received the empty list or list with a single node
		if not tmp or not tmp.next:
			return

		# Iterate till the end to get the last and second last node
		while tmp and tmp.next :
			sec_last = tmp
			tmp = tmp.next

		# point the next of the second last node to None
		sec_last.next = None

		# Make the last node as the first Node
		tmp.next = self.head
		self.head = tmp


llist = LinkedList()
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)
print ("Linked List before moving last to front ")
llist.printList()
llist.moveToFront()
print ("Linked List after moving last to front ")
llist.printList()

```

## Add “1” to a number represented as a Linked List.

```python
import sys
import math

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


def newNode(data):
	return Node(data)

def reverseList(head):
	if not head:
		return
	curNode = head
	prevNode = head
	nextNode = head.next
	curNode.next = None
	while(nextNode):
		curNode = nextNode
		nextNode = nextNode.next
		curNode.next = prevNode
		prevNode = curNode
	return curNode


def addOne(head):
	# Reverse linked list and add one to head
	head = reverseList(head)
	k = head
	carry = 0
	prev = None
	head.data += 1

	# update carry for next calculation
	while (head != None) and (head.data > 9 or carry > 0):
		prev = head
		head.data += carry
		carry = head.data // 10
		head.data %= 10
		head = head.next

	if carry > 0:
		prev.next = Node(carry)
	# Reverse the modified list
	return reverseList(k)

def printList(head):
	if not head:
		return
	while head:
		print(f"{head.data}", end="")
		head = head.next

head = newNode(1)
head.next = newNode(9)
head.next.next = newNode(9)
head.next.next.next = newNode(9)
print("List is: ", end="")
printList(head)
head = addOne(head)
print("\nResultant list is: ", end="")
printList(head)
```

## Add two numbers represented by linked lists.

```python
    class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	# Method to traverse list and return it in a format
	def traverse(self):
		linkedListStr = ""
		temp = self.head
		while temp:
			linkedListStr += f"{str(temp.data)} -> "
			temp = temp.next
		return f"{linkedListStr}NULL"

	# Method to insert data in linked list
	def insert(self, data):
		newNode = Node(data)
		if self.head is not None:
			newNode.next = self.head
		self.head = newNode

# Helper function to reverse the list
def reverse(Head):
	
	if (Head is None and
		Head.next is None):
		return Head
		
	prev = None
	curr = Head
	
	while curr:
		temp = curr.next
		curr.next = prev
		prev = curr
		curr = temp
		
	Head = prev
	return Head

# Function to add two lists
def listSum(l1, l2):

	if l1 is None:
		return l1
	if l2 is None:
		return l2

	# Reverse first list
	l1 = reverse(l1)

	# Reverse second list
	l2 = reverse(l2)

	# Storing head whose reverse is to be returned This is where which will be final node
	head = l1
	prev = None
	c = 0
	sum = 0
	while l1 is not None and l2 is not None:
		sum = c + l1.data + l2.data
		l1.data = sum % 10
		c = int(sum / 10)
		prev = l1
		l1 = l1.next
		l2 = l2.next
		
	if l1 is not None or l2 is not None:
		if l2 is not None:
			prev.next = l2
		l1 = prev.next
		
		while l1 is not None:
			sum = c + l1.data
			l1.data = sum % 10
			c = int(sum / 10)
			prev = l1
			l1 = l1.next	
	if c > 0:
		prev.next = Node(c)
	return reverse(head)
	

linkedList1 = LinkedList()
linkedList1.insert(3)
linkedList1.insert(6)
linkedList1.insert(5)

linkedList2 = LinkedList()
linkedList2.insert(2)
linkedList2.insert(4)
linkedList2.insert(8)

linkedList3 = LinkedList()
linkedList3.head = listSum(linkedList1.head, linkedList2.head)
print(linkedList3.traverse())
```

## Intersection of two Sorted Linked List

```python
class Node:
	def __init__(self):
		self.data = 0
		self.next = None

def printList(node):
	while (node != None):
		print(node.data, end=" ")
		node = node.next

def new_node(data):
	return Node()
	
def push(head_ref, new_data):
	new_node = Node()
	new_node.data = new_data
	new_node.next = head_ref
	head_ref = new_node
	return head_ref


def intersection(tmp1,tmp2,k):
	res = [0]*k
	set1 = set()
	while (tmp1 != None):
		set1.add(tmp1.data)
		tmp1 = tmp1.next
	cnt = 0
	while (tmp2 != None):
		if tmp2.data in set1:
			res[cnt] = tmp2.data
			cnt += 1
		tmp2 = tmp2.next
	return res

def printList(node):
	while (node != None):
		print(node.data, end=" ")
		node = node.next	

# Start with the empty lists
ll = None
ll1 = None
		
ll = push(ll , 7)
ll = push(ll , 6)
ll = push(ll , 5)
ll = push(ll , 4)
ll = push(ll , 3)
ll = push(ll , 2)
ll = push(ll , 1)
ll = push(ll , 0)
		
ll1 = push(ll1 , 7)
ll1 = push(ll1 , 6)
ll1 = push(ll1 , 5)
ll1 = push(ll1 , 4)
ll1 = push(ll1 , 3)
ll1 = push(ll1 , 12)
ll1 = push(ll1 , 0)
ll1 = push(ll1 , 9)

arr = intersection(ll , ll1 , 6)
print(arr)
```

## Intersection Point of two Linked Lists

```python
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

# function to get the intersection point of two linked lists head1 and head
def getIntersectionNode(head1, head2):
	while head2:
		temp = head1
		while temp:
			# if both Nodes are same
			if temp == head2:
				return head2
			temp = temp.next
		head2 = head2.next
	# intersection is not present between the lists
	return None

'''
Create two linked lists
1st 3->6->9->15->30
2nd 10->15->30
15 is the intersection point
'''
newNode = Node(10)
head1 = newNode
newNode = Node(3)
head2 = newNode
newNode = Node(6)
head2.next = newNode
newNode = Node(9)
head2.next.next = newNode
newNode = Node(15)
head1.next = newNode
head2.next.next.next = newNode
newNode = Node(30)
head1.next.next = newNode
if intersectionPoint := getIntersectionNode(head1, head2):
	print("Intersection Point:", intersectionPoint.data)
else:
	print(" No Intersection Point ")
```

## Merge Sort For Linked lists

```python
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None
	
	# push new value to linked list using append method
	def append(self, new_value):
		
		# Allocate new node
		new_node = Node(new_value)
		
		# if head is None, initialize it to new node
		if self.head is None:
			self.head = new_node
			return
		curr_node = self.head
		while curr_node.next is not None:
			curr_node = curr_node.next
			
		# Append the new node at the end of the linked list
		curr_node.next = new_node
		
	def sortedMerge(self, a, b):
		result = None
		
		# Base cases
		if a is None:
			return b
		if b is  None:
			return a
			
		# pick either a or b and recur..
		if a.data <= b.data:
			result = a
			result.next = self.sortedMerge(a.next, b)
		else:
			result = b
			result.next = self.sortedMerge(a, b.next)
		return result
	
	def mergeSort(self, h):
		# Base case if head is None
		if h is None or h.next is None:
			return h

		# get the middle of the list
		middle = self.getMiddle(h)
		nexttomiddle = middle.next

		# set the next of middle node to None
		middle.next = None

		# Apply mergeSort on left list
		left = self.mergeSort(h)

		# Apply mergeSort on right list
		right = self.mergeSort(nexttomiddle)

		return self.sortedMerge(left, right)

	def getMiddle(self, head):
		if head is None:
			return head
		slow = head
		fast = head
		while (fast.next != None and
			fast.next.next != None):
			slow = slow.next
			fast = fast.next.next
		return slow
		
def printList(head):
	if head is None:
		print(' ')
		return
	curr_node = head
	while curr_node:
		print(curr_node.data, end = " ")
		curr_node = curr_node.next
	print(' ')
	

li = LinkedList()
li.append(15)
li.append(10)
li.append(5)
li.append(20)
li.append(3)
li.append(2)
li.head = li.mergeSort(li.head)
print ("Sorted Linked List is:")
printList(li.head)
```

## Quicksort for Linked Lists

```python
class Node:
	def __init__(self, val):
		self.data = val
		self.next = None

class QuickSortLinkedList:
	def __init__(self):
		self.head=None

	def addNode(self,data):
		if self.head is None:
			self.head = Node(data)
			return
		curr = self.head
		while (curr.next != None):
			curr = curr.next
		newNode = Node(data)
		curr.next = newNode

	def printList(self,n):
		while (n != None):
			print(n.data, end=" ")
			n = n.next

	''' takes first and last node,but do not
	break any links in the whole linked list'''
	def paritionLast(self,start, end):
		if start == end or start is None or end is None:
			return start

		pivot_prev = start
		curr = start
		pivot = end.data

		'''iterate till one before the end,
		no need to iterate till the end because end is pivot'''

		while (start != end):
			if (start.data < pivot):

				# keep tracks of last modified item
				pivot_prev = curr
				temp = curr.data
				curr.data = start.data
				start.data = temp
				curr = curr.next
			start = start.next

		'''swap the position of curr i.e. next suitable index and pivot'''
		temp = curr.data
		curr.data = pivot
		end.data = temp

		''' return one previous to current because current is now pointing to pivot '''
		return pivot_prev

	def sort(self, start, end):
		if start is None or start == end or start == end.next:
			return

		# split list and partition recurse
		pivot_prev = self.paritionLast(start, end)
		self.sort(start, pivot_prev)

		'''
		if pivot is picked and moved to the start, that means start and pivot is same so pick from next of pivot
		'''
		if(pivot_prev != None and pivot_prev == start):
			self.sort(pivot_prev.next, end)

		# if pivot is in between of the list,start from next of pivot, since we have pivot_prev, so we move two nodes
		elif (pivot_prev != None and pivot_prev.next != None):
			self.sort(pivot_prev.next.next, end)


ll = QuickSortLinkedList()
ll.addNode(30)
ll.addNode(3)
ll.addNode(4)
ll.addNode(20)
ll.addNode(5)
n = ll.head
while n.next is not None:
	n = n.next
print("\nLinked List before sorting")
ll.printList(ll.head)
ll.sort(ll.head, n)
print("\nLinked List after sorting");
ll.printList(ll.head)

```

## Find the middle Element of a linked list

```python
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None 


class LinkedList:
	def __init__(self):
		self.head = None

	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	def printList(self):
		node = self.head
		while node:
			print(f"{str(node.data)}->", end="")
			node = node.next
		print("NULL")


	def printMiddle(self):
		# Initialize two pointers, one will go one step a time (slow), another two at a time (fast)
		slow = self.head
		fast = self.head
		# Iterate till fast's next is null (fast reaches end)
		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next
		# return the slow's data, which would be the middle element.
		print("The middle element is ", slow.data)


# Start with the empty list
llist = LinkedList()
for i in range(5, 0, -1):
	llist.push(i)
llist.printList()
llist.printMiddle()

```

## Check if a linked list is a circular linked list

```python
class Node:
	def __init__(self, data):
		self.data = data # Assign data
		self.next = None # Initialize next as null


class LinkedList:
	def __init__(self):
		self.head = None

def Circular(head):
	if head is None:
		return True
	node = head.next
	i = 0
	while((node is not None) and (node is not head)):
		i = i + 1
		node = node.next
	return node==head


llist = LinkedList()
llist.head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)

llist.head.next = second;
second.next = third;
third.next = fourth

if (Circular(llist.head)):
	print('Yes')
else:
	print('No')

fourth.next = llist.head

if (Circular(llist.head)):
	print('Yes')
else:
	print('No')
```

## Split a Circular linked list into two halves

```python
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class CircularLinkedList:
	def __init__(self):
		self.head = None
	# circular linked list
	def push(self, data):
		ptr1 = Node(data)
		temp = self.head
		
		ptr1.next = self.head

		# If linked list is not None then set the next of last node
		if self.head is not None:
			while(temp.next != self.head):
				temp = temp.next
			temp.next = ptr1

		else:
			ptr1.next = ptr1 # For the first node

		self.head = ptr1


	def printList(self):
		temp = self.head
		if self.head is not None:
			while(True):
				print ("%d" %(temp.data),end=' ')
				temp = temp.next
				if (temp == self.head):
					break


	# Function to split a list (starting with head) into two lists. head1 and head2 are the head nodes of the two resultant linked lists
	def splitList(self, head1, head2):
		slow_ptr = self.head
		fast_ptr = self.head
	
		if self.head is None:
			return
		
		# If there are odd nodes in the circular list then fast_ptr->next becomes head and for even nodes fast_ptr->next->next becomes head
		while(fast_ptr.next != self.head and
			fast_ptr.next.next != self.head ):
			fast_ptr = fast_ptr.next.next
			slow_ptr = slow_ptr.next

		# If there are even elements in list then move fast_ptr
		if fast_ptr.next.next == self.head:
			fast_ptr = fast_ptr.next

		# Set the head pointer of first half
		head1.head = self.head

		# Set the head pointer of second half
		if self.head.next != self.head:
			head2.head = slow_ptr.next

		# Make second half circular
		fast_ptr.next = slow_ptr.next
	
		# Make first half circular
		slow_ptr.next = self.head


# Initialize lists as empty
head = CircularLinkedList()
head1 = CircularLinkedList()
head2 = CircularLinkedList()

head.push(12)
head.push(56)
head.push(2)
head.push(11)

print ("Original Circular Linked List")
head.printList()

# Split the list
head.splitList(head1 , head2)

print ("\nFirst Circular Linked List")
head1.printList()

print ("\nSecond Circular Linked List")
head2.printList()
```

## Write a Program to check whether the Singly Linked list is a palindrome or not

```python
class Node:
	def __init__(self,data):
		self.data = data
		self.ptr = None

def ispalindrome(head):
	# Temp pointer
	slow = head

	# Declare a stack
	stack = []
	
	ispalin = True

	# Push all elements of the list to the stack
	while slow != None:
		stack.append(slow.data)
		# Move ahead
		slow = slow.ptr

	# Iterate in the list again and check by popping from the stack
	while head != None:
		# Get the top most element
		i = stack.pop()
		
		# Check if data is not same as popped element
		if head.data == i:
			ispalin = True
		else:
			ispalin = False
			break

		# Move ahead
		head = head.ptr
	return ispalin


# Addition of linked list
one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(3)
six = Node(2)
seven = Node(1)

# Initialize the next pointer of every current pointer
one.ptr = two
two.ptr = three
three.ptr = four
four.ptr = five
five.ptr = six
six.ptr = seven
seven.ptr = None

result = ispalindrome(one)
print("isPalindrome:", result)
```

## Deletion from a Circular Linked List

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def deleteNode(head, key):
    t = head
    while t and t.next != head:
        if t.next.data == key:
            t.next = t.next.next
        t = t.next

def reverse(head):
    arr = []
    t = head
    arr.append(t.data)
    t = t.next
    while t != head:
        arr.append(t.data)
        t = t.next
    arr = arr[::-1]
    t = head
    i = 0 
    while t != None:
        if t.next == head:
            t.data = arr[len(arr)-1]
            break
        else:
            t.data = arr[i]
        t = t.next
        i+=1
def push(data, prev):
    if prev is None:
        prev = Node(data)
        return prev
    tmp = Node(data)
    prev.next = tmp
    return tmp

def printList(head):
    flg = False
    tmp = head
    while flg is False or tmp != head:
        flg = True
        print(tmp.data, end=" ")
        tmp = tmp.next
    print()

n = 5
arr = [1,2,3,4,5]
delNode = 4

head = Node(None)
prev = head
for i in arr:
    prev = push(i, prev)
head = head.next
prev.next = head
deleteNode(head, delNode)
reverse(head)
printList(head)
```

## Reverse a Doubly Linked list

```python
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None


class DoublyLinkedList:
	
	def __init__(self):
		self.head = None
	
	def reverse(self):
		temp = None
		current = self.head

		# Swap next and prev for all nodes of doubly linked list
		while current is not None:
			temp = current.prev
			current.prev = current.next
			current.next = temp
			current = current.prev

		# Before changing head, check for the cases like empty list and list with only one node
		if temp is not None:
			self.head = temp.prev

	# Given a reference to the head of a list and an integer,inserts a new node on the front of list
	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		if self.head is not None:
			self.head.prev = new_node
		self.head = new_node

	def printList(self, node):
		while(node is not None):
			print(node.data,end=' ')
			node = node.next


dll = DoublyLinkedList()
dll.push(2)
dll.push(4)
dll.push(8)
dll.push(10)

print ("\nOriginal Linked List")
dll.printList(dll.head)

dll.reverse()
print ("\nReversed Linked List")
dll.printList(dll.head)

```

## Find pairs with a given sum in a DLL

```python
class Node:
	def __init__(self, x):
		self.data = x
		self.next = None
		self.prev = None


def pairSum(head, x):
	
	# Set two pointers, first to the beginning of DLL and second to the end of DLL.
	first = head
	second = head
	while (second.next != None):
		second = second.next

	# To track if we find a pair or not
	found = False

	# The loop terminates when they cross each other (second.next == first), or they become same (first == second)
	while (first != second and second.next != first):
			
		# Pair found
		if ((first.data + second.data) == x):
			found = True
			print("Pair found: ", first.data, second.data)
			# Move first in forward direction
			first = first.next
			# Move second in backward direction
			second = second.prev
		elif ((first.data + second.data) < x):
			first = first.next
		else:
			second = second.prev

	# If pair is not present
	if not found:
		print("No pair found")

def insert(head, data):
	temp = Node(data)
	if head:
		temp.next = head
		head.prev = temp
	head = temp
	return head


head = None
head = insert(head, 9)
head = insert(head, 8)
head = insert(head, 6)
head = insert(head, 5)
head = insert(head, 4)
head = insert(head, 2)
head = insert(head, 1)
x = 7
pairSum(head, x)
```

## Count triplets in a sorted DLL whose sum is equal to given value “X”

```python
class Node:
	def __init__(self, x):
		self.data = x
		self.next = None
		self.prev = None


def countPairs(first, second, value):
	count = 0

	# The loop terminates when either of two pointers become None, or they cross each other (second.next == first), or they become same (first == second)
	while (first != None and second != None and
		first != second and second.next != first):

		# Pair found
		if ((first.data + second.data) == value):
			
			# Increment count
			count += 1

			# Move first in forward direction
			first = first.next

			# Move second in backward direction
			second = second.prev

		# If sum is greater than 'value' move second in backward direction
		elif ((first.data + second.data) > value):
			second = second.prev

		# Else move first in forward direction
		else:
			first = first.next

	# Required count of pairs
	return count


def countTriplets(head, x):
	
	# If list is empty
	if head is None:
		return 0

	current, first, last = head, None, None
	count = 0

	# Get pointer to the last node of the doubly linked list
	last = head

	while (last.next != None):
		last = last.next

	# Traversing the doubly linked list
	while current != None:

		# For each current node
		first = current.next

		# count pairs with sum(x - current.data) in the range first to last and add it to the 'count' of triplets
		count, current = count + countPairs(
			first, last, x - current.data), current.next

	# Required count of triplets
	return count


def insert(head, data):
	temp = Node(data)
	if head != None:
		temp.next = head
		head.prev = temp
	head = temp
	return head


head = None
head = insert(head, 9)
head = insert(head, 8)
head = insert(head, 6)
head = insert(head, 5)
head = insert(head, 4)
head = insert(head, 2)
head = insert(head, 1)
x = 17
print("Count = ", countTriplets(head, x))

```

## Sort a “k”sorted Doubly Linked list

```python
class Node:
	def __init__(self, val):
		self.data = val
		self.prev = None
		self.next = None

# function to sort a k sorted doubly linked list Using Insertion Sort
# Time Complexity: O(n*k)
# Space Complexity: O(1)
def sortAKSortedDLL(head , k):
	if head is None or head.next is None:
		return head

	# perform on all the nodes in list
	i = head.next
	while (i != None):
		j = i

		# There will be atmost k swaps for each element in the list since each node is k steps away from its correct position
		while (j.prev != None and j.data < j.prev.data):

			# swap j and j.prev node
			temp = j.prev.prev
			temp2 = j.prev
			temp3 = j.next
			j.prev.next = temp3
			j.prev.prev = j
			j.prev = temp
			j.next = temp2
			if (temp != None):
				temp.next = j
			if (temp3 != None):
				temp3.prev = temp2

			# if j is now the new head then reset head
		if j.prev is None:
			head = j
		i = i.next

	return head

# Function to insert a node at the beginning of the Doubly Linked List
def push(new_data):
	global head
	new_node = Node(new_data)
	new_node.prev = None
	new_node.next = head
	if (head != None):
		head.prev = new_node
	head = new_node


def printList(node):
	while (node != None):
		print(node.data,end = " ")
		node = node.next


head = None
# Let us create a k sorted doubly linked list to test the functions Created doubly linked list will be 3<->6<->2<->12<->56<->8
push(8)
push(56)
push(12)
push(2)
push(6)
push(3)

k = 2

print("Original Doubly linked list:")
printList(head)
sortedDLL = sortAKSortedDLL(head, k)
print("")
print("Doubly Linked List after sorting:")
printList(sortedDLL)
```

## Rotate DoublyLinked list by N nodes

```python
class Node:
	def __init__(self, next = None, prev = None, data = None):
		self.next = next 
		self.prev = prev 
		self.data = data

def push(head, new_data):
	new_node = Node(data = new_data)
	new_node.next = head
	new_node.prev = None
	if head is not None:
		head.prev = new_node
	head = new_node
	return head

def printList(head):
	node = head
	print("Given linked list")
	while(node is not None):
		print(node.data, end = " ")
		last = node
		node = node.next
	
def rotate(start, N):
	if N == 0 :
		return

	# Let us understand the below code for example N = 2 and list = a <-> b <-> c <-> d <-> e.
	current = start

	# current will either point to Nth or None after this loop. Current will point to node 'b' in the above example
	count = 1
	while count < N and current != None :
		current = current.next
		count += 1

	# If current is None, N is greater than or equal to count of nodes in linked list. Don't change the list in this case
	if current is None:
		return

	# current points to Nth node. Store it in a variable. NthNode points to node 'b' in the above example
	NthNode = current

	# current will point to last node after this loop current will point to node 'e' in the above example
	while current.next != None :
		current = current.next

	# Change next of last node to previous head. Next of 'e' is now changed to node 'a'
	current.next = start

	# Change prev of Head node to current Prev of 'a' is now changed to node 'e'
	start.prev = current

	# Change head to (N+1)th node head is now changed to node 'c'
	start = NthNode.next

	# Change prev of New Head node to None Because Prev of Head Node in Doubly linked list is None
	start.prev = None

	# change next of Nth node to None next of 'b' is now None
	NthNode.next = None

	return start


head = None
head = push(head, 'e')
head = push(head, 'd')
head = push(head, 'c')
head = push(head, 'b')
head = push(head, 'a')
printList(head)
print("\n")
N = 2
head = rotate(head, N)
printList(head)
```

## Rotate a Doubly Linked list in group of Given Size

```python
class Node:
	def __init__(self):
		self.data = 0
		self.next = None
		self.next = None


def insertAtEnd(head, data):
	new_Node = Node()
	new_Node.data = data
	new_Node.next = None
	temp = head
	if head is None:
		new_Node.prev = None
		head = new_Node
		return head
	while (temp.next != None):
		temp = temp.next
	temp.next = new_Node
	new_Node.prev = temp
	return head


def printDLL(head):
	while (head != None):
		print(head.data, end=" ")
		head = head.next
	print()


# Function to Reverse a doubly linked list in groups of given size
def reverseByN(head, k):
	if head is None:
		return None

	head.prev = None
	temp=None
	curr = head
	newHead = None
	count = 0

	while (curr != None and count < k):
		newHead = curr
		temp = curr.prev
		curr.prev = curr.next
		curr.next = temp
		curr = curr.prev
		count += 1

	# Checking if the reversed LinkedList size is equal to K or not. If it is not equal to k that means we have reversed the last set of size K and we don't need to call the recursive function
	if (count >= k):
		rest = reverseByN(curr, k)
		head.next = rest
		if (rest != None):

			# it is required for prev link otherwise u wont be backtrack list due to broken links
			rest.prev = head
	return newHead


head = None
for i in range(1,11):
	head = insertAtEnd(head, i)
printDLL(head)
n = 4
head = reverseByN(head, n)
printDLL(head)
```

## Can we reverse a linked list in less than O(n) ?

```python
It is not possible to reverse a simple singly linked list in less than O(n). A simple singly linked list can only be reversed in O(n) time using recursive and iterative methods. 

A doubly linked list with head and tail pointers while only requiring swapping the head and tail pointers which require lesser operations than a singly linked list can also not be done in less than O(n) since we need to traverse till the end of the list anyway to find the tail node.
```

## Why Quicksort is preferred for. Arrays and Merge Sort for LinkedLists ?]

```python
Quick Sort in its general form is an in-place sort (i.e. it doesn’t require any extra storage) whereas merge sort requires O(N) extra storage, N denoting the array size which may be quite expensive. Allocating and de-allocating the extra space used for merge sort increases the running time of the algorithm.
Comparing average complexity we find that both type of sorts have O(NlogN) average complexity but the constants differ. For arrays, merge sort loses due to the use of extra O(N) storage space.
Most practical implementations of Quick Sort use randomized version. The randomized version has expected time complexity of O(nLogn). The worst case is possible in randomized version also, but worst case doesn’t occur for a particular pattern (like sorted array) and randomized Quick Sort works well in practice.
Quick Sort is also a cache friendly sorting algorithm as it has good locality of reference when used for arrays.
Quick Sort is also tail recursive, therefore tail call optimizations is done.

Why is Merge Sort preferred for Linked Lists?
In case of linked lists the case is different mainly due to difference in memory allocation of arrays and linked lists. Unlike arrays, linked list nodes may not be adjacent in memory.
Unlike array, in linked list, we can insert items in the middle in O(1) extra space and O(1) time if we are given reference/pointer to the previous node. Therefore merge operation of merge sort can be implemented without extra space for linked lists.
In arrays, we can do random access as elements are continuous in memory. Let us say we have an integer (4-byte) array A and let the address of A[0] be x then to access A[i], we can directly access the memory at (x + i*4). Unlike arrays, we can not do random access in linked list.
Quick Sort requires a lot of this kind of access. In linked list to access i’th index, we have to travel each and every node from the head to i’th node as we don’t have continuous block of memory. Therefore, the overhead increases for quick sort. Merge sort accesses data sequentially and the need of random access is low.
```

## Flatten a Linked List

```python
class Node():
	def __init__(self,data):
		self.data = data
		self.right = None
		self.down = None

class LinkedList():
	def __init__(self):
		self.head = None

	def push(self,head_ref,data):
		new_node = Node(data)
		new_node.down = head_ref
		head_ref = new_node
		return head_ref

	def printList(self):
		temp = self.head
		while(temp != None):
			print(temp.data,end=" ")
			temp = temp.down
		print()

	
	def merge(self, a, b):
		# if first linked list is empty then second is the answer
		if a is None:
			return b

		# if second linked list is empty then first is the result
		if b is None:
			return a

		# compare the data members of the two linked lists and put the larger one in the result
		result = None

		if (a.data < b.data):
			result = a
			result.down = self.merge(a.down,b)
		else:
			result = b
			result.down = self.merge(a,b.down)

		result.right = None
		return result

	def flatten(self, root):

		# Base Case
		if root is None or root.right is None:
			return root

		# recur for list on right
		root.right = self.flatten(root.right)

		# now merge
		root = self.merge(root, root.right)

		# return the root it will be in turn merged with its left
		return root




'''
Let us create the following linked list
			5 -> 10 -> 19 -> 28
			| |	 |	 |
			V V	 V	 V
			7 20 22 35
			|		 |	 |
			V		 V	 V
			8		 50 40
			|			 |
			V			 V
			30			 45
'''
L = LinkedList()
L.head = L.push(L.head, 30);
L.head = L.push(L.head, 8);
L.head = L.push(L.head, 7);
L.head = L.push(L.head, 5);

L.head.right = L.push(L.head.right, 20);
L.head.right = L.push(L.head.right, 10);

L.head.right.right = L.push(L.head.right.right, 50);
L.head.right.right = L.push(L.head.right.right, 22);
L.head.right.right = L.push(L.head.right.right, 19);

L.head.right.right.right = L.push(L.head.right.right.right, 45);
L.head.right.right.right = L.push(L.head.right.right.right, 40);
L.head.right.right.right = L.push(L.head.right.right.right, 35);
L.head.right.right.right = L.push(L.head.right.right.right, 20);

L.head = L.flatten(L.head);
L.printList()
```

## Sort a LL of 0's, 1's and 2's

```python
import math

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


def sortList(head):
	if head is None or head.next is None:
		return head

	# Create three dummy nodes to point to beginning of three linked lists. These dummy nodes are created to avoid many None checks.
	zeroD = Node(0)
	oneD = Node(0)
	twoD = Node(0)

	# Initialize current pointers for three lists and whole list.
	zero = zeroD
	one = oneD
	two = twoD

	# Traverse list
	curr = head
	while curr:
		if (curr.data == 0):
			zero.next = curr
			zero = zero.next
		elif curr.data == 1:
			one.next = curr
			one = one.next
		else:
			two.next = curr
			two = two.next
		curr = curr.next
	# Attach three lists
	zero.next = oneD.next or twoD.next
	one.next = twoD.next
	two.next = None

	# Updated head
	head = zeroD.next

	# Delete dummy nodes
	return head

# function to create and return a node
def newNode(data):
	newNode = Node(data)
	newNode.data = data
	newNode.next = None
	return newNode

# Function to print linked list
def printList(node):
	while (node != None):
		print(node.data, end = " ")
		node = node.next
	

head = newNode(1)
head.next = newNode(2)
head.next.next = newNode(0)
head.next.next.next = newNode(1)
print("Linked List Before Sorting")
printList(head)
head = sortList(head)
print("\nLinked List After Sorting")
printList(head)
```

## Clone a linked list with next and random pointer

```python
class Node:
	def __init__(self, data):
		self.data = data	
		self.next = None
		self.random = None


class MyDictionary(dict):
	def __init__(self):
		super().__init__()
		self = {}

	def add(self, key, value):
		self[key] = value


class LinkedList:
	def __init__(self, node):
		self.head = node

	def __repr__(self):
		temp = self.head
		while temp is not None:
			random = temp.random
			random_data = (random.data if
						random is not None else -1)
							
			data = temp.data
			print(
				f"Data-{data}, Random data: {random_data}")
			temp = temp.next
			
		return "\n"

	def push(self, data):
		node = Node(data)
		node.next = self.head
		self.head = node


	def clone(self):
		
		# Initialize two references, one with original list's head.
		original = self.head
		clone = None

		# Initialize two references, one with original list's head.
		mp = MyDictionary()

		# Traverse the original list and make a copy of that in the clone linked list
		while original is not None:
			clone = Node(original.data)
			mp.add(original, clone)
			original = original.next

		# Adjusting the original list reference again.
		original = self.head

		# Traversal of original list again to adjust the next and random references of clone list using hash map.
		while original is not None:
			clone = mp.get(original)
			clone.next = mp.get(original.next)
			clone.random = mp.get(original.random)
			original = original.next
			
		# Return the head reference of the clone list.
		return LinkedList(self.head)


l = LinkedList(Node(5))
l.push(4)
l.push(3)
l.push(2)
l.push(1)

l.head.random = l.head.next.next
l.head.next.random = l.head.next.next.next
l.head.next.next.random = l.head.next.next.next.next
l.head.next.next.next.random = (l.head.next.next.next. next.next)
l.head.next.next.next.next.random = l.head.next

clone = l.clone()
print("Original linked list")
print(l)
print("Cloned linked list")
print(clone)
```

## Merge K sorted Linked list

```python
class Node:
	def __init__(self):
		self.data = 0
		self.next = None


def printList(node):
	while (node != None):
		print(node.data, end = ' ')
		node = node.next

def SortedMerge(a, b):
	result = None
	# Base cases
	if a is None:
		return b
	elif b is None:
		return a 

	# Pick either a or b, and recur
	if (a.data <= b.data):
		result = a
		result.next = SortedMerge(a.next, b)
	else:
		result = b
		result.next = SortedMerge(a, b.next)
	return result


def mergeKLists(arr, last):
	# Repeat until only one list is left
	while (last != 0):
		i = 0
		j = last

		# (i, j) forms a pair
		while (i < j):
			
			# Merge List i with List j and store merged list in List i
			arr[i] = SortedMerge(arr[i], arr[j])

			# Consider next pair
			i += 1
			j -= 1
			
			# If all pairs are merged, update last
			if (i >= j):
				last = j
	return arr[0]


def newNode(data):
	temp = Node()
	temp.data = data
	temp.next = None
	return temp


k = 3  # Number of linked lists
n = 4  # Number of elements in each list
arr = [0 for _ in range(k)]
arr[0] = newNode(1)
arr[0].next = newNode(3)
arr[0].next.next = newNode(5)
arr[0].next.next.next = newNode(7)
arr[1] = newNode(2)
arr[1].next = newNode(4)
arr[1].next.next = newNode(6)
arr[1].next.next.next = newNode(8)
arr[2] = newNode(0)
arr[2].next = newNode(9)
arr[2].next.next = newNode(10)
arr[2].next.next.next = newNode(11)
head = mergeKLists(arr, k - 1)
printList(head)
```

## Multiply 2 no. represented by LL

```python
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node
			
	def printList(self):
		ptr = self.head
		while (ptr != None):
			print(ptr.data, end = '')
			if ptr.next != None:
				print('->', end = '')
			ptr = ptr.next	
		print()
	
# Multiply contents of two Linked Lists
def multiplyTwoLists(first, second):
	num1 = 0
	num2 = 0
	first_ptr = first.head
	second_ptr = second.head
	while first_ptr != None or second_ptr != None:
		if first_ptr != None:
			num1 = (num1 * 10) + first_ptr.data
			first_ptr = first_ptr.next
		if second_ptr != None:
			num2 = (num2 * 10) + second_ptr.data
			second_ptr = second_ptr.next
	return num1 * num2
	

first = LinkedList()
second = LinkedList()

# Create first Linked List 9->4->6
first.push(6)
first.push(4)
first.push(9)
print("First list is: ", end = '')
first.printList()

# Create second Linked List 8->4
second.push(4)
second.push(8)
print("Second List is: ", end = '')
second.printList()

result = multiplyTwoLists(first, second)
print("Result is: ", result)
```

## Delete nodes which have a greater value on right side

```python
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:

	def __init__(self):
		self.head = None

	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	def printList(self):
		temp = self.head
		while(temp):
			print (temp.data,end=" ")
			temp = temp.next

	def del_gr_right(self):
		i = self.head
		
		while i:
			value = i.data
			found = False
			j = i.next
			
			while j:
				if j.data > value:
					found = True
					break
				j = j.next
			
			if found:
				temp = i.next
				i.data = i.next.data
				i.next = i.next.next
				temp = None
			else:
				i = i.next


llist = LinkedList()
llist.push(11)
llist.push(18)
llist.push(20)
llist.push(14)
llist.push(15)

print ("Given Linked List is:")
llist.printList()
print()

llist.del_gr_right()

print ("\nLinked list after deletion is")
llist.printList()
```

## Segregate even and odd nodes in a Linked List

```python

class Node:

	def __init__(self, data):
		self.data = data 
		self.next =None

# Function to segregate even and odd nodes.
def segregateEvenOdd():
	global head
	evenStart = None 	# Starting node of list having even values.
	evenEnd = None 	# Ending node of even values list.	
	oddStart = None 	# Starting node of odd values list.	
	oddEnd = None 	# Ending node of odd values list.		
	currNode = head # Node to traverse the list.

	while (currNode != None):
		val = currNode.data

		# If current value is even, add it to even values list.
		if (val % 2 == 0):
			if evenStart is None:
				evenStart = currNode
				evenEnd = evenStart
			else:
				evenEnd . next = currNode
				evenEnd = evenEnd . next

		elif oddStart is None:
			oddStart = currNode
			oddEnd = oddStart
		else:
			oddEnd . next = currNode
			oddEnd = oddEnd . next

		# Move head pointer one step in forward direction
		currNode = currNode . next

	# If either odd list or even list is empty, no change is required as all elements are either even or odd.
	if oddStart is None or evenStart is None:
		return

	# Add odd list after even list.	
	evenEnd.next = oddStart
	oddEnd.next = None

	# Modify head pointer to starting of even list.
	head = evenStart


def push(new_data):
	global head
	new_node = Node(new_data)
	new_node.next = head
	head = new_node

def printList():
	global head
	node = head
	while (node != None):
		print(node.data, end = " ")
		node = node.next
	print()
	

''' Let us create a sample linked list as following
0.1.4.6.9.10.11 '''

head = None 
push(11)
push(10)
push(9)
push(6)
push(4)
push(1)
push(0)

print("Original Linked list")
printList()
segregateEvenOdd()
print("Modified Linked list")
printList()
```

## Program for n’th node from the end of a Linked List

```python
class Node:
	def __init__(self, new_data):
		self.data = new_data
		self.next = None
	
class LinkedList:
	def __init__(self):
		self.head = None

	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	def printNthFromLast(self, n):
		temp = self.head # used temp variable
		length = 0
		while temp is not None:
			temp = temp.next
			length += 1

		# print count
		if n > length: 
			# if entered location is greater than length of linked list
			print('Location is greater than the length of LinkedList')
			return
		temp = self.head

		for _ in range(length - n):
			temp = temp.next
		print(temp.data)


llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(35)
llist.printNthFromLast(4)
```

## Find the first non-repeating character from a stream of characters

```python
from queue import Queue

def firstnonrepeating(Str):
	global MAX_CHAR
	q = Queue()
	charCount = [0] * MAX_CHAR
	
	# traverse whole Stream
	for i in range(len(Str)):

		# push each character in queue
		q.put(Str[i])

		# increment the frequency count
		charCount[ord(Str[i]) -
				ord('a')] += 1

		# check for the non repeating character
		while (not q.empty()):
			if (charCount[ord(q.queue[0]) - ord('a')] > 1):
				q.get()
			else:
				print(q.queue[0], end = " ")
				break

		if (q.empty()):
			print(-1, end = " ")
	print()

MAX_CHAR = 26
Str = "aabc"
firstnonrepeating(Str)
```