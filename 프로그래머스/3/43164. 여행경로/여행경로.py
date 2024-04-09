rs = []
ls = ["ICN"]
go = {}
cnt = [0]

def track(num):
    if num == cnt[0]:
        rs.append(ls[:])
        return
    
    for g in go.get(ls[-1],[]):
        if not g[1]:
            g[1] = True
            ls.append(g[0])
            track(num + 1)
            ls.pop()
            g[1] = False

def solution(tickets):
    for a,b in tickets:
        cnt[0] += 1
        go[a] = go.get(a, [])
        go[a].append([b, False])
        
    track(0)
    
    rs.sort(key=lambda x : "".join(x))
    
    return rs[0]