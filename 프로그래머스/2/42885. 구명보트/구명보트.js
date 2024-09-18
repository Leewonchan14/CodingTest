function solution(people, limit) {
    people.sort((a,b) => a - b);
    let cnt = 0;
    let first = 0;
    let last = people.length - 1
    while (first < last){
        if (people[first] +people[ last] <= limit){
            cnt += 1;
            first += 1; last -= 1;
            continue;
        }
        
        last -= 1;
        cnt += 1;
    }
    
    return cnt + (first === last ? 1 : 0)
    
}