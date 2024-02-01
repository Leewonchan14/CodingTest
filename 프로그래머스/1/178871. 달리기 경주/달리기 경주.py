def solution(players, callings):
    dic = {}
    for i in range(len(players)):
        dic[players[i]] = i
    
    for call in callings:
        index = dic[call]
        
        pre = players[index-1]
        
        players[index-1], players[index] = players[index], players[index - 1]
        
        dic[pre] = index
        dic[call] = index - 1
        
    return players