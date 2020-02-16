#This program prints repetitive numbers in right angle triange.
num=int(input("Enter the number of rows:"))
for i in range(num,0,-1): #this for loop condition is implemented for rows
    for n in range(1,i+1): #this for loop condition is implemented for coloumns
        print(i,end=" ")
    print()

"""

OUTPUT:
Enter the number of rows:6
6 6 6 6 6 6
5 5 5 5 5
4 4 4 4
3 3 3
2 2
1

"""
