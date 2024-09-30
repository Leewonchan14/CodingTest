const fs = require('fs')

const [n, ...inputs] = fs.readFileSync('/dev/stdin').toString().trim().split("\n").map(c => Number(c.trim()))

const order = [...Array(n)].map((_, i) => n - i);
inputs.reverse()

const stk = []
const result = []

let flag = true;

while(!!order.length || !!inputs.length){
    while (!stk.length || (stk.length && order.length && inputs.length && stk.at(-1) < inputs.at(-1))){
        stk.push(order.pop());
        result.push(1);
    }
    
    while (stk.length && inputs.length && stk.at(-1) === inputs.at(-1)){
        stk.pop()
        inputs.pop()
        result.push(0);
    }
    
    if (stk.length && inputs.length && stk.at(-1) > inputs.at(-1)){
        flag = false;
        break;
    }
}

if (flag){
    console.log(result.map((a) => a ? "+" : "-").join("\n"))
} else {
    console.log("NO");
}
