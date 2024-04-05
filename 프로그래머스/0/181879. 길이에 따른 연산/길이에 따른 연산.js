function solution(num_list) {
    let mul = num_list.reduce((a,b) => a * b, 1)
    let sum = num_list.reduce((a,b) => a+b,0)
    return num_list.length >= 11 ? sum : mul
}