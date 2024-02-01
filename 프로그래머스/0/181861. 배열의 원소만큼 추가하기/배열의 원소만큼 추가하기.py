def solution(arr):
    answer = []
    for i in arr:
        answer.extend([i for _ in range(i)])
        
    return answer