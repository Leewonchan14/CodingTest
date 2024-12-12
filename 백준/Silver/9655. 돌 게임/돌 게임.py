mapper = {"f": "b", "b": "f"}
key = [0, "f", "b", "f", "b"]


def recur(n, who):
    while n >= len(key):
        n -= 4

    return key[n] == who


print("SK" if recur(int(input()), "f") else "CY")
