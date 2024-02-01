def solution(myString):
    answer = myString.split('x')
    answer = list(filter(lambda v : v != '', answer))
    answer.sort()
    return answer