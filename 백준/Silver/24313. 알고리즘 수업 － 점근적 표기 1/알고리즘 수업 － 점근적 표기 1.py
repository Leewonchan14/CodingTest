a,b = map(int, input().split())

c = int(input())

n_ = int(input())

if a <= c :
    if a*n_ + b <= c * n_:
        print(1)
    else:
        print(0)
else:
    print(0)
    