function solution(progresses, speeds) {
    const result = []
    let idx = 0;
    let days = 0;
    while(idx < progresses.length){
        days += Math.ceil((100 - (progresses[idx] + speeds[idx] * days)) / speeds[idx]);
        let cnt = 0
        while(idx < progresses.length && progresses[idx] + speeds[idx] * days >= 100){
            cnt += 1;
            idx += 1;
        }
        result.push(cnt);
    }
    
    return result;
}