import math


def solution(w, h):
    w, h = max(w, h), min(w, h)  # 편의상 가로가 더 길게

    gcd = math.gcd(w, h)  # 최대 공약수 -> (패턴 반복수)

    ww = w // gcd
    hh = h // gcd  # 간소화 된 w, h
    # print(ww, hh, gcd)

    # ww * hh 에서 대각선을 지나지 않는 크기는 (ww-1) * (hh-1)
    # 테트리스를 생각하면 이해가 쉽다.
    
    # cut: 패턴의 한부분 ww * hh 에서 잘리지 않는 부분을 뺀 것
    # 실제로는 w + h -1 과 같다.
    cut = (ww * hh) - (ww - 1) * (hh - 1)

    return w * h - cut * gcd
