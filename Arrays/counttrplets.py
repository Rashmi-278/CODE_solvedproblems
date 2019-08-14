#https://practice.geeksforgeeks.org/problems/count-the-triplets/0
def triplets(arr, n):
    arr.sort()
    arr_set = set(arr)
    max_ele = arr[-1]
    res = 0
    for i in range(n-1):
        for j in range(i+1, n-1):
            s = arr[i]+arr[j]
            if s > max_ele:
                break
            if s in arr_set:
                res += 1
    print(res if res>0 else -1)
    
if __name__=='__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        triplets(arr, n)
