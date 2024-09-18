function solution(my_string) {
    let gap = 'a'.charCodeAt() - 'A'.charCodeAt()
    return [...my_string].map(v => {
        let code;
        if ('a' <= v && v <= 'z') code = v.charCodeAt() - gap;
        else code = v.charCodeAt() + gap;
        return String.fromCharCode(code)
    }).join("")
}