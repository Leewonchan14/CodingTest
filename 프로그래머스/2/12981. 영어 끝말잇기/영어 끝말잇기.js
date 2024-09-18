function solution(n, words) {
    let map = {[words[0]] : 0}
    let result;
    for(let i = 1; i < words.length; i++){
        if (words[i - 1].at(-1) !== words[i][0] || words[i] in map) {
            result = [i % n + 1, Math.floor(i / n) + 1];
            break;
        }
        
        map[words[i]] = 0;
    }
    
    return result ?? [0, 0]
}