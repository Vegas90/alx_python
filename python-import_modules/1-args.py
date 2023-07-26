import sys
center_args=0
def main():
  num_args=len(sys.argv)
  
  if num_args == 1:
    print( num_args,"argument:")
  
  else:
    print("{} arguments:".format(num_args))
   # Print the arguments
    for i in range(1, num_args - 1):
          print(i, ":", sys.argv[i+1])



if __name__ == "__main__":
  main()

