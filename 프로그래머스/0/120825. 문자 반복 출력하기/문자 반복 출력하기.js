function solution(my_string, n) {
    return [...my_string].map((v) => [...Array(n)].fill(v).join("")).join("")
}