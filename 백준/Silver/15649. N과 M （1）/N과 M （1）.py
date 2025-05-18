import sys
input = sys.stdin.readline

n, m = map(int, input().split())

def main():
    li = []
    def recur():
        if len(li) == m:
            print(*li)
            return
        
        for i in range(1, n + 1):
            if i in li:
                continue
            li.append(i)
            recur()
            li.pop()
    
    recur()
    
    
main()
    

