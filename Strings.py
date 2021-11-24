# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 15:16:06 2021

@author: Shade
"""

# STRINGS #

# \n = new line
#\t = TAB
# end=" " puts the answers on a single line

print("one",end=" ")
print("two",end=" ")
print("three",end=" ")
print("four")

print("One, 'two', ''three'', four, \\five\\\nOnce, 'I' caught a \n\t fish '//alive\\\\'")

my_string = "Supercallifragiliciousespiallidocious"

print(len(my_string)) # length of the string
print(my_string[0])
print(my_string[20])
print("You are", my_string[0:5]) #string slicing, asking for the letters 0-5
print(my_string[:5],"man") #don't have to put in 0
print(my_string[5:10])
print(my_string[-1]) #returns last character

letter = my_string[4] #sets 'letter' as the 4th letter
print(letter)

print(my_string.upper()) #converts string to caps
print(my_string.lower())
print(my_string.title()) # Capitalise

rhyme = "The quick, brown fox jumped over the lazy dog"
rhyme_1 = rhyme.split(" ") #will split string into words

print(rhyme_1)

for char in range(len(rhyme_1)): # however long this list is
    rhyme_1[char] = rhyme_1[char].strip("\n") # strips empty space

print(rhyme_1)
print("Sherlock" in rhyme_1) # is the word Sherlock in the rhyme

phrase_1 = "The Cat sat on the mat"
phrase_2 = "So did the dog"
phrase_3 = phrase_1 + " " + phrase_2 #string concatenation

# # SPELL OUT A WORD BACKWARDS    
word = input("Please enter a word:>")
reverse_string = ""
for char in word:
    reverse_string = char + reverse_string
print(reverse_string)

print(word[::1])
