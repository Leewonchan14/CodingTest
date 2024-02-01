def solution(my_string, overwrite_string, s):
    a = my_string[:s]
    b = overwrite_string
    c = my_string[s + len(overwrite_string):]
    return  "".join([a,b,c])