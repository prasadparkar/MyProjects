#This program prints numbers in spiral pattern
num= int(input("Enter the number of rows:"))
n_list= [[0 for x in range (num)] for y in range (num)]
n= 1
low= 0
high= num-1
count= int((num+1)/2)
for i in range(count):
    for j in range(low,high+1): #this for loop executes upper horizontal  line
        n_list[i][j]= n
        n= n+1

    for j in range (low+1,high+1):  #this for loop executes right outer vertical line
        n_list[j][high]= n
        n= n+1

    for j in range(high-1,low-1,-1):    #this for loop executes lower horizontal line
        n_list[high][j]= n
        n= n+1

    for j in range(high-1,low,-1):  #this for loop executes left outer vertical line
        n_list[j][low]= n
        n=n+1

    low= low+1
    high=high-1

for i in range (num):   #this for loop executes the final result
    for j in range (num):
        print (n_list[i][j],end="\t")
    print()

"""
OUTPUT:
Enter the number of rows:3
1       2       3
8       9       4
7       6       5

"""
