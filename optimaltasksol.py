#optimal task assignment
arr = [6,3,2,7,5,5] 
def minsumarray(a):
    a=sorted(a)
    for i in range(len(a)//2):
        print(a[i],a[~i])
minsumarray(arr)
    
