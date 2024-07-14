function solution(n, computers) {
    let isVisit = Array.from({length : n}).fill(false);
    
    let cnt = 0;
    for(let i=0 ; i < n ; i++){
        if (isVisit[i]) continue;
        cnt += 1;
        dfs(i,isVisit,computers, n);
    }
    
    return cnt;
}

let dfs = (i, isVisit,computers, n) => {
    for(let a = 0; a < n; a++){
        if(computers[i][a] === 1 && !isVisit[a]) {
            isVisit[a] = true;
            dfs(a,isVisit,computers, n);
        }
    }
}