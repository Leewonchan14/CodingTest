def solution(array, height):
    array.sort()
    
    for i in range(0, len(array)):
        if array[i] > height:
            return len(array) - i
    
    return 0