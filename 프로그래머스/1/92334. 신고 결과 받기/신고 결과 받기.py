from collections import Counter

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    report_dict = {id:[] for id in id_list}

    for e in set(report):
        reporter, reported = e.split()
        report_dict[reporter].append(reported)

    sum_reported = sum(report_dict.values(), [])
    counts = Counter(sum_reported)

    for reporter, reported in report_dict.items():
        for id in reported:
            if counts[id] >= k :
                answer[id_list.index(reporter)] += 1

    return answer
