function solution(s1, s2) {
    return s1.map(i => {
        return s2.filter(n => n === i).length
    }).reduce((a,b)=> a+b, 0)
}