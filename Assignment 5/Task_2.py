# Assignment 5

# Task 2:- Demonstrate List Slicing
"""
Problem Statement: Write a Python program that:
    1. Creates a list of numbers from 1 to 10.
    2. Extracts the first five elements from the list.
    3. Reverses these extracted elements.
    4. Prints both the extracted list and the reversed list
"""

number_list = []
for i in range(1,11):
    number_list.append(i)

first_five = number_list[:5]

print(f"Original list: {number_list}")
print(f"Extracted first five numbers: {first_five}")
print(f"Reversed list: {first_five[::-1]}")
