// 입력을 받아오기 위해 아래 두줄의 코드를 사용하세요. (수정 금지)
const fs = require('fs');
const stdin = fs.readFileSync('/dev/stdin').toString().trim();

let [n, maps] = stdin.split("\n");
n = Number(n)
maps = maps.split(" ").map(Number);
let costs = new Array(n).fill(Infinity);
costs[0] = 0;

let que = [[0, 0]];
while(que.length) {
    let [x, cnt] = que.shift();
    for(let i = 1; i <= maps[x]; i++ ){
        let nx = x + i;
        if(nx < n && cnt + 1 < costs[nx]){
            costs[nx] = cnt + 1;
            que.push([nx, cnt + 1]);
        }
    }
}

console.log(costs.at(-1) == Infinity ? -1 : costs.at(-1));