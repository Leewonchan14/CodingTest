columns = {}
dig_x = {}
dig_y = {}
cnt = [0]
    
def track(num, M):
    if num == M:
        cnt[0] += 1
        return
    
    r = num
    
    for c in range(M):
        if c not in columns and r + c not in dig_x and r - c not in dig_y:
            columns[c] = 0
            dig_x[r+c] = 0
            dig_y[r-c] = 0
            track(num + 1, M)
            columns.pop(c)
            dig_x.pop(r+c)
            dig_y.pop(r-c)
            

def solution(n):
    track(0, n)
    
    return cnt[0]
    
    