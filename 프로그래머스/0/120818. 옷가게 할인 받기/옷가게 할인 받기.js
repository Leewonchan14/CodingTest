let man = 10000;

function getHal(price) {
    if (price >= 50 * man) return 20;
    if (price >= 30 * man) return 10;
    if (price >= 10 * man) return 5;
    return 0;
    
}

function solution(price) {
    let hal = getHal(price);
    return Math.floor(price - (price * (hal / 100)))
}


    