from collections import deque
import heapq

def solution(scoville, K):
    
    heapq.heapify(scoville)
    
    cnt = 0
    
    while scoville and scoville[0] < K and len(scoville) >= 2:
        cnt += 1
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville) * 2
        heapq.heappush(scoville, a + b)
        
    return cnt if scoville and scoville[0] >= K else -1

        
    