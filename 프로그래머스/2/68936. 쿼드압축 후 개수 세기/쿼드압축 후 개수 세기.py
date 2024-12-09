# [0, 1] 갯수
def recursive(arr, y, x, l):
    if l == 1:
        if arr[y][x] == 0:
            return [1, 0]
        else:
            return [0, 1]
    
    temp = arr[y][x]
    isAllSame = True
    for ny in range(y, y + l):
        if not isAllSame:
            break
        for nx in range(x, x + l):
            if temp != arr[ny][nx]:
                isAllSame = False
                break
            
    if isAllSame and temp == 0:
        return [1, 0]
    elif isAllSame and temp == 1:
        return [0, 1]
    
    # 1
    r1_0, r1_1 = recursive(arr, y, x, l // 2)
    r2_0, r2_1 = recursive(arr, y, x + l // 2, l // 2)
    r3_0, r3_1 = recursive(arr, y + l // 2, x, l // 2)
    r4_0, r4_1 = recursive(arr, y + l // 2, x + l // 2, l // 2)
    
    return [r1_0 + r2_0 + r3_0 + r4_0, r1_1 + r2_1 + r3_1 + r4_1]
    

def solution(arr):
    return recursive(arr, 0, 0, len(arr))
    