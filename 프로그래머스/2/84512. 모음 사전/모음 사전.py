def create_dict(dictionary=[] , char='', step=0):
    '''
    1~5자리 대문자 모음 사전(dictionary)을 생성
    
    dictionary: 사전 리스트
    char: 사전에 추가할 단어
    step: 단어 자릿수
    '''
    if step == 6: return
    if char != '':
        dictionary.append(char)

    for i in ['A', 'E', 'I', 'O', 'U']:
        create_dict(dictionary, ''.join([char, i]), step + 1)
        
def solution(word):
    '''
    입력된 word가 사전에서 몇 번째 단어인지 return
    '''
    dictionary = []
    create_dict(dictionary, '', 0)
    return dictionary.index(word) + 1
