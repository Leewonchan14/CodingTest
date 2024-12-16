def recur(arr, k, li):
    if len(li) == k:
        print(" ".join([str(i) for i in li]))
        return
    
    for a in arr:
        if a not in li:
            li.append(a)
            recur(arr, k, li)
            li.pop()

def main(arr, k):
    recur(arr, k, [])
    
_, k = map(int, input().split())
arr = [int(i) for i in input().split()]
arr.sort()

main(arr, k)