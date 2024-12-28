const fs = require('fs');

let [tc, ...arr] = fs.readFileSync('dev/stdin').toString().trim().split("\n")
arr = arr.map(Number);
const dp = [[arr[0], arr[0], 0]]

for(let i = 1; i < arr.length; i++){
    const a = dp.at(-1)[2] + arr[i];
    const b = dp.at(-1)[0] + arr[i];
    const c = Math.max(dp.at(-1)[0], dp.at(-1)[1])
    dp.push([a,b,c]);
}

console.log(Math.max(dp.at(-1)[0], dp.at(-1)[1]));
