const fs = require('fs');
const stdin = fs.readFileSync('dev/stdin').toString().trim();

const read = stdin.split("\n");
const tc = Number(read[0]);
let rest = read.slice(1);

for(let i = 0; i < tc; i ++ ){
    let [x1, y1, x2, y2] = rest[0].split(" ").map(Number);
    let n = Number(rest[1]);    
    
    let points = rest.slice(2, 2 + n).map(p => p.split(" ").map(Number));
    rest = rest.slice(2 + n);
    
    const dist = (x1, y1, x2, y2) => {
        return (y1 - y2) ** 2 + (x1 - x2) ** 2;
    }
    let cnt = 0;
    for(let [x,y,r] of points){
        let a = dist(x, y, x1, y1) <= r ** 2;
        let b = dist(x, y, x2, y2) <= r ** 2;
        if((a || b) && a != b) {
            cnt += 1;
        }
    }
    
    console.log(cnt);
}