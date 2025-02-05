const fs = require('fs');
const read = fs.readFileSync('dev/stdin').toString().trim();

let arr = read.split("\n").slice(1);
let result = "";

for(let v of arr){
    let [a, b] = v.split(" ").map(Number);
    result += a + b + "\n";
}

console.log(result);

