#This program prints stars in hollow equilateral triangle.
num=int(input("Enter the number of rows:\n"))

for i in range(1,num+1):
    for j in range(1,num*2):
        if i==num  or i+j==num+1 or j-i==num-1:
            print("*",end="")
        else:
            print(end=" ")
    print()

"""

OUTPUT:
Enter the number of rows:
6
     *
    * *
   *   *
  *     *
 *       *
***********

"""
