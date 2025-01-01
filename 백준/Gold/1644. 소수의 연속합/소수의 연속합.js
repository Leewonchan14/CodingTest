const fs = require('fs');

const read = fs.readFileSync('dev/stdin').toString().trim();

const n = Number(read);

const get_primes = () => {
    const li = new Array(n + 1).fill(true);
    li[0] = false; li[1] = false;
    for (let i = 2; i < n + 1; i ++ ){
        if (li[i]) {
            for (let j = i * 2; j < n + 1; j += i) {
                li[j] = false;
            }
        }
    }
    
    return Array.from(li).map((_, i) => i).filter(i => li[i] && i >= 2);
}

const main = () => {
    const primes = get_primes()
    
    let left = 0
    let right = 0;
    let sumv = 0;
    let cnt = 0;
    while (right <= primes.length) {
        if (sumv < n){
            if(right >= primes.length) break;
            sumv += primes[right++];
            continue;
        }
        
        if (sumv == n){
            cnt += 1;
        }
        sumv -= primes[left++];
    }
    
    return cnt;
}

console.log(main())