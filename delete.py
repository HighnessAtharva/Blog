"""
Input: {{"you", "we"},
        {"have", "are"},
        {"sleep", "eat", "drink"}}

Output:
  you have sleep
  you have eat
  you have drink
  you are sleep
  you are eat
  you are drink
  we have sleep
  we have eat
  we have drink
  we are sleep
  we are eat
  we are drink 
"""

R = 3
C = 3

# A recursive function to print all possible sentences that can be formed from a list of word list
def printUtil(arr, m, n, output):

	# Add current word to output array
	output[m] = arr[m][n]

	# If this is last word of current output sentence, then print the output sentence
	if m==R-1:
		for i in range(R):
			print (output[i],end= " ")
		print()
		return

	# Recur for next row
	for i in range(C):
		if arr[m+1][i] != "":
			printUtil(arr, m+1, i, output)

def printf(arr):

	# Create an array to store sentence
	output = [""] * R

	# Consider all words for first row as starting points and print all sentences
	for i in range(C):
		if arr[0][i] != "":
			printUtil(arr, 0, i, output)


arr = [ ["you", "we",""],
		["have", "are",""],
		["sleep", "eat", "drink"]]
printf(arr)

