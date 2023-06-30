---
title: "DSA in Python - Stacks and Queues"
date: 2022-07-09T13:14:34+05:30
draft: false
cover: 
    image: blog/dsa/Stack-Queue.webp
    alt: Stacks and Queues
    caption: Learn Stack and Queue Algorithms in Python
tags: ["python"] 
---

## Free Preview - 5 Stack and Queue Problems

### Implement Stack from Scratch

```python
class Stack:
    def __init__(self, size):
        self.arr = [None] * size
        self.capacity = size
        self.top = -1

    def push(self, val):
        if self.isFull():
            print('Stack Overflow!! Calling exit()…')
            exit(-1)
 
        print(f'Inserting {val} into the stack…')
        self.top = self.top + 1
        self.arr[self.top] = val

    def pop(self):
        if self.isEmpty():
            print('Stack Underflow!! Calling exit()…')
            exit(-1)
 
        print(f'Removing {self.peek()} from the stack')
 
        # decrease stack size by 1 and (optionally) return the popped element
        top = self.arr[self.top]
        self.top = self.top - 1
        return top

    def peek(self):
        if self.isEmpty():
            exit(-1)
        return self.arr[self.top]

    def size(self):
        return self.top + 1

    def isEmpty(self):
        return self.size() == 0

    def isFull(self):
        return self.size() == self.capacity
 

stack = Stack(3)
stack.push(1)       # Inserting 1 in the stack
stack.push(2)       # Inserting 2 in the stack
stack.pop()         # removing the top element (2)
stack.pop()         # removing the top element (1)
stack.push(3)       # Inserting 3 in the stack

print('Top element is', stack.peek())
print('The stack size is', stack.size())

stack.pop()         # removing the top element (3)
if stack.isEmpty():
    print('The stack is empty')
else:
    print('The stack is not empty')
```

### Implement Queue from Scratch

```python
class Queue:
    def __init__(self, size=1000):
        self.q = [None] * size      # list to store queue elements
        self.capacity = size        # maximum capacity of the queue
        self.front = 0              # front points to the front element in the queue
        self.rear = -1              # rear points to the last element in the queue
        self.count = 0              # current size of the queue
 
    def dequeue(self):
        # check for queue underflow
        if self.isEmpty():
            print('Queue Underflow!! Terminating process.')
            exit(-1)
        x = self.q[self.front]
        print('Removing element…', x)
        self.front = (self.front + 1) % self.capacity
        self.count = self.count - 1
        return x
    def enqueue(self, value):
        # check for queue overflow
        if self.isFull():
            print('Overflow!! Terminating process.')
            exit(-1)
        print('Inserting element…', value)
        self.rear = (self.rear + 1) % self.capacity
        self.q[self.rear] = value
        self.count = self.count + 1

    def peek(self):
        if self.isEmpty():
            print('Queue UnderFlow!! Terminating process.')
            exit(-1)
        return self.q[self.front]
 
    def size(self):
        return self.count

    def isEmpty(self):
        return self.size() == 0
 
    def isFull(self):
        return self.size() == self.capacity
 
 
# create a queue of capacity 5
q = Queue(5)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print('The queue size is', q.size())
print('The front element is', q.peek())
q.dequeue()
print('The front element is', q.peek())
q.dequeue()
q.dequeue()
if q.isEmpty():
    print('The queue is empty')
else:
    print('The queue is not empty')
```

### Implement 2 stack in an array

```python
class Stack:
    # Constructor
    def __init__(self, n):
        self.capacity = n
        self.A = [None] * n
        self.top1 = -1
        self.top2 = n
 
    # Function to insert a given element into the first stack
    def push_first(self, key):
        # check if the list is full
        if self.top1 + 1 == self.top2:
            print('Stack Overflow')
            exit(-1)
        self.top1 = self.top1 + 1
        self.A[self.top1] = key
 
    # Function to insert a given element into the second stack
    def push_second(self, key):
        # check if the list is full
        if self.top1 + 1 == self.top2:
            print('Stack Overflow')
            exit(-1)
        self.top2 = self.top2 - 1
        self.A[self.top2] = key
 
    # Function to pop an element from the first stack
    def pop_first(self):
        # if no elements are left in the list
        if self.top1 < 0:
            print('Stack Underflow')
            exit(-1)
        top = self.A[self.top1]
        self.top1 = self.top1 - 1
        return top
 
    # Function to pop an element from the second stack
    def pop_second(self):
        # if no elements are left in the list
        if self.top2 >= self.capacity:
            print('Stack Underflow')
            exit(-1)
        top = self.A[self.top2]
        self.top2 = self.top2 + 1
        return top
 

first = [1, 2, 3, 4, 5]
second = [6, 7, 8, 9, 10]
stack = Stack(len(first) + len(second))
[stack.push_first(i) for i in first]
[stack.push_second(j) for j in second]
print('Popping element from the first stack:', stack.pop_first())
print('Popping element from the second stack:', stack.pop_second())
```

