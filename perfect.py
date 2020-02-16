#This program is to check entered number is Perfect or not.
num = int(input("Enter the number:"))
result = 0
for i in range (1,num):
    if (num%i)==0:
        result = result+i

if result==num:
    print(num,"is perfect number.")

else:
    print(num,"is not perfect number.")

"""

OUTPUT:
Enter the number:6
6 is perfect number.

"""
