#https://www.hackerearth.com/challenges/competitive/she-codes-indeed-challenge-2019/algorithm/divisibe-or-2d8e196a/

def solve (A):
    first,last=[],[]
    for i in range(len(A)//2):
        first.append(A[i][0])
    for i in range(len(A)//2,len(A)):
        last.append(A[i][-1])
    full="".join(first)+"".join(last)
    
    if int(full)%11==0:
        return "OUI"
    else:
        return "NON"
    

N = int(input())
A = list(map(str, input().split()))

out_ = solve(A)
print (out_)
