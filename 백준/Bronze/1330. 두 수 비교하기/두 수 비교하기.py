a , b = map(int, input().split())
    
s = "<" if a < b else ">"
if a == b:
    s = "=="
print(s)