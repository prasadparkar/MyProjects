#This program gathers input from user and sorts number in ascending order.
print("Enter any 5 numbers of your choice.")
list1 = [int(input("Enter the number:")) for x in range(5)]
print("\nUnsorted list is:",list1)

for i in range(len(list1)):
    m_index = i     #consider number at zeroth index is minimum
    for j in range(i+1,len(list1)):
        if list1[j] < list1[m_index]:   #this if condition executes input in ascending order.
            m_index = j

    if (list1[i] != list1[m_index]):    #this if conditions swaps the numbers.
        list1[i],list1[m_index] = list1[m_index],list1[i]

print("\nSorted list is:",list1)

"""
OUTPUT:
Enter any 5 numbers of your choice.

Enter the number:12

Enter the number:64

Enter the number:36

Enter the number:75

Enter the number:54

Unsorted list is: [12, 64, 36, 75, 54]

Sorted list is: [12, 36, 54, 64, 75]

"""
