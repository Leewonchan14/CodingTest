let map = {
    ["{"] : "}",
    ["["] : "]",
    ["("] : ")",
    ["}"] : "{",
    ["]"] : "[",
    [")"] : "("
}

function isCollect(s){
    let stk = [];
    let close = "}])";
    
    for(let v of s){
        if(close.includes(v) && map[v] === stk.at(-1)) {
            stk.pop();
            continue;
        }
        stk.push(v)
    }
    
    return stk.length === 0 ? true : false
}

function solution(s) {
    let cnt = 0;
    for(let i = 0; i < s.length; i++){
        cnt += isCollect(s) ? 1 : 0;
        s = s.slice(1) + s[0]
    }
    
    return cnt;
}