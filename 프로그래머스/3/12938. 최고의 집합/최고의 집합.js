function solution(n, s) {
    if (n > s) return [-1]
    
    var answer = (new Array(n)).fill(parseInt(s / n))
    for(var i = n - s % n; i< n ; i++){
        answer[i] += 1
    }
    return answer
}