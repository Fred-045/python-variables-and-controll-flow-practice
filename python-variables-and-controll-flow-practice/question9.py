def target(input_list, target_sum):
    
    seen_numbers = set()
    
    
    for number in input_list:
        complement = target_sum - number  
        
        if complement in seen_numbers:
            return True  
        elif number not in seen_numbers:
            seen_numbers.add(number)  
        else:
            
            continue  

    return False


num_list = [10, 15, 3, 7]
target = 17
result =target(num_list, target)
print(f"Does the list have a pair that adds up to {target}? {result}")
