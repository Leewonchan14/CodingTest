function solution(my_string) {
    let preFixes = [...Array(my_string.length)].map((v, i) => my_string.slice(-i))
    
    return preFixes.sort();
}