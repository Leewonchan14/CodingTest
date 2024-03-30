import sys

input = sys.stdin.readline


def machine_oper(stk, oper):
    if oper.startswith("NUM"):
        value = int(oper.split()[1])
        stk.append(value)
        return True

    if len(stk) == 0:
        return False

    if oper.startswith("POP"):
        stk.pop()
        return True

    if oper.startswith("INV"):
        stk[-1] *= -1
        return True

    if oper.startswith("DUP"):
        stk.append(stk[-1])
        return True

    if len(stk) < 2:
        return False

    if oper.startswith("SWP"):
        stk[-1], stk[-2] = stk[-2], stk[-1]
        return True

    f = stk.pop()
    b = stk.pop()

    if oper.startswith("ADD"):
        value = f + b
        stk.append(value)
        return -1000000000 <= value <= 1000000000

    if oper.startswith("SUB"):
        value = b - f
        stk.append(value)
        return -1000000000 <= value <= 1000000000

    if oper.startswith("MUL"):
        value = f * b
        stk.append(value)
        return -1000000000 <= value <= 1000000000

    if f == 0:
        return False

    if oper.startswith("DIV"):
        value = (abs(b) // abs(f))
        if b * f < 0:
            value *= -1
        stk.append(value)
        return -1000000000 <= value <= 1000000000

    if oper.startswith("MOD"):
        value = abs(b) % abs(f)
        if b < 0:
            value *= -1
        stk.append(value)
        return -1000000000 <= value <= 1000000000


first = input().rstrip()
while True:
    operations = []
    while first != "END":
        operations.append(first)
        first = input().rstrip()

    n = int(input())

    for _ in range(n):
        stk = [int(input())]
        for oper in operations:
            if not machine_oper(stk, oper):
                print("ERROR")
                break
        else:
            if len(stk) != 1:
                print("ERROR")
            else:
                print(stk[0])

    input()
    first = input().rstrip()
    if first == "QUIT":
        break
    print()
