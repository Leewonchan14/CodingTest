function solution(participant, completion) {
    const dic = {}
    participant.forEach(v => {
        dic[v] = (dic[v] ?? 0) + 1
    });
    
    completion.forEach(v => {
        dic[v] -= 1;
        if (dic[v] === 0) delete dic[v];
    });
    
    return Object.keys(dic)[0]
}