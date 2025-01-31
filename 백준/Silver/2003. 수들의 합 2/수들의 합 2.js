const fs = require('fs');

let read = fs.readFileSync('dev/stdin').toString().trim();

let [nm, arr] = read.split("\n");

const [n,m] = nm.split(" ").map(Number);
arr = arr.split(" ").map(Number);

const main = () => {
    let l = 0;
    let r = 1;
    let sumv = arr[0];
    let cnt = 0;
    while (true){
        if (sumv === m){
            cnt += 1;
            sumv -= arr[l];
            l += 1;
            continue;
        }
        if (sumv < m) {
            if (r >= n) break;
            sumv += arr[r];
            r += 1;
            continue;
        }
        if (sumv > m) {
            sumv -= arr[l];
            l += 1;
            continue;
        }
    }
    
    return cnt;
}

console.log(main());