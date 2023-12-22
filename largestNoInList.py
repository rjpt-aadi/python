print("*********Aditya Kumar*********")

def largest(numbers):
    # Check if the list is not empty
    if not numbers:
        return None

    # Assume the first number is the largest
    max_num = numbers[0]

    # Iterate through the list to find the largest number
    for num in numbers:
        if num > max_num:
            max_num = num

    return max_num

# Get the number of elements from the user
n = int(input("Enter the number of elements: "))

# Initialize an empty list to store the numbers
num_list = []

# Get the numbers from the user
for i in range(n):
    num = float(input(f"Enter number {i + 1}: "))
    num_list.append(num)

# Call the largest function and print the result
result = largest(num_list)

if result is not None:
    print(f"The largest number is: {result}")
else:
    print("No numbers provided.")
