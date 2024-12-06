from collections import deque

def solution(people, limit):
    people.sort()  # 사람들의 몸무게를 정렬
    people = deque(people)  # 양쪽에서 요소를 제거하기 위해 deque 사용
    boats = 0  # 필요한 보트 수

    while people:
        # 양 끝을 조합하여 제한을 초과하지 않는다면 둘 다 태움
        if len(people) >= 2 and people[0] + people[-1] <= limit:
            people.popleft()
            people.pop()
        else:
            # 그렇지 않으면 무거운 사람(끝쪽)을 태움
            people.pop()

        boats += 1  # 보트 사용 증가

    return boats