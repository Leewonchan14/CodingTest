const fs = require('fs')

const [n, ...inputs] = fs.readFileSync("/dev/stdin").toString().trim().split("\n")

const que = [];

for(let s of inputs){
    s = s.trim();
    const [a, b] = s.split(" ");
    
    if (a === "push"){
        que.push(b);
    } else if(a === "pop"){
        console.log(que.length ? que.shift() : -1);
    } else if(a === "size"){
        console.log(que.length)
    } else if (a === "empty"){
        console.log(que.length === 0 ? 1 : 0)
    } else if (a === "front"){
        console.log(que[0] ?? -1)
    } else if (a === "back"){
        console.log(que.at(-1) ?? -1)
    }
}