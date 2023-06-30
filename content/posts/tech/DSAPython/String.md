---
title: "DSA in Python - Strings"
date: 2022-07-09T13:14:34+05:30
draft: false
cover: 
    image: blog/dsa/String.webp
    alt: Strings
    caption: Learn String Algorithms in Python
description: "Master FAANG Interviews with the most frequently asked String problems with solutions and comprehensive explanations. Boost Skills, Get Paid!"
tags: ["python"] 
---

## Free Preview - 5 String Problems

### Check whether a String is Palindrome or not

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

### Find Duplicate characters in a string

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

### Write a Code to check whether one string is a rotation of another

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

### Write a Program to check whether a string is a valid shuffle of two strings or not

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

### Count and Say problem

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

### Write a program to find the longest Palindrome in a string.[ Longest palindromic Substring]

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

## Buy the Interview Guide

{{< gumroad "https://highnessatharva.gumroad.com/l/dsa-python-string" "/blog/gumroad-marketing.webp" >}}