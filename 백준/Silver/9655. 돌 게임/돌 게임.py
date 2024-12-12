mapper = {"f": "b", "b": "f"}
key = [0, "f", "b", "f", "b"]


def recur(n, who):
    if n < len(key):
        return key[n] == who

    return recur(n - 4, who)


print("SK" if recur(int(input()), "f") else "CY")
