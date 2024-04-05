function solution(n, control) {
    let m = {"w": 1, "s": -1, "d" : 10, "a":-10}
    return  n + [...control].reduce((a,b) => {
        return a + m[b]
    }, 0)
}