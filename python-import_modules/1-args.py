import sys
def main():
  # Get the number of arguments
  num_args = len(sys.argv)
  # Print the number of arguments
  print("Number of arguments:", num_args)
  # Print the arguments
  if num_args == 0:
      print("0 arguments.")
  
  for i in range(1, num_args + 1):
    print(i, ":", sys.argv[i - 1])
if __name__ == "__main__":
  main()
