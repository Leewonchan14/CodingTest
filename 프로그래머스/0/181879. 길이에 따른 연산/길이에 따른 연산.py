def solution(num_list):
    mul = 1
    for i in num_list:
        mul *= i
    return sum(num_list) if len(num_list) >= 11 else mul