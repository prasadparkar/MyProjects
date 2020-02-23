#This program prints number of vowels present in a sentence.
snt= input("Type a sentence here:")
str= snt.lower()
count= 0
list1= ["a","e","i","o","u"]

for char in str:
    if char in list1:
        count= count+1

print("Number of vowels in given sentence:",count)

"""
OUTPUT:
Type a sentence here:I love my India.
Number of vowels in given sentence: 6

"""
