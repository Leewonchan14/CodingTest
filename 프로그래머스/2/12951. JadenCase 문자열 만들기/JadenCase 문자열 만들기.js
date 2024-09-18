function solution(s) {
    s = s.toLowerCase();
    let result = ""
    Array.from(s).forEach((v, i) => {
        let pre = i !== 0 ? s.charAt(i - 1) : " "
        result += pre === " " ? v.toUpperCase() : v
    })
    
    return result;
}