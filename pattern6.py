#This program prints string in right angled triangle pattern.
str=input("Enter a string:")
length= len(str)
for row in range(length):
    for col in range(row+1):
        print(str[col],end="")
    print()

"""

OUTPUT:
Enter a string:hello world
h
he
hel
hell
hello
hello
hello w
hello wo
hello wor
hello worl
hello world

"""
