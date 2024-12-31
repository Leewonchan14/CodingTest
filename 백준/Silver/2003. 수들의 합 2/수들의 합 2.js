const fs = require('fs');

let read = fs.readFileSync('dev/stdin').toString().trim();

let [nm, arr] = read.split("\n");

const [n,m] = nm.split(" ").map(Number);
arr = arr.split(" ").map(Number);

const main = () => {
    const dp = [0];
    for (let i of arr){
        dp.push(dp.at(-1) + i);
    }
    
    let cnt = 0;
    for (let i = 1; i < dp.length; i++) {
        for (let j = 0; j < i; j ++){
            if (dp[i] - dp[j] == m) cnt += 1;
        }
    }
    
    return cnt;
}

console.log(main());