https://www.hackerearth.com/practice/math/number-theory/basic-number-theory-1/practice-problems/algorithm/mystery-20/
#include <stdio.h>
#include <math.h>
int main()
{
  int t,n,i,j,ans;
  scanf("%d",&t);
  while(t--)
  { 
    scanf("%d",&n);
    ans=0,j=sqrt(n);
      if(n==0 || n==1) 
        printf("%d\n",n);
      else
      { 
        for(i=1;i<=j;i++)
          {
          if(n%i==0) ans++; 
          } 
        if(j*j==n) 
          printf("%d\n",2*ans-1);
        else
          printf("%d\n",2*ans);
    } 
  }
}
