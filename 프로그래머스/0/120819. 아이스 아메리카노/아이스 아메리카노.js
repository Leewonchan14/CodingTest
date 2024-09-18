function solution(money) {
    let cnt = Math.floor(money / 5500);
    return [cnt , money - cnt * 5500]
}