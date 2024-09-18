function solution(n) {
    return [...Array(n + 1)].map((v,i) => i).filter(v => v % 2 === 1)
}