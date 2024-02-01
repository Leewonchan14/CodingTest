def solution(numbers):
    a = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i in range(len(a)):
        numbers = numbers.replace(a[i], str(i))
    
    return int(numbers)