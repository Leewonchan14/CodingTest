const dp = [
    [],
    [0, ...[...Array(9)].map(() => 1)]
]

const main = (n) => {
    for(let i = dp.length; i <= n; i++){
        dp.push([...Array(10)].map(() => 0))
        for(let j = 0; j < 10; j++){
            a = j - 1 >= 0 ? dp.at(-2)[j - 1] : 0;
            b = j + 1 <= 9 ? dp.at(-2)[j + 1] : 0;
            dp.at(-1)[j] = (a + b) % 1000000000;
        }
    }
    
    sumv = 0
    for(let a of dp.at(-1)) sumv = (sumv + a) % 1000000000;
    
    return sumv
}

const fs = require('fs');
const n = Number(fs.readFileSync('/dev/stdin').toString().trim());

console.log(main(n))