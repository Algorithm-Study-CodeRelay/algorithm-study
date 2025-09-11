import re

def solution(new_id):
    
    answer = ''
    
    # 1단계
    answer = new_id.lower()
    
    # 2단계, 4단계
    answer = re.sub(r'[^a-z0-9_.-]', '', answer).strip('.')
    
    # 3단계
    answer = re.sub(r'\.+', '.', answer)
    
    # 5단계
    if len(answer) == 0:
        answer = 'a'
        
    # 6단계
    if len(answer) > 15:
        answer = answer[:15].rstrip('.')
        
    # 7단계
    if len(answer) < 3:
        while len(answer) != 3:
            answer += answer[-1]
    
    return answer