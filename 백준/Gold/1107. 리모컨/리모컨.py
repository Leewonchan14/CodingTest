def canNum(n, canli):
    return all([int(i) in canli for i in str(n)])


def main(chanel, canli):
    minv = abs(100 - chanel)
    for i in range((10**6) + 1):
        if canNum(i, canli):
            key = len(str(i)) + abs(i - chanel)
            minv = min(key, minv)

    return minv


chanel = int(input())
cnt = input()

if int(cnt) != 0:
    broken = list(map(int, input().split()))
else:
    broken = []

canli = [i for i in range(10) if i not in broken]
print(main(chanel, canli))
