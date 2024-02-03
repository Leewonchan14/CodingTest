while True:
    a,b,c = map(int, input().split())
    if a ==b ==c == 0:
        break

    li = [a,b,c]
    if sum(li) - max(li) <= max(li):
        print("Invalid")
    elif a == b == c:
        print("Equilateral")
    elif a != b and b != c and c != a:
        print("Scalene")
    else:
        print("Isosceles")
        