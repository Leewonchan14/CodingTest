def recursive(numbers, target, li):
    if len(li) == len(numbers):
        if sum(li) == target:
            return 1
        else:
            return 0

    li1 = li[:]
    li2 = li[:]
    li1.append(numbers[len(li)])
    li2.append(numbers[len(li)] * -1)

    return recursive(numbers, target, li1) + recursive(numbers, target, li2)


def solution(numbers, target):
    return recursive(numbers, target, [])
