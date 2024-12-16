import sys

input = sys.stdin.readline

moum = []
jaum = []


def recur(arr, k, li):
    global moum, jaum
    if len(li) == k:
        mo = len([arr[i] for i in li if arr[i] in moum])
        ja = len([arr[i] for i in li if arr[i] in jaum])

        if mo >= 1 and ja >= 2:
            print("".join([arr[i] for i in li]))
            return

    for i, v in enumerate(arr):
        if not li or i > li[-1]:
            li.append(i)
            recur(arr, k, li)
            li.pop()


def main(arr, k):
    global moum, jaum
    moum = [i for i in arr if i in "aeiou"]
    jaum = [i for i in arr if i not in "aeiou"]
    recur(arr, k, [])


k, _ = map(int, input().split())
arr = input().split()
arr.sort()

main(arr, k)
