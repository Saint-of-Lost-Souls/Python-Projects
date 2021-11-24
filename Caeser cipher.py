# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 10:41:32 2021

@author: Shade
"""
# CAESAR CIPHER #

# alphabet = "abcdefghijklmnopqrstuvwxyz"
# input_text = "the cat sat on the mat"
# output = ""
# define variables outside of function

# for char in input_text: # find char in text
#     alpha_index = alphabet.find(char) # find what index it is in the alphabet string
#     output = output + alphabet[alpha_index+3]
# print(output)

# alpha_index = the index number of the letter we are on
# compare our text with the alpha_index and number it
# for each char we found the index of it in alphabet

# What if the cipher index goes beyond the end of alphabet

# output = ""
# for char in input_text:
#     alpha_index = alphabet.find(char) 
#     output = output + alphabet[alpha_index+30]
# print(output)

# tell the code once the index reaches 26, go back to 4, use %

# Write a function to deal with the shift

# def shift_amount(i):
#     return i%26

# output_1 = ""
# for char in input_text:
#     alpha_index = alphabet.find(char) 
#     output_1 = output_1 + alphabet[shift_amount(alpha_index+30)]
# print(output_1)
    
# A COMPLETE FUNCTION #

alphabet = "abcdefghijklmnopqrstuvwxyz"
cipher = "the cat sat on the mat"

def shift_amount(i):
    return i%26

def encrypt(text,required_shift):
    out_string = ""
    text = text.lower()
    for char in text:
        if char not in alphabet: # if the char we encounter isn't in the alphabet, don't do anything
            out_string = out_string + char # don't shift it, we just add it to the string
        else:
            alpha_index = alphabet.find(char)
            out_string = out_string + alphabet[shift_amount(alpha_index+required_shift)]
    return out_string
            
shift = encrypt(cipher,5)
print(shift)

rhyme = "the quick brown fox jumped over the lazy dog"
encrypt_rhyme = encrypt(rhyme,5)
print(encrypt_rhyme)

print(encrypt(encrypt_rhyme,-5))
            