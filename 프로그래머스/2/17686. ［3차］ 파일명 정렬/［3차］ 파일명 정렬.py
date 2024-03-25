def solution(files):
    def sorter(file):
        index = 0
        while True:
            if '0' <= file[index] <= '9':
                break
            index += 1
        
        str_end_index = index
        
        while index < len(file) and '0' <= file[index] <= '9':
            index += 1
        
        num_end_index = index
        
        first_key = file[:str_end_index].lower()
        second_key = int(file[str_end_index:num_end_index])
        return first_key, second_key 
    
    files.sort(key=sorter)
    
    return files
        