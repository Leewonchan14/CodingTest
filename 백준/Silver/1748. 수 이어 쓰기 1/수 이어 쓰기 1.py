def main(n):
    length = len(str(n))
    
    sumv = 0
    for i in range(1, length):
        sumv += 9 * (10 ** (i - 1)) * i
        
    last = 10 ** (length - 1) - 1
    
    return (n - last) * length + sumv


n = int(input())
print(main(n))
    