const fs = require('fs');

const [n, ...input] = fs.readFileSync('/dev/stdin').toString().trim().split("\n").map(Number);

const dp = [[1, 0], [0, 1]];

for(let i of input){
    for(let j = dp.length; j <= i; j++){
        const [a1, a2] = dp.at(-1);
        const [b1, b2] = dp.at(-2);
        dp.push([a1 + b1, a2 + b2]);
    }
    
    console.log(dp[i].join(" "));
}