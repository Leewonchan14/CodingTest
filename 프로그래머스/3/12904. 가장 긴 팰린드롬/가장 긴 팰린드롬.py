def isPal(i, s, n):
    cnt = 0
    for j in range(1, n):
        left = i - j
        right = i + j
        if left < 0 or right >= n or s[left] != s[right]:
            break;
        cnt += 1
            
    return cnt * 2 + 1

def isPalGap(i, s, n):
    cnt = 0
    left = i
    right = i - 1
    for j in range(n):
        left -= 1
        right += 1
        if left < 0 or right >= n or s[left] != s[right]:
            break;
        cnt += 1
            
    return cnt * 2

def solution(s):
    n = len(s)
    ls = []
    for i in range(n):
        ls.append(isPalGap(i, s, n))
        ls.append(isPal(i, s, n))

    ls.append(isPalGap(n, s, n))
    ls.sort()
    return ls[-1]