a, b = map(int, input().split())
_set = set([input() for _ in range(a)])
print(len(list(filter(lambda v : v in _set, [input() for _ in range(b)]))))