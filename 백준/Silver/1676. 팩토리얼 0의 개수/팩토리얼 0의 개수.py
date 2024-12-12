def fact(n):
    def cnt(nn):
        cc = 0
        while nn % 5 == 0:
            cc += 1
            nn //= 5
        return cc

    return sum([cnt(i) for i in range(5, n + 1, 5)])


b = fact(int(input()))
print(b)
