def solution(str1, str2):
    return "".join(list(map(lambda v : "".join(v) ,zip(list(str1), list(str2)))))