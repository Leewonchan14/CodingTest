li = []
cache = {}

def recursive(cnt, n, words):
    order = cnt % n
    if cnt >= len(words):
        return [0, 0]
    word = words[cnt]
    if word in cache or (li and li[-1][-1] != word[0]):
        return [order + 1, cnt // n + 1]
    
    li.append(word)
    cache[word] = 0
    
    return recursive(cnt + 1, n, words) 

def solution(n, words):
    k = recursive(0, n, words)
    return k