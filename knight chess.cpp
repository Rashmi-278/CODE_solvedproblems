#include <stdio.h>
#include<stdlib.h>
#include<string.h>
#include <iostream>
using namespace std;
 #define LI long int

/*
Abhineet the Chess master of NIT Kurukshetra got bored of 8x8 chess board and invented the new variation of Chess, the one on an infinite chess board. There is only a white king and N black knights. The white king has to avoid checkmate as long as it can.

A situation is given. Determine if white king is in checkmate or not. The white king is in checkmate if and only if it is in check and it is not able to move to any of its neighboring positions which is not in check.

Input:
The first line will contain T, number of test cases. Then the test cases follow.
The first line of each test case contains a single integer N.
The next N line contains 2 space-separated integers Xi and Yi denoting the position of knights.
The next line contains 2 space-separated integers A and B denoting the position of king

*/
int main()
{
    LI x[10000],y[10000],x_king,y_king,i,j,T,N;
    cin>>T;
    bool flag=true;
    
    while(T--)
    {
    flag=false;
    cin>>N;
    
    for(LI p=0;p<N;p++)
    {
        cin>>x[p]>>y[p];
        
    }
    cin>>x_king>>y_king;
    
    for(LI p=0;p<N;p++)
    {
        x[p]=abs(x[p]-x_king);
        y[p]=abs(y[p]-y_king);
        
        if(x[p]==1|x[p]==2 && (x[p]+y[p]==3))
        {
            flag=true;
            break;
        }
    }
    if(flag)
        cout<<"YES\n";
    else
        cout<<"NO\n";
    
    }

}