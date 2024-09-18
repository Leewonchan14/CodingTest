function solution(n) {
    let fibo = [0 , 1]
    if (n <= 1) return fibo[n]
    
    for(let i = 2; i <= n; i++){
        fibo.push((fibo.at(-2) + fibo.at(-1)) % 1234567)
    }
    
    return fibo.at(-1)
}