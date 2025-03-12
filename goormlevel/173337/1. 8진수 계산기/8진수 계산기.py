# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n = input()

arr = [int(i) for i in input().split()]
sumv = sum(arr)

result = ""
while sumv >= 8:
	d,m = divmod(sumv, 8)
	result = str(m) + result
	sumv = d
	
result =  str(sumv) + result

print(result)

