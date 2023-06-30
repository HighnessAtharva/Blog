---
title: "DSA in Python - Elementry Algos"
date: 2022-07-09T23:18:34+05:30
draft: false
cover: 
    image: blog/dsa/Elementary.webp
    alt: elementary
    caption: Learn Elementary Algorithms in Python
description: "Master FAANG Interviews with the most frequently asked Elementary problems with solutions and comprehensive explanations. Boost Skills, Get Paid!"
tags: ["python"] 
---

## Free Preview - 5 Elementary Problems

### Check Leap Year

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

### Generate Random Number

```python
import random
print(random.randint(0,9))
```

### Largest No of 3

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

### Prime Number

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

### Factorial

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

## Buy the Interview Guide

{{< gumroad "https://highnessatharva.gumroad.com/l/dsa-python-elementary" "/blog/gumroad-marketing.webp" >}}