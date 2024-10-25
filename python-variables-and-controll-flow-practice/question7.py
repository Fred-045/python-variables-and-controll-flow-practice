def duplicates(input_list):
    
    unique_list = []
    
    
    for item in input_list:
        
        if item not in unique_list:
            unique_list.append(item)  
        elif item in unique_list:
           
            continue  
        else:
            
            continue  
            
    return unique_list

#
my_list = [11, 12, 12, 13, 14,14, 15, 15, 16]
result = duplicates(my_list)
print(f"The list after removing duplicates: {result}")

