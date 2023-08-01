def solution(players, callings):
    
    players_dict = {player : rank for rank, player in enumerate(players)}
    for upward_person in callings:
        idx = players_dict[upward_person]
        players_dict[upward_person] -= 1
        players_dict[players[idx - 1]] += 1
        players[idx - 1], players[idx] = players[idx], players[idx - 1]
    return players