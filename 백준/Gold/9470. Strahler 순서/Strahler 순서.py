import sys
from collections import defaultdict, deque
import pprint

def solution(graph, node_length):
    """
    하천계의 Strahler 순서 반환
    """
    # 진입 계수 계산
    indegree = {}
    for u in graph:
        for v in graph[u]:
            indegree[v] = indegree.get(v, 0) + 1

    # Strahler
    strahler = {}
    for i in range(1, node_length+1):
        strahler[i] = [0] * 3 # strahler 순서, strahler max, 개수

    # 강의 근원 deque 추가
    q = deque()
    for node in range(1, node_length + 1):  # 전체 노드 범위로 변경
        if node not in indegree:
            q.append((node))
            strahler[node][0] = 1
    
    while q:
        node = q.popleft()
       
        for adj_node in graph[node]:
            indegree[adj_node] -= 1

            if strahler[adj_node][1] < strahler[node][0]: 
                strahler[adj_node][1] = strahler[node][0]
                strahler[adj_node][2] = 1
            elif strahler[adj_node][1] == strahler[node][0]:
                strahler[adj_node][2] += 1
            
            if indegree[adj_node] == 0:
                if strahler[adj_node][2] >= 2:
                    strahler[adj_node][0] = strahler[adj_node][1] + 1
                else:
                    strahler[adj_node][0] = strahler[adj_node][1]
                
                q.append(adj_node)

    return max(info[0] for info in strahler.values())

if __name__ == "__main__":
    T = int(sys.stdin.readline()) # 테스트 케이스
    for _ in range(T):
        # 테스트 케이스 번호, 노드 수, 간선 수
        case_num, node_length, edge_length = map(int, sys.stdin.readline().split())
        graph = defaultdict(list)
        for _ in range(edge_length):
            start, end = map(int, sys.stdin.readline().split())
            graph[start].append(end)

        order = solution(graph, node_length)
        print(f'{case_num} {order}')