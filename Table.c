//This program is to print table for the given number.
#include<stdio.h>
int main()
{
  int i=1,num=0;
  printf("Enter a number: ");
  scanf("%d",&num);

  do
  {
    printf("%d \n",(num*i));    
    i++;
  }

  while(i<=10);
  return 0;
}
