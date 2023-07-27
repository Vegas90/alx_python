#!/usr/bin/env python3
#no_c = __import__('0-no_c').no_c


def no_c(my_string):
    # Initialize an empty string to store the result
    result = ""
     # Loop through each character in the input string
    for char in my_string:
         # Check if the character is not 'c' and not 'C'
         if char != 'c' and char !='C':
                   # Append the character to the result string

             result +=char
    return result    
       
    #no_c(my_string)
#if __name__ == "__main__":
   # main()








#if __name__ == "__main__":
#  main()
