def install_cctv(car1, car2):
    if car1[1] >= car2[0]:
        return [max(car1[0], car2[0]), min(car1[1], car2[1])]
    else:
        return None  # 겹치지 않음

def solution(routes):
    """
    input:
        routes: 차량의 이동 경로 [진입 지점, 진출 지점]
    return: 
        모든 차량이 한 번은 단속용 카메라를 만나도록 하는 카메라 최소 설치 개수
    """
    routes.sort()  # 진입 기준 오름차순 정렬
    answer = 0
    i = 0
    n = len(routes)
    
    while i < n:
        overlap = routes[i]
        i += 1

        # 다음 차량들과 겹치는 구간 좁혀가기
        while i < n:
            new_overlap = install_cctv(overlap, routes[i])
            if new_overlap is None:
                break  # 겹치지 않으면 현재 cctv 위치 확정
            overlap = new_overlap
            i += 1

        answer += 1  # 카메라 하나 설치

    return answer

if __name__ == "__main__":
    routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3], [0, 100], [2, 10], [20, 101], [80, 95]]
    print(solution(routes))  # 출력: 4
