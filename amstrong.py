#This program prints Amstrong number between 1 to 100.
for i in range(101):
    num=i
    result=0
    n=len (str(i))

    if (i!=0):
        digit=i%10
        result=result+digit**n
        i=i//10

    if num==result:
        print(result)

"""
OUTPUT:
0
1
2
3
4
5
6
7
8
9
25
36

"""
