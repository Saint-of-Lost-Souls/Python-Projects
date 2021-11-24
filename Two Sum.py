# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 13:52:50 2021

@author: Shade
"""

# Two Sums #

def two_sums(nums, target):
    d = {} #empty dictionary
    
    for i in range(len(nums)): # iterate over the indices in this list
        if target - nums[i] in d: # if the target - the value of the index is in the dictionary
            print(d)
            return [d[target-nums[i]],i] # return the value stored in the dictionary and the value we are on
        d[nums[i]] = i
    return -1

L = [8,6,11,3]
print(two_sums(L,9))

# the first time we go around, there is nothing in the dictionary, so 8 is assigned 0
# 2nd time we go around, 6 is assigned 1
# 3rd time we go around, 11 is assigned 2
# 4th time we go around, 3 is assigned and 6 + 3 make 9 so it evaluates to TRUE

L2 = [2,5,3,7,4]
print(two_sums(L2,10))
# the first time we go around, there is nothing in the dictionary, so 2 is assigned 0
# 2nd time we go around, 5 is assigned 1
# 3rd time we go around, 3 is assigned 2
# 4th time we go around, 7 + 3 make 10 so it evaluates to TRUE and stops before adding 7,4

print(two_sums([3,3],6))
# if 6 minus 3 is in d, there is nothing in d yet so it adds the key/value pair of 3:0
# goes around again, and checks if 3 is in d, it is so it evaluates as TRUE