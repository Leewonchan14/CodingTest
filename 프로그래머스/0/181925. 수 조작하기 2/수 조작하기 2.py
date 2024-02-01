def solution(numLog):
    sum = numLog[0]
    m = {1 : "w", -1 : "s", 10 : "d", -10 : "a"}
    answer = ""
    for i in range(1, len(numLog)):
        answer += m[numLog[i] - sum]
        sum = numLog[i]
        
    return answer
    