const fs=  require('fs');

const read = fs.readFileSync('dev/stdin').toString().trim();

let [nm, arr] = read.split("\n");

const [n, m] = nm.split(" ").map(Number);
arr = arr.split(" ").map(Number);

const main = () => {
    let left = 0;
    let right = 0;
    let sumv = 0;
    const result = [];
    while (right <= arr.length){
        if (sumv >= m){
            result.push(right - left)
            sumv -= arr[left++];
            continue
        }
        
        if (right >= arr.length) break;
        
        sumv += arr[right++];
    }
    
    result.sort((a,b) => a - b)
    return result.length ? result[0] : 0;
}

console.log(main())