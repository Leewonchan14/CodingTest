def solution(n, words):
    dic = {words[0] : 0}
    result = []
    for i in range(1, len(words)):
        if words[i - 1][-1] != words[i][0] or words[i] in dic:
            result = [i % n + 1, i // n + 1]
            break;
            
        dic[words[i]] = 0
        
    return result if result else [0 ,0]
        
        