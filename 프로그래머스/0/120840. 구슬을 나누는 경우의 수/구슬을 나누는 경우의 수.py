def solution(balls, share):
    mul1 = 1
    mul2 = 1
    for i in range(share, 0 , -1):
        mul1 *= balls
        balls -= 1
        mul2 *= i
    return int(mul1 / mul2)