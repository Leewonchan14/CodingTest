import sys

sys.setrecursionlimit(10**9)


def recursion(n, li):
    i = 0
    while n != 1:
        pre = n
        i += 1
        if n % 2 == 0:
            n //= 2
        else:
            n *= 3
            n += 1

        li.append((pre + n) / 2)

    return li, i


def solution(k, ranges):
    li, n = recursion(k, [])
    
    answer = []
    for a,b in ranges:
        b = n + b
        if a > b:
            answer.append(-1)
            continue
        answer.append(sum(li[a:b]))
        
    return answer
    



