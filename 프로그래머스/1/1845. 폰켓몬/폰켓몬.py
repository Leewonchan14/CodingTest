def solution(nums):
    dic = {i: 0 for i in nums}
    if len(nums) // 2 <= len(dic):
        return len(nums) // 2
    return len(dic)