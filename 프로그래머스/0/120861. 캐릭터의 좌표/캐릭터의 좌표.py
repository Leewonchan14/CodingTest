def solution(keyinput, board):
    dx = [0, -1, 0, 1]
    dy = [1, 0 ,-1, 0]
    
    dir = "up left down right".split()
    
    s1,s2 = 0,0
    c1,c2 = -(board[0] // 2), board[0] // 2
    d1,d2 = -(board[1] // 2), board[1] // 2
    
    
    dic = dict(zip(dir, zip(dx, dy)))
    for k in keyinput:
        a,b = dic[k]
        if  c1 <= s1 + a <= c2 and d1 <= s2 + b <= d2:
            s1 += a
            s2 += b
        
    return [s1,s2]