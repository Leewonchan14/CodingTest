function solution(prices) {
    const dic = {}
    const result = []
    for(let i = prices.length - 1; i >= 0; i--) {
        if (i === prices.length - 1 ) {
            dic[i] = 0;
            result.push(0);
            continue;
        }
        
        let start = i;
        let temp = i + 1
        let tV = prices[i + 1];
        
        while (tV >= prices[i] && dic[temp] != 0){
            temp += dic[temp]
            tV = prices[temp]
        }
        
        dic[i] = temp - start;
        result.push(temp - start);
    }
    
    result.reverse();
    return result;
}