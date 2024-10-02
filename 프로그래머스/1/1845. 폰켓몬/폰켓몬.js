function solution(nums) {
    doc = {}
    for(let i of nums){
        doc[i] = (doc[i] ?? 0) + 1;
    }
    
    let max = Object.keys(doc).length;
    let div = Math.floor(nums.length / 2);

    return max >= div ? div : max
}