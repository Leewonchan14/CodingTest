const fs = require('fs')

const read =fs.readFileSync('dev/stdin').toString().trim();

let [n, arr] = read.split("\n");
n = Number(n)
arr = arr.split(" ").map(Number)

const main = () => {
    const mask = new Array(100000 * 20 + 1).fill(false);
    const li = [];
    const recur = (sumv) => {
        if (li.length) mask[sumv] = true;
        if (li.length == n) return;
        
        for(let i = 0 ; i < arr.length; i++ ){
            if(!li.length || i > li.at(-1)) {
                li.push(i)
                recur(sumv + arr[i]);
                li.pop()
            }
        }
    }
    
    recur(0);
    
    let i = 1
    while (mask[i]) i++;
    return i;
}

console.log(main())