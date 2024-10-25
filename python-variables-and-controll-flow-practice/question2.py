def Family_members():
    user_inputs = []  # List to store all inputs

    while True:
        user_input = input("Name Your Family Members ( press 'exit' to stop): ")
        
        if user_input.lower() == 'exit':  # Exit condition
            break
        
        print(f"You entered: {user_input}")  # Print each word
        user_inputs.append(user_input)  # Save each word to the list

    # Print all collected inputs after exit
    print("\nAll data entered:")
    for word in user_inputs:
        print(word)

# Run the function
Family_members()
