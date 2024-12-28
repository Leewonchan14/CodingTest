const fs = require('fs');

const [_, ..._arr] = fs.readFileSync('dev/stdin').toString().trim().split("\n");
const arr = _arr.map(s => s.split(" ").map(Number))

const range = (start, end) => {
    return Array.from({length : end - start}).map((e,i) => i);
}

const getPairSum = (team) => {
    let sumv = 0
    for (let i = 0; i < team.length - 1; i++){
        for(let j = i + 1; j < team.length; j++){
            sumv += arr[team[i]][team[j]] + arr[team[j]][team[i]]
        }
    }
    
    return sumv
}

const combi = (n, k) => {
    const result = []
    const li = []
    const recur = () => {
        if (li.length == k){
            result.push([...li])
            return
        }
        
        for (let i = 0; i < n; i++ ){
            if(li.length == 0 || i > li.at(-1)){
                li.push(i)
                recur()
                li.pop()
            }
        }
    }
    
    recur()
    
    return result
}

const main = () => {
    let minv = Infinity
    const pair = combi(Math.floor(arr.length / 2), 2);
    for(let teamA of combi(arr.length, Math.floor(arr.length / 2))){
        let teamB = range(0, arr.length).filter(i => !teamA.includes(i));
        minv = Math.min(minv, Math.abs(getPairSum(teamA) - getPairSum(teamB)));
    }
    
    console.log(minv)
}

main()