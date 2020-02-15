#This program executes Factorial numberr using for loop.
n= int(input("Enter the number:\n"))
result=1
for i in range(n,0,-1):
    result=result*i

print("Factorial of",n,"is",result)

"""

OUTPUT:
Enter the number:
7
Factorial of 7 is 5040

"""  
