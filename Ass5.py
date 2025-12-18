# Create a dictionary with student names and marks
'''
students = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "David": 66
}

name = input("Enter the student's name: ")

if name in students:
    print(f"{name}'s marks: {students[name]}")
else:
    print("Student not found in the dictionary.")
'''

# Create a list of numbers from 1 to 10
numbers = list(range(1, 11))

# Extract the first five elements
first_five = numbers[:5]

# Reverse the extracted elements
reversed_list = first_five[::-1]

# Print the results
print("Original list:", numbers)
print("Extracted first five elements:", first_five)
print("Reversed extracted elements:", reversed_list)
