import sys
while True:
    try:
        s = sys.stdin.readline()
        print(s.rstrip())
        if s[-1] != "\n":
            break
    except Exception:
        break
        