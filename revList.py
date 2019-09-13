#https://www.hackerearth.com/practice/data-structures/linked-list/singly-linked-list/practice-problems/algorithm/reversed-linked-list-01b722df/

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedList:
    def __init__ (self):
        self.head = None
    def append(self,data):
        newNode = Node(data)
        if (self.head is None):
            self.head = newNode
        lastNode = self.head
        while (lastNode.next):
            lastNode = lastNode.next
        lastNode.next = newNode
    def printList(self):
        lastNode = self.head
        while(lastNode):
            print(lastNode.data)
            lastNode = lastNode.next

def solve(a):
    flip = False
    res = []
    dummy = []
    for i in a:
        if i%2 == 0:
            flip = True
            if flip:
                dummy.append(i)
        else:
            if flip:
                res.extend(dummy[::-1])
                dummy =  []
                flip = False
            res.append(i)

    if dummy is not []:
        res.extend(dummy[::-1])
    for i in res:
        print(i , end =' ')
        
N = int(input())
arr = list(map(int,input().split()))
solve(arr)


    
    
