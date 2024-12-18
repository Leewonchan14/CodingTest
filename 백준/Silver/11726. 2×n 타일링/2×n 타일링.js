const fs = require('fs');
const n = Number(fs.readFileSync('/dev/stdin').toString().trim());

const dp = [0, 1, 2]

for(let i = 0; i <= n; i ++){
    if (i < dp.length) continue
    
    dp.push((dp.at(-1) + dp.at(-2)) % 10007)
}

console.log(dp[n])
