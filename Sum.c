
//This program takes input from user and prints sum of two nos.
#include<stdio.h>
int main()
{
int x=0,y=0,result=0;

printf("Enter first number:");
scanf("%d",&x);
printf("Enter second number:");
scanf("%d",&y);
// %d is used to print the signed integer value where signed integer means that the variable can hold both positive and negative values.

result=x+y;
printf("Sum of two numbers:%d ",result);

return 0;
}
