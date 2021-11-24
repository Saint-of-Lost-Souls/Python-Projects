# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 14:09:57 2021

@author: Shade
"""

# f = open("kipling.txt","w") #  will create if no file of this name , 'w' is the mode, 'write' (or read, append)

# f.write("If you can keep your head while all about you\n\
#         are losing theirs and blaming it on you,\n")
# f.write("If you can trust yourself when all men doubt you \n\
#         But make allowance for their doubting too;\n")
# f.write("If you can wait and not be tired by waiting,\n\
#         Or being lied about, don't deal in lies,\n")
# f.write("Or being hated, don't give way to hating,\n\
#         And yet don't look too good, nor talk too wise:\n")

# f.close() #always close

# f = open("kipling.txt","r")
# # print(f.read())
# # print(f.readline()) #prints first line
# content = f.readlines() #make it a list so you can iterate over it

# f.close()

# f = open("kipling.txt","a")
# f.write("If you can dream - and not make dreams your master;\n\
#         If you can think - and not make thoughts your aim;\n")
# f.close()
# print()
# f = open("kipling.txt","r")
# print(f.read())
# f.close()
# print()
with open("kipling.txt","r") as f:
    for line in f.readlines(): #will return a list
        print(line,end=" ")
        
# 1 Create a new file, store the names of 5 capitals in the file on the same line

file = open("capitals.txt","w")
file.write("London, ")
file.write("Paris, ")
file.write("Madrid, ")
file.write("Lisbon, ")
file.write("Rome,")
file.close()

# 2 Ask the user to input another city. Add that city to the list then print

user_input = input("Please enter a capital city:>")
                   
file = open("capitals.txt","a")
file.write("\n" + user_input)
file.close

file = open("capitals.txt", "r")
print(file.read())
file.close            