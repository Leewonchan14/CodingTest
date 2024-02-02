# "45분 일찍 알람 설정하기"
# 10 10
# 9 25
a,b = map(int, input().split())

c = a*60 + b - 45
if c < 0:
    c += 24 * 60
a = c // 60
b = c % 60
print(f"{a} {b}")
    
