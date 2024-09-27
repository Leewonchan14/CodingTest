const fs = require('fs');
const n = Number(fs.readFileSync('/dev/stdin').toString().trim());

const dp = [0, 0, 1, 1, 2];

for(let i = 5; i <= n; i++){
    let a = dp[i - 1] + 1;
    let b = i % 2 === 0 ? dp[i / 2] + 1 : Infinity;
    let c = i % 3 === 0 ? dp[i / 3] + 1 : Infinity;
    dp.push(Math.min(a,b,c))
}

console.log(dp[n])