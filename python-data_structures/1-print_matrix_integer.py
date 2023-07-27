#!/usr/bin/python3
print_matrix_integer = __import__('1-print_matrix_integer').print_matrix_integer
def print_matrix_integer(matrix=[[]]):
   for row in matrix:
        for element in row:
            print("{:d}".format(element), end=" ")
        print() 
        # Add a newline after each row 
    
print_matrix_integer(matrix)
#print("{a}".format(a=a), end='\n')
#print("{}".format(b), end='\n')
#print("{}".format(c), end='\n')
