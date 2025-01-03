import sys

input = sys.stdin.readline

t = int(input())
input()
arr1 = [int(i) for i in input().split()]
input()
arr2 = [int(i) for i in input().split()]

def get_dp(arr):
    dp = [0]
    for i in range(len(arr)):
        dp.append(dp[-1] + arr[i])
    return dp

def get_all_sub_sum(dp):
    result = {}
    for i in range(1, len(dp)):
        for j in range(i):
            sub = dp[i] - dp[j]
            result[sub] = result.get(sub, 0) + 1
            
    return result
        

def main():
    dp1 = get_dp(arr1)
    sub1 = get_all_sub_sum(dp1)
    dp2 = get_dp(arr2)
    sub2 = get_all_sub_sum(dp2)
    cnt = 0
    for i in sub1.keys():
        j = t - i
        if j in sub2:
            cnt += sub1[i] * sub2[j]
            
    return cnt

print(main())
    
    