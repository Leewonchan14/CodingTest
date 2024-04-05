function solution(rsp) {
    let m = {"2" : "0", "0" : "5", "5" : "2"}
    return [...rsp].map(i => m[i]).join('')
}