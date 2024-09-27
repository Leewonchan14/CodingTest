const dp = [0, 1, 2, 4]

const fs = require('fs');

const input = fs.readFileSync("/dev/stdin").toString().trim().split('\n').map(a => Number(a));

for(let n of input.slice(1)){
  for(let j = dp.length; j <= n; j++){
    dp.push(dp.at(-1) + dp.at(-2) + dp.at(-3));
  }
  console.log(dp[n]);
}
