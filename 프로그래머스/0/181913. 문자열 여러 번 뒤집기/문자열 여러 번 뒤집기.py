def solution(my_string, queries):
    
    for i in queries:
        a = my_string[:i[0]]
        b = my_string[i[0]:i[1] + 1][::-1]
        c = my_string[i[1] + 1:]
        my_string = "".join([a,b,c])
    
    return my_string