"""
Given three stacks of the positive numbers, the task is to find the possible equal maximum sum of the stacks with the removal of top elements allowed. Stacks are represented as an array, and the first index of the array represent the top element of the stack.

Examples: 

Input : stack1[] = { 3, 10}
  stack2[] = { 4, 5 }
  stack3[] = { 2, 1 }
Output : 0
Sum can only be equal after removing all elements 
from all stacks.
"""
def maxSum(stack1, stack2, stack3, n1, n2, n3):
	sum1, sum2, sum3 = 0, 0, 0
	
	# Finding the initial sum of stack1.
	for i in range(n1):
		sum1 += stack1[i]
	
	# Finding the initial sum of stack2.
	for i in range(n2):
		sum2 += stack2[i]
	
	# Finding the initial sum of stack3.
	for i in range(n3):
		sum3 += stack3[i]

# As given in question, first element is top of stack..
	top1, top2, top3 = 0, 0, 0
	ans = 0
	
	while True:
	# If any stack is empty
		if (top1 == n1 or top2 == n2 or top3 == n3):
			return 0
	# If sum of all three stack are equal.
		if sum1 == sum2 == sum3:
			return sum1

	# Finding the stack with maximum sum and removing its top element.
		if (sum1 >= sum2 and sum1 >= sum3):
			sum1 -= stack1[top1]
			top1=top1+1
		elif (sum2 >= sum1 and sum2 >= sum3):
			sum2 -= stack2[top2]
			top2=top2+1
		elif (sum3 >= sum2 and sum3 >= sum1):
			sum3 -= stack3[top3]
			top3=top3+1


stack1 = [ 3, 2, 1, 1, 1 ]
stack2 = [ 4, 3, 2 ]
stack3 = [ 1, 1, 4, 1 ]
n1 = len(stack1)
n2 = len(stack2)
n3 = len(stack3)
print (maxSum(stack1, stack2, stack3, n1, n2, n3))

