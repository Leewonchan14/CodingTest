const fs = require('fs');
const [n, k] = fs.readFileSync('/dev/stdin').toString().trim().split(" ").map(Number);
const li = [];
const recur = () => {
    if (li.length == k) {
        console.log(li.join(" "));
        return;
    }
    
    for(let i = 1; i <= n; i++){
        if (li.length == 0 || i > li.at(-1)){
            li.push(i)
            recur()
            li.pop()    
        }
    }
}

recur()