import itertools


def track(li, banned_id, visited_u, visited_b):
    if all(visited_u):
        return True

    for iu, ui in enumerate(li):
        if visited_u[iu]:
            continue
        for i, bi in enumerate(banned_id):
            if not visited_b[i] and not visited_u[iu] and can_ban(bi, ui):
                visited_u[iu] = True
                visited_b[i] = True

                rs = track(li, banned_id, visited_u, visited_b)
                if rs:
                    return True

                visited_u[iu] = False
                visited_b[i] = False

    return False


def can_ban(ban_id, user_id):
    if len(ban_id) != len(user_id):
        return False
    for b, u in zip(ban_id, user_id):
        if b != '*' and b != u:
            return False
    return True


def solution(user_id, banned_id):
    cnt = 0
    per = list(itertools.combinations(user_id, len(banned_id)))

    for li in per:
        visited_u = [False] * len(banned_id)
        visited_b = [False] * len(banned_id)
        if track(li, banned_id, visited_u, visited_b):
            cnt += 1

    return cnt

