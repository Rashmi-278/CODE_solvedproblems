#https://practice.geeksforgeeks.org/problems/check-set-bits/0

'''

def solve (a) :
    # approach 1
    for i in a:
        if i != '1':
            return "NO"
    return "YES"
    
    #approach 2
    if not (n&n+1):
        return "YES"
    else:
        return "NO"
    
T = int(input())
for _ in range(T):
     #N = str(bin(int(input())))
    n = int(input())
    print(solve(n))

'''
for _ in range(int(input())):
    n = int(input())
    print("YES") if not (n&n+1) else print("NO")




