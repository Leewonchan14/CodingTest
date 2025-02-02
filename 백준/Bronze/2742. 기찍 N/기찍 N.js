const fs = require('fs');
const stdin = fs.readFileSync('dev/stdin').toString().trim();

let n = Number(stdin);


let str = "";

for (let i = n ; i >= 1; i-=1){
    str += i + "\n";
}

console.log(str);