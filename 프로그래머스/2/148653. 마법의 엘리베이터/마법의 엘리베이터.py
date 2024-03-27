def solution(storey):
    cnt = 0
    while storey != 0:
        n = storey % 10
        if n < 5:
            cnt += n
            storey //= 10
            continue

        if n > 5:
            cnt += 10 - n
            storey = storey // 10 + 1
            continue

        if n == 5:
            # 앞 숫자
            front = storey // 10 % 10
            if front < 5:
                cnt += 5
                storey //= 10
                continue
            elif front >= 5:
                storey = storey // 10 + 1
                cnt += 5
                continue
                
    return cnt  
