#Missing number in array
'''Given an array C of size N-1 and given that there are numbers from 1 to N with one element missing, the missing number is to be found.

Input:
The first line of input contains an integer T denoting the number of test cases. For each test case first line contains N(size of array). The subsequent line contains N-1 array elements.

Output:
Print the missing number in array.

Constraints:
1 ≤ T ≤ 200
1 ≤ N ≤ 107
1 ≤ C[i] ≤ 107

Example:
Input:
2
5
1 2 3 5
10
1 2 3 4 5 6 7 8 10

Output:
4
9
'''

def getmissing (N,array):
    set1 = set([i for i in range(1,N+1)])
    set2 = set(array)
    return(set1.difference(set2))
T = int(input())
for i in range(T):
    size = int(input())
    arr = list(map(int,input().rstrip().split()))
    for i in list (getmissing(size,arr)):
         print(i)
    
    
    

