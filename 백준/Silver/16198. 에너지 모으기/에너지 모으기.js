const fs = require('fs');

const read = fs.readFileSync('dev/stdin').toString().trim();

let [n, arr] = read.split("\n");
arr = arr.split(" ").map(Number);

const main = () => {
    const visited = Array.from(arr).fill(false);
    let maxv = 0
    const recur = (sumv, cnt) => {
        if (cnt === arr.length - 2){
            maxv = Math.max(maxv, sumv);
            return;
        }
        
        for (let i = 1; i < arr.length - 1; i++){
            if (visited[i]) continue;
            
            let left = i - 1
            let right = i + 1
            while (visited[left]) left -= 1;
            while(visited[right]) right += 1;
            
            visited[i] = true
            recur(sumv + arr[left] * arr[right], cnt + 1);
            visited[i] = false
        }
    }
    
    recur(0, 0)
    return maxv
}

console.log(main())