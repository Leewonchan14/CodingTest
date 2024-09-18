function getOneCount(s){
    return s. toString(2).split("").filter(v => v === "1").length;
}

function solution(n) {
    let oCnt = getOneCount(n);
    n += 1
    while (oCnt !== getOneCount(n)) {
        n += 1
    }
    return n;
}