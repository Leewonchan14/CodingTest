const fs = require("fs");
const [a, b] = fs.readFileSync(0, 'utf-8').toString().trim().split(' ')
console.log(+a + +b);