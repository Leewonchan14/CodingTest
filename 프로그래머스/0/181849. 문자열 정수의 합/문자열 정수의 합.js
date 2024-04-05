function solution(num_str) {
    return [...num_str].reduce((a,b)=>{
        return a + parseInt(b)
    }, 0)
}