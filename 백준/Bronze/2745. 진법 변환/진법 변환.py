key1 = [str(i) for i in range(10)]
key = [chr(i) for i in range(ord("A"), ord("Z") + 1)]

value1 = [i for i in range(10)]
value = [i for i in range(10, 36)]

key = sum([key1, key], [])
value = sum([value1,value], [])

dic = dict(zip(key, value))

s , n = input().split()

n = int(n)

_sum = 0
s = s[::-1]
count = 0
for i in s :
    _sum += dic[i] * n**count
    count += 1
print(_sum)