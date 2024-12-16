def recur(n, m, li):
    if len(li) == m:
        print(" ".join([str(i) for i in li]))
        return
    
    for i in range(1, n + 1):
        li.append(i)
        recur(n, m, li)
        li.pop()

def main(n, m):
    recur(n, m, [])
    
n, m = map(int, input().split())
main(n, m)