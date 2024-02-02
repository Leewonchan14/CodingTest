# 점 (x, y)의 사분면 번호(1, 2, 3, 4 중 하나)를 출력한다.

#예제 입력 1 
#12
#5
a,b = int(input()), int(input())
if a > 0 and b > 0:
    print(1)
elif a > 0 and b < 0 :
    print(4)
elif a < 0 and b > 0 :
    print(2)
elif a < 0 and b < 0 :
    print(3)