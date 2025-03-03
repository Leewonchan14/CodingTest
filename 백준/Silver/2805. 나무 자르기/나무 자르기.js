// 입력을 받아오기 위해 아래 두줄의 코드를 사용하세요. (수정 금지)
const fs = require('fs');
const stdin = fs.readFileSync('/dev/stdin').toString().trim();

let [nm, arr] = stdin.split("\n");
let [n,m] = nm.split(" ").map(Number);

arr = arr.split(" ").map(Number);

const search = (left, right) => {
    
    if (left > right) {
        return right;
    }

    let mid = Math.floor((left + right) / 2);
    
    let sumv = arr.reduce((acc, i) => acc + Math.max(0, i - mid), 0);
    
    if (sumv >= m) {
        left = mid + 1;
    } else if (sumv < m) {
        right = mid - 1;
    }
    
    return search(left, right);
}

const main = () => {
    console.log(search(0, Math.max(...arr)))
}

main()