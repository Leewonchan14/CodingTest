def solution(dirs):
    visited = set()
    dic = dict(zip("U D R L".split(), [(1, 0), (-1 ,0), (0 , 1), (0 , -1)]))
    y = 0
    x = 0
    for d in dirs:
        dy,dx = dic[d]
        ny = y + dy
        nx = x + dx
        if -5 <= ny <= 5 and -5 <= nx <= 5:
                visited.add(((y,x),(ny,nx)))
                visited.add(((ny,nx), (y,x)))
                y = ny
                x = nx
    
    return len(visited) // 2