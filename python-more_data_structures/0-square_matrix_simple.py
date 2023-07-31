

def square_matrix_sample(matrix=[]):  
 # Create a new matrix using list comprehension
    new_matrix = [[x ** 2 for x in row] for row in matrix]
    return new_matrix


