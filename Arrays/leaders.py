'''Leaders in an array'''
''' Given an array of positive integers. Your task is to find the leaders in the array.
Note: An element of array is leader if it is greater than or equal to all the elements to its right side. Also, the rightmost element is always a leader. 

Input:
The first line of input contains an integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains a single integer N denoting the size of array.
The second line contains N space-separated integers A1, A2, ..., AN denoting the elements of the array.

Output:
Print all the leaders.

Constraints:
1 <= T <= 100
1 <= N <= 107
0 <= Ai <= 107

Example:
Input:
3
6
16 17 4 3 5 2
5
1 2 3 4 0
5
7 4 5 7 3
Output:
17 5 2
4 0
7 7 3 '''


def leader(a,n):
    maxx=-1
    l=[]
    for i in range(n-1,-1,-1):
        if a[i]>=maxx:
            maxx=a[i]
            l.append(maxx)
    
    length=len(l)
    for i in range(length-1,-1,-1):
        print(l[i],end=' ')
    print()
    
    
    
t=int(input())
for i in range(t):
    n=int(input())
    arr=[int(x) for x in input().split()]
    leader(arr,n)
    
    #commented
    '''sol = [arr[-1],]
    maxfromright = arr[-1]
    for i in range(N-2,0,-1):
        if arr[i]>maxfromright:
            sol.append(arr[i])
            maxfromright=arr[i]
    
    
    
    return sol[::-1] '''
    #commented
    '''   
T = int(input())
for _ in range(T):
    N=int(input())
    arr = list(map(int,input().rstrip().split()))
    print( " ".join(map(str,leader(N,arr))) ) 
    '''
    
