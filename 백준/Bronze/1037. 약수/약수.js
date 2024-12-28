const fs = require('fs');

const [_, _arr] =fs.readFileSync('dev/stdin').toString().trim().split("\n")
const arr = _arr.split(" ").map(Number);
arr.sort((a,b) => a -b);
console.log(arr.at(-1) * arr[0]);