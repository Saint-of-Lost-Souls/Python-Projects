# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 15:58:28 2021

@author: Shade
"""

# Modulus gives you the remainder of the result after division #
# 10 % 2 = 0 because 2 goes into 10 without a remainder
# 11 % 2 = 1 because the answer is 5.1
# 10 % 4 = 2 because the answer is 2.2

# FIZZBUZZ #

n = 100
for i in range(1,n+1): #between 1, 101
    if i % 3 == 0 and i % 5 == 0: #if a number is divisible by 3 & 5 with a remainder of 0, print FizzBuzz
        print(i, "FizzBuzz!")
    elif i % 5 == 0:
        print(i, "Buzz")
    elif i % 3 == 0:
        print(i, "Fizz")
    else:
        print(i)
        
# Order is very important

# 1
# Write some code that will determine all odd an even numbers between 1 and 100
# Put the numbers in their respective lists
# Instantiate- create- empty lists
n = 100 

odds = []
evens = []

for number in range(n+1): #1
    if not number % 2: #If the number is divisible by 2
        evens.append(number)
    else:
        odds.append(number) #put other numbers here
        print(f"The evens are {evens}")
        print(f"The odds are {odds}")
            