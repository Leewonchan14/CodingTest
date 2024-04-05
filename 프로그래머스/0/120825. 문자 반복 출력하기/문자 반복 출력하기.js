function solution(my_string, n) {
    return my_string.split("").map(s => s.repeat(n)).join('')
}