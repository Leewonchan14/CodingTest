import sys

# 0 ~ 1000000 index에 대응하는 True 로 이루어진 리스트 생성
is_prime = [True for _ in range(1000000 + 1)]
length = len(is_prime)

# 0, 1 은 소수가 아님
is_prime[0] = False
is_prime[1] = False

# 소수의 배수이면 False로 변경!
index = 0
while index < length:
    # 이미 소수가 아니면 continue
    if not is_prime[index]:
        index += 1
        continue

    # 소수 이면 배수들 모두 False
    for i in range(2 * index, length, index):
        is_prime[i] = False

    index += 1

# 골드바흐 추측은 3이상이다.
prime_list = [prime_num for prime_num, is_true in enumerate(is_prime) \
              if is_true and prime_num >= 3]

while True:
    input_num = int(sys.stdin.readline().rstrip())
    # 0이면 종료
    if input_num == 0:
        break

    for prime_num in prime_list:
        # 반대숫자가 소수가 아니면 continue
        if not is_prime[input_num - prime_num]:
            continue
        # 두 소수의 합이 input_num과 같다면
        print(input_num, "=", prime_num, "+", input_num - prime_num)
        break
