const fs = require('fs');

const [a,b] = fs.readFileSync('dev/stdin').toString().trim().split(" ").map(Number);
const aa = Math.min(a,b);
const bb = Math.max(a,b);
const gcd = () => {
    for (let i = aa; i >= 1; i--){
        if (aa % i === 0 && bb % i === 0) {
            return i;
        }
    }
}
const lcm = () => {
    let temp1 = aa
    let temp2 = bb
    
    while(temp1 != temp2){
        if (temp1 < temp2){
            temp1 += aa
        } else{
            temp2 += bb
        }
    }
    
    return temp1;
}

console.log(gcd())
console.log(lcm())