def solution(num_list):
    A = "".join([str(i) for i in num_list if i % 2 == 0])
    B = "".join([str(i) for i in num_list if i % 2 == 1])
    
    return sum([int(A), int(B)])