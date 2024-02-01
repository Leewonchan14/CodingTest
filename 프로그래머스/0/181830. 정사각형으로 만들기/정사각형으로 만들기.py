def solution(arr):
    ro = len(arr)
    co = len(arr[0])
    if len(arr[0]) == len(arr):
        return arr
    
    # 행이 많음
    if len(arr[0]) < len(arr):
        for col in arr:
            for i in range(ro - co):
                col.append(0)
    
    # 열이 많음
    if len(arr[0]) > len(arr):
        for i in range(len(arr[0]) - len(arr)):
            arr.append([0 for _ in range(len(arr[0]))])
    
    return arr