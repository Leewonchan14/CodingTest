function solution(n) {
    return [...Array(n + 1)].map((v, i) => i).filter(a => a % 2 === 0).reduce((acc,b) => acc + b , 0)
}