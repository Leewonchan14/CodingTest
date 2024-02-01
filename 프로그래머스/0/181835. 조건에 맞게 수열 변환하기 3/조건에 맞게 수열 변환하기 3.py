
    
def solution(arr, k):
    def mapper(v):
        return v * k if k % 2 == 1 else v + k
    
    return list(map(mapper,arr))