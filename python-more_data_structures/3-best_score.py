def best_score(a_dictionary):
    largest_key= None
     # Initialize to negative infinity to handle negative values
    largest_key = float('-inf')
    
    for key in a_dictionary:
        if largest_key is None or key > largest_key:
            largest_key = key
            
            print(largest_key)