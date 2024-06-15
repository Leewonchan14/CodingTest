class Poper:
    def __init__(self, li, n):
        self.stack = li
        self.index = n - 1
        while self.index > 0 and self.stack[self.index] == 0:
            self.index -= 1

    def get_index(self):
        return self.index + 1

    def reload_index(self):
        while self.index > 0 and self.stack[self.index] == 0:
            self.index -= 1

    def pop(self):
        r = self.index + 1

        if self.index >= 0 and self.stack[self.index] > 0:
            self.stack[self.index] -= 1

        self.reload_index()
        return r

    def is_empty(self):
        return self.index == 0 and self.stack[0] == 0

    def now_num(self):
        return self.stack[self.index]


def solution(cap, n, deliveries, pickups):
    delivery = Poper(deliveries, n)
    pickup = Poper(pickups, n)

    cnt = 0
    while not delivery.is_empty() or not pickup.is_empty():
        cnt += max(delivery.get_index(), pickup.get_index()) * 2

        for i in range(cap):
            delivery.pop()
            pickup.pop()
            
    return cnt

