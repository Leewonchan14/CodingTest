function solution(num_list) {
    let ggac = num_list.filter(a => a % 2 === 0 ).length
    return [ggac , num_list.length - ggac]
    
}