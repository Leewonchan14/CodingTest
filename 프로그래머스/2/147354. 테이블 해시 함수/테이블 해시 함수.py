def sortKey(x, col):
    return (x[col - 1], 1 / x[0])


def bitwise(a, b):
    al = list(bin(a)[2:])
    bl = list(bin(b)[2:])
    result = [""] * max(len(al), len(bl))
    i = -1
    while i >= -max(len(al), len(bl)):
        if i >= -min(len(al), len(bl)):
            if al[i] != bl[i]:
                result[i] = "1"
            else:
                result[i] = "0"
        else:
            result[i] = al[i] if i >= -len(al) else bl[i]

        i -= 1

    return int("".join(result), 2)

def getMod(row_begin, row_end, data):
    result = []
    for i in range(row_begin - 1, row_end):
        key = list(map(lambda x: x % (i + 1), data[i]))
        result.append(sum(key)) 
        
    return result
    


def solution(data, col, row_begin, row_end):
    data.sort(key=lambda x: sortKey(x, col))
    li = getMod(row_begin, row_end, data)
    result = li[0]
    for i in range(1, len(li)):
        result = bitwise(result, li[i])
        
        
    return result
     
  
