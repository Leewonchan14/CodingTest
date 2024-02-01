def solution(n):
    count = 0
    for i in range(1, n+1):
        if i**2 == n:
            count = (count * 2 + 1)
            break
            
        if i**2 > n:
            count *= 2
            break
            
        if n % i == 0 :
            count += 1
            print(i)

        
    return count