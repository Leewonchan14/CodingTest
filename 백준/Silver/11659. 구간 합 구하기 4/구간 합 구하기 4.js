const fs = require('fs');
const read = fs.readFileSync('dev/stdin').toString().trim();

let [nm, arr, ...abs] = read.split("\n");

let [n,m] = nm.split(" ").map(Number);
arr = arr.split(" ").map(Number);

let dp = [arr[0]];
for(let i = 1; i < n; i++ ){
    dp.push(dp.at(-1) + arr[i]);
}

for(let ab of abs) {
    let [a,b] = ab.split(" ").map(Number);
    let result = dp[b - 1] - (a - 2 >= 0 ? dp[a - 2] : 0)
    console.log(result);
}