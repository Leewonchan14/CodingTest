def solution(binomial):
    B = binomial.split()
    a = B[0]
    op = B[1]
    b = B[2]
    if op == "+":
        return int(a) + int(b)
    
    if op == "-":
        return int(a) - int(b)
    
    if op == "*":
        return int(a) * int(b)