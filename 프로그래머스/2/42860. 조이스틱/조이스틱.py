def solution(name):
    a_int, z_int = ord('A'), ord('Z')

    # 모든 상, 하 움직임 수를 더함
    vertical_moves = sum(min(ord(c) - a_int, z_int - ord(c) + 1) for c in name)

    # 최악의 경우 len(name) - 1 만큼의 움직임이 필요함
    min_horizontal_moves = len(name) - 1

    # 모든 문자에 대해 최소 움직임을 계산
    for i, s in enumerate(name):
        # A인 경우는 넘어감
        if s == 'A':
            continue
        # A가 아닌 경우, 다음이 A가 아닌 문자가 나올때까지 이동
        next_char_index = i + 1
        while next_char_index < len(name) and name[next_char_index] == 'A':
            next_char_index += 1

        # next_char_index = i + 1 부터 A가 아닌 문자가 나올때까지의 거리

        # 최소 움직임은 i번째 문자까지의 움직임과, 뒤로 돌아가는 움직임의 합
        direct_move = i
        # 뒤로 돌아가는 움직임은 len(name) - next_char_index
        backward_move = len(name) - next_char_index

        # 최소 움직임은 i번째 문자까지의 움직임과, 뒤로 돌아가는 움직임의 합, 그리고 둘 중 작은 값을 더한 값
        min_horizontal_moves = min(min_horizontal_moves, direct_move + backward_move + min(direct_move, backward_move))
        
    # 모든 문자가 A인 경우는 0을 반환
    if name == "A" * len(name):
        return 0

    # 최종 움직임은 상, 하 움직임 수와 최소 가로 움직임 수의 합
    return vertical_moves + min_horizontal_moves