function solution(n) {
    n = n - n % 2
    return (n / 2) * (n / 2 + 1)
}