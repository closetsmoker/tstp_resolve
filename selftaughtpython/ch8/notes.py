# importing modules 
import math 

math.pow(2, 3)

# random to get random integer between two numbers 
import random 
random.randint(0, 1000)

# statistics module will calculate mean, median, mode, etc. 
import statistics 

# mean 
nums = [1, 5, 33, 12, 46, 33, 21]
statistics.mean(nums)

# median 
statistics.median(nums) 

# mode 
statistics.mode(nums)

# keyword will check if a string is a Python keyword: 
import keyword 

keyword.iskeyword("for")
keyword.iskeyword("football")