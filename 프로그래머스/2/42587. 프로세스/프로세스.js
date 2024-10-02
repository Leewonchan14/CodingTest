function solution(priorities, location) {
    const cS = [...priorities]
    cS.sort((a,b) => a - b);
    priorities = priorities.map((v,i) => [v,i]);
    
    let cnt = 0;
    
    while(cS.at(-1) != priorities[0][0] || location != priorities[0][1]){
        if (cS.at(-1) === priorities[0][0]){
            priorities.shift()
            cS.pop()
            cnt += 1;
            continue;
        }
        priorities.push(priorities.shift());
    }
    
    return cnt + 1
}