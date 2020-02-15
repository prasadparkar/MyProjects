#This program prints number in Floyd's triangle pattern.
num=int(input("Enter the number of rows:"))
n=1
for i in range(1,num+1): #this for loop condition is implemented for rows
    for j in range(1,i+1): #this for loop condition is implemented for coloumns
        print(n,end=" ")
        n=n+1
    print()

"""

OUTPUT:
Enter the number of rows:5
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15

"""
