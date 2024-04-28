def solution(myString):
    answer = myString.split('x')
    return sorted([x for x in answer if x])