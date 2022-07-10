"""
Given three strings A, B and C. Write a function that checks whether C is an interleaving of A and B. C is said to be interleaving A and B, if it contains all and only characters of A and B and order of all characters in individual strings is preserved. 

Example: 

Input: strings: "XXXXZY", "XXY", "XXZ"
Output: XXXXZY is interleaved of XXY and XXZ
The string XXXXZY can be made by 
interleaving XXY and XXZ
String:    XXXXZY
String 1:    XX Y
String 2:  XX  Z

Input: strings: "XXY", "YX", "X"
Output: XXY is not interleaved of YX and X
XXY cannot be formed by interleaving YX and X.
The strings that can be formed are YXX and XYX
"""

dp = [[0]*101]*101
def dfs(i, j, A, B, C):
	
	# If path has already been calculated from this index then return calculated value.
	if(dp[i][j]!=-1):
		return dp[i][j]
		
	# If we reach the destination return 1
	n,m=len(A),len(B)
	if(i==n and j==m):
		return 1
	
	# If C[i+j] matches with both A[i] and B[j] we explore both the paths
	if (i<n and A[i]==C[i + j] and j<m and B[j]==C[i + j]):
		# go down and store the calculated value in x
		# and go right and store the calculated value in y.
		x = dfs(i + 1, j, A, B, C)
		y = dfs(i, j + 1, A, B, C)
		
		# return the best of both.
		dp[i][j] = x|y
		return dp[i][j]
	
	# If C[i+j] matches with A[i].
	if (i < n and A[i] == C[i + j]):
		# go down
		x = dfs(i + 1, j, A, B, C)
		
		# Return the calculated value.
		dp[i][j] = x
		return dp[i][j]
	
	# If C[i+j] matches with B[j].
	if (j < m and B[j] == C[i + j]):
		y = dfs(i, j + 1, A, B, C)
		
		# Return the calculated value.
		dp[i][j] = y
		return dp[i][j]
	
	# if nothing matches we return 0
	dp[i][j] = 0
	return dp[i][j]

# The main function that returns true if C is
# an interleaving of A and B, otherwise false.
def isInterleaved(A, B, C):

	# Storing the length in n,m
	n = len(A)
	m = len(B)

	# C can be an interleaving of A and B only of the sum
	# of lengths of A & B is equal to the length of C.
	if((n+m)!=len(C)):
		return 0
	# initializing dp array with -1
	for i in range(n+1):
		for j in range(m+1):
			dp[i][j]=-1
	# calling and returning the answer
	return dfs(0,0,A,B,C)
	
def test(A, B, C):
	if (isInterleaved(A, B, C)):
		print(C, "is interleaved of", A, "and", B)
	else:
		print(C, "is not interleaved of", A, "and", B)

test("XXY", "XXZ", "XXZXXXY")
test("XY", "WZ", "WZXY")
test("XY", "X", "XXY")
test("YX", "X", "XXY")
test("XXY", "XXZ", "XXXXZY")
test("ACA", "DAS", "DAACSA")

