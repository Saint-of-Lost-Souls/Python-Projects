# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 16:04:48 2021

@author: Shade
"""
# print("Hello World!")
# To create a function, write def (name of function) ()

# def hello(): #create the funtion
#     print("Hello World!") #what you want inside the function

# hello() # function call

# for i in range(5):
#     hello() # repeat hello world 5 times
    
# def hi(name):
#     print(f"Hello, {name}")
    
# hi("Shade")

# def hi_2(name="Shade"): # if no name is provided, it will default to shade
#     print(f"Hello, {name}!")
    
# hi_2("lee") # keyword arguemnt

# Put this into function #

n = 20 
a = 0
b = 1

for i in range(1,n+1):
    a,b = b,a+b
print(a)

def fib(n): # header
    '''Calculates and returns the nth Fibonacci number''' # dock string
    a = 0
    b = 1
    for i in range(n): #body
        a,b = b,a+b
    return a
    
fib_num = fib(20)
print(fib_num) #print the 20th number

for i in range(21): #print all up to 20
    print(fib(i))
    

# def calc_mean(first,*remainder): # allows us to say we don't know how much input
#     '''This calculates the mean of numbers'''
#     mean = (first + sum(remainder))/(1 + len(remainder))
#     return mean
# print(calc_mean(23,43,56,76,45))

# Functions have the ability to call themselves
# This is called Resursion Function(function(...)) is draining

# def fib_2(n):
#     if n == 0: #checking for a base case
#         return 0 
#     elif n == 1: #checking for a base case
#         return 1
#     else:
#         return fib_2(n-1) + fib_2(n-2)
    
# x = fib_2(36)
# print(x)

# y = fib(1000)
# print(y)

# def sum_and_mult(a,b):
#     total = a + b
#     product = a * b
#     return total, product

# func_call = sum_and_mult(3,4)
# print(func_call)

# var_1, var_2 = sum_and_mult(6,7)
# print(var_1)
# print(var_2)
    
# Functions are their own environment

# var_3 = 5
# var_4 = 6

# def add1(var_3,var_4):
#     var_3 = var_3 + 1
#     var_4 = var_4 + 1
    
#     print(f"Inside the function var_3 = {var_3} and var_4 = {var_4}")
#     return var_3, var_4

# add1(18,19)
# print(f"But outside the function, var_3 = {var_3} and var_4 = {var_4}")

# NEVER DO THIS #

def lengthen_list(n,my_list = [1,2,3]): #123 is mutable, so the values will always change
    my_list.append(n)
    return my_list

x = lengthen_list(4)
# x = lengthen_list(4)
# x = lengthen_list(4)

# DO THIS INSTEAD #

# def lengthen_list_2(n,my_list = None):
#     if my_list == None:
#         my_list = [1,2,3]
#         my_list.append(n)
#         return my_list
    
# y = lengthen_list_2(4)
# y = lengthen_list_2(4)
# y = lengthen_list_2(4)

# 1 Create a function that adds two numbers

def sum_two(a,b):
    '''This function returns the sum of two numbers'''
    return a + b

print(f"The sum of 3, 4 is {sum_two(3,4)}")
    
# 2 Write a funtion that performs multiplication of two arguments. 
# By default the function should multiply the first argument by 2

def multiply(a,b=2):
    '''This function returns the product of a,b. 
    If b is not defined, it defaults to 2'''
    return a * b
print(f"Innputting 3 gives {multiply(3)}")
print(f"Inputting 3 and 5 gives {multiply(3,5)}")


# 3 Write a funtion to calculate a to the power of b. 
# If b is not given, default to 2

def power(a,b=2):
    '''Returns the product of a to the power of b. If b is not defined, 
    it defaults to 2'''
    return a**b
print(f"Inputting 3, gives {power(3)}")
print(f"Inputting 3 and 5 gives {power(3,5)}")


# 4 Write a funtion that will copy the contents of one file to another

def copy_file(infile, outfile):
    '''Copies the contents of one file to another'''
    
    with open(infile) as file_1:
        with open(outfile, "w") as file_2:
            file_2.write(file_1.read())
            
copy_file("capitals.txt","new capitals.txt")            
