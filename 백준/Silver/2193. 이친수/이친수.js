const main = (n) => {
    const dp = [[], [0n, 1n], [1n, 0n]];
    
    for (let i = dp.length; i <= n; i++){
        const a = dp.at(-1)[0] + dp.at(-1)[1];
        const b = dp.at(-1)[0]
        dp.push([a, b])
    }
    
    return dp[n][0] + dp[n][1]
}

const fs = require('fs');
const n = Number(fs.readFileSync('/dev/stdin').toString().trim());
console.log(main(n).toString())