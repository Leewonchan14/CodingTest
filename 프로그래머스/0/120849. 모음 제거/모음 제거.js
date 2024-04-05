function solution(my_string) {
    let moum = 'aeiou'.split("")
    return my_string.split("").reduce((a,b) => {
        return moum.every(mo => mo !== b) ? a+b : a
    }, "")
}