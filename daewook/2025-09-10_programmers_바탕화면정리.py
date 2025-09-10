def solution(wallpaper):
    
    # 위치값 초기화
    lux, luy, rdx, rdy = 100, 100, 0, 0
    edit = [False, False]
    
    row = 0
    for files in wallpaper:
        check = list(files)
        
        # luy 구하기 - 지속적으로 수정 필요
        # rdx, rdy 구하기
        if '#' in check:
            luy = min(luy, check.index('#'))
            rdx = row
            
            # rdy 추가 계산
            check = check[::-1]
            tmp = check.index('#')
            comp = len(check) - tmp
            rdy = max(rdy, comp)
        
        # lux 구하기 - 한번 구하면, 수정할 필요 없음.
        if ('#' in check) and (edit[0] == False):
            lux = row
            edit[0] = True           
            
        row += 1
            
    rdx += 1
    answer = [lux, luy, rdx, rdy]
    return answer