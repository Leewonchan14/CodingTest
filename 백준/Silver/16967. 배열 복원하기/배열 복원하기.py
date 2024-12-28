import sys

input = sys.stdin.readline

def main():
    arr1 = [[arr[r][c] for c in range(w)] for r in range(h)]
    arr2 = [[arr[r][c] for c in range(y, y + w)] for r in range(x, x + h)]
    
    for r in range(x, h):
        for c in range(y, w):
            arr1[r][c] = arr2[r - x][c - y] - arr1[r - x][c - y]
    
    for rr in arr1:
        print(*rr)

h,w,x,y = map(int, input().split())
arr = [[int(i) for i in input().split()] for _ in range(h + x)]
main()