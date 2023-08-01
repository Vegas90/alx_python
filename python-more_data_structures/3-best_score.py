def best_score(a_dictionary):
    largest_key= None
    best_value = int
    for key, value in a_dictionary.item:
      if isinstance(value, int) and value > best_value:
            largest_key = key
            best_value = value
             
            print(largest_key)