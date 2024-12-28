const fs = require('fs');

const [hw, ..._arr] = fs.readFileSync('dev/stdin').toString().trim().split("\n");
const [h,w,x,y] =hw.split(" ").map(Number);
const arr = _arr.map(r => r.split(" ").map(Number));

const main = () => {
    const arr1 = arr.slice(0, h).map(r => r.slice(0, w));
    const arr2 = arr.slice(x, x + h).map(r => r.slice(y, y + w));
    
    for(let r = x; r < h; r++){
        for(let c = y; c < w; c++){
            arr1[r][c] = arr2[r - x][c - y] - arr1[r - x][c - y]
        }
    }
    
    for(let rr of arr1){
        console.log(...rr);
    }
}
main()

