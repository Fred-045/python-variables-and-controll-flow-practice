def print_even_keys(input_dict):
    for key, value in input_dict.items():  # Iterate through the dictionary
        if isinstance(value, int) and value % 2 == 0:  # Check if value is an even integer
            print(key)  # Print the key

# Test the function
example_dict = {'a': 2, 'b': 3, 'c': 4, 'd': 5, 'e': 6}
print("Keys with even values:")
print_even_keys(example_dict)
