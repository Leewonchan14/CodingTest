const fs = require('fs');
const read = fs.readFileSync('dev/stdin').toString().trim();

let [n, arr, oper] = read.split("\n");
arr = arr.split(" ").map(Number);
oper = oper.split(" ").map(Number);

const calcFun = [(a,b) => a + b, (a,b) => a - b, (a,b) => a * b, (a,b) => ~~(a / b)];

const main = () => {
    const result = [-(10 ** 9 + 1), 10 ** 9 + 1];
    const recur = (arr_order, calcv) => {
        if (arr_order === arr.length){
            result[0] = Math.max(calcv, result[0])
            result[1] = Math.min(calcv, result[1])
            return;
        }
        
        for (let i = 0; i < 4; i++){
            if (oper[i] > 0){
                oper[i] -= 1
                recur(arr_order + 1, calcFun[i](calcv, arr[arr_order]));
                oper[i] += 1
            }
        }
    }
    
    recur(1, arr[0])
    
    for(let a of result){
        console.log(a)
    }
}

main()