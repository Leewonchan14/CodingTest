def solution(s):
    s = s.split(" ")
    _map = list(map(int, s))
    return f"{min(_map)} {max(_map)}"