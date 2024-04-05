function solution(num_list) {   
    let mul = num_list.reduce((a,b)=>{
        return a*b 
    }, 1)
    
    let sum = num_list.reduce((a,b)=>{
        return a+b
    }, 0)
    
    return sum**2 > mul ? 1 : 0
}