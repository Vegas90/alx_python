def best_score(a_dictionary):
    best_key= None
    best_score = int
    for key, value in a_dictionary.item:
      if isinstance(value, int) and value > best_score:
           best_key = key
           best_score = value
             
    print(best_key)