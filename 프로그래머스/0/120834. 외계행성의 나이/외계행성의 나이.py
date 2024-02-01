def solution(age):
    m = dict(zip(list("0123456789"), list("abcdefghij")))
    return "".join([m[i] for i in str(age)])