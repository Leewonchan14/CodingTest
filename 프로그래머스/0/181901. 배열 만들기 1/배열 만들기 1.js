function solution(n, k) {
    return [...new Array(n)].map((_, i) => {
        return i + 1
    }).filter(i=>i%k === 0)
}