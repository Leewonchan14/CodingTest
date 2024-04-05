function solution(num_list, n) {
    let rs = []
    for (let i = 0; i < num_list.length ; i += n){
        rs.push(num_list[i])
    }
    return rs
}