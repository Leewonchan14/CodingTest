import sys
sys.setrecursionlimit(10 ** 9)

def gcm(a, b):
    def ddir(k, a ,b, acc):
        if k > a and k > b:
            return acc * a * b
        
        nK = k + 1
        
        if a % k ==0 and b % k == 0:
            a /= k
            b /= k
            acc *= k
            nK = k
            
        return ddir(nK, a, b, acc)
    
    return ddir(2, a, b, 1)


def recursion(li):
    if len(li) == 1:
        return li[0]
    
    li.append(gcm(li.pop(), li.pop()))
    
    return recursion(li)
    


def solution(arr):
    return recursion(arr)