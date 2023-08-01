def best_score(a_dictionary):
    best_key= None
    largest_value= int
    for key, value in a_dictionary.items():
      if value > largest_value:
           best_key = key
           largest_value = value
             
    print(best_key)