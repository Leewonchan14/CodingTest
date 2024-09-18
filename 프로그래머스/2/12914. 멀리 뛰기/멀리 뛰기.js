function solution(n) {
    let dp = [1, 2];
    
    if (n < 2) return dp[n - 1];
    
    for(let i = 3; i <= n; i++){
        dp.push((dp.at(-1) + dp.at(-2)) % 1234567)
    }
    
    return dp.at(-1)
    
}