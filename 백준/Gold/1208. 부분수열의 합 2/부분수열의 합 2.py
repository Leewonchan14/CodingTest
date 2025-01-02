import sys

input = sys.stdin.readline

n, s = map(int, input().split())
arr = [int(i) for i in input().split()]


def sumDic(li):
    dic = {}
    ll = []

    def recur(sumv):
        if ll:
            dic[sumv] = dic.get(sumv, 0) + 1

        if len(ll) == len(li):
            return

        for i in range(len(li)):
            if not ll or i > ll[-1]:
                ll.append(i)
                recur(sumv + li[i])
                ll.pop()

    recur(0)
    dic[0] = dic.get(0, 0) + 1
    return dic


def main():
    mid = len(arr) // 2
    dic1 = sumDic(arr[:mid])
    dic2 = sumDic(arr[mid:])

    arr1 = sorted(dic1.keys(), key=lambda x: x)
    arr2 = sorted(dic2.keys(), key=lambda x: -1 * x)

    left = 0
    right = 0
    cnt = 0
    while left < len(arr1) and right < len(arr2):
        now_sum = arr1[left] + arr2[right]

        # 크면 줄여야함
        if now_sum > s:
            right += 1
            continue

        # 작으면 커져야함
        if now_sum < s:
            left += 1
            continue

        # 같으면 카운트
        cnt += dic1[arr1[left]] * dic2[arr2[right]]
        left += 1
        right += 1

    if s == 0:
        cnt -= 1

    return cnt


print(main())
