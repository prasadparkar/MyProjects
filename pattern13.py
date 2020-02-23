#this program prints numbers in pyramid pattern.
num = int(input("Enter the number of rows:"))

for i in range(1,num+1):
    for j in range(1,num+1-i):  #this for loop prints space at light side of triangle.
        print(end=" ")
    for j in range(i,0,-1):     #this for loop prints numbers on L.H.S. of triangle.
        print(j,end="")
    for j in range(2,i+1):      #this for loop prints number on R.H.S. of triangle.
        print(j,end="")
    print()

"""
OUTPUT:
Enter the number of rows:6
     1
    212
   32123
  4321234
 543212345
65432123456

"""
