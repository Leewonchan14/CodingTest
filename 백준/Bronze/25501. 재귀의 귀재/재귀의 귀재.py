def recursion(s, l, r, count):
    if l >= r:
        return 1, count
    elif s[l] != s[r]:
        return 0, count
    else:
        return recursion(s, l + 1, r - 1, count + 1)


def isPalindrome(s):
    return recursion(s, 0, len(s) - 1, 1)


n = int(input())
for i in range(n):
    s = isPalindrome(input())
    print(f"{s[0]} {s[1]}")
