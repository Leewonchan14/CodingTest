const fs = require('fs');

const [_, ..._arr] = fs.readFileSync('dev/stdin').toString().trim().split("\n");
const arr = _arr.map(s => s.split(" ").map(Number))

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
        let teamB = Array.from({length: arr.length}).map((e, i) => i).filter(i => !teamA.includes(i));
        const sumA = pair.reduce((acc, [a,b]) => acc + arr[teamA[a]][teamA[b]] + arr[teamA[b]][teamA[a]], 0);
        const sumB = pair.reduce((acc, [a,b]) => acc + arr[teamB[a]][teamB[b]] + arr[teamB[b]][teamB[a]], 0);
        
        minv = Math.min(minv, Math.abs(sumA - sumB));
    }
    
    console.log(minv)
}

main()