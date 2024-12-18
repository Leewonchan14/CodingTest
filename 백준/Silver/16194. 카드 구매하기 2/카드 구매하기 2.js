const main = (arr) => {
    const dp = [0, ...arr]
    
    for(let i = 1; i <= arr.length; i++){
        for (let j = i + 1; j <= arr.length; j ++){
            dp[j] = Math.min(dp[j - i] + dp[i], dp[j])
        }
    }
    
    return dp[arr.length];
}

const fs = require('fs');
let [n, arr] = fs.readFileSync('/dev/stdin').toString().trim().split("\n");
arr = arr.split(" ").map(Number)

console.log(main(arr))

