from collections import defaultdict
import heapq

def solution(n, costs):
    answer = 0
    visited = set()
    graph = defaultdict(list)
    
    # 그래프 구성
    for a, b, c in costs:
        graph[a].append((c, b))
        graph[b].append((c, a))

    # 우선순위 큐 (최소 힙)
    min_heap = graph[0][:]
    heapq.heapify(min_heap)
    visited.add(0)

    while len(visited) < n:
        cost, next_node = heapq.heappop(min_heap)
        if next_node in visited:
            continue
        visited.add(next_node)
        answer += cost
        for edge in graph[next_node]:
            if edge[1] not in visited:
                heapq.heappush(min_heap, edge)
    
    return answer

if __name__ == "__main__":
    n = 4	
    costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
    print(solution(n, costs))  # 출력: 4
