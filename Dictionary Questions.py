# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 12:38:01 2021

@author: Shade
"""
# 1
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

user_input= input("Which country would you like to check?:>") # pick a country
user_input = user_input.lower() # covert to lower case

while("united kingdom" not in user_input and not user_input.isalpha()): # isn't UK and isn't a word
    if user_input == "united states": # UK and US are used because they have a space in them, which isn't alpha
          break #out of the loop
    print("You must type a word")
    user_input = input("Please type the name of a country:>")

user_input = user_input.title() # Capitalise 

if user_input in capitals: # user_input exists in the countries dictionary
    print(f"The capital of {user_input} is {capitals[user_input]}")
else:
    print("No data available")


# 2
# Write code that will create a dictionary containing key, value pairs that 
# represent the first 12 values of the fibonacci sequence
n = 12 # how many numbers do we want
a = 0
b = 1
d = dict() # or d = {}

for i in range(1,n+1): # for key in range
    d[i] = a # for each new index, add the value of a, which then becomes b
    a,b = b,a+b
print(d)

# 3
# Create a dictionary to represent the open, high, low, close values of the companies

companies = ["Python DS","PythonSoft","Pythazon","PyBook"]
key_names = ["open","high","low","close"]
prices = [[12.87,13.23,11.42,13.10],[23.54,25.76,21.87,22.33],
          [98.99,102.34,97.21,100.065],[203.54,207.54,202.43,205.24]]
d_1 = {} # empty dictionary

for i in range(len(key_names)): # open,high,low,close
    d_1[companies[i]] = dict(zip(key_names,prices[i])) 
    # put the companies in the dictionary and assign each those 4 values, 
    # then combine the values with the prices in a zip and add to the companies
print(d_1)

# 4
# Pick a module and implement it
import datetime

today = datetime.date.today() 

print(f"Today's date is {today}")
holiday = datetime.date(2021,12,25)
delta = holiday - today
print(f"Just {delta.days} days until the holidays!")

# 5
# Create a dictionary containing the letters a-z, the values should be 
# random numbers created from the random module. Make a bar graph
keys = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
d = {}

import random

for letter in keys: # for every letter a-z
    d[letter] = random.randint(1,101)# add to the dictionary and give a random number
print(d)

import matplotlib.pyplot as graph # display as graph
x,y = zip(*d.items())
graph.bar(x,y) 

# 6
# Create a dictionary containing 4 suits of 13 cards
suits = ["Spades","Clubs","Hearts","Diamonds"]
cards = ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
deck = {}

for i in suits: # go through every suit
    deck[i] = cards # create keys = cards are the values so we assign them to a key
print(deck)