#!/usr/bin/python3

def square_matrix_sample(matrix=[]):
#new_matrix=0   
 # Create a new matrix using list comprehension
    new_matrix = [[x ** 2 for x in row] for row in matrix]
#new_matrix=print(list(map(lambda x:[i**2 for i in x], matrix)))
    return new_matrix


