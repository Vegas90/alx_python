import sys

def main():
  num_args=len(sys.argv) -1
  
  if num_args == 1:
    print( num_args,"argument:")

  else:
    print("{} arguments:".format(num_args))
  
   # Print the arguments
    for i in range(1, num_args):
          print(i, ":", sys.argv[i])



if __name__ == "__main__":
  main()

