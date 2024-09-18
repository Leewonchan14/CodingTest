function solution(s){
    let stk = [];
    for(let v of s){
        if (stk.at(-1) === v){
            stk.pop();
            continue;
        } 
        
        stk.push(v)
    }
    
    return stk.length === 0 ? 1 : 0;
}