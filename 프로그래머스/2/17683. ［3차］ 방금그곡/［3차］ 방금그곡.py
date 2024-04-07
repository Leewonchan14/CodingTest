keys = "C# D# F# G# A# E# B#".split()
values = "c d f g a e b".split()
mapper = dict(zip(keys, values))


def to_music(music):
    for k in mapper.keys():
        music = music.replace(k, mapper[k])
        
    return music

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
        
        melody = music * repeat + music[:div]
        
        if m in melody:
            ls.append((-gap_minute, len(ls), title))
            
    ls.sort(key=lambda x: x[0])
    if ls:
        return ls[0][2]
    
    return "(None)"
            