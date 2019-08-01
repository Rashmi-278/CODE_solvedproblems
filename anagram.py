s1="abcd"
s2="dcba"
from collections import Counter
s1=s1.replace(" ","").lower()
s2=s2.replace(" ","").lower()
 # this requires nlogn time because of sorting
print(sorted(s1)==sorted(s2))
#optmised
def isanagram(s1,s2):
    if len(s1) != len(s2):
        return False
    a=Counter(s1)
    b=Counter(s2)
    
    if a == b:
        return True
        
print(isanagram(s1,s2))
