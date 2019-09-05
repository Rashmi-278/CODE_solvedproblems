#Algorithm to find prime numbers upto N
#If N = 16 prime numbers upto 15 will be printed

def Sieveofsundaram(n):
    k = int((n-2)/2)
    a = [0]*(k+1)
    for i in range(1,k+1):
        j=i
        while(i+j+2*i*j<=k):
            a[i+j+2*i*j]=1 
            j+=1 
        if (n>2):
            print(2," ")
        for i in range(1,k+1):
            if a[i] == 0:
                print(2*i+1, " ")
n =120
Sieveofsundaram(n)
