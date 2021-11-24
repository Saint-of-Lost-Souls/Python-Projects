# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 16:15:51 2021

@author: Shade
"""

# PLAYING CARD CLASS #
# Create a playing card

# class Card(object):

#     def __inti__ (self,value,suit): #initialise these variables
#         self.value = value # it will have some value
#         self.suit = suit # it will have some suit
        
#     def get_value(self):
#         return self.value
    
#     def get_suit(self):
#         return self.suit
        
#     def __str__(self):
#         my_card = str(self.value) + " of " + str(self.suit)
#         return my_card

# my_card = Card(3,"d")
# print(my_card)


class Card(object):
    
    suits = {"d":"Diamonds","h":"Hearts","s":"Spades","c":"Clubs"}
    cards = {1:"Ace",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",10:"10",
             11:"Jack",12:"Queen",13:"King"}
     
    def __init__(self,value,suit):
        self.value = value
        self.suit = suit
        # we set the values
        
    def get_value(self):
        return self.value
        # now we get the values
        
    def get_suit(self):
        return self.suit
    
    def __str__(self):
        my_card = str(self.value) + " of " + str(self.suit)
        return my_card
                

my_card = Card(3,"d")
print([suit{:}]+[cards{:2}])