def main(a, b, c):
    if a == b == c:
        return a

    def nextOne(li):
        li[0] = (li[0]) % 15 + 1
        li[1] = (li[1]) % 28 + 1
        li[2] = (li[2]) % 19 + 1

    def check(abc, li):
        return all([abc[i] == li[i] for i in range(3)])

    cnt = 1
    li = [1, 1, 1]

    while not check((a, b, c), li):
        nextOne(li)
        cnt += 1

    return cnt


a, b, c = map(int, input().split())
print(main(a, b, c))
