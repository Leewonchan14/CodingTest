function solution(my_string) {
    return [...my_string].filter(i => "123456789".includes(i)).reduce((a,b)=>{
        return a + parseInt(b)
    }, 0)
}