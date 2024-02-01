def solution(arr, n):
    answer = []
    if len(arr) % 2 == 1:
        answer = [arr[i] + n if i %2 ==0 else arr[i] for i in range(len(arr))]
    else :
        answer = [arr[i] + n if i %2 ==1 else arr[i] for i in range(len(arr))]
    return answer