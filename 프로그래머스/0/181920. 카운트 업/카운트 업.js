function solution(start_num, end_num) {
    return [...Array(end_num - start_num + 1)].map((v,i) => i + start_num)
}