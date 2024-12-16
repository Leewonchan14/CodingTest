def recur(arr, k, li):
    if len(li) == k:
        print(" ".join([str(arr[i]) for i in li]))
        return
    
    for i,a in enumerate(arr):
        if not li or i >= li[-1]:
            li.append(i)
            recur(arr, k, li)
            li.pop()


def main(arr, k):
    recur(arr, k, [])
    
_, k = map(int, input().split())

arr = [int(i) for i in input().split()]
arr.sort()
main(arr, k)