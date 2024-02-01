def solution(hp):
    answer = hp // 5
    hp -= answer * 5
    
    answer += hp // 3
    answer += hp % 3
    return answer