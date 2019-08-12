#convert to base 9
#https://www.hackerearth.com/practice/math/number-theory/basic-number-theory-1/practice-problems/algorithm/can-you-guess-1/#c193514
def solve(x):
    if x<9:
        return x
    return x%9 +10*solve(x//9)
from sys import stdin as inp
N = inp.read().split()
for i in N:
    print(solve(int(i)))

