def main(s):
    if s.count("0") == 0:
        return -1

    key = [int(i) for i in s]

    if sum(key) % 3 != 0:
        return -1

    key.sort(reverse=True)

    return "".join([str(ss) for ss in key])


# print(sum([int(i) for i in list("8875542")]))
print(main(str(int(input()))))
