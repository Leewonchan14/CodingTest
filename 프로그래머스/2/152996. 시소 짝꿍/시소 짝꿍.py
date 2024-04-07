import itertools

def solution(weights):
    count_sort = {}
    for w in weights:
        count_sort[w] = count_sort.get(w, 0) + 1
        
    total = 0
    for weight, count in count_sort.items():
        total += count * (count - 1)
        
        ls = []
    
        ls.append(weight * 2)
        if weight % 2 == 0:
            _ls = [weight // 2 * 3, weight // 2]
            ls = sum([ls, _ls], [])

        if weight % 3 == 0:
            _ls = [weight // 3 * 2, weight // 3 * 4]
            ls = sum([ls, _ls], [])

        if weight % 4 == 0:
            ls.append(weight // 4 * 3)
        
        for w in ls:
            if w in count_sort:
                total += count * count_sort[w]
    
    return total // 2