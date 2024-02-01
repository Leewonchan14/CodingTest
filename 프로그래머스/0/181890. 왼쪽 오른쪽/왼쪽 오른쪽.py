def solution(str_list):
    answer = []
    
    for i in range(len(str_list)):
        if str_list[i] == "l" or str_list[i] == "r":
            if str_list[i] == "r":
                answer = str_list[i+1:]
                break
            else:
                answer = str_list[:i]
                break
                
    return answer