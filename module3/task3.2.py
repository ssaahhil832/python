
#task2:
import math 
def calculate_square_root(number):
    if number < 0:
        raise ValueError("Cannot calculate square root of a negative number")
    a=math.sqrt(number)
    print('square root of',num,'is', a)
    b=math.log(number)
    print('log of',num,'is', b)
    c = math.sin(math.radians(number))
    print('sin of',num,'is', c)
    
num=int(input("Enter a number :"))
calculate_square_root(num)