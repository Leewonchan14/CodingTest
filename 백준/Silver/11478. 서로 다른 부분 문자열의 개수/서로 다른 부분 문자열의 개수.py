s = input()
_s = set()
for i in range(1, len(s) + 1):
    for j in range(len(s) + 1 - i):
        _s.add(s[j:j + i])

print(len(_s))
