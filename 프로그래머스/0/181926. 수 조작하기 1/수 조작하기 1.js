function solution(n, control) {
    let m = {"w": 1, "s": -1, "d" : 10, "a":-10}
    return [...control].reduce((acc, v) => acc + m[v], n)
}