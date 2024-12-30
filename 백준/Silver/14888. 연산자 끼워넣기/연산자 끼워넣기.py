import sys

input = sys.stdin.readline

n = int(input())
arr = [int(i) for i in input().split()]
oper = [int(i) for i in input().split()]
calc_fun = [
    lambda x: x[0] + x[1],
    lambda x: x[0] - x[1],
    lambda x: x[0] * x[1],
    lambda x: int(x[0] / x[1]),
]


def permu():
    li = [float("inf"), -float("inf")]

    def recur(order, calcv):
        if order == len(arr):
            li[0] = min(li[0], calcv)
            li[1] = max(li[1], calcv)
            return

        for i in range(4):
            if oper[i] > 0:
                oper[i] -= 1
                ncalcv = calc_fun[i]((calcv, arr[order]))
                recur(order + 1, ncalcv)
                oper[i] += 1

    recur(1, arr[0])
    return li


def main():
    for a in permu()[::-1]:
        print(a)


main()
