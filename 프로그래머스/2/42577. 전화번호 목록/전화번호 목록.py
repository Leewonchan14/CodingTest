def solution(phone_book):
    dic = set()
    phone_book.sort()
    for p in phone_book:
        for i in range(1, len(p) + 1):
            if p[:i] in dic:
                return False
        dic.add(p)
    return True

