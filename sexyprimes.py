#https://www.geeksforgeeks.org/sexy-prime/

#code

def sexyprimes(l,r):
    prime = [True]*(r+1)
    
    p=2
    while(p*p<r):
        
        if prime[p] == True:
        
            for i in range(p*2,r+1,p):
                prime[i] = False
        p+=1
        
    for i in range(l,r-6+1):
        if(prime[i] and prime[i+6] is True):
            print(i,i+6,end=" ")
            
for i in range(int(input())):
    l,r=list(map(int,input().rstrip().split()))
    sexyprimes(l,r)

        
    
    
