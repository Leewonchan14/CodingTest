n = int(input())

def get_prime(n):
    li = [True] * (n + 1)
    for i in range(2, n):
        if li[i]:
            for j in range(i ** 2, n + 1, i):
                li[j] = False
                
    return [i for i in range(2, n + 1) if li[i]]


def main():
    primes = get_prime(n)
    left = 0
    right = 0
    sumv = 0
    
    cnt  = 0
    
    while right <= len(primes):
        if sumv < n:
            if right >= len(primes):
                break
            sumv += primes[right]
            right += 1
            continue
            
        if sumv == n:
            cnt += 1
        sumv -= primes[left]
        left += 1
    
    return cnt

print(main())
        