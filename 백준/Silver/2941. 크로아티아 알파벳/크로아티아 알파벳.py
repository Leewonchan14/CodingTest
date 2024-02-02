li = "c= c- dz= d- lj nj s= z=".split()

s = input()

for i in li:
    s = s.replace(i, "|")
print(len(s))