# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 15:36:44 2021

@author: Shade
"""

#WHILE loops# go through a loop until a condition is true or not true

n = 10

while n > 0:
    print(n)
    n = n-1 # will keep decreasing n by 1 until it is no longer greater than 0, therefore the condition is FALSE
    # can create an infinite loop by commenting out last line, because the result will always be TRUE
    
user_input = int(input("Please enter the ages of class member. Type -1 to end:>"))
ages = [] # making an open list called ages
while user_input > 0:
    ages.append(user_input) #add user_input to the ages list
    user_input = int(input("The next age:>"))
print("The ages are", ages)

#Put a counter in a WHILE loop#

count= 0
class_names = []
name = input("Please enter a name, type n to stop:>")
while name != "n": #while name does not equal 'n'
    count +=1 #increase count by 1
    class_names.append(name) #add to class_names list
    print(f"{name} has been added.")
    name = input("Next name:>")
print(f"There are {count} people in the class, they are {class_names}")

# 1
# Ask the user for two numbers between 1-100. Then count from the lower number to the higher number,
num_1 = int(input("Please enter a number between 1-100:>"))
num_2 = int(input("Please enter a number between 1-100:>"))

while num_1 < 0 or num_2 < 0 or num_1 > 100 or num_2 > 100 or num_1 == num_2: # checking that the input was valid
    print("Numbers must be different values between 1-100. Please try again.")
    num_1 = int(input("Please enter a number between 1-100:>"))
    num_2 = int(input("Please enter a number between 1-100:>"))
    
if num_1 < num_2:
    for num in range(num_1, num_2+1): # finds the range between the two inputs
        print(num, end=" ")
else:
    for num in range(num_2, num_1+1):
        print(num, end=" ")
        
# 2
# Ask the user for a number between 1-12 then display the times table for that number
user_input = (input("Please enter a number between 1-12:>"))

while (not user_input.isdigit()) or (int(user_input) < 1 or (int(user_input) > 12)):
    print("Must be anumber between 1-12.")
    user_input = ("Please enter a number between 1-12:>")
user_input = int(user_input)
print("=============================================")
print()
print(f"This is the {user_input} times table")
print()
for i in range(1,13):
    print(f"{i} x {user_input} = {i*user_input}")
    
# 3
# Ask the user to iput a series of numbers then calculate the mean
user_input = input("Please enter a number or type exit to stop:>")
numbers = []
while user_input.lower() != "exit":
    while not user_input.isdigit():
        print("That is not a number! Numbers only please.")
        user_input("Please enter a number:>")
    numbers.append(int(user_input))
    user_input = input("Please enter another number:>")
total = 0
for i in numbers:
    total += i
print(f"Mean total is {total/len(numbers)}")

print(sum(numbers/len(numbers))) # Python function of above        