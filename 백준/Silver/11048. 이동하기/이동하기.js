// 입력을 받아오기 위해 아래 두줄의 코드를 사용하세요. (수정 금지)
const fs = require('fs');
const stdin = fs.readFileSync('/dev/stdin').toString().trim();


let [nm, ...maps] = stdin.split("\n");
let [n,m] = nm.split(" ").map(Number);
maps = maps.map(row => row.split(" ").map(Number));

let d = [[-1, 0],[0, -1],[-1,-1]];

for(let r = 0; r < n; r ++) {
    for (let c = 0; c < m; c++ ){
        let maxv = 0;
        for(let i = 0; i < 3; i ++ ){
            let [nr , nc] = [r + d[i][0], c + d[i][1]];
            if (0 <= nr && 0 <= nc) {
                maxv = Math.max(maxv, maps[nr][nc]);
            }
        }
        maps[r][c] += maxv;
    }
}

console.log(maps.at(-1).at(-1));
