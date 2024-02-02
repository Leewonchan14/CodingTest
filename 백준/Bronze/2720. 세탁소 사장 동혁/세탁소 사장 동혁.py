n = int(input())
for i in range(n):
    li = []
    
    s = input()
    s = int(s)
    
    li.append(str(s // 25))
    s = s % 25
    li.append(str(s // 10))
    s = s % 10
    li.append(str(s // 5))
    s = s % 5
    li.append(str(s))
    
    print(" ".join(li))
        
    