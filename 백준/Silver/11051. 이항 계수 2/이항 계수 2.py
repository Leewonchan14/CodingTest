def main(n, k):
    mul = 1
    stk = []
    while k > 0:
        mul = mul * n
        stk.append(k)
        while stk and mul % stk[-1] == 0:
            mul //= stk.pop()

        n -= 1
        k -= 1
    return mul % 10007


n, k = [int(i) for i in input().split()]
print(main(n, k))
