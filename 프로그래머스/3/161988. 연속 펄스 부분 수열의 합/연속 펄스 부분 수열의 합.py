def solve(sequence):
    for i in range(1, len(sequence)):
        sequence[i] = max(sequence[i - 1] + sequence[i], sequence[i])
    
    return max(sequence)
    

def solution(sequence):
    length = len(sequence)
    a = [(-1 if i % 2 == 0 else 1) * sequence[i] for i in range(length)]
    b = [(-1 if i % 2 != 0 else 1) * sequence[i] for i in range(length)]
    return max(solve(a), solve(b))