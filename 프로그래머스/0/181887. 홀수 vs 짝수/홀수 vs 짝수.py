def solution(num_list):
    return max(
        sum([num_list[i] for i in range(len(num_list))  if (i + 1) % 2 == 0]),
        sum([num_list[i] for i in range(len(num_list))  if (i + 1) % 2 == 1])
     )
             
             