function solution(start, end_num) {
    rs = []
    for(let i = start ; i >= end_num ; i--){
        rs.push(i)
    }
    return rs
}