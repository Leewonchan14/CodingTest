import sys

input = sys.stdin.readline
n = int(input())
arr = [int(i) for i in input().split()]
oper = [int(i) for i in input().split()]

calc_fun = [lambda x: x[0] + x[1], lambda x: x[0] - x[1], lambda x: x[0] * x[1], lambda x: int(x[0] / x[1])]


def main():
    li = [-float('inf'), float('inf')]
    def recur(order, calcv):
        if order == len(arr):
            li[0], li[1] = max(li[0], calcv), min(li[1], calcv)
            return
        
        for i in range(4):
            if oper[i] > 0:
                oper[i] -= 1
                recur(order + 1, calc_fun[i]((calcv, arr[order])))
                oper[i] += 1
                
    recur(1, arr[0])
    
    print(li[0])
    print(li[1])

main()