def solution(data, ext, val_ext, sort_by):
    dic = dict(zip(["code", "date", "maximum", "remain"], [0,1,2,3]))
    fi = filter(lambda x : (
        x[dic[ext]] < int(val_ext)
    ), data)
    
    fi = list(fi)
    
    fi.sort(key=lambda x: x[dic[sort_by]])
    
    return fi