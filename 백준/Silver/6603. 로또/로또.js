const fs = require('fs');
const arr = fs.readFileSync('dev/stdin').toString().trim().split("\n");
arr.pop()

const combi = (n, k, callback = () => {}) => {
    const li = [];
    const recur = () => {
        if (li.length === k){
            return callback(li);
        }
        
        for(let i = 0; i < n; i++ ){
            if(li.length == 0 || i > li.at(-1)){
                li.push(i)
                recur()
                li.pop()
            }
        }
    }
    
    recur();
}

const solve = (s) => {
    const [_, ...array] = s.split(" ").map(Number)
    combi(array.length, 6, (li) => {
        console.log(...li.map(i => array[i]));
    });
}

const main = () => {
    for (let i = 0; i < arr.length; i++) {
        solve(arr[i]);
        if (i != arr.length - 1){
            console.log();
        }
    }    
}

main()