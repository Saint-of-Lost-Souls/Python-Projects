# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 15:23:24 2021

@author: Shade
"""

some_condition = False

if some_condition:
    print("The variable 'some_condition' is True")
else:
    print("The variable 'some_condition' is False")

# 1
# WHAT SHOULD I WEAR? #
temp = int(input("Please enter your tempertaure in Celcius.\nAn integer between 0-40:>>>"))

if temp > 30:
    print("\nWear shorts and sunscreen")
elif temp <= 30 and temp > 20: # if the temp input was less than 30 but greater than 20, print this
    print("\nIt's warm, but not shorts weather!")
elif temp <= 20 and temp > 10: # if the temp input was less than 20 but greater than 10, print this
    print("\nYou'll probably need a vest today!")
else: #if the above two conditions have not been met, print this
    print("\nToo cold- don't go out!")

# 2
# GUESS THE WORD? #
word = "summer"
guess = input("I'm thinking of a word, can you guess what it is?\nHint: It's a season!\nAnswer:")

guess = guess.lower() #converts whatever the user writes into lower case
if guess == "summer":
    print("Yes, it's Summer, well done!")
elif guess == "Winter":
    print("It's not Winter, sorry")
elif guess == "auumn":
    print("It's not Autumn, sorry!")
elif guess == "spring":
    print("It's not Spring, sorry!")
else:
    print(guess.capitalize(), "is not a season!")
    
# 3
# SPELL THE NUMBER #
print("Hello User! I really need you to input a number between 1 - 5 and then I will work out how to spell it for you")

user_input = int(input("Ok, tell me your number:"))

if user_input == 1:
    print("One")
elif user_input == 2:
    print("Two")
elif user_input == 3:
    print("Three")
elif user_input == 4:
    print("Four")
elif user_input == 5:
    print("Five")
else:
    print("That is not the number I am looking for!")
    
print("Pretty smart, eh?")
    
# 4
# WRITE THE NUMBER #
print("Hello User! I really need you to write a number between one - five and I will show you what it looks like in my world")

user_input = input("Ok, write your number:")
user_input = user_input.lower()

if user_input == "one":
    print("1")
elif user_input == "two":
    print("2")
elif user_input == "three":
    print("3")
elif user_input == "four":
    print("4")
elif user_input == "five":
    print("5")
else:
    print("What are you stoopid or something??!")

# 5
# GUESS THE NUMBER #
secret_number = 3

print("Hello User! I am thinking of a number between 1-10; can you guess what it is?")
guess = input("Your answer:")

if guess.isdigit():
    guess = int(guess) # if the guess is a digit
    if guess == secret_number: # convert it into an int
        print("Well done, you got it!")
    elif guess < secret_number and guess >= 1: #the user can only guess between 1-2, AND creates RANGE
        print("Too low, you lose!")
    elif guess > secret_number and guess <= 10: #the user can only guess between 4-10, AND creates RANGE
        print("Too high, you lose!")
    else:
        print("Wrong number, idiot!") #if the user inputs any other number, any number OUT OF RANGE
else:
    print("That's a funny looking number")


# 6
# NUMBER OF LETTERS #
print("Hello User! Give me a word I will tell you how many letters it has. Maybe.")

word = input("What is your word?")   
word_len = len(word) # count the characters

if word_len < 5:
    print("Your word contains", word_len,"number of letters")
else:
    print("Figure it out yourself, dummy!!")

# 7
int_1 = int(input("Please give me a number between 1- 20\n>>>"))
int_2 = int(input("Please give me another number between 1-20\n>>>"))

if int_1 > 15 and int_2 > 15:
    print(int_1 * int_2)
elif int_1 > 15 or int_2 > 15:
    print(int_1 + int_2)
else:
    print(0)
    
  