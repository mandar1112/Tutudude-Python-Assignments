# Assignment 3

# Task 1: Calculate Factorial Using a Function


def factorial_recursion(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial_recursion(num-1)

def factorial_itarration(num):
    if num == 0:
        return 1
    fact = 1
    for i in range(1,num+1):
        fact *= i
    return fact


num = int(input("Enter a Number: "))
print(f"Factorial Using Recursion of Number {num} is: {factorial_recursion(num)}")
print(f"Factorial Using Itteration of Number {num} is: {factorial_itarration(num)}")