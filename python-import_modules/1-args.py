import sys
center_args=0
def main():
  num_args=len(sys.argv)-1
  if len(sys.argv) < 3:
    print( num_args,"argument:")
  
  else:
    print("{} arguments:".format(num_args))
   # Print the arguments
    for i in range(0, num_args):
      print(i+1, ":", sys.argv[i+1])



if __name__ == "__main__":
  main()

