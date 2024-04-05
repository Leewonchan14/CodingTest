function solution(n) {
    return [...new Array(n)].map((_, i) => i + 1).filter(n => n % 2 == 1)
}