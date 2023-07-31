#!/usr/bin/python3
#square_matrix_simple = __import__('0-square_matrix_simple').square_matrix_simple
matrix=0
matrix:[[1,2,3], [4,5,6], [7,8,9]]

new_matrix=print(list(map(lambda x:[i**2 for i in x], matrix)))

print (new_matrix)
print (matrix)

if __name__ == "__main__":
  main()