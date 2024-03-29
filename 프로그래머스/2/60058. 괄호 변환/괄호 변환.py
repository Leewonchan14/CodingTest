from collections import deque


def is_collect(s):
    stk = []
    index = 0
    while index < len(s):

        if not stk or s[index] == "(":
            stk.append(s[index])
            index += 1
            continue

        if s[index] == ")":
            index += 1
            stk.pop()

    return len(stk) == 0


def div_blance(s):
    count_9 = 0
    count_0 = 0
    index = 0
    flag = False
    while index < len(s):
        if s[index] == "(":
            count_9 += 1
        elif s[index] == ")":
            count_0 += 1

        index += 1
        if count_9 == count_0:
            flag = True
            break

    if flag and len(s) != index:
        return s[:index], s[index:]

    if flag and len(s) == index:
        return s, ""


def dfs(s):
    mapper = {"(": ")", ")": "("}

    if s == "":
        return s

    if is_collect(s):
        return s

    u, v = div_blance(s)

    if is_collect(u):
        return u + dfs(v)

    a = "(" + dfs(v) + ")"
    b = "".join(list(map(lambda x: mapper[x], list(u[1:-1]))))

    return a + b


def solution(p):
    return dfs(p)

# print(solution(")("))
