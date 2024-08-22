function solution(my_string) {
    const arr =[];
    Array.from(my_string).forEach((i, index) => {
        arr.push(my_string.slice(index));
    });
    
    arr.sort();
    
    return arr;
}