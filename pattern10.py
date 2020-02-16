#This program prints stars in right angled triangle pattern.
num = int(input("Enter the number of rows:"))

row = 0
while row<num:
    star = row+1
    while star>0:
        print("*",end="")
        star = star-1
    row = row+1
    print()

"""
OUTPUT:
Enter the number of rows:6
*
**
***
****
*****
******

"""
