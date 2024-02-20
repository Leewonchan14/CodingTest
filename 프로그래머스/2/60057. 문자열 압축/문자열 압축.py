def solution(s):
    length = len(s)
    _min = length
    # 2개로 압축하는거 부터
    for i in range(1, length):
        index = 0
        count = 0
        zip_str = ""

        # 압축을 위한 while
        while True:
            pre_sub = s[index:index + i]

            index += i

            # index가 작을때만 잘라온다.
            if index + i < length:
                sub = s[index:index + i]
            # 나머지 잘라온다.
            else:
                sub = s[index:]

            count += 1

            # 같으면 다음 연산
            if pre_sub == sub:
                continue

            count = "" if count <= 1 else str(count)

            # 이전 문자열이랑 다르다면 지금까지 만든 zip에 추가한다.
            zip_str += (count + pre_sub)
            count = 0
            
            # 마지막이라면 break
            if index >= length:
                break

        if _min > len(zip_str):
            _min = len(zip_str)

    return _min
