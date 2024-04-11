def solution(routes):
    routes.sort(key=lambda x : x[1])
    cnt = 1
    place = routes[0][1]
    for a,b in routes:
        if a <= place <= b:
            continue
            
        place = b
        cnt += 1
        
    return cnt