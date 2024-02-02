def solution(m, musicinfos):
    answer = '(None)'
    m = m.replace('A#', 'H').replace('C#', 'I').replace('D#', 'J').replace('F#', 'K').replace('G#', 'L')
    max_time = 0
    for info in musicinfos:
        start, end, title, melody = info.split(',')
        start = start.split(':')
        end = end.split(':')
        time = (int(end[0]) - int(start[0])) * 60 + int(end[1]) - int(start[1])
        melody = melody.replace('A#', 'H').replace('C#', 'I').replace('D#', 'J').replace('F#', 'K').replace('G#', 'L')
        melody = melody * (time // len(melody)) + melody[0:time % len(melody)]
        if m in melody and time > max_time:
            max_time = time
            answer = title
    return answer
# def solution(m, musicinfos):
#     song = "",0
#     keys = "C# D# F# G# A# E#".split()
#     values = "c d f g a e".split()
#     none_list = dict(zip(keys,values))
    
#     for k in keys:
#         m = m.replace(k, none_list[k])
    
#     for i in musicinfos:
#         music = i.split(",")
        
#         start = music[0].split(":")
#         end = music[1].split(":")
        
#         diff_h = int(end[0]) - int(start[0])
#         diff_m = int(end[1]) - int(start[1])
        
#         diff = diff_h * 60 + diff_m
        
#         sound = music[3]
        
#         for k in keys:
#             sound = sound.replace(k, none_list[k])
        
#         sound = "".join([sound[x % len(sound)] for x in range(diff)])
        
#         title = music[2]
        
#         if m in sound and song[1] < diff :
#             song = title , diff
#             print(song)
    
#     return song[0] if len(song[0]) > 0 else None

# # print(solution("BA", ["12:00,12:02,Song,AB"] ))
# # print(solution("BA", ["12:00,12:03,Song,AB"] ))
# # print(solution("BA", ["12:00,12:04,Song,A#B"]))
        
# # print(solution("BA", ["12:00,12:04,Song,A#B"]))
# # print(solution("A", ["12:00,12:01,Song,A#"]))
# # print(solution("A#", ["12:00,12:01,Song,A#"]))

# # print(solution("ABA", ["12:00,13:00,Song,AB"]))

# # print(solution("A", ["12:00,12:01,Sing,A", "12:00,12:01,Song,A"]))
# # print(solution("A", ["12:00,12:01,Sing,A", "12:00,12:02,Song,A"]))
# # print(solution("A", ["12:00,12:01,Sing,A", "12:00,13:00,Song,A"]))


        