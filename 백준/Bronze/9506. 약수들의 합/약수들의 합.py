while True:
    n = int(input())
    if n == -1:
        break
    li = []
    for i in range(1, n):
        if i**2 >  n:
            break
        if n % i == 0:
            li.append(i)
            li.append(n // i)
    _sum = sum(li) - n
    if li[-1] == li[-2]:
        _sum -= li[-1]
        li.pop()
        
    li.sort()
    li.pop()
    if _sum == n :
        s = " + ".join(list(map(str, li)))
        print(f"{n} = {s}")
    else:
        print(f"{n} is NOT perfect.")
