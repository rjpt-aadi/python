print("************Aditya Kumar**************")

# a) Create a string containing at least 5 words and store it in a variable.
original_string = "Python is a versatile programming language"

# b) Print out the string.
print("Original String:", original_string)

# c) Convert the string to a list of words using the string split method.
word_list = original_string.split()
print("string to a list of words:", word_list)

# d) Sort the list into reverse alphabetical order using the list methods.
# You can use the sort() method with the reverse parameter set to True.
word_list.sort()
# Print out the sorted list.
print("Sorted List:", word_list)
word_list.sort(reverse=True)

# e) Print out reversed list of words.
print("Reversed List of Words:", word_list)
