# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 14:06:04 2021

@author: Shade
"""

# Create a class to represent a bank account. It will need a balance, 
#a method of withdrawing, depositing and showing the new balance

# class BankAccount(object):
#     '''Displays the opening balance, allows user to withdraw and/or deposit 
#     and displays new balance'''
    
#     def __init__(self,balance=0.0):
#         self.balance = balance
        
#     def display_balance(self):
#         print(f"Your balance is {self.balance}")
        
#     def make_deposit(self):
#         amount = float(input("How much would you like to deposit?"))
#         self.balance += amount
#         print(f"Balance is now {self.balance}")        
        
#     def make_withdrawal(self):
#         amount = float(input("How much would you like to withdraw?"))
#         if amount > self.balance:
#             print(f"You do not have sufficient funds, your balance is {self.balance}")
#         else:
#             self.balance -= amount
#             print(f"Withdrawal successful, your new balance is {self.balance}")

# my_bank = BankAccount(300)
# print(my_bank.display_balance())   
 
# my_bank.make_deposit()  
# my_bank.make_withdrawal()     

#2 Create a circle class that will take the value of a radius and return
#the area of a circle

import math #gives us access to pi

class Circle(object):
    '''Represents a circle with radius. Calculates area'''
    
    def __init__(self,radius): #constructor vairable __init__ creates the self.radius variable
        self.radius = radius
        
    def calc_area(self):
        area = math.pi * (self.radius)**2
        return area

my_circ = Circle(8)     
print(f"The area of the circle is {my_circ.calc_area()} meters")

