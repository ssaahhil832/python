#task1 :
# This program calculates the factorial of a number using recursion.
def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a number: "))
print('Factorial of ',num,'is', factorial(num))  

#task2:
import math 
def calculate_square_root(number):
    if number < 0:
        raise ValueError("Cannot calculate square root of a negative number")
    return math.sqrt(number)

num= int(input("Enter a number: "))
try:
    result = calculate_square_root(num)
    print(f"The square root of {num} is {result}")
except ValueError as e:
    print(e)
