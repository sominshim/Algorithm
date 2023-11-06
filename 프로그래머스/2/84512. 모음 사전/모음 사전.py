def create_dict(dictionary=[] , char='', step=0):
    if step == 6: return 
    if char != '':
        dictionary.append(char)

    for i in ['A', 'E', 'I', 'O', 'U']:
        create_dict(dictionary, ''.join([char, i]), step + 1)
        
def solution(word):
    dictionary = []
    create_dict(dictionary, '', 0)
    return dictionary.index(word) + 1