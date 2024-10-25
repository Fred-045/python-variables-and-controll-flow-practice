def reverse(fruits):
    reversed_list = []  
    for string in fruits:
        if not string:  # Check if the string is empty
            reversed_list.append("")  # Append an empty string to the result
        elif string.isalpha():  # Check if the string contains only alphabetic characters
            reversed_list.append(string[::-1])  # Reverse the string and add to the list
        else:
            reversed_list.append("Invalid input")  # Handle non-alphabetic strings

    return reversed_list

# Test the function
input_list = ["mango", "orange", "apple"]
print("Reversed strings:", reverse(input_list))
