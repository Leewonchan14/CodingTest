import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

n,k = map(int, input().split())
arr = [int(i) for i in input().split()]
arr.sort()

def main():
    li = []
    def recur():
        if len(li) == k:
            print(*[arr[i] for i in li])
            return
        visited = [] 
        for i in range(n):
            if i not in li and arr[i] not in visited:
                visited.append(arr[i])
                li.append(i)
                recur()
                li.pop()
                
    recur()

main()