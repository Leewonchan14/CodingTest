function getLeast(n){
    if (n === 0) return 0;
    if (n === 1) return 1;
    if(n % 2 === 0) return getLeast(n / 2)
    if (n % 2 === 1) return getLeast((n - 1) / 2) + 1
}

function solution(n){
    return getLeast(n);
}