const fs = require('fs')

const [a1,a2,a3,a4] = fs.readFileSync('/dev/stdin').toString().trim().split("\n");

const dic = {}

for(var s of a2.trim().split(" ")) {
    dic[s] = ""
}

for(var s of a4.trim().split(" ")) {
    console.log((s in dic) ? 1 : 0)
}