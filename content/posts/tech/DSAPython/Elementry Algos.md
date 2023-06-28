---
title: "DSA in Python - Elementry Algos"
date: 2022-07-09T23:18:34+05:30
draft: true
cover: 
    image: blog/dsa/elementary.jpg
    alt: elementary
    caption: Learn Elementary Algorithms in Python
tags: ["python"] 

---

- [Check Leap Year](#check-leap-year)
- [Generate Random Number](#generate-random-number)
- [Largest No of 3](#largest-no-of-3)
- [Prime Number](#prime-number)
- [Factorial](#factorial)
- [Prime Number Intervals](#prime-number-intervals)
- [Fibonacci Sequence](#fibonacci-sequence)
- [Armstrong Number](#armstrong-number)
- [Decimal to Binary/Hexadecimal/Octal](#decimal-to-binaryhexadecimaloctal)
- [GCD](#gcd)
- [LCM](#lcm)
- [Factorial Using Recursion](#factorial-using-recursion)
- [10 Triange Pattern Programs](#10-triange-pattern-programs)

## Check Leap Year

```python

year = 2000

# divided by 100 means century year (ending with 00) century year divided by 400 is leap year
if (year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year".format(year))

# not divided by 100 means not a century year year divided by 4 is a leap year
elif (year % 4 ==0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))

# if not divided by both 400 (century year) and 4 (not century year) year is not leap year
else:
    print("{0} is not a leap year".format(year))
```

## Generate Random Number

```python
import random
print(random.randint(0,9))
```

## Largest No of 3

```python
num1 = 10
num2 = 14
num3 = 12

if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The largest number is", largest)
```

## Prime Number

```python
num = 29
# define a flag variable
flag = False

# prime numbers are greater than 1
if num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break

# check if flag is True
if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")
```

## Factorial

```python

num = 7
factorial = 1

# check if the number is negative, positive or zero
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)
```

## Prime Number Intervals

```python
lower = 900
upper = 1000

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
```

## Fibonacci Sequence
```python

nterms = int(input("How many terms? "))
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1
```

## Armstrong Number

```python
num = int(input("Enter a number: "))
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
```

## Decimal to Binary/Hexadecimal/Octal

```python
dec = 344

print("The decimal value of", dec, "is:")
print(bin(dec), "in binary.")
print(oct(dec), "in octal.")
print(hex(dec), "in hexadecimal.")

```

## GCD

```python
def compute_hcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i 
    return hcf

num1 = 54 
num2 = 24

print("The H.C.F. is", compute_hcf(num1, num2))
```

## LCM

```python
def compute_gcd(x, y):
   while(y):
       x, y = y, x % y
   return x

def compute_lcm(x, y):
   lcm = (x*y)//compute_gcd(x,y)
   return lcm

num1 = 54
num2 = 24 

print("The L.C.M. is", compute_lcm(num1, num2))
```

## Factorial Using Recursion

```python
def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)

num = 7

if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of", num, "is", recur_factorial(num))

```

## 10 Triange Pattern Programs

```python
"""
*
* *
* * *
* * * *
* * * * *
"""
rows = int(input("Enter number of rows: "))
for i in range(rows):
    for j in range(i+1):
        print("* ", end="")
    print("\n")



"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""

rows = int(input("Enter number of rows: "))
for i in range(rows):
    for j in range(i+1):
        print(j+1, end=" ")
    print("\n")


"""
A
B B
C C C
D D D D
E E E E E
"""
rows = int(input("Enter number of rows: "))
ascii_value = 65
for i in range(rows):
    for j in range(i+1):
        alphabet = chr(ascii_value)
        print(alphabet, end=" ")
    ascii_value += 1
    print("\n")

"""
* * * * *
* * * *
* * *
* *
*
"""
rows = int(input("Enter number of rows: "))
for i in range(rows, 0, -1):
    for j in range(0, i):
        print("* ", end=" ")
    print("\n")


"""
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
"""
rows = int(input("Enter number of rows: "))
for i in range(rows, 0, -1):
    for j in range(1, i+1):
        print(j, end=" ")
    print("\n")

"""
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
"""

rows = int(input("Enter number of rows: "))
k = 0
for i in range(1, rows+1):
    for space in range(1, (rows-i)+1):
        print(end="  ")
    while k!=(2*i-1):
        print("* ", end="")
        k += 1
    k = 0
    print()


"""
        1 
      2 3 2 
    3 4 5 4 3 
  4 5 6 7 6 5 4 
5 6 7 8 9 8 7 6 5
"""

rows = int(input("Enter number of rows: "))

k = 0
count=0
count1=0

for i in range(1, rows+1):
    for space in range(1, (rows-i)+1):
        print("  ", end="")
        count+=1
    
    while k!=((2*i)-1):
        if count<=rows-1:
            print(i+k, end=" ")
            count+=1
        else:
            count1+=1
            print(i+k-(2*count1), end=" ")
        k += 1
    
    count1 = count = k = 0
    print()

"""
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
"""

rows = int(input("Enter number of rows: "))

for i in range(rows, 1, -1):
    for space in range(0, rows-i):
        print("  ", end="")
    for j in range(i, 2*i-1):
        print("* ", end="")
    for j in range(1, i-1):
        print("* ", end="")
    print()


"""
           1
         1   1
       1   2   1
     1   3   3    1
   1  4    6   4   1
 1  5   10   10  5   1
"""

rows = int(input("Enter number of rows: "))
coef = 1

for i in range(1, rows+1):
    for space in range(1, rows-i+1):
        print(" ",end="")
    for j in range(0, i):
        if j==0 or i==0:
            coef = 1
        else:
            coef = coef * (i - j)//j
        print(coef, end = " ")
    print()

"""
1
2 3
4 5 6
7 8 9 10
"""
rows = int(input("Enter number of rows: "))
number = 1

for i in range(1, rows+1):
    for j in range(1, i+1):
        print(number, end=" ")
        number += 1
    print()

```