### find the middle element of a stack

```python
# Recursive function to find the peak element in a list
def findPeak(nums, left=None, right=None):
 
    # Initialize left and right
    if left is None and right is None:
        left, right = 0, len(nums) - 1
 
    # find the middle element. To avoid overflow, use mid = left + (right - left) / 2
    mid = (left + right) // 2
 
    # check if the middle element is greater than its neighbors
    if ((mid == 0 or nums[mid - 1] <= nums[mid]) and (mid == len(nums) - 1 or nums[mid + 1] <= nums[mid])):
        return mid
  
def findMiddleElement(nums):
    if not nums:
        exit(-1)
    index = findPeak(nums)
    return nums[index]
 
nums = [8, 9, 10, 11, 2, 5, 6]
print('The middle element is', findPeakElement(nums))
 
```

### Implement "N" stacks in an Array

```python
class KStacks:	
	def __init__(self, k, n):
		self.k = k # Number of stacks.
		self.n = n # Total size of array holding  all the 'k' stacks.

		# Array which holds 'k' stacks.
		self.arr = [0] * self.n

		# All stacks are empty to begin with (-1 denotes stack is empty).
		self.top = [-1] * self.k

		# Top of the free stack.
		self.free = 0

		# Points to the next element in either 1. One of the 'k' stacks or, 2. The 'free' stack.
		self.next = [i + 1 for i in range(self.n)]
		self.next[self.n - 1] = -1

	# Check whether given stack is empty.
	def isEmpty(self, sn):
		return self.top[sn] == -1

	# Check whether there is space left for pushing new elements or not.
	def isFull(self):
		return self.free == -1

	# Push 'item' onto given stack number 'sn'.
	def push(self, item, sn):
		if self.isFull():
			print("Stack Overflow")
			return

		# Get the first free position to insert at.
		insert_at = self.free

		# Adjust the free position.
		self.free = self.next[self.free]

		# Insert the item at the free position we obtained above.
		self.arr[insert_at] = item

		# Adjust next to point to the old top of stack element.
		self.next[insert_at] = self.top[sn]

		# Set the new top of the stack.
		self.top[sn] = insert_at

	# Pop item from given stack number 'sn'.
	def pop(self, sn):
		if self.isEmpty(sn):
			return None

		# Get the item at the top of the stack.
		top_of_stack = self.top[sn]

		# Set new top of stack.
		self.top[sn] = self.next[self.top[sn]]

		# Push the old top_of_stack to  the 'free' stack.
		self.next[top_of_stack] = self.free
		self.free = top_of_stack
		return self.arr[top_of_stack]

	def printstack(self, sn):
		top_index = self.top[sn]
		while (top_index != -1):
			print(self.arr[top_index])
			top_index = self.next[top_index]


# Create 3 stacks using an array of size 10.
kstacks = KStacks(3, 10)
# Push some items onto stack number 2.
kstacks.push(15, 2)
kstacks.push(45, 2)
# Push some items onto stack number 1.
kstacks.push(17, 1)
kstacks.push(49, 1)
kstacks.push(39, 1)
# Push some items onto stack number 0.
kstacks.push(11, 0)
kstacks.push(9, 0)
kstacks.push(7, 0)
print(f"Popped element from stack 2 is {str(kstacks.pop(2))}")
print(f"Popped element from stack 1 is {str(kstacks.pop(1))}")
print(f"Popped element from stack 0 is {str(kstacks.pop(0))}")
kstacks.printstack(0)
```

## Buy the Interview Guide

{{< gumroad "https://highnessatharva.gumroad.com/l/dsa-python-stack-queue" "/blog/gumroad-marketing.webp" >}}