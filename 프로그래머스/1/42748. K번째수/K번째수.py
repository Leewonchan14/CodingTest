def solution(array, commands):
    ls = []
    for i,j,k in commands:
        ls.append(sorted(array[i - 1:j])[k-1])
        
    return ls