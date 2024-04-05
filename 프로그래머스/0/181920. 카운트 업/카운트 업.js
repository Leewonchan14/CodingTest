function solution(start_num, end_num) {
    return [...new Array(end_num - start_num + 1)].map((_, i) => {
        return i + start_num
    })
}