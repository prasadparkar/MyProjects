//This program is to calculate the grade of the students.
#include <stdio.h>
int main()
{
    int marks;
    printf("hello! Enter your marks.");
    scanf("%d",&marks);

    if(marks > 85 && marks <= 100)
    {
        printf("Excellent! You scored grade A.");
    }

    else if (marks > 60 && marks <= 85)
    {
        printf("Very Good! You scored grade B.");
    }

    else if (marks > 40 && marks <= 60)
    {
        printf("Good! You scored grade C.");
    }
    else if (marks > 30 && marks <= 40)
    {
        printf("Need Improvement! You scored grade D.");
    }

    else
    {
        printf("Sorry you are fail.");
    }
}
