def solution(prices):
    answer = []
    n=len(prices)
    for i in range(n):
        c=0
        for j in range(i+1,n):
            if prices[j]<prices[i]:
                c+=1
                break
            c+=1
        answer.append(c)
    return answer