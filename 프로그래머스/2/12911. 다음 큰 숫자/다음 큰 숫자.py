def solution(n):
    bin_num = bin(n)
    zero_count = bin(n).count("1")
    next_n = n + 1
    while bin(next_n).count("1") != zero_count:
        next_n += 1
    return next_n 
        
    