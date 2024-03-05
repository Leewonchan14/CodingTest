import itertools
from collections import deque


def calcul(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    else:
        return a * b


def solution(expression: str):
    product = list(itertools.permutations(["*", "+", "-"], 3))
    stk = []

    answer_list = []
    # 모든 우선순위를 조사
    for rank in product:

        num = ""

        after_operation = []

        for index, s in enumerate(list(expression)):
            # 숫자라면 num에 추가 하고 다음 문자 확인
            if s not in rank:
                num += s
                continue

            # 연산자라면 숫자로 만들어주고 후위 에 넣어준다.
            after_operation.append(int(num))
            num = ""

            # stk 이 비어 있다면 연산자를 넣어주고 다음 확인
            if len(stk) == 0:
                # 넣어주고 다음 확인
                stk.append(s)
                continue

            # 스택이 비어 있지 않다면 우선순위를 확인
            # 우선 순위가 지금 나온게 더 높다면 그냥 넣어준다.
            if rank.index(stk[-1]) > rank.index(s):
                stk.append(s)
                continue

            # 지금 나온게 더 낮거나 같다면
            while len(stk) != 0 and rank.index(stk[-1]) <= rank.index(s):
                b = after_operation.pop()
                a = after_operation.pop()
                after_operation.append(calcul(a, b, stk.pop()))

            stk.append(s)

        after_operation.append(int(num))

        while len(stk) != 0:
            b = after_operation.pop()
            a = after_operation.pop()
            after_operation.append(calcul(a, b, stk.pop()))

        answer_list.append(abs(after_operation[0]))

    answer_list.sort()

    return answer_list[-1]