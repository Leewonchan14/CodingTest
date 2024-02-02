key1 = [str(i) for i in range(10)]
key = [chr(i) for i in range(ord("A"), ord("Z") + 1)]

value1 = [i for i in range(10)]
value = [i for i in range(10, 36)]

key = sum([key1, key], [])
value = sum([value1,value], [])

dic = dict(zip(value, key))

s , n = input().split()
s = int(s)
n = int(n)

_sum = ""

while s // n > 0 :
    _sum = dic[s % n] + _sum
    s = s // n
    
_sum = dic[s % n] + _sum

print(_sum)