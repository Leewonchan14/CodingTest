def solution(s):
    count = 0
    zero_count = 0
    while s != "1":
        count += 1
        non_zero = list(filter(lambda x : x != "0", list(s)))
        length = len(non_zero)
        pre_length = len(s)
        
        zero_count += (pre_length - length)
        
        bin_length = bin(length)[2:]
        s = bin_length
    return [count, zero_count]
    
    