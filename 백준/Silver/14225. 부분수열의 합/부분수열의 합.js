const fs = require('fs');

let [_, arr] = fs.readFileSync('dev/stdin').toString().trim().split("\n");
arr = arr.split(" ").map(Number);

const main = () => {
    const dp = Array.from({length : 10 ** 6 + 1}).fill(true);
    const li = []
    const recur = (sumv) => {
        if (li.length != 0 && sumv < dp.length) {
            dp[sumv] = false;
        }
        
        if (li.length === arr.length) return;
        
        for (let i = 0; i < arr.length; i++){
            if(!li.length || i > li.at(-1)){
                li.push(i)
                recur(sumv + arr[i]);
                li.pop()
            }
        }
    }
    
    recur(0)
    
    for(let i = 1; i < dp.length; i++){
        if(dp[i]) return i;
    }
}

console.log(main())