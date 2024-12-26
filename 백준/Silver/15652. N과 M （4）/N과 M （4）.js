const fs = require('fs');

const [n, k] = fs.readFileSync('/dev/stdin').toString().split(" ").map(Number);

const li = []
let answer = "";
const recur = () => {
    if(li.length === k){
        answer += li.join(" ") + "\n";
        return;
    }
    
    for (let i = 1; i <= n; i++){
        if(li.length === 0 || i >= li.at(-1)) {
            li.push(i)
            recur()
            li.pop()
        }
    }
}

recur()
console.log(answer);