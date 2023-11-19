def solution(record):
    command_msg = {'Enter' : '님이 들어왔습니다.',
                                'Leave': '님이 나갔습니다.'}
    uid_nickname = {}
    answer = []
    tmp = []

    for log in record:
        command, uid = log.split()[:2]
        if command != 'Leave':
            uid_nickname[uid] = log.split()[2]
        if command != 'Change':
            tmp.append([uid, command_msg[command]])
    for msg in tmp:
        answer.append(''.join([uid_nickname[msg[0]], msg[1]]))
    return answer