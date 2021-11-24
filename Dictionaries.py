# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 16:29:54 2021

@author: Shade
"""

# Dictionaries #

# Consist of key-value pairs, separated by :, within {}, not ordered but can
# be accessed quickly
# Object on the right is the KEY, object on the left is the VALUE
 
# VALUES = MUTABLE
# LISTS = MUTABLE
# DICTIONAIRES = MUTABLE
# KEYS = IMMUTABLE
# TUPLES = IMMUTABLE
# STRINGS = IMMUTABLE

capitals = {"France":"Paris",
            "Spain":"Madrid",
            "United Kingdom":"London",
            "India":"New Delhi",
            "United States":"Washington DC",
            "Italy":"Rome",
            "Denmark":"Copenhagen",
            "Germany":"Berlin",
            "Greece":"Athens",
            "Bulgaria":"Sofia",
            "Ireland":"Dublin",
            "Mexico":"Mexico City"}

print(capitals["Germany"])
print(capitals.get("Germany"))

capitals["South Korea"] = "Seoul" # adding a key = giving it a value
print(capitals)
print()
print(capitals.items()) # shows value pairs, these are called tuples

# for country in capitals: # find the countries in capital dictionary
#     print(country) # print only the countries
    
# for country, city in capitals.items():
#     print(f"The capital of {country}, is {city}")
    
# print(capitals.keys()) # print only the countries
# print()
# print(capitals.values()) # print only the cities

# if "Sydney" in capitals:
#     print("It contains Sydney")
# else:
#     print("You are an idiot")
    
# print("Sydney" in capitals) #as above as FALSE

# print(capitals.items())
# print()
# x,y = zip(*capitals.items())
# print(x)

   
# l = [1,2,3,4,5]
# print(5 in l) # 5 is in 'l' so answer is TRUE, else FALSE
    
# Counting the letters #
rhyme = "The quick, brown fox jumped over the lazy dog"

letter_count = {}
for letter in rhyme:
    letter_count[letter.lower()] = letter_count.get(letter,0) + 1
letter_count["m"] = 1    
print(letter_count)
print()

import matplotlib.pyplot as graph

x,y = zip(*letter_count.items()) # unpacks the items so you can plot it
graph.bar(x,y) # creates a bar graph
graph.show()

letter_count_clean = {} # new dictionary

for k,v in letter_count.items(): # .items finds the key and value
    if k.isalpha(): # if key is a letter
        letter_count_clean[k] = v # make the key-value pair and put it in the dictionary

print(letter_count_clean)
x,y = zip(*letter_count_clean.items())
graph.bar(x,y)
graph.show()

from collections import Counter
print(Counter(rhyme.lower())) # converts letters to lower case and counts them all
new_dict = dict(Counter(rhyme.lower()))
new_dict = {k:v for k,v in new_dict.items() if k.isalpha()} # dictionary comprehension
print(new_dict)


l = [x**2 for x in range(1,11)] # creates a list of 10 square numbers
print(l)

cube = [x**3 for x in range(1,11)]
print(cube)      

# my_tuple = (1,2,3,4)
# my_list = [5,6,7,8]
# my_string = "Australia"

# print(my_tuple[0]) # prints 1st value
# print(my_tuple[:3]) # prints 1st 3 , tuple clicing
# my_list[0] = 1000 # amending the list to put 1000 at the front
# print(my_list)

# The value of the KEY(country) is itself a dictionary #

countries = {"France":{"Capital":"Paris","Language":"French"},
            "Spain":{"Capital":"Madrid","Language":"Spanish"},
            "United Kingdom":{"Capital":"London","Language":"English"},
            "India":{"Capital":"New Delhi","Language":"Indian"},
            "United States":{"Capital":"Washington DC","Language":"English"},
            "Italy":{"Capital":"Rome","Language":"Italian"},
            "Denmark":{"Capital":"Copenhagen","Language":"Danish"},
            "Germany":{"Capital":"Berlin","Language":"German"},
            "Greece":{"Capital":"Athens","Language":"Greek"},
            "Bulgaria":{"Capital":"Sofia","Language":"Bulgarian"},
            "Ireland":{"Capital":"Dublin","Language":"Irish"},
            "Mexico":{"Capital":"Mexico City","Language":"Spanish"}
            }

print(countries["France"]) #returns the dictionary for that key
for key, value in countries.items():
    print(key,value)
    
for key, value in countries.items():
    print(f'{value["Capital"]} is the capital of {key} and they speak {value["Language"]}')
