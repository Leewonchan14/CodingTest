const fs = require('fs');
const [n, k] = fs.readFileSync('/dev/stdin').toString().trim().split(" ").map(Number);

let cnt = 0;
let answer = ''
const li = []
const recur = () => {
    if(li.length == k) {
        answer += li.join(" ") + "\n"
        return;
    }
    
    for(let i = 1; i <=n; i++){
        li.push(i);
        recur()
        li.pop();
    }
}

recur()

console.log(answer)