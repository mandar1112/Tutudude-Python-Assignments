# Assignment 4

# Task 2:- Write and Append Data to a File

"""
Problem Statement: Write a Python program that:
    1. Takes user input and writes it to a file named output.txt.
    2. Appends additional data to the same file.
    3. Reads and displays the final content of the file.
"""

with open("output.txt", "wt+") as fh:

    fh.write(input("Enter text to write to the file: ") + "\n")
    print("Data successfully written to output.txt.")
    

    fh.write(input("Enter additional text to append: ") + "\n")
    print("Data sucessfully appended.")


    fh.seek(0)

    print("Final content of output.txt: ")
    for line in fh:
        print(line, end="")
        
