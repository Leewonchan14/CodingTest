def solution(numbers):
    str_ls = list(map(str, numbers))
    str_ls.sort(reverse=True, key=lambda x: x*4)
    return str(int("".join(str_ls)))