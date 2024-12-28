import sys

input = sys.stdin.readline

tc = int(input())

arr = [int(input()) for _ in range(tc)]
dp = [[arr[0], arr[0], 0]]

#10, 10, 0 (10)
#20, 30, 10 (20)
#25, 35, 30 (15)
#55, 50, 35 (25)
#45, 65, 55 (10)
#75, 65, 65 (20)



def main():
    for i in range(1, len(arr)):
        # 바로전
        a = dp[-1][2] + arr[i]
        # 두칸전
        b = dp[-1][0] + arr[i]
        # 지금
        c = max(dp[-1][1], dp[-1][0])
        
        dp.append([a,b,c])
        
    print(max(dp[-1][0], dp[-1][1]))        
    

main()