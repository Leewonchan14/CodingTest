function solution(k, tangerine) {
    let map = {}
    for(let t of tangerine){
        map[t] = (map[t] ?? 0) + 1;
    }
    
    let values = Object.values(map).sort((a,b) => a - b);
    
    let cnt = 0;
    while (k > 0){
        k -= values.pop();
        cnt += 1
    }
    
    return cnt;
}