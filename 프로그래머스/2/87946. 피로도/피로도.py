def back(k, dungeons, visited, length, ls):
    ls[-1] = max(ls[-1], length)
    for i in range(len(dungeons)):
        if not visited[i] and k >= dungeons[i][0]:
            visited[i] = True
            back(k - dungeons[i][1], dungeons, visited, length + 1, ls)
            visited[i] = False

def solution(k, dungeons):
    visited = [False] * len(dungeons)
    ls = [0]
    back(k, dungeons, visited, 0, ls)
    return ls[-1]