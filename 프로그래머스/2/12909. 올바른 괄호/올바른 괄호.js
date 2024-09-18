function solution(s){
    let stk = []
    
    for(let v of s) {
        if (v === ")" && stk.at(-1) === "(") {
            stk.pop();continue;
        }
        
        stk.push(v);
    }
    
    return stk.length === 0 ? true : false;

}