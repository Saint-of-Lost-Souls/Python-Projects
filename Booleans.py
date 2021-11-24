# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 15:20:37 2021

@author: Shade
"""

#BOOLEANS#

print(3 == 3) #is 3 equal to 3?
print(3 == 2) #is 3 equal to 2?

x = 5
y = 6
print("x =",x, "y =",y)
print("Checking less than with '<':", x < y) #asking if 5 less than 6
print("Checking greater than with '>':", x > y) #asking if 5 is greater than 6

var_1 = 7
var_2 = 7

print("var_1 =", var_1, "var_2 =", var_2)
print("Checking equality with '==' :", var_1 == var_2)
print("Checking not equal with '!=' :", var_1 != var_2)
print("Checking less than or equal to with '<=' :", var_1 <= var_2)
print("Checking greater than or equal to with '>=' :", var_1 >= var_2)

# #LOGICAL OPERATORS#

# #True AND true = TRUE - 'AND' is the logical operator, both variables have to be TRUE
# #True OR false = TRUE- 'OR' is the logical operator, only one variable has to be TRUE


var_3, var_4, var_5 = 15, 20, 25

print("var_3 =", var_3)
print("var_4 =", var_4, "var_5 =", var_5, end = "\n\n")
 
print("var_4 and var_5 < 100?", var_4 < 100 and var_5 < 100) #are both variables less than 100? both sides are TRUE, returns TRUE
print("var_4 and var_5 < 22?", var_4 < 22 and var_5 < 22) #are both variables less than 22? only one side is TRUE, returns FALSE
print("var_4 or var_5 < 22?", var_4 < 22 or var_5 < 22) #are both variables less than 22? only one side is TRUE, returns TRUE
print("var_4 or var_5 < 1?", var_4 < 1 or var_5 < 1, end = "\n\n") #are both variables less than 22? neither is TRUE, returns FALSE

# NOT negates the result of the condition

print("not True is", not True)
print("not False is", not False, end = "\n\n")
 
print("not (var_4 and var_5 < 100?)",not(var_4 < 100 and var_5 < 100)) 
print("not (var_4 and var_5 < 22?)",not(var_4 < 22 and var_5 < 22)) 
print("not (var_4 or var_5 < 22?)",not(var_4 < 22 or var_5 < 22)) 
print("not (var_4 or var_5 < 1?)",not(var_4 < 1 or var_5 < 1), end="\n\n") 

print("True and not", 4>7, "= TRUE", end = "\n\n")



