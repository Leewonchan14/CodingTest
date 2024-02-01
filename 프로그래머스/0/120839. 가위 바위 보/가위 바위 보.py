def solution(rsp):
    m = {"2" : "0", "0" : "5", "5" : "2"}
    
    return "".join(map(lambda v : m[v], rsp))