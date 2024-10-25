def sum_of_numbers(nums):
    total = 0  # Initialize the total sum as 0

    for num in nums:
        if num < 0:
            print(f"Skipping negative number: {num}")  # Handle negative
        elif num == 0:
            print("Zero encountered, not adding to the total.")  # Handle zero
        else:
            total += num  

    return total

# Test the function
nums = [1, 2, 3, 4, 5]
print("The sum is:", sum_of_numbers(nums))



    