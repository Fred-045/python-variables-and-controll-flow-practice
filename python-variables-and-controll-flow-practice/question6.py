def find_largest_number(numbers):
    
    largest = numbers[0]
    
    
    for num in numbers[1:]:
        if num > largest:
            largest = num
        elif num == largest:
            
            continue  #
        else:
            
            continue  
            
    return largest

# Example usage
numbers_tuple = (110, 220, 380, 470, 250)
largest_number = find_largest_number(numbers_tuple)
print(f"The largest number in the tuple is: {largest_number}")
