function solution(hp) {
    return [5,3,1].reduce((acc, v) => {
        let cnt = Math.floor(hp / v);
        hp -= cnt * v;
        return acc + cnt
    }, 0)
}