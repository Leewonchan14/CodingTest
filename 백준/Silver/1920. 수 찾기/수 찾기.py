import sys

input = sys.stdin.readline

n = int(input())
arr = [int(i) for i in input().split()]
arr.sort()

m = int(input())
arr2 = [int(i) for i in input().split()]

def main():
    dic = {}
    for i in arr:
        dic[i] = 0
    
    for i in arr2:
        if i in dic:
            print(1)
        else:
            print(0)
            
main()
