#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_num = abs(number) %10
# YOUR CODE HERE
if number < 0:
    last_num = -last_num
    
if last_num > 5:
    print("Last digit of {0} is {1} and is greater than 5".format(number,last_num))

elif last_num==0:
     print("Last digit of {0} is {1} and is 0".format(number,last_num))
     
elif last_num < 6 and last_num !=0:
    print("Last digit of {0} is {1} and is less than 6 and not 0".format(number,last_num))
    
    