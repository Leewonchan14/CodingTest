const fs = require('fs');
const n = Number(fs.readFileSync('/dev/stdin').toString().trim());

const main = (n) => {
    const dp = [0, 1, 3];
    for (let i = 0; i <= n; i++){
        if (i < dp.length) continue;
        dp.push((dp.at(-1) + dp.at(-2) * 2) % 10007)
    }
    
    return dp[n]
}

console.log(main(n))