---
title: "DSA in Python - Stacks and Queues"
date: 2022-07-09T13:14:34+05:30
draft: false
cover: 
    image: blog/dsa/stack-queue.jpg
    alt: Stacks and Queues
    caption: Learn Stack and Queue Algorithms in Python
tags: ["DSA-Python"] 

---
- [Implement Stack from Scratch](#implement-stack-from-scratch)
- [Implement Queue from Scratch](#implement-queue-from-scratch)
- [Implement 2 stack in an array](#implement-2-stack-in-an-array)
- [find the middle element of a stack](#find-the-middle-element-of-a-stack)
- [Implement "N" stacks in an Array](#implement-n-stacks-in-an-array)
- [Check the expression has valid or Balanced parenthesis or not.](#check-the-expression-has-valid-or-balanced-parenthesis-or-not)
- [Reverse a String using Stack](#reverse-a-string-using-stack)
- [Design a Stack that supports getMin() in O(1) time and O(1) extra space.](#design-a-stack-that-supports-getmin-in-o1-time-and-o1-extra-space)
- [Find the next Greater element](#find-the-next-greater-element)
- [The celebrity Problem](#the-celebrity-problem)
- [Evaluation of Postfix expression](#evaluation-of-postfix-expression)
- [Reverse a stack using recursion](#reverse-a-stack-using-recursion)
- [Sort a Stack using recursion](#sort-a-stack-using-recursion)
- [Merge Overlapping Intervals](#merge-overlapping-intervals)
- [Largest rectangular Area in Histogram](#largest-rectangular-area-in-histogram)
- [Length of the Longest Valid Substring](#length-of-the-longest-valid-substring)
- [Expression contains redundant bracket or not](#expression-contains-redundant-bracket-or-not)
- [Implement Stack using Queue](#implement-stack-using-queue)
- [Implement Stack using Deque](#implement-stack-using-deque)
- [Stack Permutations (Check if an array is stack permutation of other)](#stack-permutations-check-if-an-array-is-stack-permutation-of-other)
- [Implement Queue using Stack](#implement-queue-using-stack)
- [Implement "n" queue in an array](#implement-n-queue-in-an-array)
- [Implement a Circular queue](#implement-a-circular-queue)
- [LRU Cache Implementation](#lru-cache-implementation)
- [Reverse a Queue using recursion](#reverse-a-queue-using-recursion)
- [Reverse the first “K” elements of a queue](#reverse-the-first-k-elements-of-a-queue)
- [Interleave the first half of the queue with second half](#interleave-the-first-half-of-the-queue-with-second-half)
- [Find the first circular tour that visits all Petrol Pumps](#find-the-first-circular-tour-that-visits-all-petrol-pumps)
- [Minimum time required to rot all oranges](#minimum-time-required-to-rot-all-oranges)
- [Distance of nearest cell having 1 in a binary matrix](#distance-of-nearest-cell-having-1-in-a-binary-matrix)
- [First negative integer in every window of size “k”](#first-negative-integer-in-every-window-of-size-k)
- [Check if all levels of two trees are anagrams or not.](#check-if-all-levels-of-two-trees-are-anagrams-or-not)
- [Sum of minimum and maximum elements of all subarrays of size “k”.](#sum-of-minimum-and-maximum-elements-of-all-subarrays-of-size-k)
- [Minimum sum of squares of character counts in a given string after removing “k” characters.](#minimum-sum-of-squares-of-character-counts-in-a-given-string-after-removing-k-characters)
- [Next Smaller Element](#next-smaller-element)

## Implement Stack from Scratch

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

## Implement Queue from Scratch

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

## Implement 2 stack in an array

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

## find the middle element of a stack

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

## Implement "N" stacks in an Array

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

## Check the expression has valid or Balanced parenthesis or not.

```python
from collections import deque
 
def isBalanced(exp):
    if not exp or len(exp) & 1:
        return False
 
    # take an empty stack of characters
    stack = deque()
 
    # traverse the input expression
    for ch in exp:
 
        # if the current character in the expression is an opening brace, push the corresponding closing brace into the stack.
        if ch == '(':
            stack.append(')')
        elif ch == '{':
            stack.append('}')
        elif ch == '[':
            stack.append(']')
 
        # return false if the popped character is not the same as the current character
        elif not stack or stack.pop() != ch:
            return False
 
    # the expression is only balanced if the stack is empty at this point
    return not stack
 
exp = '{()}[{}]'
if isBalanced(exp):
    print('The expression is balanced')
else:
    print('The expression is not balanced')
```

## Reverse a String using Stack

```python
from collections import deque
 
def reverse(s):
    stack = deque(s)
    return ''.join(stack.pop() for _ in range(len(s)))
 
s = 'Reverse me'
s = reverse(s)
print(s)
 
```

## Design a Stack that supports getMin() in O(1) time and O(1) extra space.

```python
class stack:
  def __init__(self):
    self.array = []
    self.top = -1
    self.max = 100  
  
  def isEmpty(self):
    return self.top == -1  

  def isFull(self):  
    return self.top == self.max - 1   
  
  def push(self, data):
    if self.isFull():
      print('Stack OverFlow')
      return
    else:
      self.top += 1
      self.array.append(data)     
  
  def pop(self):
    if self.isEmpty():
      print('Stack UnderFlow')
      return
    else: 
      self.top -= 1
      return self.array.pop()
  
# A class that supports all the stack   operations and one additional  operation getMin() that returns the  minimum element from stack at  any time.  This class inherits from the stack class and uses an  auxiliary stack that holds  minimum elements  
class SpecialStack(stack):
  def __init__(self):
    super().__init__()
    self.Min = stack()  

  def push(self, x):
    if self.isEmpty():
      super().push(x)
      self.Min.push(x)
    else:
      super().push(x)
      y = self.Min.pop()
      self.Min.push(y)
      if x <= y:
        self.Min.push(x)
      else:
        self.Min.push(y)  
  
  
  def pop(self):
    x = super().pop()
    self.Min.pop()
    return x  
  
  def getmin(self):
    x = self.Min.pop()
    self.Min.push(x)
    return x
  
s = SpecialStack()
s.push(10)
s.push(20)
s.push(30)
print(s.getmin())
s.push(5)
print(s.getmin())
```

## Find the next Greater element

```python
from collections import deque

def findNextGreaterElements(arr):
    if not arr:
        return
    result = [-1] * len(arr)
    s = deque()
    for i in range(len(arr)):
        # loop till we have a greater element on top or stack becomes empty. Keep popping elements from the stack smaller than the current element, and set their next greater element to the current element
        while s and arr[s[-1]] < arr[i]:
            result[s[-1]] = arr[i]
            s.pop()
 
        # push current "index" into the stack
        s.append(i)
    return result
 
 
arr = [2, 7, 3, 5, 4, 6, 8]
print(findNextGreaterElements(arr))
```

## The celebrity Problem

```python
"""
In a party of N people, only one person is known to everyone. Such a person may be present in the party, if yes, (s)he doesn’t know anyone in the party. We can only ask questions like “does A know B? “. Find the stranger (celebrity) in the minimum number of questions.
We can describe the problem input as an array of numbers/characters representing persons in the party. We also have a hypothetical function HaveAcquaintance(A, B) which returns true if A knows B, false otherwise. How can we solve the problem. 

Examples:  

Input:
MATRIX = { {0, 0, 1, 0},
           {0, 0, 1, 0},
           {0, 0, 0, 0},
           {0, 0, 1, 0} }
Output:id = 2
Explanation: The person with ID 2 does not 
know anyone but everyone knows him

Input:
MATRIX = { {0, 0, 1, 0},
           {0, 0, 1, 0},
           {0, 1, 0, 0},
           {0, 0, 1, 0} }
Output: No celebrity
Explanation: There is no celebrity.
"""


# Max # of persons in the party
N = 8

# Person with 2 is celebrity
MATRIX = [ [ 0, 0, 1, 0 ],
		[ 0, 0, 1, 0 ],
		[ 0, 0, 0, 0 ],
		[ 0, 0, 1, 0 ] ]

def knows(a, b):
	return MATRIX[a][b]


def findCelebrity(n):
	# Handle trivial case of size = 2
	s = list(range(n))

	# Find a potential celebrity
	while (len(s) > 1):

		# Pop out the first two elements from stack
		A = s.pop()
		B = s.pop()

		# if A knows B, we find that B might be the celebrity and vice versa
		if (knows(A, B)):
			s.append(B)
		else:
			s.append(A)

	# If there are only two people and there is no potential candidate
	if not s:
		return -1

	# Potential candidate?
	C = s.pop();

	# Last candidate was not examined, it leads one excess comparison (optimize)
	if (knows(C, B)):
		C = B

	if (knows(C, A)):
		C = A

	# Check if C is actually a celebrity or not
	for i in range(n):

		# If any person doesn't know 'a' or 'a' doesn't know any person, return -1
		if ((i != C) and (knows(C, i) or not(knows(i, C)))):
			return -1
	return C

	
n = 4
id_ = findCelebrity(n)

if id_ == -1:
	print("No celebrity")
else:
	print("Celebrity ID ", id_)
```

## Evaluation of Postfix expression

```python
from collections import deque
 def evalPostfix(exp):
    if not exp:
        exit(-1)
    stack = deque()
 
    for ch in exp:
 
        # if the current is an operand, push it into the stack
        if ch.isdigit():
            stack.append(int(ch))
 
        # if the current is an operator
        else:
            # remove the top two elements from the stack
            x = stack.pop()
            y = stack.pop()
 
            # evaluate the expression 'x op y', and push the result back to the stack
            if ch == '+':
                stack.append(y + x)
            elif ch == '-':
                stack.append(y - x)
            elif ch == '*':
                stack.append(y * x)
            elif ch == '/':
                stack.append(y // x)
 
    # At this point, the stack is left with only one element, i.e., expression result
    return stack.pop()
  
exp = '138*+'
print(evalPostfix(exp))
```

## Reverse a stack using recursion

```python

from collections import deque
def insertAtBottom(s, item):
    # base case: if the stack is empty, insert the given item at the bottom
    if not s:
        s.append(item)
        return
 
    # Pop all items from the stack and hold them in the call stack
    top = s.pop()
    insertAtBottom(s, item)
 
    # After the recursion unfolds, push each item in the call stack  at the top of the stack
    s.append(top)
 

def reverseStack(s):
    if not s:
        return
    item = s.pop()
    reverseStack(s)
    insertAtBottom(s, item)

s = deque(range(1, 6))
print('Original stack is', s)
reverseStack(s)
print('Reversed stack is', s)
```

## Sort a Stack using recursion

```python
from collections import deque
 
def sortedInsert(stack, key):
 
    # base case: if the stack is empty or the key is greater than all elements in the stack
    if not stack or key > stack[-1]:
        stack.append(key)
        return
 
    ''' We reach here when the key is smaller than the top element '''
    top = stack.pop()
    sortedInsert(stack, key)
    stack.append(top)
 
def sortStack(stack):
    if not stack:
        return
    top = stack.pop()
    sortStack(stack)
    sortedInsert(stack, top)
 
A = [5, -2, 9, -7, 3] 
stack = deque(A)
print('Stack before sorting:', list(stack))
sortStack(stack)
print('Stack after sorting:', list(stack))
```

## Merge Overlapping Intervals

```python
"""
Consider an event where a log register is maintained containing the guest’s arrival and departure times. Given an array of arrival and departure times from entries in the log register, find the point when there were maximum guests present in the event.

Note that if an arrival and departure event coincides, the arrival time is preferred over the departure time.

 
For example,

Input:
 
arrival = { 1, 2, 4, 7, 8, 12 }
departure = { 2, 7, 8, 12, 10, 15 }
 
Output: Maximum number of guests is 3, present at time 7
"""

def findMaxGuests(arrival, departure):
 
    # Find the time when the last guest leaves the event
    t = max(departure)
 
    # create a count array initialized by 0
    count = [0] * (t + 2)
 
    for i in range(len(arrival)):
        count[arrival[i]] += 1
        count[departure[i] + 1] -= 1
 
    # keep track of the time when there are maximum guests
    max_event_tm = count[0]
 
    # perform a prefix sum computation to determine the guest count at each point
    for i in range(1, t + 1):
        count[i] += count[i - 1]
        if count[max_event_tm] < count[i]:
            max_event_tm = i
 
    print("Event Time:", max_event_tm)
    print("The maximum number of guests is", count[max_event_tm])

 
arrival = [1, 2, 4, 7, 8, 12]
departure = [2, 7, 8, 12, 10, 15]
findMaxGuests(arrival, departure)
```

## Largest rectangular Area in Histogram

```python
"""
ind the largest rectangular area possible in a given histogram where the largest rectangle can be made of a number of contiguous bars. For simplicity, assume that all bars have same width and the width is 1 unit. 
For example, consider the following histogram with 7 bars of heights {6, 2, 5, 4, 5, 1, 6}. The largest possible rectangle possible is 12 (see the below figure, the max area rectangle is highlighted in red)
"""

def getMaxArea(arr):
  s = [-1]
  n = len(arr)
  area = 0
  left_smaller = [-1]*n
  right_smaller = [n]*n
  for i in range(n):
    while s and (s[-1] != -1) and (arr[s[-1]] > arr[i]):
        right_smaller[s[-1]] = i
        s.pop()
    if((i > 0) and (arr[i] == arr[i-1])):
        left_smaller[i] = left_smaller[i-1]
    else:
        left_smaller[i] = s[-1]
    s.append(i)
  for j in range(n):
    area = max(area, arr[j]*(right_smaller[j]-left_smaller[j]-1))
  return area

hist = [6, 2, 5, 4, 5, 1, 6]
print("maxArea = ", getMaxArea(hist))
```

## Length of the Longest Valid Substring

```python

from collections import deque
def findMaxLen(s):
    if not s:
        return 0
 
    # create a stack of integers for storing an index of parenthesis in the string
    stack = deque()
 
    # initialize the stack by -1
    stack.append(-1)
 
    # stores the length of the longest balanced parenthesis
    length = 0
 
    # iterate over the characters of the string
    for i, e in enumerate(s):
 
        # if the current character is an opening parenthesis, push its index in the stack
        if e == '(':
            stack.append(i)
 
        # if the current character is a closing parenthesis
        else:
            # pop the top index from the stack
            stack.pop()
 
            # if the stack becomes empty, push the current index into the stack
            if not stack:
                stack.append(i)
                continue
 
            # get the length of the longest balanced parenthesis ending at the current character
            curr_len = i - stack[-1]
 
            # update the length of the longest balanced parenthesis
            if length < curr_len:
                length = curr_len
    return length

print(findMaxLen('((()()'))         # prints 4
print(findMaxLen('(((()'))          # prints 2
print(findMaxLen('(((('))           # prints 0
print(findMaxLen('()()'))           # prints 4
print(findMaxLen('(()())(()'))      # prints 6
```

## Expression contains redundant bracket or not

```python

from collections import deque 
def hasDuplicateParenthesis(exp):
    if not exp or len(exp) <= 3:
        return False
    stack = deque()
 
    # traverse the input expression
    for c in exp:
        # if the current char in the expression is not a closing parenthesis
        if c != ')':
            stack.append(c)
        # if the current char in the expression is a closing parenthesis
        else:
            # if the stack's top element is an opening parenthesis, the subexpression of the form ((exp)) is found
            if stack[-1] == '(':
                return True
 
            # pop till '(' is found for current ')'
            while stack[-1] != '(':
                stack.pop()
 
            # pop '('
            stack.pop()
 
    # if we reach here, then the expression does not have any duplicate parenthesis
    return False
 

exp = '((x+y))' # assumes valid expression
if hasDuplicateParenthesis(exp):
    print('The expression has duplicate parenthesis.')
else:
    print('The expression does not have duplicate parenthesis')
```

## Implement Stack using Queue

```python
from collections import deque
 
class Stack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
 
    # Insert an item into the stack
    def add(self, data):
        # Move all elements from the first queue to the second queue
        while len(self.q1):
            self.q2.append(self.q1.pop())
 
        # Push the given item into the first queue
        self.q1.append(data)
 
        # Move all elements back to the first queue from the second queue
        while len(self.q2):
            self.q1.append(self.q2.pop())

    def pop(self):
        # if the first queue is empty
        if not self.q1:
            print('Underflow!!')
            exit(0)
        front = self.q1.popleft()
        return front
 
 
keys = [1, 2, 3, 4, 5]
s = Stack()
for key in keys:
    s.add(key)
while s:
    print(s.pop())
print(s.pop())
```

## Implement Stack using Deque

```python

from collections import deque

class Stack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
 
    # Insert an item into the stack
    def add(self, data):
        self.q1.append(data)
 
    # Remove the top item from the stack
    def poll(self):
        # if the first queue is empty
        if not self.q1:
            print('Stack Underflow!!')
            exit(0)
 
        # Move all elements except last from the first queue to the second queue
        front = None
        while self.q1:
            if len(self.q1) == 1:
                front = self.q1.popleft()
            else:
                self.q2.append(self.q1.popleft())
 
        # Return the last element after moving all elements back to the first queue.
        while self.q2:
            self.q1.append(self.q2.popleft())
        return front
 
  
keys = [1, 2, 3, 4, 5]
s = Stack()
for key in keys:
    s.add(key)
while s:
    print(s.poll())
```

## Stack Permutations (Check if an array is stack permutation of other)

```python
"""
Given two arrays, both of unique elements. One represents the input queue and the other represents the output queue. Our task is to check if the given output is possible through stack permutation.

Examples: 

Input : First array: 1, 2, 3  
        Second array: 2, 1, 3
Output : Yes
Procedure:
push 1 from input to stack
push 2 from input to stack
pop 2 from stack to output
pop 1 from stack to output
push 3 from input to stack
pop 3 from stack to output


Input : First array: 1, 2, 3  
        Second array: 3, 1, 2
Output : Not Possible  
"""

def checkStackPermutation(ip, op, n):
	# we will be appending elements from input array to stack uptill top of our stack matches with first element of output array
	s = []
	# will maintain a variable j to iterate on output array
	j = 0

	# will iterate one by one in input array
	for i in range(n):

		# appended an element from input array to stack
		s.append(ip[i])
		# if our stack isn't empty and top matches with output array then we will keep popping out from stack uptill top matches with output array
		while s and s[-1] == op[j]:
			s.pop()

			# increasing j so next time we can compare next element in output array
			j += 1

	# if output array was a correct permutation of arr array then by now our stack should be empty
	if not s:
		return True

	return False
	

arr = [4,5,6,7,8] # Input Array
output = [8,7,6,5,4] # Output Array
n = 5
if (checkStackPermutation(arr, output, n)):
	print("Yes")
else:
	print("Not Possible")
```

## Implement Queue using Stack

```python
from collections import deque
 
class Queue:
    def __init__(self):
        self.s1 = deque()
        self.s2 = deque()
 
    def enqueue(self, data):
        self.s1.append(data)
    
    def dequeue(self):
        # if both stacks are empty
        if not self.s1 and not self.s2:
            print('Underflow!!')
            exit(0)
 
        # if the second stack is empty, move elements from the first stack to it
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
 
        # return the top item from the second stack
        return self.s2.pop()
 
 
keys = [1, 2, 3, 4, 5]
q = Queue()
for key in keys:
    q.enqueue(key)
print(q.dequeue())        # 1
print(q.dequeue())        # 2
```

## Implement "n" queue in an array

```python
class KQueues:
	def __init__(self, number_of_queues, array_length):
		self.number_of_queues = number_of_queues
		self.array_length = array_length
		self.array = [-1] * array_length
		self.front = [-1] * number_of_queues
		self.rear = [-1] * number_of_queues
		self.next_array = list(range(1, array_length))
		self.next_array.append(-1)
		self.free = 0

	# To check whether the current queue_number is empty or not
	def is_empty(self, queue_number):
		return self.front[queue_number] == -1

	# To check whether the current queue_number is full or not
	def is_full(self, queue_number):
		return self.free == -1

	# To enqueue the given item in the given queue_number where queue_number is from 0 to number_of_queues-1
	def enqueue(self, item, queue_number):
		if self.is_full(queue_number):
			print("Queue FULL")
			return
		next_free = self.next_array[self.free]
		if self.is_empty(queue_number):
			self.front[queue_number] = self.rear[queue_number] = self.free
		else:
			self.next_array[self.rear[queue_number]] = self.free
			self.rear[queue_number] = self.free
		self.next_array[self.free] = -1
		self.array[self.free] = item
		self.free = next_free

	# To dequeue an item from the given queue_number where queue_number is from 0 to number_of_queues-1
	def dequeue(self, queue_number):
		if self.is_empty(queue_number):
			print("Queue EMPTY")
			return

		front_index = self.front[queue_number]
		self.front[queue_number] = self.next_array[front_index]
		self.next_array[front_index] = self.free
		self.free = front_index
		return self.array[front_index]
		
# Let us create 3 queue in an array of size 10
ks = KQueues(3, 10)
	
# Let us put some items in queue number 2
ks.enqueue(15, 2)
ks.enqueue(45, 2)
# Let us put some items in queue number 1
ks.enqueue(17, 1);
ks.enqueue(49, 1);
ks.enqueue(39, 1);
	
# Let us put some items in queue number 0
ks.enqueue(11, 0);
ks.enqueue(9, 0);
ks.enqueue(7, 0);
	
print(f"Dequeued element from queue 2 is {ks.dequeue(2)}")
print(f"Dequeued element from queue 1 is {ks.dequeue(1)}")
print(f"Dequeued element from queue 0 is {ks.dequeue(0)}")
```

## Implement a Circular queue

```python
class CircularQueue():
	def __init__(self, size): 
		self.size = size
		self.queue = [None for _ in range(size)]
		self.front = self.rear = -1

	def enqueue(self, data):
		
		# condition if queue is full
		if ((self.rear + 1) % self.size == self.front):
			print(" Queue is Full\n")
			
		# condition for empty queue
		elif (self.front == -1):
			self.front = 0
			self.rear = 0
			self.queue[self.rear] = data
		else:
			
			# next position of rear
			self.rear = (self.rear + 1) % self.size
			self.queue[self.rear] = data
			
	def dequeue(self):
		if (self.front == -1): # condition for empty queue
			print ("Queue is Empty\n")
			
		# condition for only one element
		elif (self.front == self.rear):
			temp=self.queue[self.front]
			self.front = -1
			self.rear = -1
			return temp
		else:
			temp = self.queue[self.front]
			self.front = (self.front + 1) % self.size
			return temp

	def display(self):
		# condition for empty queue
		if (self.front == -1):
			print ("Queue is Empty")

		elif (self.rear >= self.front):
			print("Elements in the circular queue are:",
											end = " ")
			for i in range(self.front, self.rear + 1):
				print(self.queue[i], end = " ")
			print ()

		else:
			print ("Elements in Circular Queue are:",
										end = " ")
			for i in range(self.front, self.size):
				print(self.queue[i], end = " ")
			for i in range(self.rear + 1):
				print(self.queue[i], end = " ")
			print ()

		if ((self.rear + 1) % self.size == self.front):
			print("Queue is Full")

ob = CircularQueue(5)
ob.enqueue(14)
ob.enqueue(22)
ob.enqueue(13)
ob.enqueue(-6)
ob.display()
print ("Deleted value = ", ob.dequeue())
print ("Deleted value = ", ob.dequeue())
ob.display()
ob.enqueue(9)
ob.enqueue(20)
ob.enqueue(5)
ob.display()
```

## LRU Cache Implementation

```python
class DLLNode:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        # capacity:  capacity of cache
        # Initialize all variable
        self.capacity = capacity
        self.map = {}
        self.head = DLLNode(0, 0)
        self.tail = DLLNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.count = 0

    def deleteNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def addToHead(self, node):
        node.next = self.head.next
        node.next.prev = node
        node.prev = self.head
        self.head.next = node

    # This method works in O(1)
    def get(self, key):
        if key in self.map:
            node = self.map[key]
            result = node.val
            self.deleteNode(node)
            self.addToHead(node)
            print(f'Got the value : {result} for the key: {key}')
            return result
        print(f'Did not get any value for the key: {key}')
        return -1

    # This method works in O(1)
    def set(self, key, value):
        print(f'going to set the (key, value) : ( {key}, {value})')
        if key in self.map:
            node = self.map[key]
            node.val = value
            self.deleteNode(node)
        else:
            node = DLLNode(key, value)
            self.map[key] = node
            if self.count < self.capacity:
                self.count += 1
            else:
                del self.map[self.tail.prev.key]
                self.deleteNode(self.tail.prev)

        self.addToHead(node)


print('Going to test the LRU Cache Implementation')
cache = LRUCache(2)
# it will store a key (1) with value 10 in the cache.
cache.set(1, 10)
# it will store a key (1) with value 10 in the cache.
cache.set(2, 20)
print(f'Value for the key: 1 is {cache.get(1)}')
# evicts key 2 and store a key (3) with value 30 in the cache.
cache.set(3, 30)
print(f'Value for the key: 2 is {cache.get(2)}')
# evicts key 1 and store a key (4) with value 40 in the cache.
cache.set(4, 40)
print(f'Value for the key: 1 is {cache.get(1)}')
print(f'Value for the key: 3 is {cache.get(3)}')
print(f'Value for the key: 4 is {cache.get(4)}')

```

## Reverse a Queue using recursion

```python
from queue import Queue
def Print(queue):
	while (not queue.empty()):
		print(queue.queue[0], end=", ")
		queue.get()

def reversequeue(queue):
	Stack = []
	while (not queue.empty()):
		Stack.append(queue.queue[0])
		queue.get()
	while Stack:
		queue.put(Stack[-1])
		Stack.pop()


queue = Queue()
queue.put(10)
queue.put(20)
queue.put(30)
queue.put(40)
queue.put(50)
queue.put(60)
queue.put(70)
queue.put(80)
queue.put(90)
queue.put(100)
reversequeue(queue)
Print(queue)
```

## Reverse the first “K” elements of a queue

```python
from queue import Queue

def reverseQueueFirstKElements(k, Queue):
	if (Queue.empty() == True or
			k > Queue.qsize()):
		return
	if (k <= 0):
		return

	Stack = []

	# put the first K elements into a Stack
	for _ in range(k):
		Stack.append(Queue.queue[0])
		Queue.get()

	# Enqueue the contents of stack at the back of the queue
	while Stack:
		Queue.put(Stack[-1])
		Stack.pop()

	# Remove the remaining elements and enqueue them at the end of the Queue
	for _ in range(Queue.qsize() - k):
		Queue.put(Queue.queue[0])
		Queue.get()


def Print(Queue):
	while (not Queue.empty()):
		print(Queue.queue[0], end =" ")
		Queue.get()


Queue = Queue()
Queue.put(10)
Queue.put(20)
Queue.put(30)
Queue.put(40)
Queue.put(50)
Queue.put(60)
Queue.put(70)
Queue.put(80)
Queue.put(90)
Queue.put(100)
k = 5
reverseQueueFirstKElements(k, Queue)
Print(Queue)
```

## Interleave the first half of the queue with second half

```python
from queue import Queue

def interLeaveQueue(q):
	if (q.qsize() % 2 != 0):
		print("Input even number of integers.")

	# Initialize an empty stack of int type
	s = []
	halfSize = int(q.qsize() / 2)

	# put first half elements into the stack queue:16 17 18 19 20, stack: 15(T) 14 13 12 11
	for _ in range(halfSize):
		s.append(q.queue[0])
		q.get()

	# enqueue back the stack elements queue: 16 17 18 19 20 15 14 13 12 11
	while s:
		q.put(s[-1])
		s.pop()

	# dequeue the first half elements of queue and enqueue them back queue: 15 14 13 12 11 16 17 18 19 20
	for _ in range(halfSize):
		q.put(q.queue[0])
		q.get()

	# Again put the first half elements into the stack queue: 16 17 18 19 20, stack: 11(T) 12 13 14 15
	for _ in range(halfSize):
		s.append(q.queue[0])
		q.get()

	# interleave the elements of queue and stack queue: 11 16 12 17 13 18 14 19 15 20
	while s:
		q.put(s[-1])
		s.pop()
		q.put(q.queue[0])
		q.get()



q = Queue()
q.put(11)
q.put(12)
q.put(13)
q.put(14)
q.put(15)
q.put(16)
q.put(17)
q.put(18)
q.put(19)
q.put(20)
interLeaveQueue(q)
length = q.qsize()
for _ in range(length):
	print(q.queue[0], end=" ")
	q.get()
```

## Find the first circular tour that visits all Petrol Pumps

```python
"""
Suppose there is a circle. There are N petrol pumps on that circle. You will be given two sets of data.
1. The amount of petrol that every petrol pump has.
2. Distance from that petrol pump to the next petrol pump.
Find a starting point where the truck can start to get through the complete circle without exhausting its petrol in between.
Note :  Assume for 1 litre petrol, the truck can go 1 unit of distance.

Example 1:

Input:
N = 4
Petrol = 4 6 7 4
Distance = 6 5 3 5
Output: 1
Explanation: There are 4 petrol pumps with
amount of petrol and distance to next
petrol pump value pairs as {4, 6}, {6, 5},
{7, 3} and {4, 5}. The first point from
where truck can make a circular tour is
2nd petrol pump. Output in this case is 1
(index of 2nd petrol pump).
"""

# A petrol pump has petrol and distance to next petrol pump
class petrolPump:
    def __init__(self,a, b):
        self.petrol = a
        self.distance = b
    
# The function returns starting point if there is a possible solution, otherwise returns -1
def printTour( p, n):
    # deficit is used to store the value of the capacity as soon as the value of capacity becomes negative so as not to traverse the array twice in order to get the solution
    start = 0
    deficit = 0
    capacity = 0
    for i in range(n):
        capacity += p[i].petrol - p[i].distance
        if (capacity < 0):
            # If this particular step is not done then the between steps would be redundant
            start = i + 1
            deficit += capacity
            capacity = 0
    return start if (capacity + deficit >= 0) else -1


arr = [petrolPump(6, 4),petrolPump(3, 6),petrolPump(7, 3)] 
n = len(arr)
start = printTour(arr, n)
if (start == -1):
    print("No solution")
else:
    print("Start = " , start)

```

## Minimum time required to rot all oranges

```python
"""
Given a matrix of dimension m*n where each cell in the matrix can have values 0, 1 or 2 which has the following meaning:  

0: Empty cell
1: Cells have fresh oranges
2: Cells have rotten oranges
Determine what is the minimum time required so that all the oranges become rotten. A rotten orange at index [i,j] can rot other fresh orange at indexes [i-1,j], [i+1,j], [i,j-1], [i,j+1] (up, down, left and right). If it is impossible to rot every orange then simply return -1.

Examples: 

Input:  arr[][C] = { {2, 1, 0, 2, 1},
                     {1, 0, 1, 2, 1},
                     {1, 0, 0, 2, 1}};
Output:
All oranges can become rotten in 2-time frames.
Explanation: 
At 0th time frame:
 {2, 1, 0, 2, 1}
 {1, 0, 1, 2, 1}
 {1, 0, 0, 2, 1}

At 1st time frame:
 {2, 2, 0, 2, 2}
 {2, 0, 2, 2, 2}
 {1, 0, 0, 2, 2}

At 2nd time frame:
 {2, 2, 0, 2, 2}
 {2, 0, 2, 2, 2}
 {2, 0, 0, 2, 2}
"""


from collections import deque

# function to check whether a cell is valid / invalid
def isvalid(i, j):
	return (i >= 0 and j >= 0 and i < 3 and j < 5)

# Function to check whether the cell is delimiter which is (-1, -1)
def isdelim(temp):
	return (temp[0] == -1 and temp[1] == -1)

# Function to check whether there is still a fresh orange remaining
def checkall(arr):
	for i in range(3):
		for j in range(5):
			if (arr[i][j] == 1):
				return True
	return False

# This function finds if it is possible to rot all oranges or not. If possible, then it returns minimum time required to rot all, otherwise returns -1
def rotOranges(arr):

	# Create a queue of cells
	Q = deque()
	temp = [0, 0]
	ans = 1

	# Store all the cells having rotten orange in first time frame
	for i in range(3):
		for j in range(5):
			if (arr[i][j] == 2):
				temp[0]= i
				temp[1] = j
				Q.append([i, j])

	# Separate these rotten oranges from the oranges which will rotten due the oranges in first time frame using delimiter which is (-1, -1)
	temp[0] = -1
	temp[1] = -1
	Q.append([-1, -1])
	# print(Q)

	# Process the grid while there are rotten oranges in the Queue
	while False:
	
		# This flag is used to determine whether even a single fresh orange gets rotten due to rotten oranges in current time frame so we can increase the count of the required time.
		flag = False
		print(len(Q))

		# Process all the rotten oranges in current time frame.
		while not isdelim(Q[0]):
			temp = Q[0]
			print(len(Q))

			# Check right adjacent cell that if it can be rotten
			if (isvalid(temp[0] + 1, temp[1]) and arr[temp[0] + 1][temp[1]] == 1):
				
				# if this is the first orange to get rotten, increase count and set the flag.
				if (not flag):
					ans, flag =ans + 1, True

				# Make the orange rotten
				arr[temp[0] + 1][temp[1]] = 2

				# append the adjacent orange to Queue
				temp[0] += 1
				Q.append(temp)

				temp[0] -= 1 # Move back to current cell

			# Check left adjacent cell that if it can be rotten
			if (isvalid(temp[0] - 1, temp[1]) and arr[temp[0] - 1][temp[1]] == 1):
				if (not flag):
					ans, flag =ans + 1, True
				arr[temp[0] - 1][temp[1]] = 2
				temp[0] -= 1
				Q.append(temp) # append this cell to Queue
				temp[0] += 1

			# Check top adjacent cell that if it can be rotten
			if (isvalid(temp[0], temp[1] + 1) and arr[temp[0]][temp[1] + 1] == 1):
				if (not flag):
					ans, flag = ans + 1, True
				arr[temp[0]][temp[1] + 1] = 2
				temp[1] += 1
				Q.append(temp) # Push this cell to Queue
				temp[1] -= 1

			# Check bottom adjacent cell if it can be rotten
			if (isvalid(temp[0], temp[1] - 1) and arr[temp[0]][temp[1] - 1] == 1):
				if (not flag):
					ans, flag = ans + 1, True
				arr[temp[0]][temp[1] - 1] = 2
				temp[1] -= 1
				Q.append(temp) # append this cell to Queue
			Q.popleft()

		# Pop the delimiter
		Q.popleft()

		# If oranges were rotten in current frame than separate the rotten oranges using delimiter for the next frame for processing.
		if (len(Q) == 0):
			temp[0] = -1
			temp[1] = -1
			Q.append(temp)

		# If Queue was empty than no rotten oranges left to process so exit

	# Return -1 if all arranges could not rot, otherwise return ans.
	return ans + 1 if(checkall(arr)) else -1

arr = [[2, 1, 0, 2, 1],
	[1, 0, 1, 2, 1],
	[1, 0, 0, 2, 1]]
ans = rotOranges(arr)
if (ans == -1):
	print("All oranges cannot rotn")
else:
	print("Time required for all oranges to rot => " , ans)
```

## Distance of nearest cell having 1 in a binary matrix

```python
"""
Given a binary matrix of N x M, containing at least a value 1. The task is to find the distance of nearest 1 in the matrix for each cell. The distance is calculated as |i1 – i2| + |j1 – j2|, where i1, j1 are the row number and column number of the current cell and i2, j2 are the row number and column number of the nearest cell having value 1.

Examples: 

Input : N = 3, M = 4
        mat[][] = { 0, 0, 0, 1,
                    0, 0, 1, 1,
                    0, 1, 1, 0 }
Output : 3 2 1 0
         2 1 0 0
         1 0 0 1
Explanation:
For cell at (0, 0), nearest 1 is at (0, 3),
so distance = (0 - 0) + (3 - 0) = 3.
Similarly, all the distance can be calculated.

"""
import sys
class matrix_element:
	def __init__(self, row, col):
		self.row = row
		self.col = col
		
def printDistance(arr):
	Row_Count = len(arr)
	Col_Count = len(arr[0])	
	q = []

	# Adding all ones in queue
	for i in range(Row_Count):
		for j in range(Col_Count):
			if (arr[i][j] == 1):
				q.append(matrix_element(i, j))
			
	# In order to find min distance we will again traverse all elements in Matrix. If its zero then it will check against all 1's in Queue. Whatever will be dequeued from queued, will be enqueued back again.
	Queue_Size = len(q)
	for i in range(Row_Count):
		for j in range(Col_Count):
			distance = 0
			min_distance = sys.maxsize
			
			if (arr[i][j] == 0):
				for k in range(Queue_Size):
					One_Pos = q[0]
					q = q[1:]
					One_Row = One_Pos.row
					One_Col = One_Pos.col
					distance = abs(One_Row - i) + abs(One_Col - j)
					min_distance = min(min_distance, distance)
					if (min_distance == 1):
						arr[i][j] = 1
						q.append(matrix_element(One_Row, One_Col))
						break
					q.append(matrix_element(One_Row,One_Col))
					arr[i][j] = min_distance
			else:
				arr[i][j] = 0
								

	for i in range(Row_Count):
		for j in range(Col_Count):
			print(arr[i][j] ,end = " ")
		print()
		

arr = [ [ 0, 0, 0, 1 ], [ 0, 0, 1, 1 ], [ 0, 1, 1, 0 ] ]
printDistance(arr)
```

## First negative integer in every window of size “k”

```python
"""
Given an array and a positive integer k, find the first negative integer for each window(contiguous subarray) of size k. If a window does not contain a negative integer, then print 0 for that window.

Examples:  

Input : arr[] = {-8, 2, 3, -6, 10}, k = 2
Output : -8 0 -6 -6

First negative integer for each window of size k
{-8, 2} = -8
{2, 3} = 0 (does not contain a negative integer)
{3, -6} = -6
{-6, 10} = -6

Input : arr[] = {12, -1, -7, 8, -15, 30, 16, 28} , k = 3
Output : -1 -1 -7 -15 -15 0

"""

def printFirstNegativeInteger(arr, k):
	firstNegativeIndex = 0
	for i in range(k - 1, len(arr)):
		# skip out of window and positive elements
		while firstNegativeIndex < i and (firstNegativeIndex <= i - k or arr[firstNegativeIndex] >= 0):
			firstNegativeIndex += 1
		# check if a negative element is found, otherwise use 0
		firstNegativeElement = min(arr[firstNegativeIndex], 0)
		print(firstNegativeElement, end=' ')

arr = [12, -1, -7, 8, -15, 30, 16, 28]
k = 3
printFirstNegativeInteger(arr, k)

```

## Check if all levels of two trees are anagrams or not.

```python
class newNode:
	def __init__(self, data):
		self.data = data
		self.left = self.right = None
		
# Returns true if trees with root1 and root2 are level by level anagram, else returns false.
def areAnagrams(root1, root2):

	if root1 is None and root2 is None:
		return True
	if root1 is None or root2 is None:
		return False

	q1 = [root1]
	q2 = [root2]
	while (1) :

		# n1 (queue size) indicates number of Nodes at current level in first tree and n2 indicates number of nodes in current level of second tree.
		n1 = len(q1)
		n2 = len(q2)

		# If n1 and n2 are different
		if (n1 != n2):
			return False

		# If level order traversal is over
		if (n1 == 0):
			break

		# Dequeue all Nodes of current level and Enqueue all Nodes of next level
		curr_level1 = []
		curr_level2 = []
		while (n1 > 0):
			node1 = q1[0]
			q1.pop(0)
			if (node1.left != None) :
				q1.append(node1.left)
			if (node1.right != None) :
				q1.append(node1.right)
			n1 -= 1

			node2 = q2[0]
			q2.pop(0)
			if (node2.left != None) :
				q2.append(node2.left)
			if (node2.right != None) :
				q2.append(node2.right)

			curr_level1.append(node1.data)
			curr_level2.append(node2.data)

		# Check if nodes of current levels are anagrams or not.
		curr_level1.sort()
		curr_level2.sort()
		if (curr_level1 != curr_level2) :
			return False
	return True


root1 = newNode(1)
root1.left = newNode(3)
root1.right = newNode(2)
root1.right.left = newNode(5)
root1.right.right = newNode(4)
root2 = newNode(1)
root2.left = newNode(2)
root2.right = newNode(3)
root2.left.left = newNode(4)
root2.left.right = newNode(5)
if areAnagrams(root1, root2):
	print("Yes")
else:
	print("No")
```

## Sum of minimum and maximum elements of all subarrays of size “k”.

```python
"""Given an array of both positive and negative integers, the task is to compute sum of minimum and maximum elements of all sub-array of size k.

Examples: 

Input : arr[] = {2, 5, -1, 7, -3, -1, -2}  
        K = 4
Output : 18
Explanation : Subarrays of size 4 are : 
     {2, 5, -1, 7},   min + max = -1 + 7 = 6
     {5, -1, 7, -3},  min + max = -3 + 7 = 4      
     {-1, 7, -3, -1}, min + max = -3 + 7 = 4
     {7, -3, -1, -2}, min + max = -3 + 7 = 4   
     Sum of all min & max = 6 + 4 + 4 + 4 
                          = 18             """


from collections import deque

# Returns Sum of min and max element of all subarrays of size k
def SumOfKsubArray(arr, n , k):

	Sum = 0 # Initialize result

	# The queue will store indexes of useful elements in every window In deque 'G' we maintain decreasing order of values from front to rear In deque 'S' we maintain increasing order of values from front to rear
	S = deque()
	G = deque()

	for i in range(k):
		# Remove all previous greater elements that are useless.
		while ( len(S) > 0 and arr[S[-1]] >= arr[i]):
			S.pop() # Remove from rear

		# Remove all previous smaller that are elements are useless.
		while ( len(G) > 0 and arr[G[-1]] <= arr[i]):
			G.pop() # Remove from rear

		# Add current element at rear of both deque
		G.append(i)
		S.append(i)

	# Process rest of the Array elements
	for i in range(k, n):
		
		# Element at the front of the deque 'G' & 'S' is the largest and smallest element of previous window respectively
		Sum += arr[S[0]] + arr[G[0]]

		# Remove all elements which are out of this window
		while ( len(S) > 0 and S[0] <= i - k):
			S.popleft()
		while ( len(G) > 0 and G[0] <= i - k):
			G.popleft()

		# remove all previous greater element that are useless
		while ( len(S) > 0 and arr[S[-1]] >= arr[i]):
			S.pop() # Remove from rear

		# remove all previous smaller that are elements are useless
		while ( len(G) > 0 and arr[G[-1]] <= arr[i]):
			G.pop() # Remove from rear

		# Add current element at rear of both deque
		G.append(i)
		S.append(i)

	# Sum of minimum and maximum element of last window
	Sum += arr[S[0]] + arr[G[0]]
	return Sum


arr=[2, 5, -1, 7, -3, -1, -2]
n = len(arr)
k = 3
print(SumOfKsubArray(arr, n, k))
```

## Minimum sum of squares of character counts in a given string after removing “k” characters.

```python
"""
Given a string of lowercase alphabets and a number k, the task is to print the minimum value of the string after removal of ‘k’ characters. The value of a string is defined as the sum of squares of the count of each distinct character. 
For example consider the string “saideep”, here frequencies of characters are s-1, a-1, i-1, e-2, d-1, p-1 and value of the string is 1^2 + 1^2 + 1^2 + 1^2 + 1^2 + 2^2 = 9.
Expected Time Complexity: O(k*logn)

Examples: 

Input :  str = abccc, K = 1
Output :  6
We remove c to get the value as 12 + 12 + 22

Input :  str = aaab, K = 2
Output :  2
"""

from queue import PriorityQueue
MAX_CHAR = 26

def minStringValue(str, k):
	l = len(str) # find length of string

	# if K is greater than length of string so reduced string will become 0
	if(k >= l):
		return 0
	
	# Else find Frequency of each character and store in an array
	frequency = [0] * MAX_CHAR
	for i in range(0, l):
		frequency[ord(str[i]) - 97] += 1

	# Push each char frequency negative into a priority_queue as the queue by default is minheap
	q = PriorityQueue()
	for i in range(0, MAX_CHAR):
		q.put(-frequency[i])

	# Removal of K characters
	while(k > 0):
		
		# Get top element in priority_queue multiply it by -1 as temp is negative remove it. Increment by 1 and again push into priority_queue
		temp = q.get()
		temp = temp + 1
		q.put(temp, temp)
		k = k - 1

	# After removal of K characters find sum of squares of string Value	
	result = 0; # initialize result
	while not q.empty():
		temp = q.get()
		temp = temp * (-1)
		result += temp * temp
	return result


str1 = "abbccc"
k = 2
print(minStringValue(str1, k))
str2 = "aaab"
k = 2
print(minStringValue(str2, k))

```

## Next Smaller Element

```python
"""
Given an array, print the Next Smaller Element (NSE) for every element. The NSE for an element x is the first smaller element on the right side of x in array. Elements for which no smaller element exist (on right side), consider NSE as -1. 
Examples: 
a) For any array, rightmost element always has NSE as -1. 
b) For an array which is sorted in increasing order, all elements have NSE as -1. 
c) For the input array [4, 8, 5, 2, 25}, the NSE for each element are as follows.

Element         NSE
   4      -->    2
   8      -->    5
   5      -->    2
   2      -->   -1
   25     -->   -1
"""

def printNSE(arr, n):
	mp = {}
	s = []
	for i in range(n):
		if not s:
			s.append(arr[i])
			continue

		# if stack is not empty, then pop an element from stack. If the popped element is greater than next, then a) print the pair b) keep popping while elements are greater and stack is not empty 
		while s and s[-1] > arr[i]:
			mp[s[-1]] = arr[i]
			s.pop()

		# push next to stack so that we can find next smaller for it
		s.append(arr[i])

	# After iterating over the loop, the remaining elements in stack do not have the next smaller element, so print -1 for them
	while s:
		mp[s[-1]] = -1
		s.pop()

	for i in range(n):
		print(arr[i], "--->", mp[arr[i]])


arr = [11, 13, 21, 3]
n = len(arr)
printNSE(arr, n)
```