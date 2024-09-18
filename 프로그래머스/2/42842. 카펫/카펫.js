function solution(brown, yellow) {
    for (let h of [...Array(Math.floor(Math.sqrt(yellow)) + 1)].map((v,i) => i)){
        if (yellow % h !== 0) continue;
        let w = yellow / h;
        
        if (2* (w + h) + 4 === brown) return [w + 2, h + 2]
    }
}