import sys

sys.setrecursionlimit(10**9)

spt = list("+-*")


def cal(o, a, b):
    a = int(a)
    b = int(b)
    if o == "*":
        return a * b

    if o == "+":
        return a + b

    return a - b


def order(li, result):
    if len(li) == 3:
        result.append(li[:])
        return result

    for s in spt:
        if s not in li:
            li.append(s)
            result = order(li, result)
            li.pop()

    return result


def split(exp, li):
    if not exp:
        return li

    i = 0
    while i < len(exp) and exp[i] not in spt:
        i += 1

    li.append(exp[:i])
    if i < len(exp) and exp[i] in spt:
        li.append(exp[i])
        i += 1

    return split(exp[i:], li)


def postorder(expression, orders):
    stk = []
    new_exp = []
    for e in expression:
        if e not in spt:
            new_exp.append(e)
            continue

        if not stk:
            stk.append(e)
            continue

        while stk and orders.index(stk[-1]) <= orders.index(e):
            new_exp.append(stk.pop())

        stk.append(e)

    while stk:
        new_exp.append(stk.pop())

    return new_exp


def calculate(expression, orders):
    post = postorder(expression, orders)
    stk = []
    for p in post:
        if p not in spt:
            stk.append(p)
            continue

        b = stk.pop()
        a = stk.pop()
        stk.append(cal(p, a, b))

    return stk[0]


def solution(expression):
    orders = order([], [])

    maxv = 0
    for o in orders:
        key = calculate(split(expression, []), o)
        maxv = max(maxv, abs(key))

    return maxv


# solution("100-200*300-500+20")
# print(calculate(split("100-200*300-500+20", []), ["*", "+", "-"]))
