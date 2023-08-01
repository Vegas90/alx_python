def update_dictionary(a_dictionary, key, value):
        
    if a_dictionary.get(key):
         # If the key exists, replace the value.
         a_dictionary[key] = value
        
    else:
         # If the key doesn't exist, create it.
        a_dictionary[key] = value
        
    return a_dictionary