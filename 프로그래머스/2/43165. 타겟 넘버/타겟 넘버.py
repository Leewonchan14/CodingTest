class Main:
    numbers = []
    target = 0

    def __init__(self, numbers, target):
        self.numbers = numbers
        self.target = target

    def recursive(self, li):
        if len(li) == len(self.numbers):
            if sum(li) == self.target:
                return 1
            else:
                return 0

        return self.recursive([*li, self.numbers[len(li)]]) + self.recursive(
            [*li, self.numbers[len(li)] * -1]
        )


def solution(numbers, target):
    return Main(numbers, target).recursive([])
