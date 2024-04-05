function solution1(numbers) {
    let sum = 0;
    for (let i = 0; i < numbers.length ; i++){
        sum += numbers[i]
    }
    return sum / numbers.length
}

function solution2(numbers) {
    let sum = 0;
    numbers.forEach(num => {
        sum += num
    })
    return sum / numbers.length
}

function solution(numbers) {
    let sum = numbers.reduce((a,b) => a+b, 0)
    return sum / numbers.length
}