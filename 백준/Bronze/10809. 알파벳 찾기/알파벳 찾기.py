s = input()
li = []
for i in range(ord("a"), ord("z")+1):
    if chr(i) in s:
        li.append(s.index(chr(i)))
        continue
    li.append(-1)        
li = list(map(str, li))
print(" ".join(li))