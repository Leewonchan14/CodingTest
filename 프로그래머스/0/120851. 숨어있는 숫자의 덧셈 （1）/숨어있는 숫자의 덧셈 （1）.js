function solution(my_string) {
    return [...my_string].filter(v => "123456789".includes(v)).reduce((acc, v)=>acc + Number(v), 0)
}