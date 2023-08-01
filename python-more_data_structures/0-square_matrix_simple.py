#!/usr/bin/python3
square_matrix_simple = __import__('0-square_matrix_simple').square_matrix_simple

if __name__ == "__main__":
  def square_matrix_sample(matrix=[]):  
 # Create a new matrix using list comprehension
    new_matrix = [[x ** 2 for x in row] for row in matrix]
    return new_matrix

