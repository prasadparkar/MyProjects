#This program prints stars in hollow right angle triangle.
num=int(input("Enter the number of rows:\n"))
for i in range(num): #this for loop condition is implemented for rows
    for n in range(num): #this for loop condition is implemented for coloumns

        if n==0 or i==(num-1) or i==n:
            print("*",end="")

        else:
            print(end=" ")
    print()

"""
OUTPUT:
Enter the number of rows:
6
*
**
* *
*  *
*   *
******

"""
