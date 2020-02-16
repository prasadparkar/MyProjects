#This program prints numbers in right angle triange.
num=int(input("Enter the number of rows:"))
for i in range(num,0,-1): #this for loop condition is implemented for rows
    for n in range(1,i+1): #this for loop condition is implemented for coloumns
        print(n,end=" ")
    print()

"""

OUTPUT:

Enter the number of rows:6
1 2 3 4 5 6
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1

"""
