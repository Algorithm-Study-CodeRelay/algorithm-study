def solution(schedules, timelogs, startday):
    
    # 상품받는 직원 수
    answer = 0
    
    # 참가자 수
    person = len(schedules)
    
    # 직원수 계산
    for i in range(person):
        day = startday
        check = 0
        expected = (schedules[i] // 100 * 60) + (schedules[i] % 100)
        
        for real_time in timelogs[i]:
            
            # 주말인 경우 판단 X
            if day == 6 or day == 7:
                day += 1
                continue
            
            # 분 차이 계산
            real_min = (real_time // 100 * 60) + (real_time % 100)
            diff = real_min - expected
            
            day += 1
            if diff > 10:
                break
                
            check += 1 
            # 평일 기준 5일 모두 통과하면, answer 추가
            if check == 5:
                answer += 1   
            
    return answer