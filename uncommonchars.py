#https://practice.geeksforgeeks.org/problems/uncommon-characters/0/?ref=self

def solve(a,b):
    seta=set(a)
    setb=set(b)
    # "".join(seta.difference(setb)) + "".join(setb.difference(seta))
    v = seta.difference(setb) | setb.difference(seta)
    return "".join(sorted(v))
for i in range(int(input())):
    a=input()
    b=input()
    print(solve(a,b))
