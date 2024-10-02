const fs = require('fs')

const [_, a, __, b] = fs.readFileSync('/dev/stdin').toString().trim().split("\n").map(c => c.trim())

const dic = {}

for(let i of a.split(" ")){
    dic[i] = (dic[i] ?? 0) + 1;
}
console.log(b.split(" ").map(c => dic[c] ?? 0).join(" "))
              