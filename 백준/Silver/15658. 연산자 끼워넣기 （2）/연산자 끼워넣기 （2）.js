const fs = require('fs');
const read = fs.readFileSync('dev/stdin').toString().trim()
let [n, arr, oper] = read.split("\n");

arr = arr.split(" ").map(Number);
oper = oper.split(" ").map(Number);
const calcFun = [(a,b) => a+b, (a,b) => a-b, (a,b) => a*b, (a,b) => parseInt(a/b) + 0];

const main = () => {
    const li = [-Infinity, Infinity]
    const recur = (order, calcv) => {
        if(order === arr.length){
            li[0] = Math.max(li[0], calcv)
            li[1] = Math.min(li[1], calcv)
            return
        }
        for(let i = 0; i < 4; i++){
            if (oper[i] > 0){
                oper[i] -= 1
                recur(order + 1, calcFun[i](calcv, arr[order]))
                oper[i] += 1
            }
        }
    }
    
    recur(1, arr[0])
    
    li.forEach((a) => {
        console.log(a);
    })
}

main()