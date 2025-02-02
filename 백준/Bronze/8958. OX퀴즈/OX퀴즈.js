const fs = require('fs');
const stdin = fs.readFileSync('dev/stdin').toString().trim();

const ARR = stdin.split("\n").slice(1).map(s => s.split(""))

for (let arr of ARR) {
    let cnt = 0;
    let sumv = 0;
    for(let v of arr){
        if(v === "O") {
            cnt += 1;
            sumv += cnt;
        } else {
            cnt = 0;
        }
    }
    console.log(sumv);
}