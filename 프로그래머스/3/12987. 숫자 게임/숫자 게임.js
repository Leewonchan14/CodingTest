function solution(A, B) {
    A.sort((a,b) => a - b);
    B.sort((a,b) => a - b);
    
    let ai = 0;
    let bi = 0;
    let cnt = 0;
    while (ai < A.length && bi < B.length){
        if (A[ai] < B[bi]){
            ai++;
            bi++;
            cnt++;
        }
        else {
            bi++;
        }
    }
    
    return cnt;
}