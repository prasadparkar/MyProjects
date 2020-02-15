#This program prints repetitive numbers in right angle triange.
n=int(input("Enter the number of rows:"))
for i in range(1,n+1):  #this for loop condition is implemented for rows
    for j in range(1,i+1):  #this for loop condition is implemented for coloumns
        print(i,end="")
    print()

"""
OUTPUT:
Enter the number of rows:6
1
22
333
4444
55555
666666

"""    
