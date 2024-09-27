const fs = require("fs");

const n = Number(fs.readFileSync("/dev/stdin").toString().trim())

const dp = [Infinity,Infinity,Infinity,1,Infinity,1];

for(let i = 6; i <= n; i++)
    dp.push(Math.min(dp[i - 5], dp[i - 3]) + 1);
             
console.log(dp[n] === Infinity ? -1 : dp[n]);

