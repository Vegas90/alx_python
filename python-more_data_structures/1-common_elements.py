def common_elements(set_1, set_2):
    common_elements_set = set()
    #iterate through the set 1 and for each element we check if its present in set 2 
    for item in set_1:
        if item in set_2:
            #common items added in the new set by add.(item)
            common_elements_set.add(item)
    return common_elements_set
  