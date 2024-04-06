function solution(n, works) {
    let count = [...new Array(50001)].fill(0)
    let maxv = -1
    works.forEach(x =>{
        count[x] += 1
        maxv = maxv < x ? x : maxv
    })
    
    while (n > 0){
        n -= 1
        count[maxv] -= 1
        count[maxv - 1] += 1
        if (count[maxv] == 0){
            maxv -= 1
            if (maxv == 0){
                break;
            }
        }
    }
    return count.map((v, i) => {
        return i ** 2 * v
    }).reduce((a,b)=> a+b , 0)
}