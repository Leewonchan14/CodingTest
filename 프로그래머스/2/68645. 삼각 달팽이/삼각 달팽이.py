def solution(n):
    maps = [[0] * i for i in range(1, n + 1)]
    y, x = 0, 0
    count = 1
    maps[0][0] = 1
    
    limit = (n * (n + 1)) // 2
    
    while count != limit:
        # 아래
        while y + 1 < len(maps) and maps[y + 1][x] == 0:
            y += 1
            count += 1
            maps[y][x] = count
            
        # 오른쪽   
        while x + 1 < len(maps[y]) and maps[y][x+1] == 0:
            x += 1
            count += 1
            maps[y][x] = count
        
        # 왼쪽 위
        while x - 1 >= 0 and y - 1 >= 0 and maps[y-1][x-1] == 0:
            x -= 1
            y -= 1
            count += 1
            maps[y][x] = count
            
    return sum(maps, [])
        