function solution(sequence) {
    var dp1 = sequence.map((v, i)=>(
        (i % 2 == 0 ? 1 : -1) * v
    ))
    
    var dp2 = sequence.map((v, i)=>(
        (i % 2 != 0 ? 1 : -1) * v
    ))
    
    for(var i = 1; i < sequence.length; i++){
        
        dp1[i] = Math.max(dp1[i-1] + dp1[i], dp1[i])
        dp2[i] = Math.max(dp2[i-1] + dp2[i], dp2[i])
    }
    
    dp1.sort((a,b)=>a - b)
    dp2.sort((a,b)=>a - b)
    
    return Math.max(dp1[dp1.length - 1], dp2[dp1.length - 1])
}