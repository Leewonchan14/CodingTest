def solution(m, musicinfos):
    song = "",0
    keys = "C# D# F# G# A# E#".split()
    values = "c d f g a e".split()
    none_list = dict(zip(keys,values))
    
    for k in keys:
        m = m.replace(k, none_list[k])
    
    for i in musicinfos:
        start, end, title, sound = i.split(",")
        
        start = start.split(":")
        end = end.split(":")
        
        diff_h = int(end[0]) - int(start[0])
        diff_m = int(end[1]) - int(start[1])
        
        diff = diff_h * 60 + diff_m
        
        for k in keys:
            sound = sound.replace(k, none_list[k])
        
        sound = "".join([sound[x % len(sound)] for x in range(diff)])
        
        if m in sound and song[1] < diff :
            song = title , diff
    
    return song[0] if len(song[0]) > 0 else '(None)'
        