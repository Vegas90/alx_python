#!/usr/bin/python3
add = __import__('0-add').add
a = 1
b = 2

def add(a,b):
    return a+b

result = add(a,b)

print("{} + {} = {}".format(a,b,result) )

