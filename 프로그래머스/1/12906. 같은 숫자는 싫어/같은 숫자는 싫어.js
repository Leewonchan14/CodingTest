function solution(arr)
{
    const result = []
    for(let i of arr){
        if (result[result.length - 1] === i) continue;
        result.push(i);
    }
    
    return result;
}