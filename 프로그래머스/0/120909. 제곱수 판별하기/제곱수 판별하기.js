function solution(n) {
    return Math.sqrt(n) === Math.floor(n / Math.sqrt(n)) ? 1 : 2;
}