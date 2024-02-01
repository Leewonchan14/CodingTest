def solution(my_string):
    split =my_string.split()
    sum = 0
    pre = "+"
    for i in split:
        if i == "+" or i == "-":
            pre = i
            continue
        
        sum += int(i) * (-1 if pre == "-" else 1)
    return sum