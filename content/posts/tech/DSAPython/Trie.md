---
title: "DSA in Python - Trie"
date: 2022-07-08T13:18:34+05:30
draft: true
cover: 
    image: blog/dsa/trie.jpg
    alt: Trie
    caption: Learn Trie Algorithms in Python
tags: ["python"] 

---

- [Construct a trie from scratch](#construct-a-trie-from-scratch)
- [Find shortest unique prefix for every word in a given list](#find-shortest-unique-prefix-for-every-word-in-a-given-list)
- [Word Break Problem | (Trie solution)](#word-break-problem--trie-solution)
- [Given a sequence of words, print all anagrams together](#given-a-sequence-of-words-print-all-anagrams-together)
- [Print unique rows in a given boolean matrix](#print-unique-rows-in-a-given-boolean-matrix)

## Construct a trie from scratch

```python
class TrieNode:
    def __init__(self):
        self.children = [None]*26
        # isEndOfWord is True if node represent the end of the word
        self.isEndOfWord = False
  
class Trie:
    def __init__(self):
        self.root = self.getNode()
  
    def getNode(self):
        # Returns new trie node (initialized to NULLs)
        return TrieNode()
  
    def _charToIndex(self,ch):
        # private helper function. 
        # Converts key current character into index use only 'a' through 'z' and lower case
        return ord(ch)-ord('a')
  
  
    def insert(self,key):
        
        # If not present, inserts key into trie
        # If the key is prefix of trie node, just marks leaf node
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
  
            # if current character is not present
            if not pCrawl.children[index]:
                pCrawl.children[index] = self.getNode()
            pCrawl = pCrawl.children[index]
  
        # mark last node as leaf
        pCrawl.isEndOfWord = True
  
    def search(self, key):
          
        # Search key in the trie
        # Returns true if key presents in trie, else false
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not pCrawl.children[index]:
                return False
            pCrawl = pCrawl.children[index]
  
        return pCrawl.isEndOfWord
  

def constructTrie():
  
    # Input keys (use only 'a' through 'z' and lower case)
    keys = ["the","a","there","answer","any", "by","their", "these"]
    output = ["Not present in trie", "Present in trie"]
  
    # Trie object
    t = Trie()
  
    # Construct trie
    for key in keys:
        t.insert(key)
  
    # Search for different keys
    print("the->",output[t.search("the")])
    print("these->",output[t.search("these")])
    print("their->",output[t.search("their")])
    print("thaw->",output[t.search("thaw")])
  
if __name__ == '__main__':
    constructTrie()
```

## Find shortest unique prefix for every word in a given list

```python
"""
Input:  [AND, BONFIRE, BOOL, CASE, CATCH, CHAR]
Output: [A, BON, BOO, CAS, CAT, CH]
Explanation:
A can uniquely identify AND
BON can uniquely identify BONFIRE
BOO can uniquely identify BOOL
CAS can uniquely identify CASE
CAT can uniquely identify CATCH
CH can uniquely identify CHAR
"""
# A class to store a Trie node
class TrieNode:
    def __init__(self):
        # each node stores a dictionary to its child nodes
        self.child = {}
 
        # keep track of the total number of times the current node is visited
        # while inserting data in Trie
        self.freq = 0
 
 
# Function to insert a given string into a Trie
def insert(root, word):
 
    # start from the root node
    curr = root
    for c in word:
        # create a new node if the path doesn't exist
        curr.child.setdefault(c, TrieNode())
 
        # increment frequency
        curr.child[c].freq += 1
 
        # go to the next node
        curr = curr.child[c]
 
 
# Function to recursively traverse the Trie in a preorder fashion and
# print the shortest unique prefix for each word in the Trie
def printShortestPrefix(root, word_so_far):
    if root is None:
        return
 
    # print `word_so_far` if the current Trie node is visited only once
    if root.freq == 1:
        print(word_so_far)
        return
 
    # recur for all child nodes
    for k, v in root.child.items():
        printShortestPrefix(v, word_so_far + k)
 
 
# Find the shortest unique prefix for every word in a given array
def findShortestPrefix(words):
 
    # construct a Trie from the given items
    root = TrieNode()
    for s in words:
        insert(root, s)
 
    # Recursively traverse the Trie in a preorder fashion to list all prefixes
    printShortestPrefix(root, '')
 
 
if __name__ == '__main__':
    words = ['AND', 'BONFIRE', 'BOOL', 'CASE', 'CATCH', 'CHAR']
    findShortestPrefix(words)
```

## Word Break Problem | (Trie solution)

```python
# Currently, Trie supports lowercase English characters. So, the character size is 26.
CHAR_SIZE = 26
 
 
# A class to store a Trie node
class Node:
    next = [None] * CHAR_SIZE
    exist = False       # true when the node is a leaf node
 
 
# Iterative function to insert a string into a Trie
def insertTrie(head, s):
 
    # start from the root node
    node = head
 
    # do for each character in the string
    for c in s:
 
        index = ord(c) - ord('a')
 
        # create a new node if the path doesn't exist
        if node.next[index] is None:
            node.next[index] = Node()
 
        # go to the next node
        node = node.next[index]
 
    # mark the last node as a leaf
    node.exist = True
 
 
# Function to determine if a string can be segmented into space-separated
# sequence of one or more dictionary words
def wordBreak(head, s):
 
    # get the length of the string
    n = len(s)
 
    # `good[i]` is true if the first `i` characters of `s` can be segmented
    good = [None] * (n + 1)
    good[0] = True      # base case
 
    for i in range(n):
        if good[i]:
            node = head
            for j in range(i, n):
                if node is None:
                    break
 
                index = ord(s[j]) - ord('a')
                node = node.next[index]
 
                # we can make [0, i] using our known decomposition
                # and [i+1, j] using this string in a Trie
                if node and node.exist:
                    good[j + 1] = True
 
    # `good[n]` would be true if all characters of `s` can be segmented
    return good[n]
 
 
if __name__ == '__main__':
 
    # List of strings to represent a dictionary
    words = ['self', 'th', 'is', 'famous', 'word', 'break', 'b', 'r', 'e', 'a', 'k', 'br', 'bre', 'brea', 'ak', 'prob', 'lem']
 
    # given string
    s = 'wordbreakproblem'
 
    # create a Trie to store the dictionary
    t = Node()
    for word in words:
        insertTrie(t, word)
 
    # check if the string can be segmented or not
    if wordBreak(t, s):
        print('The string can be segmented')
    else:
        print('The string can\'t be segmented')
```

## Given a sequence of words, print all anagrams together

```python
class TrieNode:
    def __init__(self):
        # each node stores a dictionary to its child nodes
        self.child = {}
 
        # stores anagrams in the leaf node
        self.words = []
 
 
# Function to insert a string into a Trie
def insert(root, word, originalWord):
 
    # start from the root node
    curr = root
    for c in word:
        # create a new node if the path doesn't exist
        curr.child.setdefault(c, TrieNode())
        # go to the next node
        curr = curr.child[c]
 
    # anagrams will end up at the same leaf node
    curr.words.append(originalWord)
 
 
# A recursive function that traverses a Trie in preorder fashion and
# prints all anagrams together
def printAnagrams(root):
 
    # base case
    if root is None:
        return
 
    # print the current word
    if len(root.words) > 1:
        print(root.words)
 
    # recur for all child nodes
    for child in root.child.values():
        printAnagrams(child)
 
 
# Function to group anagrams from a given list of words
def groupAnagrams(words):
 
    # construct an empty trie
    root = TrieNode()
 
    # do for each word
    for word in words:
        # Sort the characters of the current word and insert it into the Trie.
        # Note that the original word gets stored on the leaf
        insert(root, ''.join(sorted(word)), word)
 
    # print all anagrams together
    printAnagrams(root)
 
 
words = ['auctioned', 'actors', 'altered', 'streaming', 'related', 'education', 'aspired', 'costar', 'despair', 'mastering', 'act','cat','tac'
]
groupAnagrams(words)
```

## Print unique rows in a given boolean matrix

```python
# Given a binary matrix of M X N of integers, you need to return only unique rows of binary array
ROW = 4
COL = 5

def findUniqueRows(M):
    
    # Traverse through the matrix
    for i in range(ROW):
        flag = 0

        # Check if there is similar column is already printed, i.e if i and jth column match.
        for j in range(i):
            flag = 1

            for k in range(COL):
                if (M[i][k] != M[j][k]):
                    flag = 0

            if (flag == 1):
                break

        # If no row is similar
        if (flag == 0):
            
            # Print the row
            for j in range(COL):
                print(M[i][j], end = " ")
            print()    


M = [ [ 0, 1, 0, 0, 1 ],
      [ 1, 0, 1, 1, 0 ],
      [ 0, 1, 0, 0, 1 ],
      [ 1, 0, 1, 0, 0 ] ]
findUniqueRows(M)


```
