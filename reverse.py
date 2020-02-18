#This program prints reverse string of input.
def reverse(string):
    revString = ""

    for i in string:
        revString = i + revString
    print("Reversed string of", string, "is", revString)

string = input("Enter a string:\n")
reverse(string)

"""
Enter a string:
mad
Reversed string of mad is dam

"""
