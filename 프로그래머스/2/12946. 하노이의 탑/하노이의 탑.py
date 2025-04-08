def solution(n):
    answer = []
    def recur(s, e, n):
        o = 6 - s - e
        if n == 1:
            answer.append([s, e])
            return
        
        recur(s, o, n - 1)
        recur(s, e, 1)
        recur(o, e, n - 1)
        
    recur(1, 3, n)
    
    return answer
        
    