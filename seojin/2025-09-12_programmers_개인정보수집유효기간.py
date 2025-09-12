def solution(today, terms, privacies):
    answer = []
    
    today = int(today.replace(".", ""))     # 날짜 int형으로 처리
    
    term_d = {}
    for term in terms:
        t, m = term.split()                 # 종류, 기한
        term_d[t] = int(m)                  # dict 형태로 저장
    
    for i in range(len(privacies)):
        date, t = privacies[i].split()      # 일자, 종류
        date = int(date.replace(".",""))
        
        y = date // 10000                   # 연
        md = date % 10000                   # 월일
        
        md += term_d[t] * 100               # 유효기간 계산
        while md >= 1300:                   # 13월+ 일때
            md -= 1200
            y += 1
        date = y * 10000 + md - 1

        if date < today: answer.append(i + 1)
    
    return answer