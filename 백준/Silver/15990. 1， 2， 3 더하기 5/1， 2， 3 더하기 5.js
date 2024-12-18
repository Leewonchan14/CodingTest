const dp = [
    [0, 0, 0],
    [1, 0, 0],
    [0, 1, 0],
    [1, 1, 1]
]

const getDp = (n) => {
    return (dp[n][0] + dp[n][1] + dp[n][2]) % 1000000009
}

const getDp2 = (n, k) => {
    return (dp[n][0] + dp[n][1] + dp[n][2] - dp[n][k - 1]) % 1000000009
}


const main = (arr) => {
    for(let n of arr){
        
        for(let i = dp.length; i <= n; i++){
            a = getDp2(i - 1, 1);
            b = getDp2(i - 2, 2);
            c = getDp2(i - 3, 3);
            
            dp.push([a, b, c]);
        }
        
        console.log(getDp(n))
    }
}

const fs = require('fs');
let [tc, ...arr] = fs.readFileSync('/dev/stdin').toString().trim().split("\n");
arr = arr.map(Number)

main(arr)