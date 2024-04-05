function solution(arr, k) {
    return arr.map(v => {
        return k % 2 === 1 ? v * k : v + k
    })
}