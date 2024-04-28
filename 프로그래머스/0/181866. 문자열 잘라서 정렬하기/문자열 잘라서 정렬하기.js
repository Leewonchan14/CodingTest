function solution(myString) {
    return myString.split("x").filter((x) => x != '')
    .sort((a,b) => a < b ? -1 : 1)
}