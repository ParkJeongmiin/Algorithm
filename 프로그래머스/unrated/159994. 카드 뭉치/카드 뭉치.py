def solution(cards1, cards2, goal):
    answer = ''
    
    cards1 = cards1 + [0] * (len(goal)-len(cards1))
    cards2 = cards2 + [0] * (len(goal)-len(cards2))
    
    while goal:
        want_word = goal.pop(0)
        
        # 카드 뭉치에서 찾기 - 뭉치에 카드가 있어야함.
        if want_word == cards1[0]:
            cards1.pop(0)
        elif want_word == cards2[0]:
            cards2.pop(0)
        else:
            return 'No'
        
    return 'Yes'
    
    """
    1. goal에서 뭉치에서 찾을 단어를 하나 가져온다.
    2. 카드 뭉치의 길이를 goal과 맞춘다.
    3. want_word와 뭉치 1, 2에 맞는게 있는지 찾는다.
    
    """