//This program gets input from user and prints its sqaure value.
#include<stdio.h>
int main()
{
int number;
printf("enter a number:");
scanf("%d",&number);
// %d is used to print the signed integer value where signed integer means that the variable can hold both positive and negative values.
printf("Square of number is:%d ",number*number);
return 0;
}
