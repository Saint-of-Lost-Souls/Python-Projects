# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 15:26:22 2021

@author: Shade
"""

# LISTS #

# for i in range(len('name of variable')): length of 
# doesnt have to be i

data = [53,76,25,98,56,42,69,81] # square brackets mean a list
data_1 = [] # empty list

print(data[0]) # prints out the first index of a list
print(data[6])
print(data[-1]) # prints out last number
print(data[0:5]) # prints out 0-5
print(data[:5]) # same as above. Code will always start from 0 unless you say otherwise

for num in data: # num = i = banana
    print(num, end=" ") # prints out all numbers in 'data list' on one line
    
total = 0
for num in data:
    total = total + num # 0+53, then 53+76, and so on
print("The sum total of 'data' is:", total)

total_2 = sum(data)
print("total_2 =",total_2) # Python function of above

find_max = 0
for num in data:
    if num > find_max: # if num is greater than 0, change max to this number, and so on
        find_max = num
print("Max value is", find_max) # find max will keep running until it finds the highest value. This cannot work with negative numbers

print("Max value using Python function 'max()'", max(data)) # Python function of above

my_list = [1, 11, 21, 31, 41, 51]
for i in range(5):
    print(my_list[i]) # print each index
    print(my_list[i+1])
    print()

# BUBBLE SORTING # 

data_copy = data[:] # this creates a new variable, a copy of 'data' [:] means entire list
for i in range(len(data_copy)): # controls how many times to go through the list
    for j in range(0,len(data_copy)-i-1): # -1 means that when you get to the end, do not try and compare the number on the right -i means that every additional time it runs, there is no need to compare it to the last number
        if data_copy[j] > data_copy[j+1]: # if the value you are on is greater than the one on the right, switch it
            data_copy[j],data_copy[j+1] = data_copy[j+1],data_copy[j]
print(data_copy)

print(sorted(data)) # Python function of above

# COMMON LIST METHODS #

my_list = [34, 76, 58]
print(my_list)
my_list.append(100) # adds 1 value
print(my_list)
my_list.remove(34)# removes 34
print(my_list) 
my_list.reverse()# reverses the indexes
print(my_list) 
my_list.extend([67,68,69]) # adds multiple values
print(my_list)
print(my_list.index(67)) # prints the index value of 67

# 1
# Calculate the first 20 Fibonacci numbers and put them in a list

n = 20 # Number of Fib nums required

a = 0 # Set a and b to be the first 2 nums in sequence
b = 1

fib_nums = [] # create an empty list to store the numbers

for i in range(n): # create a FOR loop, repeat 'n' times
    fib_nums.append(a) # add to list- first loop 0, second loop 1 etc
    a,b = b,a+b # first loop, 0,1 = 1, 0+1, second loop 1,2 = 2, 1+2
print(f"The first {n} Fibonacci numbers are {fib_nums}")

# 2
# Write some code that will determine all odd an even numbers between 1 and 100
# Put the numbers in their respective lists
# Instantiate- create- empty lists
n = 100 

odds = []
evens = []

for number in range(n+1): # 1
    if not number % 2: # If the number is divisble by without a remainder, because % is a remainder
        evens.append(number)
    else:
        odds.append(number) # put other numbers here
        print(f"The evens are {evens}")
        print(f"The odds are {odds}")
        
my_list = [[1,2,3],[4,5,6],[7,8,9]] # lists can contain lists
print(my_list[2]) # prints the 3rd list

print(my_list[1][1]) # prints 2nd list, 1st index      

l = [x**2 for x in range(1,10)] # creates a list of 10 square numbers
print(l)  

m = [] # create an empty list
for x in range(1,11): # find the numbers
    m.append(x**2) # square them and put them in this, list comprehension
print(m)

# my_list_1 = [1,2,3,4,5]
# my_list_2 = ["a","b","c","d","e"]
# joined = list(zip(my_list_1, my_list_2)) # combines both lists
# print(f"The result of the zip function is {joined} it is of type {type(joined)}")

# cat,banana = zip(*joined) # unpacks the 'joined' list into two separate tuples
# print(cat) # result is a tuple
# print(banana)