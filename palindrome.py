#This program lets you know whether given input string is palindrome or not.
str = input("Enter a string:\t")

revStr = str[::-1]
print("Its reverse string is:",revStr)

if str == revStr:
    print("\nThe given string is Palindrome.")
else:
    print("\nThe given string is not Palindrome.")

"""
OUTPUT:
Enter a string:	malayalam
Its reverse string is: malayalam

The given string is Palindrome.

"""
