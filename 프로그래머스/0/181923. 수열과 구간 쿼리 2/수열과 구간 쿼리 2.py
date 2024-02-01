def solution(arr, queries):
    answer = []
    for i in queries:
        temp = arr[i[0]:i[1] + 1]
        if i[2] not in temp :
            temp.append(i[2])
        temp.sort()
        
        if temp[-1] == i[2] :
            answer.append(-1)
            continue
            
        answer.append(temp[temp.index(i[2])+1])
        
    return answer
        