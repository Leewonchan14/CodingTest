function solution(my_string, letter) {
    my_string = my_string.split("").filter(s => s != letter)
    return my_string.join('')
}