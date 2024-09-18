function lcm(a1, b1){
    let a = Math.max(a1,b1);
    let max = a;
    let b = a1 + b1 - a;
    while (a % b !== 0){
        a += max;
    }
    
    return a;
}

function solution(arr) {
    return arr.reduce((acc, v) => lcm(acc,v), 1);
}