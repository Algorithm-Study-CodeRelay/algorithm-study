def solution(numbers, hand):
    idx = {'1': [0,0], '2': [0,1], '3': [0,2],
            '4': [1,0], '5': [1,1], '6': [1,2],
            '7': [2,0], '8': [2,1], '9': [2,2],
            '*': [3,0], '0': [3,1], '#': [3,2]}
    
    cur_l, cur_r = idx['*'], idx['#']
    
    answer = ''
    
    for number in numbers:
        number = str(number)
        if number == '1' or number == '4' or number == '7':
            answer += 'L'
        elif number == '3' or number == '6' or number == '9':
            answer += 'R'
        else:
            dist_l = abs(cur_l[0] - idx[number][0]) + abs(cur_l[1] - idx[number][1])
            dist_r = abs(cur_r[0] - idx[number][0]) + abs(cur_r[1] - idx[number][1])
            if dist_l < dist_r:
                answer += 'L'
            elif dist_l > dist_r:
                answer += 'R'
            else:
                answer += hand[0].upper()
                
        if answer[-1] == 'L':
            cur_l = idx[number]
        else:
            cur_r = idx[number]
        
    return answer