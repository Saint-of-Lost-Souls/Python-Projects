# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 16:22:47 2021

@author: Shade
"""

# To acces a module, type import first
# Go to Python documentation for complete list

import math
print(math.pi)
print(math.cos(0))

import random
print(random.randint(1,100)) #print a random number
for number in range (100):
    print(random.randint(1,100),end=" ")
# generate 100 random numbers

# can import modules under an alias
import random as r
print(r.randint(50,200))

# or if we know what we are looking for, type
from random import randint
print(randint(1,1000))

