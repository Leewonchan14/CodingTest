def solution(a, b):
    A = str(a)
    B = str(b)
    return int(f"{A}{B}") if int(f"{A}{B}") > int(f"{B}{A}") else int(f"{B}{A}")
        
        