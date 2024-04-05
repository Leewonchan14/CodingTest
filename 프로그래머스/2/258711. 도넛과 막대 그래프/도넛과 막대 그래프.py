"""
1. 아이디어
    - 들어오는 간선이 없고 나가는 간선이 2개이상이라면 연결 노드이다.
    - 가장 큰 노드 번호가 노드의 갯수이다.
    - 연결리스트들을 저장해 놓는다.
    - 연결노드의 나가는 간선들을 조사해 각 그래프의 종류를 계산한다.
    - BFS 를 이용해 노드를 조사할때 사이클이 존재하지 않는다면 막대 그래프이다.
    - 사이클이 존재하고 각 노드가 나가는 간선이 2개이상 존재한다면 8자 그래프이다.
    - 나머지는 도넛 그래프이다.
    
2. 시간 복잡도
    - 모든 간선 접근 => 10 ^ 6
    - 연결노드 찾기 => 10 ^ 6
    - 모든 노드 접근하며 그래프 갯수 세기 => 10 ^ 6
    - 10 ^ 6 * 3
    가능
    
3. 자료구조
    - go : {node : connect_list} : 나가는 간선저장 딕셔너리
    - back : {node : connect_list} : 들어오는 간선저장 딕셔너리
    - visited : [False] * 노드갯수 : 방문점검 리스트
    
    
"""

"""
도넛 : 1
막대 : 2
8자 : 3
"""
from collections import deque

def some_graph(visited, go, start):
    que = deque()
    visited[start] = True
    que.append(start)
    is_stick = True
    is_donut = True
    is_8 = True
    while que:
        k = que.popleft()
        for nk in go.get(k, []):
            if not visited[nk]:
                # 나가는 간선이 2개 이상 존재한다면 8 그래프
                if len(go.get(k, [])) >= 2:
                    is_donut = False
                visited[nk] = True
                que.append(nk)
            # 방문한 노드를 다시 방문한다
            elif visited[nk]:
                is_stick = False
                
    if is_stick:
        return 2
    
    if not is_donut:
        return 3
    
    return 1
        

def solution(edges):
    go = {}
    back = {}
    node_count = 0
    for a,b in edges:
        node_count = max([node_count , a, b])
        
        go[a] = go.get(a, [])
        go[a].append(b)
        
        back[b] = back.get(b, [])
        back[b].append(a)
        
    connect_node = 0
    
    for k in go.keys():
        if not back.get(k,[]) and len(go[k]) >= 2:
            connect_node = k
            
    visited = [False] * (node_count + 1)
    
    rs = [connect_node, 0 ,0,0]
    
    for s in go[connect_node]:
        id = some_graph(visited, go, s)
        rs[id] += 1
        
    return rs
    