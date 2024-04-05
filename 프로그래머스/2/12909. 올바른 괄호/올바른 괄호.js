function solution(s){
    s = [...s]
    let stk = []
    for (let i = 0; i < s.length ; i ++){
        if (stk.length === 0 || s[i] === "("){
            stk.push(s[i])
            continue
        }
        
        if(stk.at(-1) === "("){
            stk.pop()
        }
    }
    
    return stk.length == 0

}