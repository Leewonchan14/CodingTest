function solution(s) {
    let cnt = 0;
    let zero = 0;
    while (s !== "1"){
        let nonZero = s.split("").filter(v => v !== "0")
        zero += s.length - nonZero.length;
        s = nonZero.length .toString(2)
        cnt++;
    }
    
    return [cnt, zero]
}