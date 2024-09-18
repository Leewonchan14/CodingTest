function solution(num_list) {
    let last = num_list.at(-1)
    let preLast = num_list.at(-2)
    if (last > preLast) num_list.push(last - preLast);
    else num_list.push(last * 2);
    return num_list
}