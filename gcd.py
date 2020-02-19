#this program calculates GCD of two positive numbers
def GCD(a,b):
    if b==0:
        return a
    else:
        return GCD(b,a%b)

num1= int(input("Enter the first number:\n"))
num2= int(input("Enter the second number:\n"))
print("\nGreatest Common Divisor of given two numbers is", GCD(num1, num2))

"""
OUTPUT:
Enter the first number:
6

Enter the second number:
9

Greatest Common Divisor of given two numbers is 3

"""
