# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 15:23:50 2021

@author: Shade
"""

# FOR LOOPS # 
# do things a certain number of times
# for i in range(len('name of variable')): length of variable
# i iterates through numbers
# char iterates through string

for i in range(10): # 'i' iterates through a range, creates a series of alues from 0-9
    print(i)
    
for i in range(10):
    print(i,end=" ") # this tells the code that the end of a line is actually just a space, putting the answers on one line
    
for i in range(1,10): # the code will start at 1, not 0
    print(i,end=" ")

for i in range(1,11): # ranges are not inclusive, this will give 1-10
    print(i,end=" ")
    
for i in range(0,101,4): # 1-100, going up in 4's- start, stop, step
    print(i, end=" ")
    
for i in range(100,0,-5): # 100-1, going down in 5's, '-' tells the code to go backwards
    print(i,end=" ")
    
word = "Python"

for i in word:
    print(i) # prints out letters after the other

for char in word: # char iterates through a string. You can call this anything, see below
    print(char, end=" ")
    
for cat in word: # use an iterator that makes sense to you. Cat is just silly
    print(cat)

word = "bunny"

for banana in word:
    print(banana, end=" ") # I give up    
    
# 1
# SPELL OUT A WORD BACKWARDS    
word = input("Please enter a word:>")
reverse_string = ""
for char in word:
    reverse_string = char + reverse_string
print(reverse_string)

print(word[::-1])
    
# 2
# Ask the user for a number between 1-12 then display the times table for that number
user_input = (input("Please enter a number between 1-12:>"))

while (not user_input.isdigit()) or (int(user_input) < 1 or (int(user_input) > 12)):
    print("Must be a number between 1-12.")
    user_input = ("Please enter a number between 1-12:>")
user_input = int(user_input)
print("=============================================")
print()
print(f"This is the {user_input} times table")
print()
for i in range(1,13):
    print(f"{i} x {user_input} = {i*user_input}")
    
# 3
# Modify above so that no input is required
for i in range(1,12):    
    print("=============================================")
    print()
    print(f"This is the {i} times table")
    print()
    for j in range(1,13):
        print(f"{j} x {i} = {j*i}")
        
# 4
# Write code that will calculate 15 factorial
n = 15
fact = 1
for i in range(1,n+1):
    fact = fact * i
print(fact)
    
# 5 
# Modify above to ask for user input
fact = 1
number = input("Please enter a number:>")

while (not number.isdigit()):
    print("I asked for a number, chuckles")
    number = input("Try again:>")
number = int(number)
for num in range(1,number+1):
    fact = fact * num
print(fact)

# 6
# Calculate the first 20 Fibonacci numbers and put them in a list
n = 20 # Number of Fib nums required

a = 0 # Set a and b to be the first 2 nums in sequence
b = 1

fib_nums = [] # create an empty list to store the numbers

for i in range(n): # create a FOR loop, repeat 'n' times
    fib_nums.append(a) # add to list- first loop 0, second loop 1 etc
    a,b = b,a+b # first loop, 0,1 = 1, 0+1, second loop 1,2 = 2, 1+2
print(f"The first {n} Fibonacci numbers are {fib_nums}")

# 7
# Create this picture 'F'
star = "*"
for column in range(1,7):
    for row in range(1,6):
        if column == 1 and row < 6:
            print("*",end=" ")
        elif column == 2 and row == 1:
            print()
            print("*")
        elif column == 3 and row < 5:
            print("*",end=" ")
        elif column == 4 and row == 1:
            print()
            print("*")
        elif column == 5 and row == 1:
            print("*")
        elif column == 6 and row == 1:
            print("*")
            
# 8
# Write some code that will determine all odd an even numbers between 1 and 100
# Put the numbers in their respective lists
# Instantiate- create- empty lists
n = 100 

odds = []
evens = []

for number in range(n+1): # 1
    if not number % 2: # If the number is divisible by 2 with no remainder
        evens.append(number)
    else:
        odds.append(number) #put other numbers here
        print(f"The evens are {evens}")
        print(f"The odds are {odds}")
                        
