plus_minus = ["+", "-"]
isMinus = 1
s = input()
num = ""
_sum = 0
for i, e in enumerate(s):
    # 숫자 라면
    if e not in plus_minus:
        num += e
        continue

    # +, - 라면
    # 이전 숫자 만들기
    pre_num = int(num)

    _sum += isMinus * pre_num

    num = ""

    # + 라면
    if e == "+":
        continue

        # - 라면
    if e == "-":
        isMinus = -1

_sum += isMinus * int(num)

print(_sum)
