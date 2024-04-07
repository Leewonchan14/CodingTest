"""
반개씩 주사위를 가져가야함

모든 주사위를 굴리고 합했을때 점수가 높으면 승리 같으면 무승부

승리할 확률이 높게 주사위를 가져가고 싶음

"""

import itertools


def solution(dice):
    dice_set = itertools.combinations(range(len(dice)), len(dice) // 2)
    dice_set_a_b = []
    for a_set_tuple in dice_set:
        k_v = {i: 0 for i in range(len(dice))}
        a_tuple = a_set_tuple
        for k in a_tuple:
            k_v.pop(k)
        b_tuple = tuple(k_v.keys())
        dice_set_a_b.append((a_tuple, b_tuple))

    win_count = {}

    for a_tuple, b_tuple in dice_set_a_b:
        # 접수 조합 구하기
        comb_a_sum = {}
        comb_b_sum = {}

        it = itertools.product(range(6), repeat=len(dice) // 2)

        # a의 점수 조합
        for dice_indexes in it:
            sumv = sum([dice[a_tuple[index]][dice_indexes[index]] for index in range(len(dice) // 2)])
            comb_a_sum[sumv] = comb_a_sum.get(sumv, 0) + 1
            sumv = sum([dice[b_tuple[index]][dice_indexes[index]] for index in range(len(dice) // 2)])
            comb_b_sum[sumv] = comb_b_sum.get(sumv, 0) + 1

        # 이긴수 계산
        a_win_count = sum(a_value * b_value for a_key, a_value in comb_a_sum.items()
                          for b_key, b_value in comb_b_sum.items() if a_key > b_key)

        win_count[a_tuple] = a_win_count

    dices, _ = sorted(win_count.items(), key=lambda x: x[1], reverse=True)[0]
    return [i + 1 for i in dices]

