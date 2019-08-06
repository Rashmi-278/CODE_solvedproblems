#https://practice.geeksforgeeks.org/problems/count-the-elements/0


def solve(b,ele):
    low = 0
    high = len(b) - 1
    ans = 0
    
    while(low<=high):
        mid = (low+high)//2
        if b[mid]<=ele:
            low = mid+1
            ans=max(ans,low)
        else:
            high = mid - 1
    
    return ans
   
            
T = int(input())
for i in range(T):
    N = int(input())
    A = list(map(int,input().rstrip().split()))
    b = list(map(int,input().rstrip().split()))
    b=sorted(b)
    nofq = int(input())
    for i in range(nofq):
        q=int(input())
        print(solve(b,A[q]))
