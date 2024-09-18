function solution(num_list) {
    let ar = ["", ""]
    num_list.forEach(v => v % 2 === 0 ? ar[0] += v : ar[1] += v)
    return Number(ar[0]) + Number(ar[1])
}