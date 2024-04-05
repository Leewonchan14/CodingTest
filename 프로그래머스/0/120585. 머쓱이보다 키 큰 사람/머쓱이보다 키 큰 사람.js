function solution(array, height) {
    return array.filter(n => n > height).length
}