import sys

while True:
    s = sys.stdin.readline().rstrip()
    li = []
    if s[0] == ".":
        break

    for _s in s:
        if _s != "(" and _s != ")" and _s != "[" and _s != "]":
            continue

        if len(li) == 0:
            li.append(_s)
            continue

        if _s == "(" or _s == "[":
            li.append(_s)

        if _s == ")":
            if li[-1] == "(":
                li.pop()
            else:
                break
        if _s == "]":
            if li[-1] == "[":
                li.pop()
            else:
                break
    if len(li) == 0:
        print("yes")
    else:
        print("no")

