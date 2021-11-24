# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 15:19:50 2021

@author: Shade
"""

#FLOOR DIVISION#

#7/3 returns a float= 2.33333..5
#7//3, answer range from 3-4, takes the lowest whole number
#-7//3, answer range from -3--2, takes the lowest negative number, -3

#1

print("Bob, Ann, Jane and Ashwin want to order pizza- they know they will each eat")
print("4 slices of pizza. The local pizza shop sells pizzas of only 6 slices\n")
print("What is the minimum number of pizzas needed?\n")

total_slices = 4 * 4 
number_of_pizzas = (total_slices + 5)//6 
#6 because thats how many slices a pizza commes in, add 5 because it is one less,
#than 6 and will take us up to the next whole number. You're adding 5 slices of another pizza
slices_left = number_of_pizzas * 6 - total_slices

print("Number of pizzas required is:", number_of_pizzas, "with", slices_left, "leftover slices")