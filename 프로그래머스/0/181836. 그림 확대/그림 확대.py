def solution(picture, k):
    def mapper(v):
        a = "".join([i * k for i in v])
        return [a for _ in range(k)]
    
    return sum(map(mapper, picture), [])
        
        