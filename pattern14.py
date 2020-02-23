#this program prints numbers in pyramid pattern using format function.
num = int(input("Enter the number of rows:"))

for i in range(1,num+1):
    for j in range(1,num+1-i):  #this for loop prints space at light side of triangle.
        print(format(" ","<3"),end="")
    for j in range(i,0,-1):     #this for loop prints numbers on L.H.S. of triangle.
        print(format(j,"<3"),end="")
    for j in range(2,i+1):      #this for loop prints number on R.H.S. of triangle.
        print(format(j,"<3"),end="")
    print()

"""
OUTPUT:

Enter the number of rows:9
                        1
                     2  1  2
                  3  2  1  2  3
               4  3  2  1  2  3  4
            5  4  3  2  1  2  3  4  5
         6  5  4  3  2  1  2  3  4  5  6
      7  6  5  4  3  2  1  2  3  4  5  6  7
   8  7  6  5  4  3  2  1  2  3  4  5  6  7  8
9  8  7  6  5  4  3  2  1  2  3  4  5  6  7  8  9

""""
