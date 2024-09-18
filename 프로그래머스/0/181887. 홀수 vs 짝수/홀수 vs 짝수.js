function solution(num_list) {
    return Math.max(
        num_list.reduce((acc, v, i) => (i + 1) % 2 === 1 ? acc + v : acc, 0),
        num_list.reduce((acc, v, i) => (i + 1) % 2 === 0 ? acc + v : acc, 0)
    )
}