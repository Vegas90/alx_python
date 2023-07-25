import sys

if __name__ == '__main__':
    # Get the number of arguments
    num_args = len(sys.argv) - 1  # The first element in sys.argv is the script name

    # Print the number of arguments
    print(f"Number of argument(s): {num_args}", end="")

    # Print "argument" or "arguments" based on the number of arguments
    if num_args == 1:
        print(" followed by argument:", end="")
    else:
        print(" followed by arguments:", end="")

    # Print a newline character after the header
    print()

    # Print each argument and its position
    for i, arg in enumerate(sys.argv[1:], start=1):
        print(f"{i}: {arg}")

    # If no arguments were passed, print a dot
    if num_args == 0:
        print(".")
