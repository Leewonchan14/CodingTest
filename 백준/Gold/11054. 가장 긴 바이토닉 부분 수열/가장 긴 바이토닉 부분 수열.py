def main(arr):
    dpl = [1] * len(arr)
    dpr = [1] * len(arr)

    for i in range(len(arr)):
        pre = [dpl[j] for j in range(i) if arr[j] < arr[i]]
        dpl[i] += max(pre) if pre else 0

    for i in range(len(arr) - 1, -1, -1):
        pre = [dpr[j] for j in range(i + 1, len(arr)) if arr[j] < arr[i]]
        dpr[i] += max(pre) if pre else 0

    return max([dpl[i] + dpr[i] for i in range(len(arr))]) - 1


import sys

input = sys.stdin.readline
input()

arr = [int(i) for i in input().split()]
print(main(arr))
