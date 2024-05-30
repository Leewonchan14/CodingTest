from itertools import combinations
def solution(relation):
    columns = len(relation[0])
    rows = len(relation)

    answers = []

    for i in range(1,columns+1):
        candidates = list(combinations(range(columns),i))

        for candidate in candidates:
            tples = []
            for row in relation:
                tple =[]
                for idx in candidate:
                    tple.append(row[idx])

                if tple not in tples:
                    tples.append(tple)

            if len(tples) == rows:
                answers.append(set(candidate))

    answers_ = answers.copy()

    for i in range(len(answers)):
        for j in range(i+1,len(answers)):
            key1 = answers[i]
            key2 = answers[j]
            if key1.issubset(key2):
                try:
                    answers_.remove(key2)
                except:
                    continue

    return len(answers_)
