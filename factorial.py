#This program executes facctorial number using recursion method
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)

n=int(input("Enter the number:\n"))
result=fact(n)
print("Factorial of",n,"is",result)

"""
OUTPUT:
Enter the number:
3
Factorial of 3 is 6

"""
