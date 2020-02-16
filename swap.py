#This program executes swapping of two numbers using third variable.
a = int(input("Enter the value for a:"))
b = int(input("Enter the value for b:"))

temp = a
a = b
b = temp
print("\nAfter swapping,")
print("value of a:",a)
print("value of b:",b)

"""
OUTPUT:
Enter the value for a:10

Enter the value for b:20

After swapping,
value of a: 20
value of b: 10

"""
