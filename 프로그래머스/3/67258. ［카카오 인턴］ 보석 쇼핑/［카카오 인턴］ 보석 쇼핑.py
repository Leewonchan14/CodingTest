def solution(gems):
    left = 0
    right = 0
    size = len(set(gems))
    
    dic = {}
    r = []
    
    while True:
        
        # 오른쪽 쭉 뻗기
        while right < len(gems) and len(dic) != size:
            dic[gems[right]] = dic.get(gems[right] , 0) + 1
            right += 1

        # 왼쪽 쭉 밀기
        while left < len(gems) and gems[left] in dic and dic[gems[left]] > 1 and left <= right:
            dic[gems[left]] -= 1
            if dic[gems[left]] == 0:
                dic.pop(gems[left])
            left += 1
            
        # size가 맞으면 추가
        if size == len(dic):
            r.append([left, right])
        
        # right가 남으면 +1
        if right < len(gems):
            dic[gems[right]] = dic.get(gems[right], 0) + 1
            right += 1
        # 안남으면 break
        else:
            break
    
    r.sort(key=lambda x : x[1] - x[0])
    return [r[0][0] + 1, r[0][1]]
        
        
        
        
        