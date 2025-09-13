def solution(today, terms, privacies):
    answer = []
    
    # terms: dictionary로 분리
    period = {}
    
    for term in terms:
        tmp1 = term.split(' ')
        period[f'{tmp1[0]}'] = tmp1[1]
        
    today_date = list(map(int, today.split('.')))
    check = 1
    
    # 파기 여부 판단
    for privacy in privacies:
        tmp2 = privacy.split(' ')
        privacy_date = list(map(int, tmp2[0].split('.')))
        
        drop = period[f'{tmp2[1]}']
        drop = int(drop)
        
        # 동의 날짜로부터 보유 가능 기간 계산
        allow = privacy_date
        
        # month가 12개월 이상일 경우 처리
        if drop > 11:
            allow[0] += (drop // 12)
            drop %= 12
        
        # 1일일 경우, 특수 예외 처리
        if allow[2] == 1:
            allow[2] = 28
            allow[1] += (drop - 1)
            
            if allow[1] > 12:
                allow[1] %= 12
                allow[0] += 1
                
            # 파기 여부 확인
            if allow[0] < today_date[0] :
                answer.append(check)
        
            elif allow[0] == today_date[0] and allow[1] < today_date[1]:
                answer.append(check)
       
            elif allow[0] == today_date[0] and allow[1] == today_date[1] and allow[2] < today_date[2]:
                answer.append(check)
            
            check += 1
            continue
        

        allow[1] += drop
        allow[2] -= 1
        
        # 12월 이상을 표현하고 있다면, 연도 올리기.
        if allow[1] > 12:
            allow[1] %= 12
            allow[0] += 1
        
        # 28일 이상을 표현하고 있다면, 월 올리기
        if allow[2] > 28:
            allow[2] %= 28
        

        # 파기여부 확인
        if allow[0] < today_date[0] :
            answer.append(check)
        
        elif allow[0] == today_date[0] and allow[1] < today_date[1]:
            answer.append(check)
       
        elif allow[0] == today_date[0] and allow[1] == today_date[1] and allow[2] < today_date[2]:
            answer.append(check)
            
        check += 1
        
    return answer