import itertools

def solution(friends, gifts):
    
    zisu = {f: 0 for f in friends}
    adj = {f: {} for f in friends}
    
    for g in gifts:
        s, e = g.split()
        
        zisu[e] -= 1
        zisu[s] += 1
        
        adj[s][e] = adj[s].get(e, 0) + 1
        
    recive = {f: 0 for f in friends}
        
    for s, e in itertools.combinations(friends, 2):
        s_e = adj[s].get(e, 0)
        e_s = adj[e].get(s, 0)
        if s_e == e_s:
            if zisu[s] < zisu[e]:
                recive[e] += 1
            elif zisu[e] < zisu[s]:
                recive[s] += 1
                
            continue
        
        elif s_e < e_s:
            recive[e] += 1
        elif e_s < s_e:
            recive[s] += 1
            
    return max(recive.values())
            
        