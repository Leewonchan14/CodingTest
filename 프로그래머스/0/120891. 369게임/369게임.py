def solution(order):
    return sum([str(order).count("3"),str(order).count("6"),str(order).count("9")])