def main(n):
    li = []
    def recur(k):
        if k == n:
            print(" ".join([str(i) for i in li]))
            return
        
        for i in range(1, n + 1):
            if i not in li:
                li.append(i)
                recur(k + 1)
                li.pop()
                
    recur(0)
            

n = int(input())
main(n)