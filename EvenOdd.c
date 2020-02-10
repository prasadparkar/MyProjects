//This program checks whether the given input is even no. or odd no.
#include<stdio.h>
int main()
{
int number=0;
printf("Enter a number:");
scanf("%d",&number);

if(number%2==0) //If the number is divisible by 2, it prints the following output.
  {
    printf("%d is even number",number);
  }

else  //If the number is not divisible by 2, it prints the following output.
  {
    printf("%d is odd number",number);    
  }
return 0;
}
