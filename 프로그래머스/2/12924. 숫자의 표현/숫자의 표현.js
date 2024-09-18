function solution(n) {
    let cnt = 0;
    let limit = 0;
    for (let i = 1; i <= n; i++) {
        if (limit >= n) break;
        
        if (i % 2 === 1){
            let center = n / i;
            if(n % i === 0 && n === center * (2 * i - 1)) cnt++;
        } else {
            let center = Math.floor(n / i)
            if((i / 2) * (2 * center + 1) === n) cnt++;
        }
    }
    
    return cnt;
}