from collections import deque
from queue import PriorityQueue


def solution(n, k, enemy):
    clear_enemy = PriorityQueue()
    enemy = deque(enemy)
    cnt = 0
    while enemy:
        en = enemy.popleft()
        if n >= en:
            n -= en
            clear_enemy.put(-en)
            cnt += 1
            continue
            
        if n < en and k <= 0:
            break

        if n < en and k > 0:
            clear_enemy.put(-en)
            while n < en and k > 0 and clear_enemy:
                k -= 1
                safe = -clear_enemy.get()
                n += safe

            if n < en:
                break

            n -= en
            cnt += 1

    return cnt
