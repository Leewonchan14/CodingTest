def spin(key):
    return [[key[-r - 1][c] for r in range(len(key))] for c in range(len(key[0]))]

def isCollect(key, lock):
    for dy in range(-len(key) + 1, len(lock)):
        for dx in range(-len(key[0]) + 1, len(lock[0])):
            if collect(key, lock, dy, dx):
                return True
            
    return False
            
                    
                    
def collect(key, lock, dy, dx):
    new_lock = [r[:] for r in lock]
    for r in range(len(lock)):
        for c in range(len(lock[0])):
            k_r = r - dy
            k_c = c - dx
            if 0 <= k_r < len(key) and 0 <= k_c < len(key[0]):
                new_lock[r][c] += key[k_r][k_c]
                
            if new_lock[r][c] != 1:
                return False
    return True

def solution(key, lock):
    for i in range(4):
        if isCollect(key, lock):
            return True    
        key = spin(key)
    return False
    


            
            