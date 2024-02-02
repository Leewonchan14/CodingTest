import sys
_li = []
while True:
    try:
        s = int(sys.stdin.readline())
        _li.append(s)
    except Exception:
        break
print(max(_li))
print(_li.index(max(_li))+1)