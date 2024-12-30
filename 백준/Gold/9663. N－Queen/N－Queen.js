const fs = require('fs');

const read = fs.readFileSync('dev/stdin').toString().trim()

const n = parseInt(read);

const main = () => {
    const cols = Array.from({length: n}).fill(false);
    const upright = {};
    const downright = {};
    let cnt = 0
    
    const recur = (r) => {
        if (r == n){
            cnt += 1
            return;
        }
        
        for(let c = 0; c < n; c++ ){
            if (cols[c]) continue;
            if (r - c in upright) continue;
            if (r + c in downright) continue;
            
            cols[c] = true
            upright[r - c] = true
            downright[r + c] = true
            recur(r + 1)
            cols[c] = false
            delete upright[r - c];
            delete downright[r + c];
        }
    }
    
    recur(0)
    return cnt;
}

console.log(main())