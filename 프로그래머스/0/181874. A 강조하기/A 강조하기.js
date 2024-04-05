function solution(myString) {
    return [...myString.toLowerCase()].map(s => s === 'a' ? 'A' : s).join('')
}