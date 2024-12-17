def permu(n):
    li = []
    result = []
    
    def recur():
        if len(li) == n:
            result.append(li[:])
            return
        
        for i in range(n):
            if i not in li:
                li.append(i)
                recur()
                li.pop()
                
    recur()
    return result

def calc(arr):
    sumv = 0
    for i in range(len(arr) - 1):
        sumv += abs(arr[i] - arr[i + 1])
        
    return sumv
        

def main(n, arr):
    maxv = -float('inf')
    for li in permu(n):
        maxv = max(maxv, calc([arr[i] for i in li]))
        
    return maxv
        

n = int(input())
arr = [int(i) for i in input().split()]

print(main(n, arr))