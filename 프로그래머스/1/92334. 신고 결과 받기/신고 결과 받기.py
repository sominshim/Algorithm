def solution(id_list, report, k):
    answer = []
    report_dict = {id : set() for id in id_list}
    reported_cnt = {id : 0 for id in id_list}
    suspended_id = []

    for e in report:
        reporter, reported = e.split()
        report_dict[reporter].add(reported)

    listed = [list(v) for v in report_dict.values()]
    sum_listed = sum(listed, [])
    for reported in sum_listed:
        reported_cnt[reported] += 1
    for id, cnt in reported_cnt.items():
        if cnt >= k:
            suspended_id.append(id)

    for reporter, reported in report_dict.items():
        cnt = 0
        for id in reported:
            if id in suspended_id: 
                cnt += 1
        answer.append(cnt)

    return answer