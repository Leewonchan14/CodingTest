function solution(strArr) {
    return  strArr.map((s, i) => {
        return i % 2 === 0 ? s.toLowerCase() : s.toUpperCase()
    })
}