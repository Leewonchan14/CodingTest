def solution(genres, plays):
    dic = {}
    for i in range(len(genres)):
        dic[genres[i]] = dic.get(genres[i], [0, []])
        dic[genres[i]][0] += plays[i]
        dic[genres[i]][1].append((plays[i], i))
        
    rs = []
        
    for k,v in sorted(dic.items(),key=lambda x:-x[1][0]):
        v[1].sort(key=lambda x:(-x[0], x[1]))
        rs.append(v[1][0][1])
        if len(v[1]) >= 2:
            rs.append(v[1][1][1])
    return rs
        