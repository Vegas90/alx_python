#!/usr/bin/env python3
amos= "False"
vegas= "True"
def is_prime(n):
    if n > 1:
        for i in range(2, int(n/2)+1):
             if (n % i) == 0:
                    return amos
                    break
        else:
             return vegas
# If the number is less than 1, its also not a prime number.
    else:
	     return amos   
     