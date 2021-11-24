# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 14:06:04 2021

@author: Shade
"""

# Create a class to represent a bank account. It will need a balance, 
# a method of withdrawing, depositing and showing the new balance

class BankAccount(object):
    '''Displays the opening balance, allows user to withdraw and/or deposit 
    and displays new balance'''
    
    def __init__(self,balance=0.0):
        self.balance = balance
        
    def display_balance(self):
        print(f"Your balance is {self.balance}")
        
    def make_deposit(self):
        amount = float(input("How much would you like to deposit?"))
        self.balance += amount
        print(f"Balance is now {self.balance}")        
        
    def make_withdrawal(self):
        amount = float(input("How much would you like to withdraw?"))
        if amount > self.balance:
            print(f"You do not have sufficient funds, your balance is {self.balance}")
        else:
            self.balance -= amount
            print(f"Withdrawal successful, your new balance is {self.balance}")

my_bank = BankAccount(300)
print(my_bank.display_balance())   
 
my_bank.make_deposit()  
my_bank.make_withdrawal()     

# 2 Create a circle class that will take the value of a radius and return
# the area of a circle

import math # gives us access to pi

class Circle(object):
    '''Represents a circle with radius. Calculates area'''
    
    def __init__(self,radius): #constructor variable __init__ creates the self.radius variable
        self.radius = radius
        
    def calc_area(self):
        area = math.pi * (self.radius)**2
        return area

my_circ = Circle(8)     
print(f"The area of the circle is {my_circ.calc_area()} meters")

# Objects combine data with functions
# Class is the blueprint for an object

# x = 1
# dir(x) # integer directory
# help(x) # integer help

# y = [1,2,3]
# help(y) # list help
# dir(y) # list directory
# y.append(5) # adds 5 to the end of the list

# z = {"a":1}
# help(z) # dictionary help
# dir(z) # dictionary directory

# class Patient(object):
#     '''Medical centre patient'''
#     def __init__(self,name,age): # creates different instance of this object, so each instance has its own variables
#         self.name = name
#         self.age = age
        
# steve = Patient("Steven Hughes",48)
# abigail = Patient("Abigail Sandwick",32)        

class Patient(object):
     '''
     Attributes
     ---------------
     name: Patient name
     age: Patient age
     conditions: Existing medical conditions
     '''
     
     status = "paient" #class-wide variable
     def __init__(self,name,age): 
         self.name = name
         self.age = age
         self.conditions = []
         
     def get_details(self):
         print(f"Patient: {self.name},{self.age} years. " \
               f"Current information: {self.conditions}.")
         
     def add_info(self,information):
         self.conditions.append(information)
         
steve = Patient("Steven Hughes",48)
abigail = Patient("Abigail Sandwick",32)  

steve.add_info("Patient treated for ear infection- amoxycilin prescribed")

# print(steve.get_details())

class Infant(Patient):
    '''Patient under 2 years'''
    
    def __init__(self,name,age):
        self.vaccinations = []
        super().__init__(name,age) #super searches the parent class for this command. Initialising the variables
    def add_vac(self,vaccine):
        self.vaccinations.append(vaccine)
        
    def get_details(self):
        print(f"Patient record: {self.name}, {self.age} years. " \
              f"Patient has had {self.vaccinations} vaccines. " \
              f"Current information: {self.conditions}. " \
              f"\n{self.name} IS AN INFANT, HAS HE HAD ALL HIS CHECKS?")

archie = Infant("Archie Fittleworth", 0)
archie.add_vac("MMR")            
print(archie.get_details())                
        

