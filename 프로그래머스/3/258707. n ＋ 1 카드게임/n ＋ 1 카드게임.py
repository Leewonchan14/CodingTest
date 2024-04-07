"""
- n 개의 카드뭉치 (n은 6의 배수)가 놓여짐
- 동전 coin 개를 가지고 있음
- 라운드를 최대한 버텨야함

### 초반
1. 카드뭉치에서 n/3장을 뽑아 모두 가진다.
2. 교환가능한 동전 coin 개를 가지고 있음

### 라운드 시작
1. 카드 뭉치에서 카드를 두장 뽑는다.
    - 카드뭉치에 뽑을 카드가 없다면 게임종료

2. 뽑은 카드는 두가지 경우의 수가 존재
    - 코인 하나를 소모해 가지기
    - 그냥 버리기

3. 카드의 적힌 수의 합이 n+1 이 되도록 카드 두장을 내고 다음 라운드로 진행
    - 두장을 낼수 없다면 게임종료
"""

from collections import deque


def get_card(cards, n, coin, hand_cards, trash_cards, is_n, card_index, double_coin_stk):
    card_num = cards[card_index]
    opposite_num = n + 1 - card_num

    # n + 1 이 된다면 손에 넣는다.
    if coin > 0 and hand_cards[opposite_num]:
        coin -= 1
        is_n.append((card_num, opposite_num))

    # 코인은 없지만 손에 n + 1카드가 있을때
    elif hand_cards[opposite_num] and double_coin_stk:
        coin += 1

        double_coin_stk.pop()
        is_n.append((card_num, opposite_num))

    # 코인이 두개 이상 있고 버린카드에 n + 1 이되는 카드가 존재한다면
    elif coin > 1 and trash_cards[opposite_num]:
        coin -= 2
        # 코인을 사용해 카드를 가져온후 n + 1 목록에 넣어준다.
        double_coin_stk.append((card_num, opposite_num))

    # 안된다면 버린다.
    else:
        trash_cards[card_num] = True

    return coin


def solution(coin, cards):
    is_n = deque()
    n = len(cards)
    hand_cards = [False] * (n + 1)
    trash_cards = [False] * (n + 1)
    for index in range(n // 3):
        hand_cards[cards[index]] = True
        # n + 1 이 가능하면 que에 넣기
        if hand_cards[n + 1 - cards[index]]:
            is_n.append((cards[index], n + 1 - cards[index]))

    round_count = 0
    card_index = n // 3
    double_coin_stk = []
    while True:
        round_count += 1
        # 뽑을 카드 두장이 없다면 (마지막이거나 이미 넘었다면)
        if card_index >= n - 1:
            break

        # 두장 뽑기
        coin = get_card(cards, n, coin, hand_cards, trash_cards, is_n, card_index, double_coin_stk)
        card_index += 1

        coin = get_card(cards, n, coin, hand_cards, trash_cards, is_n, card_index, double_coin_stk)
        card_index += 1

        # n + 1 이 되는 경우가 없다면 종료한다.
        if is_n:
            is_n.popleft()
            continue

        if double_coin_stk:
            double_coin_stk.pop()
            continue

        break

        # n+1이 되는 두장을 낸다.

    return round_count

