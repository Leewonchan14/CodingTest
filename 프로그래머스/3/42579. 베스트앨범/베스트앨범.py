def solution(genres, plays):
    dic = {}
    cnt = {}
    result = []
    
    for i in range(len(genres)):
        dic[genres[i]] = dic.get(genres[i], {})
        dic[genres[i]][i] = plays[i]
        cnt[genres[i]] = cnt.get(genres[i], 0) + plays[i]
        
    for k in sorted(cnt.keys(), key=lambda x: 1 / cnt[x]):
        v = list(dic[k].items())
        v.sort(key=lambda x: (1 / x[1], x[0]))
        
        cnt = 0
        
        for i, v in v:
            result.append(i)
            cnt += 1
            if cnt == 2:
                break
        
    
    return result
        
    