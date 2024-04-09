def solution(arr):
    ls = []
    for i in arr:
        if not ls or ls and ls[-1] != i:
            ls.append(i)
            
    return ls