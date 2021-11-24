# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 15:16:57 2021

@author: Shade
"""
# VARIABLES #
# asking the computer for a little piece of memory to store data
# variables cannot start with numbers, cannot have spaces use underscore

y = 12
x = 5
z = x + y
print(z)

new_variable = 9
radius = 2.5
pi = 3.14159
area_of_circle = pi * radius**2

user_input = input("How many apples do you have?\n >>> ") #stores answer as a string
user_input = int(input("How many apples do you have?\n >>> ")) #stores answer as an integer
user_input = float(input("How many apples do you have?\n >>>")) #stores answer as a float

# 1
print("Hi User! Give me the radius of a circle and I will tell you the area! Pretty awesome, eh?")
radius = float(input("Please enter the circle radius:\n>>>"))
pi = 3.14159
area = pi * radius**2
print("You entered", radius, "the area of the circle is", area)

# 2
print("Now we are going to convert fahrenheit to celcius")
far = float(input("Please enter the temperature in fahrenheit:\n>>>"))
cel = (far - 32) * 5/9
print("Fahrenheit to celcius is:",cel)
print("Well, that was boring")

# 3
num_1 = int(input("Please enter the first number:>"))
num_2 = int(input("Please enter the second number:>"))
# # to concatenate the answer, you need to convert the int to str, 
print("The sum of " + str(num_1) + " and " + str(num_2) + " is " + str(num_1 + num_2))

# 4
num_1 = int(input("Please enter the first number:>"))
num_2 = int(input("Please enter the second number:>"))
product = num_1 * num_2
print("The product of",num_1,"and",num_2,"is",product)

# 5
# SWAPPING VARIABLES #

int_1 = int(input("Give me a number\n>>>"))
int_2 = int(input("Give me another number\n>>>"))
print("Before swapping, int_1 =", int_1,"and int_2 =", int_2)
int_1, int_2 = int_2, int_1
print("After swapping, int_1 =", int_1,"and int_2 =", int_2)  

# MORE VARIABLES #

x = 5
x = x + 1

print("x =",x)

x += 1 #shorthand for x = x + 1

print("x =",x)

y = x

print("y =",y)

x += 1

print("x =",x)
print("y =",y)
