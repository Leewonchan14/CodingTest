def solution(name):
    # Step 1: Calculate the initial vertical cost to change each character
    name_len = len(name)
    vertical_cost = sum(min(ord(c) - ord('A'), ord('Z') - ord(c) + 1) for c in name)
    
    # Step 2: Initialize variables for horizontal movement cost
    min_move = name_len - 1 # Worst case: moving right all the time
    
    # Step 3: Optimize horizontal movement
    for idx in range(name_len):
        next_idx = idx + 1
        while next_idx < name_len and name[next_idx] == 'A':
            next_idx += 1
        
        distance = min(idx, name_len - next_idx)
        min_move = min(min_move, idx + name_len - next_idx + distance)
        
    return vertical_cost + min_move

# Example usage
# name = "JAZ"
# print(solution(name))
