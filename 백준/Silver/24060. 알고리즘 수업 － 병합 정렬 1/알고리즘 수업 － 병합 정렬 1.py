rs = [0]
answer = [0]
k = [0]

def merge_sort(left, right, ls):
    if left < right:
        mid = (left + right) // 2
        merge_sort(left, mid, ls)  # 전반부 정렬
        merge_sort(mid + 1, right, ls)  # 후반부 정렬
        merge(ls, mid, left, right)  # 병합


# A[p..q]와 A[q+1..r]을 병합하여 A[p..r]을 오름차순 정렬된 상태로 만든다.
# A[p..q]와 A[q+1..r]은 이미 오름차순으로 정렬되어 있다.
def merge(ls, mid, left, right):
    i = left
    j = mid + 1
    t = 0
    tmp = [0] * (right - left + 1)
    while i <= mid and j <= right:
        if ls[i] <= ls[j]:
            tmp[t] = ls[i]  # tmp[t] <- A[i]; t++; i++;
            i += 1
        else:
            tmp[t] = ls[j]  # tmp[t] <- A[j]; t++; j++;
            j += 1
        t += 1

    while i <= mid:  # 왼쪽 배열 부분이 남은 경우
        tmp[t] = ls[i]
        t += 1
        i += 1
    while j <= right:  # 오른쪽 배열 부분이 남은 경우
        tmp[t] = ls[j]
        t += 1
        j += 1
    i = left
    t = 0
    while i <= right:  # 결과를 A[p..r]에 저장
        ls[i] = tmp[t]
        i += 1
        rs[0] += 1
        if rs[0] == k[0]:
            answer[0] = tmp[t]
        t += 1


import sys
input = sys.stdin.readline

N,K = map(int,input().split())

k[0] = K
ls = list(map(int, input().split()))
merge_sort(0, len(ls) - 1, ls)
print(answer[0] if answer[0] != 0 else -1)
