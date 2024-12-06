def solution(s):
    li = list(map(lambda x: list(map(int ,x.split(","))) , s[2:-2].split("},{")))
    li.sort(key=lambda x:len(x))
    
    ans = []
    
    for r in li:
        for c in r:
            if c not in ans:
                ans.append(c)
                
    return ans