"""
Given an array of digits (values are from 0 to 9), find the minimum possible sum of two numbers formed from digits of the array. All digits of given array must be used to form the two numbers. 
Examples : 
 

Input: [6, 8, 4, 5, 2, 3]
Output: 604
The minimum sum is formed by numbers 
358 and 246

Input: [5, 3, 0, 7, 4]
Output: 82
The minimum sum is formed by numbers 
35 and 047 
"""

def solve(arr, n):
	# sort the array
	arr.sort()

	# let two numbers be a and b
	a = 0; b = 0
	
	for i in range(n):
		# Fill a and b with every alternate digit of input array
		if (i % 2 != 0):
			a = a * 10 + arr[i]
		else:
			b = b * 10 + arr[i]
	return a + b


arr = [6, 8, 4, 5, 2, 3]
n = len(arr)
print("Sum is ", solve(arr, n))


