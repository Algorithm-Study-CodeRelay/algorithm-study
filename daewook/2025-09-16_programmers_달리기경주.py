def solution(players, callings):
    
    nums = [i for i in range(len(players))]
    
    # 딕셔너리와 리스트를 함께 쓰자 !
    # 딕셔너리로 현재 위치를 찾고, 리스트에 값을 저장 !
    player_dict = dict(zip(players, nums))
    
    for name in callings:
        # 등수
        ranking = player_dict[name]
        players[ranking-1], players[ranking] = players[ranking], players[ranking-1]
        player_dict[name] = ranking-1
        player_dict[players[ranking]] = ranking
        
    return players