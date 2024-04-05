function solution(cipher, code) {
    rs = []
    cipher = [...cipher]
    for (let i = code - 1; i < cipher.length ; i += code){
        rs.push(cipher[i])
    }
    return rs.join('')
}