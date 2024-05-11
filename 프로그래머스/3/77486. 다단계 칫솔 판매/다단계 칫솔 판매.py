"""
enroll = 모든 노드 이름
referral = 부모노드의 이름
seller = 판매한 사람들의 목록
amount = 얼만큼 팔았는지

return : enroll 이름 순서대로 이익 리스트 반환
"""

import math

def solution(enroll, referral, seller, amount):
    parents = {}
    money = {}
    
    for i in range(len(enroll)):
        if referral[i] == "-":
            parents[enroll[i]] = "center"
            continue
        parents[enroll[i]] = referral[i]
        
    for i in range(len(seller)):
        k = seller[i]
        v = amount[i]
        v *= 100
        while k in parents and v >= 10:
            par_v = v // 10
            v -= par_v
            money[k] = money.get(k, 0) + v
            k = parents[k]
            v = par_v
        money[k] = money.get(k, 0) + v
    
    return [money[e] if e in money else 0 for e in enroll]

    
        