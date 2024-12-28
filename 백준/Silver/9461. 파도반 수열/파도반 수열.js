const fs = require('fs')

const [tc, ...arr] = fs.readFileSync('dev/stdin').toString().trim().split("\n").map(Number);

const dp = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

const solve = (n) => {
    for(let i = dp.length; i <= n; i++){
        dp.push(dp.at(-1) + dp.at(-5));
    }
    
    return dp[n];
}

for(let a of arr){
    console.log(solve(a))
}