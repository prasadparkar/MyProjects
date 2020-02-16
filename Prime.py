#This program prints whether the number is prime or not.
num=int(input("Enter the number to check whether its prime number or not:"))

if num>1:
    for i in range(2,num):
        if (num%i)==0:
            print(num,"is not a prime number.")
            break
        else:
            print(num,"is a prime number.")

"""

OUTPUT:
Enter the number to check whether its prime number or not:3
3 is a prime number.

"""
