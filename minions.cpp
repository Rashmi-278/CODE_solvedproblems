#include<iostream>
using namespace std;
/*
    mutated minion problem - codechef
    https://www.codechef.com/FLMOCK01/problems/CHN15A
T-number of test cases
N-number of minions
n[]-array of initail charterstics value of N minions
K-value added by transmorgifier
m[]=n[]+k
count-number of wolverine like minions
*/
int main()
{
int T,N,K,count=0;
int n[100],m[100];
cin>>T;
while(T--)
{
    cin>>N>>K;
    for(int i=0;i<N;i++)
    {   cin>>n[i];
        m[i]=n[i]+K;
    }
    for(int i=0;i<N;i++)
    {
        if((m[i]%7)==0)
            count++;
        
    }
    cout<<count;
    
}//while

}//main