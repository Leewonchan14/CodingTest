from bisect import bisect_left


def preprocess(info, query):
    info = list(map(lambda x: x.split(), info))
    query = list(map(lambda x: x.split(' and '), query))
    for i in range(len(query)):
        query[i][-1], score = query[i][-1].split()
        query[i].append(int(score))
    return info, query


def solution(info, query):
    info, query = preprocess(info, query)

    dic = {}

    for i in info:
        key = ''.join(i[:-1])
        if key not in dic:
            dic[key] = []
        dic[key].append(int(i[-1]))

    # Sort the scores for each key
    for key in dic:
        dic[key].sort()

    result = []

    for q in query:
        score = q.pop()
        q = [s for s in q if s != '-']
        count = 0

        for key, value in dic.items():
            # q 에 있는 모든 조건이 key 에 포함되어 있으면
            if all([i in key for i in q]):
                # Use binary search to find the number of scores that are greater or equal to the target score
                count += len(value) - bisect_left(value, score)

        result.append(count)

    return result
