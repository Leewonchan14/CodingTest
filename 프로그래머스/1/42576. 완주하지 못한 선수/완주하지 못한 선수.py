def solution(participant, completion):
    dic = {}
    for com in completion:
        dic[com] = dic.get(com, 0) + 1
    
    for par in participant:

        if par in dic:
            if dic[par] >= 2:
                dic[par] = dic[par] - 1
            else:
                dic.pop(par)
        else:
            return par
                
            