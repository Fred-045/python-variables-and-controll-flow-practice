def greater_than_n(input_dict, n):
    
    keys_list = []
    
    
    for key, value in input_dict.items():
        if value > n:
            keys_list.append(key)  
        elif value == n:
           
            continue  
        else:
           
            continue  

    return keys_list

# Example usage
example_dict = {'a': 5, 'b': 12, 'c': 3}
n = 4
result = greater_than_n(example_dict, n)
print(f"Keys with values greater than {n}: {result}")
