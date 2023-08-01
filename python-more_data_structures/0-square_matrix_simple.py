#!/usr/bin/python3
def square_matrix_sample(matrix=[]):
#new_matrix=0   
 # Create a new matrix using list comprehension
    new_matrix = [[x ** 2 for x in row] for row in matrix]
    return new_matrix

if __name__ == "__main__":
  main()
  
