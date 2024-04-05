function solution(numbers, n) {            
    let sum = 0
    let rs = 0
    for(let i = 0; i < numbers.length ; i++){
        sum += numbers[i]
        if (sum > n){
            rs = sum
            break;
        }
        
    }
    return rs
}