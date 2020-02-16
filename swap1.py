#This program executes swapping of two numbers without using third variable.
a = int(input("Enter the value for a:"))
b = int(input("Enter the value for b:"))

a = a+b
b = a-b
a = a-b
print("\nAfter swapping,")
print("value of a:",a)
print("value of b:",b)

"""
OUTPUT:
Enter the value for a:10

Enter the value for b:5

After swapping,
value of a: 5
value of b: 10

"""
