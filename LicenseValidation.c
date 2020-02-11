//this program is to check if user is eligble for driving license test.
#include <stdio.h>
int main()
{
    int age;
    printf("hi!\nEnter your age.");
    scanf("%d",&age);

    if(age>=18)
    {
        printf("Great!You are eligible for driving license test.");
    }

    else
    {
        printf("Sorry... you're underage.");
    }
}
