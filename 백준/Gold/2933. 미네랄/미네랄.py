import sys
from collections import defaultdict, deque
import pprint

def bfs(cave, R, C, start, visited):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] 
    q = deque([start])
    cluster = [start]

    while q:
        r, c = q.popleft()

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < R and 0 <= nc < C and (nr, nc) not in visited:
                if cave[nr][nc] == 'x':
                    visited.add((nr, nc))
                    cluster.append((nr, nc))
                    q.append((nr, nc))        
                        
    return cluster

def apply_gravity(cave, R, C, floating_cluster):
    # 각 열의 최하단 노드와 다른 cluster의 미네랄과의 최단거리 계산 
    bottom_rc = []
    floating_cluster.sort(key=lambda x: (x[1], -x[0]))  # 열 정렬 + 아래부터 우선

    bottom_r = floating_cluster[0][0]
    prev_c = floating_cluster[0][1]
    for r, c in floating_cluster:
        if prev_c == c:
            if r > bottom_r:
                bottom_r = r
        else: 
            bottom_rc.append((bottom_r, prev_c))
            bottom_r, prev_c = r, c            
    bottom_rc.append((bottom_r, prev_c))  # 마지막 열 추가

    # 최단 낙하 거리 계산
    min_dist = R
    for r, c in bottom_rc:
        for nr in range(r + 1, R):
            if cave[nr][c] == 'x' and (nr, c) not in floating_cluster:
                min_dist = min(min_dist, nr - r - 1)
                break
        else:
            min_dist = min(min_dist, R - r - 1)
    
    if min_dist == 0:
        return  # 이동 불가
    
    # 클러스터 좌표를 내리는 과정 (위에서 제거 후 아래에 추가)
    floating_cluster.sort(reverse=True)  # 아래부터 이동해야 덮어쓰기 문제 없음
    for r, c in floating_cluster:
        cave[r][c] = '.'
    for r, c in floating_cluster:
        cave[r + min_dist][c] = 'x'



def solution(cave, R, C, N, rows_to_remove):
    """
    RxC 동굴에서 N번의 미네랄 제거 후의 동굴을 출력하시오.

    클러스터: 상하좌우 인접 미네랄 그룹. 
    1. 왼쪽에서 오른쪽(→)방향, 오른쪽에서 왼쪽(←)방향을 번갈아가면서, 
       i행의 첫번째 혹은 마지막 미네랄'x'을 하나씩 제거한다.
    2. 이때 클러스터가 2개로 나누어질 수 있다. 이때 중력이 작용한다. 
    3. 클러스터가 떨어질 때, 바닥 또는 미네랄 위로 떨어진다. 인접한 클러스터는 합쳐진다.
    
    초기상태          6행 → 이동 후     6행 ← 이동 후      4행 → 이동 후     3행 ← 이동 후     1행 → 이동 후
    8 | ........    8 | ........    8 | ........    8 | ........    8 | ........    8 | ........
    7 | ........    7 | ........    7 | ........    7 | ........    7 | ........    7 | ........
    6 | ...x.xx.    6 | .....xx.    6 | .....x..    6 | .....x..    6 | ........    6 | ........
    5 | ...xxx..    5 | ...xxx..    5 | ...xxx..    5 | ...xxx..    5 | ........    5 | ........
    4 | ..xxx...    4 | ..xxx...    4 | ..xxx...    4 | ...xx...    4 | .....x..    4 | .....x..
    3 | ..x.xxx.    3 | ..x.xxx.    3 | ..x.xxx.    3 | ..x.xxx.    3 | ..xxxx..    3 | ..xxxx..
    2 | ..x...x.    2 | ..x...x.    2 | ..x...x.    2 | ..x...x.    2 | ..xxx.x.    2 | ..xxx.x.
    1 | .xxx..x.    1 | .xxx..x.    1 | .xxx..x.    1 | .xxx..x.    1 | .xxxxxx.    1 | ..xxxxx.
    """

    for turn, row in enumerate(rows_to_remove):
        row = R - row # 실제 cave index에 맞추기
        removed = False

        # 1. 미네랄 제거
        # 홀수일 때, 왼쪽 → 오른쪽
        if turn % 2 == 0:
            for c in range(C):
                if cave[row][c] == 'x':
                    cave[row][c] = '.'
                    removed = True
                    break
        
        # 짝수일 때, 오른쪽 ← 왼쪽
        else:
            for c in range(C-1, -1, -1):
                if cave[row][c] == 'x':
                    cave[row][c] = '.'
                    removed = True
                    break
        
        if not removed:
            continue  # 미네랄을 제거 못했으면 클러스터 갱신 불필요

        # 2. 클러스터 확인 - BFS 탐색
        visited = set()
        clusters = []

        for i in range(R):
            for j in range(C):
                if cave[i][j] == 'x' and (i, j) not in visited:
                    cluster = bfs(cave, R, C, (i, j), visited)
                    clusters.append(cluster)

        # 3. 바닥에 붙어 있지 않은 클러스터만 골라서 중력 적용
        for cluster in clusters:
            for r, _ in cluster:
                if r == R - 1:
                    break
            else:
                apply_gravity(cave, R, C, cluster)
                break  # 하나만 떨어뜨리는 경우만 있음
    
    # 최종 cave 상태 출력
    for row in cave:
        print(''.join(row))

if __name__ == "__main__":
    R, C = map(int, sys.stdin.readline().split())
    cave = []
    for _ in range(R):
        row = list(sys.stdin.readline().strip())
        cave.append(row)
    
    N = int(sys.stdin.readline())
    rows_to_remove = list(map(int, sys.stdin.readline().split()))
    solution(cave, R, C, N, rows_to_remove)