def solution(numbers, hand):
    answer = ''
    
    keypad = [[1, 4, 7, '*'], [2, 5, 8, 0], [3, 6, 9, '#']]
    
    left_loc = [0, 3]
    right_loc = [2, 3]
    
    for num in numbers:
        if num in keypad[0]:
            answer += 'L'
            temp = keypad[0].index(num)
            left_loc = [0, temp]
            
        elif num in keypad[2]:
            answer += 'R'
            temp = keypad[2].index(num)
            right_loc = [2, temp]
            
        else:
            temp = keypad[1].index(num)
            mid_loc = [1, temp]
            
            left_diff = abs(mid_loc[0] - left_loc[0]) + abs(mid_loc[1] - left_loc[1])
            right_diff = abs(mid_loc[0] - right_loc[0]) + abs(mid_loc[1] - right_loc[1])
            
            if left_diff < right_diff:
                answer += 'L'
                left_loc = mid_loc
            
            elif left_diff > right_diff:
                answer += 'R'
                right_loc = mid_loc
                
            else:
                if hand == 'right':
                    answer += 'R'
                    right_loc = mid_loc
                
                else:
                    answer += 'L'
                    left_loc = mid_loc
            

    return answer