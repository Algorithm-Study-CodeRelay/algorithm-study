def solution(park, routes):
    
    answer = []
    
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == 'S':
                answer.append(i)
                answer.append(j)
                break
    
    for move in routes:
        dir, dis = move.split(); dis = int(dis)
        
        if dir == 'N': 
            if answer[0] - dis < 0: continue 
            for i in range(1, dis+1):
                if park[answer[0]-i][answer[1]] == 'X':
                    break
            else:
                answer[0] -= dis
            
        elif dir == 'S': 
            if answer[0] + dis >= len(park): continue
            for i in range(1, dis+1):
                if park[answer[0]+i][answer[1]] == 'X':
                    break
                    
            else:     
                answer[0] += dis
            
        elif dir == 'W': 
            if answer[1] - dis < 0: continue
            for i in range(1, dis+1):
                if park[answer[0]][answer[1]-i] == 'X':
                    break
            else:
                answer[1] -= dis
            
        elif dir == 'E': 
            if answer[1] + dis >= len(park[0]): continue
            for i in range(1, dis+1):
                if park[answer[0]][answer[1]+i] == 'X':
                    break
            else:  
                answer[1] += dis
    
    
    return answer