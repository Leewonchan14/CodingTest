function solution(elements) {
    let map = {}
    for(let i = 1; i <= elements.length; i++){
        let size = 0;
        for(let k = 0; k < i; k++){
            size += elements[k];
        }
    
        map[size] = (map[size] ?? 0) + 1;
        
        for(let k = 0; k < elements.length; k++){
            size -= elements.at(k)
            size += elements.at((k + i) % elements.length)
            map[size] = (map[size] ?? 0) + 1;
        }
    }
    return Object.keys(map).length;
}