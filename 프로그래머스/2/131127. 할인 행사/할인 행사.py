def isCorrect(cur, want, number):
    return all([cur.get(want[i], 0) == number[i] for i in range(len(number))])
        

def solution(want, number, discount):
    cur = {}
    for i in range(10):
        cur[discount[i]] = cur.get(discount[i], 0) + 1
        
    i = 0
    cnt = 0
    while True:
        if isCorrect(cur, want, number):
            cnt += 1
            
        if i + 10 >= len(discount):
            break
            
        cur[discount[i + 10]] = cur.get(discount[i + 10], 0) + 1
        cur[discount[i]] -= 1
        i += 1
        
    return cnt
    
        