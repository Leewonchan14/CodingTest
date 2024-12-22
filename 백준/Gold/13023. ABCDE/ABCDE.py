import sys
input = sys.stdin.readline

def main(n, dic):
    li = []
    def dfs(start, k):
        if k == 5:
            return True
        
        for nn in dic[start]:
            if nn not in li:
                li.append(nn)
                ret = dfs(nn, k + 1)
                if ret:
                    return ret
                li.pop()
                
    for i in range(n):
        li.clear()
        li.append(i)
        if dfs(i, 1):
            return 1
    
    return 0
    
n, tc = map(int, input().split())

dic = {i: [] for i in range(n)}
for _ in range(tc):
    a,b = map(int, input().split())
    dic[a].append(b)
    dic[b].append(a)
    
print(main(n, dic))