---
title: "DSA in Python - Strings"
date: 2022-07-09T13:14:34+05:30
draft: true
cover: 
    image: blog/dsa/string.jpg
    alt: Strings
    caption: Learn String Algorithms in Python
tags: ["python"] 

---

- [Check whether a String is Palindrome or not](#check-whether-a-string-is-palindrome-or-not)
- [Find Duplicate characters in a string](#find-duplicate-characters-in-a-string)
- [Write a Code to check whether one string is a rotation of another](#write-a-code-to-check-whether-one-string-is-a-rotation-of-another)
- [Write a Program to check whether a string is a valid shuffle of two strings or not](#write-a-program-to-check-whether-a-string-is-a-valid-shuffle-of-two-strings-or-not)
- [Count and Say problem](#count-and-say-problem)
- [Write a program to find the longest Palindrome in a string.\[ Longest palindromic Substring\]](#write-a-program-to-find-the-longest-palindrome-in-a-string-longest-palindromic-substring)
- [Find Longest Recurring Subsequence in String](#find-longest-recurring-subsequence-in-string)
- [Print all Subsequences of a string.](#print-all-subsequences-of-a-string)
- [Print all the permutations of the given string](#print-all-the-permutations-of-the-given-string)
- [Split the Binary string into two substring with equal 0’s and 1’s](#split-the-binary-string-into-two-substring-with-equal-0s-and-1s)
- [Rabin Karp Algo](#rabin-karp-algo)
- [KMP Algo](#kmp-algo)
- [Convert a Sentence into its equivalent mobile numeric keypad sequence.](#convert-a-sentence-into-its-equivalent-mobile-numeric-keypad-sequence)
- [Minimum number of bracket reversals needed to make an expression balanced.](#minimum-number-of-bracket-reversals-needed-to-make-an-expression-balanced)
- [Count All Palindromic Subsequence in a given String.](#count-all-palindromic-subsequence-in-a-given-string)
- [Count of number of given string in 2D character array](#count-of-number-of-given-string-in-2d-character-array)
- [Search a Word in a 2D Grid of characters.](#search-a-word-in-a-2d-grid-of-characters)
- [Boyer Moore Algorithm for Pattern Searching.](#boyer-moore-algorithm-for-pattern-searching)
- [Converting Roman Numerals to Decimal](#converting-roman-numerals-to-decimal)
- [Longest Common Prefix](#longest-common-prefix)
- [Number of flips to make binary string alternate](#number-of-flips-to-make-binary-string-alternate)
- [Find the first repeated word in string.](#find-the-first-repeated-word-in-string)
- [Minimum number of swaps for bracket balancing.](#minimum-number-of-swaps-for-bracket-balancing)
- [Find the longest common subsequence between two strings.](#find-the-longest-common-subsequence-between-two-strings)
- [Program to generate all possible valid IP addresses from given  string.](#program-to-generate-all-possible-valid-ip-addresses-from-given--string)
- [Write a program to find the smallest window that contains all characters of string itself.](#write-a-program-to-find-the-smallest-window-that-contains-all-characters-of-string-itself)
- [Minimum characters to be added at front to make string palindrome](#minimum-characters-to-be-added-at-front-to-make-string-palindrome)
- [Find the smallest window in a string containing all characters of another string](#find-the-smallest-window-in-a-string-containing-all-characters-of-another-string)
- [Recursively remove all adjacent duplicates](#recursively-remove-all-adjacent-duplicates)
- [String matching where one string contains wildcard characters](#string-matching-where-one-string-contains-wildcard-characters)
- [Function to find Number of customers who could not get a computer](#function-to-find-number-of-customers-who-could-not-get-a-computer)
- [Transform One String to Another using Minimum Number of Given Operation](#transform-one-string-to-another-using-minimum-number-of-given-operation)
- [Check if two given strings are isomorphic to each other](#check-if-two-given-strings-are-isomorphic-to-each-other)
- [Recursively print all sentences that can be formed from list of word lists](#recursively-print-all-sentences-that-can-be-formed-from-list-of-word-lists)

## Check whether a String is Palindrome or not

```python
def isPalindrome(s):
    return s == s[::-1]
 
s = "malayalam"
ans = isPalindrome(s)
 
if ans:
    print("Yes")
else:
    print("No")
```

## Find Duplicate characters in a string

```python
def printDups(Str):
 
    count = {}
    for i in range(len(Str)):
        if(Str[i] in count):
            count[Str[i]] += 1
        else:
            count[Str[i]] = 1
        #increase the count of characters by 1
  
    for it,it2 in count.items():  #iterating through the unordered map
        if (it2 > 1):   #if the count of characters is greater then 1 then duplicate found
            print(str(it) + ", count = "+str(it2))

Str = "test string"
printDups(Str)
```

## Write a Code to check whether one string is a rotation of another

```python
def check_rotation(s, goal):

	if (len(s) != len(goal)):
		skip

	q1 = []
	for i in range(len(s)):
		q1.insert(0, s[i])

	q2 = []
	for i in range(len(goal)):
		q2.insert(0, goal[i])

	k = len(goal)
	while (k > 0):
		ch = q2[0]
		q2.pop(0)
		q2.append(ch)
		if (q2 == q1):
			return True
		k -= 1
	return False


s1 = "ABCD"
s2 = "CDAB"
if (check_rotation(s1, s2)):
	print(s2, " is a rotated form of ", s1)
else:
	print(s2, " is not a rotated form of ", s1)
s3 = "ACBD"
if (check_rotation(s1, s3)):
	print(s3, " is a rotated form of ", s1)
else:
	print(s3, " is not a rotated form of ", s1)

```

## Write a Program to check whether a string is a valid shuffle of two strings or not

```python
MAX = 256

# This function returns true if contents of arr1[] and arr2[] are same otherwise false.
def compare(arr1, arr2):
	
	global MAX

	for i in range(MAX):
		if (arr1[i] != arr2[i]):
			return False
			
	return True

# This function search for all permutations of pat[] in txt[]
def search(pat, txt):
	
	M = len(pat)
	N = len(txt)

	# countP[]: Store count of all characters of pattern
	# countTW[]: Store count of current window of text
	countP = [0 for _ in range(MAX)]
	countTW = [0 for _ in range(MAX)]

	for i in range(M):
		countP[ord(pat[i])] += 1
		countTW[ord(txt[i])] += 1

	# Traverse through remaining characters of pattern
	for i in range(M, N):

		# Compare counts of current window
		# of text with counts of pattern[]
		if (compare(countP, countTW)):
			return True

		# Add current character to current window
		countTW[ord(txt[i])] += 1

		# Remove the first character of previous window
		countTW[ord(txt[i - M])] -= 1

	# Check for the last window in text
	if(compare(countP, countTW)):
		return True
	return False


txt = "BACDGABCDA"
pat = "ABCD"

if (search(pat, txt)):
	print("Yes")
else:
	print("No")
```

## Count and Say problem

```python
def countnndSay(n):
	if (n == 1):
		return "1"
	if (n == 2):
		return "11"

	# Find n'th term by generating all terms from 3 to n-1. Every term is generated using previous term 
	s = "11"
	for _ in range(3, n + 1):
		# In below for loop, previous character is processed in current iteration. That is why a dummy character is added to make sure that loop runs one extra iteration.
		s += '$'
		l = len(s)

		cnt = 1 # Initialize count
		tmp = "" # Initialize i'th
		# Process previous term to find the next term
		for j in range(1 , l):

			# If current character doesn't match
			if (s[j] != s[j - 1]):

				# Append count of str[j-1] to temp
				tmp += str(cnt + 0)

				# Append str[j-1]
				tmp += s[j - 1]

				# Reset count
				cnt = 1

			# If matches, then increment count of matching characters
			else:
				cnt += 1

		# Update str
		s = tmp
	return s;

N = 3
print(countnndSay(N))
```

## Write a program to find the longest Palindrome in a string.[ Longest palindromic Substring]

```python
def expand(s, low, high):
    length = len(s)
 
    # expand in both directions
    while low >= 0 and high < length and s[low] == s[high]:
        low = low - 1
        high = high + 1
 
    # return palindromic substring
    return s[low + 1:high]
 

def findLongestPalindromicSubstring(s):
    if not s or not len(s):
        return ''
 
    # `max_str` stores the maximum length palindromic substring found so far
    max_str = ''
 
    # `max_length` stores the maximum length of palindromic substring found so far
    max_length = 0
 
    # consider every character of the given string as a midpoint and expand in both directions to find maximum length palindrome
 
    for i in range(len(s)):
 
        # find the longest odd length palindrome with `s[i]` as a midpoint
        curr_str = expand(s, i, i)
        curr_length = len(curr_str)
 
        # update maximum length palindromic substring if the odd length palindrome has a greater length
 
        if curr_length > max_length:
            max_length = curr_length
            max_str = curr_str
 
        # Find the longest even length palindrome with `s[i]` and `s[i+1]` as midpoints. Note that an even length palindrome has two midpoints.
 
        curr_str = expand(s, i, i + 1)
        curr_length = len(curr_str)
 
        # update maximum length palindromic substring if even length palindrome has a greater length
 
        if curr_length > max_length:
            max_length = curr_length
            max_str = curr_str
 
    return max_str
 

s = 'ABDCBCDBDCBBC'
print(f'The longest palindromic substring of {s} is', findLongestPalindromicSubstring(s))
```

## Find Longest Recurring Subsequence in String

```python
def findLongestRepeatingSubSeq( str):
    n = len(str)
    # Create and initialize DP table
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

    # Fill dp table (similar to LCS loops)
    for i in range(1,n+1):
        for j in range(1,n+1):
            # If characters match and indexes are not same
            if (str[i-1] == str[j-1] and i != j):
                dp[i][j] = 1 + dp[i-1][j-1]        
            # If characters do not match
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    return dp[n][n]

str1 = "aabb"
print("The length of the largest subsequence that repeats itself is : " ,findLongestRepeatingSubSeq(str1))
 
```

## Print all Subsequences of a string.

```python
# Below is the implementation of the above approach
def printSubsequence(input, output):

	# Base Case if the input is empty print the output string
	if len(input) == 0:
		print(output, end=' ')
		return

	# output is passed with including the 1st character of input string
	printSubsequence(input[1:], output+input[0])

	# output is passed without including the 1st character of input string
	printSubsequence(input[1:], output)


output = ""
str1 = "abcd"
printSubsequence(str1, output)
```

## Print all the permutations of the given string

```python
def permute(s, answer):
	if (len(s) == 0):
		print(answer, end = " ")
		return
	for i in range(len(s)):
		ch = s[i]
		left_substr = s[:i]
		right_substr = s[i + 1:]
		rest = left_substr + right_substr
		permute(rest, answer + ch)

answer = ""
s = "alex"
print("All possible strings are : ")
permute(s, answer)
```

## Split the Binary string into two substring with equal 0’s and 1’s

```python
def maxSubStr(str, n):
	# To store the count of 0s and 1s
	count0 = 0
	count1 = 0
	
	# To store the count of maximum substrings str can be divided into
	cnt = 0
	
	for i in range(n):
		if str[i] == '0':
			count0 += 1
		else:
			count1 += 1
			
		if count0 == count1:
			cnt += 1

# It is not possible to split the string
	if count0 != count1:
		return -1
			
	return cnt

str1 = "0100110101"
n = len(str1)
print(maxSubStr(str1, n))

```


## Rabin Karp Algo

```python
# d is the number of characters in the input alphabet
d = 256

# pat -> pattern
# txt -> text
# q -> A prime number

def search(pat, txt, q):
	M = len(pat)
	N = len(txt)
	i = 0
	j = 0
	p = 0 # hash value for pattern
	t = 0 # hash value for txt
	h = 1

	# The value of h would be "pow(d, M-1)%q"
	for _ in range(M-1):
		h = (h*d)%q

	# Calculate the hash value of pattern and first window of text
	for i in range(M):
		p = (d*p + ord(pat[i]))%q
		t = (d*t + ord(txt[i]))%q

	# Slide the pattern over text one by one
	for i in range(N-M+1):
		# Check the hash values of current window of text and pattern if the hash values match then only check for characters one by one
		if p==t:
			# Check for characters one by one
			for j in range(M):
				if txt[i+j] != pat[j]:
					break
				else: j+=1

			# if p == t and pat[0...M-1] = txt[i, i+1, ...i+M-1]
			if j==M:
				print(f"Pattern found at index {str(i)}")

		# Calculate hash value for next window of text: Remove leading digit, add trailing digit
		if i < N-M:
			t = (d*(t-ord(txt[i])*h) + ord(txt[i+M]))%q

			# We might get negative values of t, converting it to positive
			if t < 0:
				t = t+q


txt = "GEEKS FOR GEEKS"
pat = "GEEK"
q = 101
search(pat,txt,q)
```

## KMP Algo

```python
def longestPrefixSuffix(s):
	n = len(s)
	lps = [0] * n # lps[0] is always 0

	# length of the previous longest prefix suffix
	l = 0

	# the loop calculates lps[i] for i = 1 to n-1
	i = 1
	while (i < n):
		if (s[i] == s[l]):
			l = l + 1
			lps[i] = l
			i += 1

		elif l == 0:

			# if (len == 0)
			lps[i] = 0
			i += 1

		else:
			l = lps[l-1]
			# Also, note that we do not increment i here

	res = lps[n-1]

	# Since we are looking for non overlapping parts.
	return n//2 if (res > n/2) else res
		

s = "abcab"
print(longestPrefixSuffix(s))
```

## Convert a Sentence into its equivalent mobile numeric keypad sequence.

```python
"""
Input : GEEKSFORGEEKS
Output : 4333355777733366677743333557777
For obtaining a number, we need to press a
number corresponding to that character for 
number of times equal to position of the 
character. For example, for character C, 
we press number 2 three times and accordingly.

Input : HELLO WORLD
Output : 4433555555666096667775553
"""

def printSequence(arr, mystr):
	n = len(mystr)
	output = ""
	for i in range(n):

		# checking for space
		if (mystr[i] == ' '):
			output = f"{output}0"
		else:
			# calculating index for each
			# character		
			position = ord(mystr[i]) - ord('A')
			output = output + arr[position]
	
	return output
	

str1 = ["2", "22", "222",
	"3", "33", "333",   
	"4", "44", "444",
	"5", "55", "555",
	"6", "66", "666",
	"7", "77", "777", "7777",
	"8", "88", "888",
	"9", "99", "999", "9999" ]

mystr = "GEEKSFORGEEKS";
print( printSequence(str1, mystr))
```

## Minimum number of bracket reversals needed to make an expression balanced.

```python
"""
Input:  exp = "}{"
Output: 2
We need to change '}' to '{' and '{' to
'}' so that the expression becomes balanced, 
the balanced expression is '{}'

Input:  exp = "{{{"
Output: Can't be made balanced using reversals

Input:  exp = "{{{{"
Output: 2 

Input:  exp = "{{{{}}"
Output: 1 

Input:  exp = "}{{}}{{{"
Output: 3
"""
import math

def countMinReversals(expr):
	length = len(expr)

	# Expressions of odd lengths cannot be balanced
	if (length % 2 != 0):
		return -1

	left_brace = 0
	right_brace = 0

	for i in range(length):
		# If we find a left bracket then we simply increment the left bracket
		if (expr[i] == '{'):
			left_brace += 1
		elif (left_brace == 0):
			right_brace += 1
		else:
			left_brace -= 1

	return math.ceil(left_brace / 2) + math.ceil(right_brace / 2)


expr = "}}{{"
print(countMinReversals(expr))
```

## Count All Palindromic Subsequence in a given String.

```python
"""
Input : str = "abcd"
Output : 4
Explanation :- palindromic  subsequence are : "a" ,"b", "c" ,"d" 

Input : str = "aab"
Output : 4
Explanation :- palindromic subsequence are :"a", "a", "b", "aa"

Input : str = "aaaa"
Output : 15
"""
# Python 3 program to counts Palindromic
# Subsequence in a given String using recursion

def countPS(i, j):
	if(i > j):
		return 0

	if(dp[i][j] != -1):
		return dp[i][j]

	if (i == j):
		dp[i][j] = 1
	elif str[i] == str[j]:
		dp[i][j] = (countPS(i + 1, j) + countPS(i, j - 1) + 1)
	else:
		dp[i][j] = (countPS(i + 1, j) + countPS(i, j - 1) - countPS(i + 1, j - 1))
	return dp[i][j]


str = "abcb"
dp = [[-1 for _ in range(1000)] for _ in range(1000)]
n = len(str)
print("Total palindromic subsequence are :", countPS(0, n - 1))

```

## Count of number of given string in 2D character array

```python
"""
Given a 2-Dimensional character array and a string, we need to find the given string in 2-dimensional character array, such that individual characters can be present left to right, right to left, top to down or down to top.

Examples: 

Input : a ={
            {D,D,D,G,D,D},
            {B,B,D,E,B,S},
            {B,S,K,E,B,K},
            {D,D,D,D,D,E},
            {D,D,D,D,D,E},
            {D,D,D,D,D,G}
           }
        str= "GEEKS"
Output :2
"""


def internalSearch(ii, needle, row, col, hay, row_max, col_max):
	
	found = 0
	if (row >= 0 and row <= row_max and
		col >= 0 and col <= col_max and
		needle[ii] == hay[row][col]):
		match = needle[ii]
		ii += 1
		hay[row][col] = 0
		if (ii == len(needle)):
			found = 1
		else:
			
			# through Backtrack searching in every directions
			found += internalSearch(ii, needle, row, col + 1, hay, row_max, col_max)
			found += internalSearch(ii, needle, row, col - 1, hay, row_max, col_max)
			found += internalSearch(ii, needle, row + 1, col, hay, row_max, col_max)
			found += internalSearch(ii, needle, row - 1, col, hay, row_max, col_max)
		hay[row][col] = match
	return found

# Function to search the string in 2d array
def searchString(needle, row, col,strr, row_count, col_count):
	found = 0
	for r in range(row_count):
		for c in range(col_count):
			found += internalSearch(0, needle, r, c,
						strr, row_count - 1, col_count - 1)		
	return found


needle = "MAGIC"
inputt = ["BBABBM","CBMBBA","IBABBG","GOZBBI","ABBBBC","MCIGAM"]
strr = [0] * len(inputt)
for i in range(len(inputt)):
	strr[i] = list(inputt[i])
print("count: ", searchString(needle, 0, 0, strr, len(strr), len(strr[0])))

```

## Search a Word in a 2D Grid of characters.

```python
"""
Input:  grid[][] = {"GEEKSFORGEEKS",
                    "GEEKSQUIZGEEK",
                    "IDEQAPRACTICE"};
        word = "GEEKS"

Output: pattern found at 0, 0
        pattern found at 0, 8
        pattern found at 1, 0
Explanation: 'GEEKS' can be found as prefix of
1st 2 rows and suffix of first row

Input:  grid[][] = {"GEEKSFORGEEKS",
                    "GEEKSQUIZGEEK",
                    "IDEQAPRACTICE"};
        word = "EEE"

Output: pattern found at 0, 2
        pattern found at 0, 10
        pattern found at 2, 2
        pattern found at 2, 12
Explanation: EEE can be found in first row 
twice at index 2 and index 10
and in second row at 2 and 12
"""


class GFG:	
	def __init__(self):
		self.R = None
		self.C = None
		self.dir = [[-1, 0], [1, 0], [1, 1],
					[1, -1], [-1, -1], [-1, 1],
					[0, 1], [0, -1]]
					
	def search2D(self, grid, row, col, word):
		# If first character of word doesn't match with the given starting point in grid.
		if grid[row][col] != word[0]:
			return False
			
		# Search word in all 8 directions starting from (row, col)
		for x, y in self.dir:
			
			# Initialize starting point for current direction
			rd, cd = row + x, col + y
			flag = True
			
			# First character is already checked, match remaining characters
			for k in range(1, len(word)):
				
				# If out of bound or not matched, break
				if (0 <= rd <self.R and 0 <= cd < self.C and word[k] == grid[rd][cd]):
					# Moving in particular direction
					rd += x
					cd += y
				else:
					flag = False
					break
			
			# If all character matched, then value of flag must be false	
			if flag:
				return True
		return False
		
	# Searches given word in a given matrix in all 8 directions
	def patternSearch(self, grid, word):
		# Rows and columns in given grid
		self.R = len(grid)
		self.C = len(grid[0])
		# Consider every point as starting point and search given word
		for row in range(self.R):
			for col in range(self.C):
				if self.search2D(grid, row, col, word):
					print("pattern found at ", f'{str(row)}, {str(col)}')
					

grid = ["GEEKSFORGEEKS",
		"GEEKSQUIZGEEK",
		"IDEQAPRACTICE"]
gfg = GFG()
gfg.patternSearch(grid, 'GEEKS')
print('')
gfg.patternSearch(grid, 'EEE')

```

## Boyer Moore Algorithm for Pattern Searching.

```python
"""
Input:  txt[] = "THIS IS A TEST TEXT"
        pat[] = "TEST"
Output: Pattern found at index 10

Input:  txt[] =  "AABAACAADAABAABA"
        pat[] =  "AABA"
Output: Pattern found at index 0
        Pattern found at index 9
        Pattern found at index 12
"""


NO_OF_CHARS = 256

def badCharHeuristic(string, size):

	# Initialize all occurrence as -1
	badChar = [-1]*NO_OF_CHARS

	# Fill the actual value of last occurrence
	for i in range(size):
		badChar[ord(string[i])] = i;

	# return initialized list
	return badChar

def search(txt, pat):
	m = len(pat)
	n = len(txt)

	# create the bad character list by calling the preprocessing function badCharHeuristic() for given pattern
	badChar = badCharHeuristic(pat, m)

	# s is shift of the pattern with respect to text
	s = 0
	while (s <= n-m):
		j = m-1

		# Keep reducing index j of pattern while characters of pattern and text are matching at this shift s
		while j>=0 and pat[j] == txt[s+j]:
			j -= 1

		# If the pattern is present at current shift, then index j will become -1 after the above loop
		if j<0:
			print(f"Pattern occur at shift = {s}")

				# Shift the pattern so that the next character in text 	aligns with the last occurrence of it in pattern. The condition s+m < n is necessary for the case when pattern occurs at the end of text
			
			s += (m-badChar[ord(txt[s+m])] if s+m<n else 1)
		else:

			# Shift the pattern so that the bad character in text aligns with the last occurrence of it in pattern. The max function is used to make sure that we get a positive shift. We may get a negative shift if the last occurrence of bad character in pattern is on the right side of the current character.
			s += max(1, j-badChar[ord(txt[s+j])])


txt = "ABAAABCD"
pat = "ABC"
search(txt, pat)
```

## Converting Roman Numerals to Decimal

```python

def romanToInt(s):
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            number += translations[char]
        print(number)
         
romanToInt('MCMIV')
```

## Longest Common Prefix

```python
def LCP(X, Y):
    i = j = 0
    while i < len(X) and j < len(Y):
        if X[i] != Y[j]:
            break
        i = i + 1
        j = j + 1
    return X[:i]
 
 
# Function to find the longest common prefix (LCP) between a given set of strings
def findLCP(words):
    prefix = words[0]
    for s in words:
        prefix = LCP(prefix, s)
    return prefix
 
  
words = ['techie delight', 'tech', 'techie', 'technology', 'technical']
print('The longest common prefix is', findLCP(words))
```

## Number of flips to make binary string alternate

```python
"""
Input : str = “001”
Output : 1
Minimum number of flips required = 1
We can flip 1st bit from 0 to 1 

Input : str = “0001010111”
Output : 2
Minimum number of flips required = 2
We can flip 2nd bit from 0 to 1 and 9th 
bit from 1 to 0 to make alternate 
string “0101010101”.
"""

def flip( ch):
	return '1' if (ch == '0') else '0'

# Utility method to get minimum flips when alternate string starts with expected char
def getFlipWithStartingCharcter(str, expected):
	flipCount = 0
	for i in range(len( str)):
		# if current character is not expected, increase flip count
		if (str[i] != expected):
			flipCount += 1

		# flip expected character each time
		expected = flip(expected)
	return flipCount

def minFlipToMakeStringAlternate(str):	
	return min(getFlipWithStartingCharcter(str, '0'), getFlipWithStartingCharcter(str, '1'))


str1 = "0001010111"
print(minFlipToMakeStringAlternate(str1))
```

## Find the first repeated word in string.

```python

from collections import Counter

def firstRepeatedWord(sentence):
	lis = list(sentence.split(" "))
	frequency = Counter(lis)
	for i in lis:
		if(frequency[i] > 1):
			return i

sentence = "Vikram had been saying that he had been there"
print(firstRepeatedWord(sentence))
```

## Minimum number of swaps for bracket balancing.

```python
"""Input  : []][][
Output : 2
First swap: Position 3 and 4
[][]][
Second swap: Position 5 and 6
[][][]

Input  : [[][]]
Output : 0
The string is already balanced.
"""
def swapCount(s):
	swap = 0
	imbalance = 0;
	
	for i in s:
		if i == '[':
			imbalance -= 1
		else:
			imbalance += 1
			if imbalance > 0:
				swap += imbalance
	return swap

s = "[]][][";
print(swapCount(s))
s = "[[][]]";
print(swapCount(s))

```

## Find the longest common subsequence between two strings.

```python
"""
LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH” of length 3. 
LCS for input Sequences “AGGTAB” and “GXTXAYB” is “GTAB” of length 4.
"""

def lcs(X, Y, m, n):
	L = [[0 for _ in range(n+1)] for _ in range(m+1)]
	# Following steps build L[m+1][n+1] in bottom up fashion. Note that L[i][j] contains length of LCS of X[0..i-1] and Y[0..j-1]
	for i in range(m+1):
		for j in range(n+1):
			if i == 0 or j == 0:
				L[i][j] = 0
			elif X[i-1] == Y[j-1]:
				L[i][j] = L[i-1][j-1] + 1
			else:
				L[i][j] = max(L[i-1][j], L[i][j-1])

		# Create a string variable to store the lcs string
	lcs = ""

	# Start from the right-most-bottom-most corner and one by one store characters in lcs[]
	i = m
	j = n
	while i > 0 and j > 0:

		# If current character in X[] and Y are same, then current character is part of LCS
		if X[i-1] == Y[j-1]:
			lcs += X[i-1]
			i -= 1
			j -= 1

		# If not same, then find the larger of two and go in the direction of larger value
		elif L[i-1][j] > L[i][j-1]:
			i -= 1

		else:
			j -= 1

	# We traversed the table in reverse order LCS is the reverse of what we got
	lcs = lcs[::-1]
	print(f"LCS of {X} and {Y} is {lcs}")


X = "AGGTAB"
Y = "GXTXAYB"
m = len(X)
n = len(Y)
lcs(X, Y, m, n)
```

## Program to generate all possible valid IP addresses from given  string.

```python
"""
Input: 25525511135
Output: [“255.255.11.135”, “255.255.111.35”]
Explanation:
These are the only valid possible
IP addresses.

"""

def solve(s, i, j, level, temp, res):
	if (i == (j + 1) and level == 5):
		res.append(temp[1:])

	# Digits of a number ranging 0-255 can lie only between  0-3
	k = i
	while (k < i + 3 and k <= j):
		ad = s[i: k + 1]

		# Return if string starting with '0' or it is greater than 255.
		if ((s[i] == '0' and len(ad) > 1) or int(ad) > 255):
			return

		# Recursively call for another level.
		solve(s, k + 1, j, level + 1, f'{temp}.{ad}', res)

		k += 1


s = "25525511135"
n = len(s)
ans = []
solve(s, 0, n - 1, 1, "", ans)
for s in ans:
	print(s)
```

## Write a program to find the smallest window that contains all characters of string itself.

```python
"""
Input: aabcbcdbca
Output: dbca
Explanation: 
Possible substrings= {aabcbcd, abcbcd, 
bcdbca, dbca....}
Of the set of possible substrings 'dbca' 
is the shortest substring having all the 
distinct characters of given string. 

Input: aaab
Output: ab
Explanation: 
Possible substrings={aaab, aab, ab}
Of the set of possible substrings 'ab' 
is the shortest substring having all 
the distinct characters of given string.    
"""
# Python program to find the smallest
# window containing
# all characters of a pattern
from collections import defaultdict

MAX_CHARS = 256

def findSubString(strr):
	n = len(strr)
	if n <= 1:
		return strr
	dist_count = len(set(list(strr)))
	curr_count = defaultdict(lambda: 0)
	count = 0
	start = 0
	min_len = n

	for j in range(min_len):
		curr_count[strr[j]] += 1

		# If any distinct character matched, then increment count
		if curr_count[strr[j]] == 1:
			count += 1

		# Try to minimize the window i.e., check if any character is occurring more no. of times than its occurrence in pattern, if yes then remove it from starting and also remove the useless characters.
		if count == dist_count:
			while curr_count[strr[start]] > 1:
				curr_count[strr[start]] -= 1
				start += 1

			# Update window size
			len_window = j - start + 1
			if min_len > len_window:
				min_len = len_window
				start_index = start

	return str(strr[start_index: start_index + min_len])


print(f'Smallest window containing all distinct characters is: {findSubString("aabcbcdbca")}')
```

## Minimum characters to be added at front to make string palindrome

```python
"""
Input  : str = "ABC"
Output : 2
We can make above string palindrome as "CBABC"
by adding 'B' and 'C' at front.

Input  : str = "AACECAAAA";
Output : 2
We can make above string palindrome as AAAACECAAAA
by adding two A's at front of string.
"""

def ispalindrome(s):
    l = len(s)
    i = 0
    j = l - 1
    while i <= j:
        if(s[i] != s[j]):
            return False
        i += 1
        j -= 1
    return True
 
s = "BABABAA"
cnt = 0
flag = 0
while s != "":
    if(ispalindrome(s)):
        flag = 1
        break
    else:
        cnt += 1
        # erase the last element of the string
        s = s[:-1]

# print the number of insertion at front
if(flag):
    print(cnt)
```

## Find the smallest window in a string containing all characters of another string

```python
"""
nput: string = “this is a test string”, pattern = “tist” 
Output: Minimum window is “t stri” 
Explanation: “t stri” contains all the characters of pattern.

Input: string = “geeksforgeeks”, pattern = “ork” 
Output: Minimum window is “ksfor”
"""


def smallestWindow(s, p):
	n = len(s)
	if n < len(p):
		return -1
	mp = [0]*256
	# Starting index of ans
	start = 0
	# Answer, Length of ans
	ans = n + 1
	cnt = 0
	# creating map
	for i in p:
		mp[ord(i)] += 1
		if mp[ord(i)] == 1:
			cnt += 1
	i = 0

	# Traversing the window
	for j in range(n):
		mp[ord(s[j])] -= 1
		if mp[ord(s[j])] == 0:
			cnt -= 1
			while cnt == 0:
				if ans > j - i + 1:
					ans = j - i + 1
					start = i

				# Sliding I
				# Calculation for removing I
				mp[ord(s[i])] += 1
				if mp[ord(s[i])] > 0:
					cnt += 1
				i += 1
	if ans > n:
		return "-1"
	return s[start:start+ans]


s = "ADOBECODEBANC"
p = "ABC"
result = smallestWindow(s, p)
print("Smallest window that contain all character :", result)
```

## Recursively remove all adjacent duplicates

```python
def removeDuplicates(S):
	n = len(S)
	# We don't need to do anything for empty or single character string.
	if (n < 2):
		return
	# j is used to store index is result string (or index of current distinct character)
	j = 0
	
	# Traversing string
	for i in range(n):
		# If current character S[i] is different from S[j]
		if (S[j] != S[i]):
			j += 1
			S[j] = S[i]
	
	# Putting string termination character.
	j += 1
	S = S[:j]
	return S
	

S1 = "geeksforgeeks"
S1 = list(S1.rstrip())
S1 = removeDuplicates(S1)
print(*S1, sep = "")

S2 = "aabcca"
S2 = list(S2.rstrip())
S2 = removeDuplicates(S2)
print(*S2, sep = "")
```

## String matching where one string contains wildcard characters

```python
def match(first, second):

	# If we reach at the end of both strings, we are done
	if len(first) == 0 and len(second) == 0:
		return True

	# Make sure to eliminate consecutive '*'
	if len(first) > 1 and first[0] == '*':
		i = 0
		while i+1 < len(first) and first[i+1] == '*':
			i += 1
		first = first[i:]

	# Make sure that the characters after '*' are present
	# in second string. This function assumes that the first
	# string will not contain two consecutive '*'
	if len(first) > 1 and first[0] == '*' and len(second) == 0:
		return False

	# If the first string contains '?', or current characters
	# of both strings match
	if (len(first) > 1 and first[0] == '?') or (len(first) != 0
												and len(second) != 0 and first[0] == second[0]):
		return match(first[1:], second[1:])

	# If there is *, then there are two possibilities
	# a) We consider current character of second string
	# b) We ignore current character of second string.
	if len(first) != 0 and first[0] == '*':
		return match(first[1:], second) or match(first, second[1:])

	return False


def test(first, second):
	if match(first, second):
		print("Yes")
	else:
		print("No")


test("g*ks", "geeks") # Yes
test("ge?ks*", "geeksforgeeks") # Yes
test("g*k", "gee") # No because 'k' is not in second
test("*pqrs", "pqrst") # No because 't' is not in first
test("abc*bcd", "abcdhghgbcd") # Yes
test("abc*c?d", "abcd") # No because second must have 2 instances of 'c'
test("*c*d", "abcd") # Yes
test("*?c*d", "abcd") # Yes
test("geeks**", "geeks") # Yes
```

## Function to find Number of customers who could not get a computer

```python
"""
Write a function “runCustomerSimulation” that takes following two inputs 

An integer ‘n’: total number of computers in a cafe and a string: 
A sequence of uppercase letters ‘seq’: Letters in the sequence occur in pairs. The first occurrence indicates the arrival of a customer; the second indicates the departure of that same customer. 
A customer will be serviced if there is an unoccupied computer. No letter will occur more than two times. 
Customers who leave without using a computer always depart before customers who are currently using the computers. There are at most 20 computers per cafe.

For each set of input the function should output a number telling how many customers, if any walked away without using a computer. Return 0 if all the customers were able to use a computer.
runCustomerSimulation (2, “ABBAJJKZKZ”) should return 0
runCustomerSimulation (3, “GACCBDDBAGEE”) should return 1 as ‘D’ was not able to get any computer
runCustomerSimulation (3, “GACCBGDDBAEE”) should return 0
runCustomerSimulation (1, “ABCBCA”) should return 2 as ‘B’ and ‘C’ were not able to get any computer.
runCustomerSimulation(1, “ABCBCADEED”) should return 3 as ‘B’, ‘C’ and ‘E’ were not able to get any computer.
"""

MAX_CHAR = 26

# n is number of computers in cafe.
# 'seq' is given sequence of customer entry, exit events
def runCustomerSimulation(n, seq):

	# seen[i] = 0, indicates that customer 'i' is not in cafe
	# seen[1] = 1, indicates that customer 'i' is in cafe but computer is not assigned yet.
	# seen[2] = 2, indicates that customer 'i' is in cafe and has occupied a computer.
	seen = [0] * MAX_CHAR

	# Initialize result which is number of customers who could not get any computer.
	res = 0
	occupied = 0 # To keep track of occupied

	# Traverse the input sequence
	for i in range(len(seq)):

		# Find index of current character in seen[0...25]
		ind = ord(seq[i]) - ord('A')

		# If first occurrence of 'seq[i]'
		if seen[ind] == 0:

			# set the current character as seen
			seen[ind] = 1

			# If number of occupied computers is less than n, then assign a computer to new customer
			if occupied < n:
				occupied+=1

				# Set the current character as occupying a computer
				seen[ind] = 2

			# Else this customer cannot get a computer, increment
			else:
				res+=1

		# If this is second occurrence of 'seq[i]'
		else:
			# Decrement occupied only if this customer was using a computer
			if seen[ind] == 2:
				occupied-=1
			seen[ind] = 0

	return res


print (runCustomerSimulation(2, "ABBAJJKZKZ"))
print (runCustomerSimulation(3, "GACCBDDBAGEE"))
print (runCustomerSimulation(3, "GACCBGDDBAEE"))
print (runCustomerSimulation(1, "ABCBCA"))
print (runCustomerSimulation(1, "ABCBCADEED"))
```

## Transform One String to Another using Minimum Number of Given Operation

```python
"""
Input:  A = "ABD", B = "BAD"
Output: 1
Explanation: Pick B and insert it at front.

Input:  A = "EACBD", B = "EABCD"
Output: 3
Explanation: Pick B and insert at front, EACBD => BEACD
             Pick A and insert at front, BEACD => ABECD
             Pick E and insert at front, ABECD => EABCD
"""

# Function to find minimum number of operations required  transform A to B
def minOps(A, B):
	m = len(A)
	n = len(B)

	# This part checks whether conversion is possible or not
	if n != m:
		return -1

	count = [0] * 256

	for i in range(n):	 # count characters in A
		count[ord(B[i])] += 1
	for i in range(n):	 # subtract count for every char in B
		count[ord(A[i])] -= 1
	for i in range(256): # Check if all counts become 0
		if count[i]:
			return -1

	# This part calculates the number of operations required
	res = 0
	i = n-1
	j = n-1
	while i >= 0:
	
		# if there is a mismatch, then keep incrementing result 'res' until B[j] is not found in A[0..i]
		while i>= 0 and A[i] != B[j]:
			i -= 1
			res += 1

		# if A[i] and B[j] match
		if i >= 0:
			i -= 1
			j -= 1
	return res

A = "EACBD"
B = "EABCD"
print(f"Minimum number of operations required is {str(minOps(A,B))}")
```

## Check if two given strings are isomorphic to each other

```python
"""
Input:  str1 = "aab", str2 = "xxy"
Output: True
'a' is mapped to 'x' and 'b' is mapped to 'y'.

Input:  str1 = "aab", str2 = "xyz"
Output: False
One occurrence of 'a' in str1 has 'x' in str2 and 
other occurrence of 'a' has 'y'.
"""

def areIsomorphic(str1, str2):
	#initializing a dictionary to store letters from str1 and str2 as key value pairs
	charCount = {}
	#initially setting c to "a"
	c = "a"
	#iterating over str1 and str2
	for i in range(len(str1)):
		#if str1[i] is a key in charCount
		if str1[i] in charCount:
			c = charCount[str1[i]]
			if c != str2[i]:
				return False
		#if str2[i] is not a value in charCount
		elif str2[i] not in charCount.values():
			charCount[str1[i]] = str2[i]
		else:
			return False
	return True
		

str1 = "aac"
str2 = "xxy"
if (len(str1) == len(str2) and areIsomorphic(str1, str2)):
	print("Is Isomorphic")
else:
	print("Is Not Isomorphic")
```

## Recursively print all sentences that can be formed from list of word lists

```python
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
```
