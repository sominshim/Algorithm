def solution(progresses, speeds):
    q = []
    prev_day = -1
    for progress, speed in zip(progresses, speeds):
        # 남은 작업량 작업일 수 계산
        work_days = (100 - progress + speed - 1) // speed
        if work_days > prev_day:
            prev_day = work_days
            q.append(1)
        else:
            q[-1] += 1
        
    return q