def solution(numbers):
    numbers = list(map(lambda x : ((str(x) * 4)[:4],str(x)), numbers))
    numbers.sort(reverse=True)
    join = "".join(map(lambda x:x[1], numbers))
    return "0" if join[0] == "0" else join