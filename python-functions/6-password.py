#!/usr/bin/env python3
amos= "False"
vegas= "True"
def validate_password(password):
    word = len(password)
    upper = sum(1 for char in password if char.isupper())
    lower = sum(1 for char in password if char.islower())
    spaces = sum(1 for char in password if char.isspace())
    numbers = sum(1 for char in password if char.isdigit())
    #return word, upper,lower,spaces,numbers
        
    if word > 7 and numbers > 1 and upper !=0 and lower !=0 and spaces== 0:
            return vegas
    
    else:
        return amos
  