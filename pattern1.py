#This program prints numbers in right angle triange.
n=int(input("Enter the number of rows:"))
for i in range(1,n+1): #this for loop condition is implemented for rows
    for j in range(1,i+1):  #this for loop condition is implemented for coloumns
        print(j,end="")
    print()
"""
output:
Enter the number of rows:9
1
12
123
1234
12345
123456
1234567
12345678
123456789

"""
