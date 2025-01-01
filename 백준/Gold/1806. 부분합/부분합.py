import sys

input = sys.stdin.readline

n,m = map(int, input().split())
arr = [int(i) for i in input().split()]

def main():
    left = 0
    right = 0
    sumv = 0
    result = []
    while right <= len(arr):
        if sumv < m:
            if right >= len(arr):
                break
            sumv += arr[right]
            right += 1
            continue
            
        elif sumv >= m:
            result.append(right - left)
            sumv -= arr[left]
            left += 1
            
    result.sort()
    return result[0] if result else 0
            
    
print(main())