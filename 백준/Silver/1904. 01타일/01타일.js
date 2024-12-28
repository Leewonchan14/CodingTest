const fs = require('fs')

const n = Number(fs.readFileSync('dev/stdin').toString().trim())

const main = () => {
    const dp = [0, 1, 2, 3, 5];
    
    for(let i = dp.length; i <= n; i++){
        dp.push((dp.at(-1) + dp.at(-2)) % 15746);
    }
    
    console.log(dp[n]);
}

main()