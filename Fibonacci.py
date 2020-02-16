#This program prints Fibonacci series.
n=int(input("Enter how many numbers you want in series to be printed:"))
first=0
second=1

for i in range(n):
    print(first)
    temp = first
    first = second
    second = temp + second

"""

OUTPUT:
Enter how many numbers you want in series to be printed:10
0
1
1
2
3
5
8
13
21
34

"""
