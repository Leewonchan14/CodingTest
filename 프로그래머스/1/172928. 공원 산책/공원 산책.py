def solution(park, routes):
    dir = {"E" : (0 , 1), "W" : (0 , -1), "S":(1,0), "N" : (-1, 0)}
    row = 0
    col = 0
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == "S":
                row = i
                col = j
                
    for rou in routes:
        _dir = dir[rou.split()[0]]
        num = int(rou.split()[1])
        
        _row = row
        _col = col
        
        isGo = True
        
        for i in range(num):
            _row = _row + _dir[0]
            _col = _col + _dir[1]
            if  (
                    not (0<=_row<len(park)) or not (0<=_col<len(park[0])) or 
                    park[_row][_col] == "X"
            ):
                isGo = False
                break
                
        if isGo:
            row = _row
            col = _col
        isGo = False
    return [row, col]