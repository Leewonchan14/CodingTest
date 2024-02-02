n = int(input())
for i in range(n):
     s = " " * (n - 1 - i) + "*" + "**" * i
     print(s)
    
for i in range(n-2,-1,-1):
    s = " " * (n - 1 - i) + "*" + "**" * i
    print(s)