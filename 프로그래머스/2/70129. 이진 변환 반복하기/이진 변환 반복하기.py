def zeroCnt(s):
    return s.count("0")

def filterZero(s):
    return [i for i in s if i != "0"]

def toBin(s):
    return bin(s)[2:]
    
def toInt(s):
    return int(s, 2)

def solution(s):
    
    cnt = 0
    zero = 0
    
    while True:
        cnt += 1
        zero += zeroCnt(s)
        s = filterZero(s)
        s = toBin(len(s))
        
        if s == "1":
            break
    return [cnt, zero]