import itertools

def solution(numbers, target):
    n = len(numbers)
    count = 0
    for pm in itertools.product([True,False], repeat=n):
        if sum([-numbers[i] if not pm[i] else numbers[i] for i in range(n)]) == target:
            count += 1
            
    return count