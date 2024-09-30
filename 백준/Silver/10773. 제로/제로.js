const fs = require('fs')

const [n , ...inputs] = fs.readFileSync("/dev/stdin").toString().trim().split("\n").map(c => Number(c.trim()))

const stk = []

for(let i of inputs){
    if(i === 0) stk.pop();
    else stk.push(i);
}

console.log(stk.reduce((acc, value, index) => acc + value,0))