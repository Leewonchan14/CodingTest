function solution(num_list) {
    return num_list.reduce((acc, v, i) => v < 0 ? (acc !== -1 ? acc : i) : acc, -1)
}