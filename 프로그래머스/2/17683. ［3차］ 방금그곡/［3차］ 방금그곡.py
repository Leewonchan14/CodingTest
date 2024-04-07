def to_music(music):
    ls = []
    index = 0
    length = len(music)
    while index < length:
        if index + 1 < length and music[index + 1] == "#":
            ls.append(music[index:index + 2])
            index += 2
            continue
            
        ls.append(music[index:index+1])
        index += 1
    return ls
    

def to_minute(s):
    h, m = map(int,s.split(":"))
    return h * 60 + m
    

def solution(m, musicinfos):
    m = to_music(m)
    
    ls = []
    
    for m_ in musicinfos:
        start, end, title, music = m_.split(",")
        gap_minute = to_minute(end) - to_minute(start)
        music = to_music(music)
        length = len(music)
        
        repeat = gap_minute // length
        div = gap_minute % length
        
        melody = sum([music * repeat, music[:div]], [])
        
        for i in range(len(melody)):
            if m[0] == melody[i]:
                if i + len(m) <= len(melody) and all([melody[i + j] == m[j] for j in range(len(m))]):
                    ls.append((-gap_minute, title))
                    break
            
            
    ls.sort(key=lambda x: x[0])
    if ls:
        return ls[0][1]
    
    return "(None)"
            