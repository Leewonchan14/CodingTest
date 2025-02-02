const fs = require('fs');
const stdin = fs.readFileSync('dev/stdin').toString().trim();

let n = Number(stdin);

for (let i = n ; i >= 1; i-=1){
    console.log(i);
}