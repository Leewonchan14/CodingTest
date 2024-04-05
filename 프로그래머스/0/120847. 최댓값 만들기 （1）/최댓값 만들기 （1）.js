function solution(numbers) {
    numbers.sort((a,b) => a-b)
    let [a,b] = numbers.slice(-2)
    return a*b
}