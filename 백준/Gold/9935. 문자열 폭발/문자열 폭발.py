import sys

input = sys.stdin.readline

str_ls = input().rstrip()
boom = input().rstrip()
boom_len = len(boom)

builder = []


def is_endswith(builder, boom, boom_len):
    if not builder:
        return False

    if len(builder) < boom_len:
        return False

    for i in range(-1, -boom_len - 1, -1):
        if builder[i] != boom[i]:
            return False
    else:
        return True


for s in str_ls:
    builder.append(s)
    while is_endswith(builder, boom, boom_len):
        for i in range(boom_len):
            builder.pop()

print("".join(builder) if builder else "FRULA")
