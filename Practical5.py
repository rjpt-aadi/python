print("*********Aditya Kumar**********")
# Initialize an empty list to store the numbers
result_numbers = []

# Iterate through the range from 2000 to 2500
for number in range(2000, 2501):
    # Check if the number is a multiple of 17 and not a multiple of 5
    if number % 17 == 0 and number % 5 != 0:
        result_numbers.append(number)

# Print the result
print("Numbers between 2000 and 2500 that are multiples of 17 but not multiples of 5:")
print(result_numbers)
