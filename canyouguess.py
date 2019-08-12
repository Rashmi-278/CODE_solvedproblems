#https://www.hackerearth.com/practice/math/number-theory/basic-number-theory-1/practice-problems/algorithm/can-you-guess/

# Print the sum of its divisors
def translate(n):
    sol = 0
    for i in range(1,n):
        if n%i==0:
            sol+=i
            
    return sol
    
for _ in range(int(input())):
    n = int(input())
    print(translate(n))
    

