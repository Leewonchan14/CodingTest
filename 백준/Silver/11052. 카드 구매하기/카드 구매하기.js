const main = (arr) => {
    const dp = arr.map(() => 0)
    dp.push(0)
    
    for(let i = 1; i <= arr.length; i++){
        dp[i] = Math.max(dp[i], arr[i - 1]);
        for (let j = i + 1; j <= arr.length; j ++){
            dp[j] = Math.max(dp[j - i] + dp[i], dp[j])
        }
    }
    
    return dp[arr.length];
}

const fs = require('fs');
let [n, arr] = fs.readFileSync('/dev/stdin').toString().trim().split("\n");
arr = arr.split(" ").map(Number)

console.log(main(arr))

