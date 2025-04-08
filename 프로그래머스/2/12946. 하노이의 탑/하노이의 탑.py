def solution(n):
    answer = []
    def recur(s, e, other, n):
        if n == 1:
            answer.append([s, e])
            return
        
        recur(s, other, e, n - 1)
        recur(s, e, other, 1)
        recur(other, e, s, n - 1)
        
    recur(1, 3, 2, n)
    
    return answer
        
    