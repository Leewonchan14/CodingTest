from collections import deque


def solution(bridge_length, weight, truck_weights):
    brige_weight = 0
    truck_weight = deque(truck_weights)
    brige = deque([0] * bridge_length)
    time = 0

    while True:
        time += 1
        brige_weight -= brige.popleft()
        brige.append(0)

        if not truck_weight and brige_weight == 0:
            break

        if not truck_weight:
            continue

        comming = truck_weight[0]
        # 태울수 있으면 끝에 태우기
        if brige_weight + comming <= weight:
            truck_weight.popleft()
            brige_weight += comming
            brige[-1] = comming

    return time
