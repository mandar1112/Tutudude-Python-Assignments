# Assignment 5

# Task 1:- Create a Dictionary of Student Marks
"""
Problem Statement: Write a Python program that:
    1. Creates a dictionary where student names are keys and their marks are values.
    2. Asks the user to input a student's name.
    3. Retrieves and displays the corresponding marks.
    4. If the student’s name is not found, display an appropriate message.
"""

Student_Data = {
    "Alice" : 98,
    "John" : 89,
    "Carol" : 95,
    "Max" : 87
}

for i in range(1,3):
    # Search Student
    search_name = input("Enter student's name: ")

    if search_name in Student_Data:
        print(f"Marks for {search_name}: {Student_Data[search_name]}")
    else:
        print("Student not found.")

