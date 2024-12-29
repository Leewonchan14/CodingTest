const fs = require('fs');

const [a, b] = fs.readFileSync('dev/stdin').toString().trim().split("\n");
const [_, s] =a.split(" ").map(Number);
const arr = b.split(" ").map(Number);

const main = () => {
    const li = []
    let cnt = 0
    const recur = (sumv) => {
        if (li.length != 0 && sumv == s){
            cnt += 1;
        }
        
        if (li.length === arr.length) return;
        
        for (let i = 0; i < arr.length; i ++ ){
            if(li.length == 0 || i > li.at(-1)){
                li.push(i)
                recur(sumv + arr[i]);
                li.pop()
            }
        }
    }
    
    recur(0);
    
    console.log(cnt)
}

main()
