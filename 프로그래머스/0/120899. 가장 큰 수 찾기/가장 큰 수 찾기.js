function solution(array) {
    return array.reduce(([max, idx], v, i) => {
        if (v > max) return [v, i];
        return [max, idx];
    }, [0, 0])
    
}