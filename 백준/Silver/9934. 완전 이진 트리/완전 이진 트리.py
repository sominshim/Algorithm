from collections import deque
K = int(input())  # 트리의 깊이
nodes = list(map(int, input().split()))  # 중위 순회 결과
    
# 각 레벨별로 노드를 저장할 리스트
levels = [[] for _ in range(K)]
    
# 큐에 초기 상태로 (노드 리스트, 현재 레벨)을 넣음
queue = deque([(nodes, 0)])
    
while queue:
    current_nodes, level = queue.popleft()  # 현재 처리할 노드와 레벨
    if not current_nodes:
        continue
        
    mid = len(current_nodes) // 2  # 중간값이 루트
    levels[level].append(current_nodes[mid])  # 현재 레벨에 루트 노드 추가
        
    # 왼쪽 자식과 오른쪽 자식들을 큐에 추가 (다음 레벨에서 처리)
    queue.append((current_nodes[:mid], level + 1))  # 왼쪽 서브트리
    queue.append((current_nodes[mid + 1:], level + 1))  # 오른쪽 서브트리
    
# 각 레벨별로 노드 출력
for level in levels:
    print(' '.join(map(str, level)))