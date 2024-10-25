def dict_tuple(tuples_list):
    
    result_dict = {}
    
    
    for item in tuples_list:
        if len(item) == 2:
            key, value = item
            result_dict[key] = value  
        elif len(item) < 2:
            
            print(f"Tuple {item} has less than two elements, skipping.")
            continue  
        else:
            
            print(f"Tuple {item} has more than two elements, skipping.")
            continue  

    return result_dict


tuples_list = [("apple", 5), ("banana", 3), ("cherry", 10)]
result = dict_tuple(tuples_list)
print(f"The resulting dictionary: {result}")
