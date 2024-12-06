def solution(elements):
    dic = {}
    for i in range(len(elements)):
        size = sum(elements[:i])
        dic[size] = 0
        for k in range(len(elements)):
            size -= elements[k]
            size += elements[(k + i) % len(elements)]
            dic[size] = 0
    return len(dic.keys())