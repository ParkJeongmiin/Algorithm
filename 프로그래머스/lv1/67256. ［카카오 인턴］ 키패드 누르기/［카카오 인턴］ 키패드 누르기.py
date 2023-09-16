def solution(numbers, hand):
    answer = ''
    
    key_pad = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '*', '0', '#']
    left_location = '*'
    right_location = '#'
    hand = hand[0].upper()
    
    # 눌러야하는 숫자를 가져온다.
    for number in numbers:
        number = str(number)
        
        # 왼손, 오른손만 누를 수 있는 버튼이면 바로 이동
        if number in "147*":
            answer += 'L'
            left_location = number
        elif number in "369#":
            answer += 'R'
            right_location = number
        elif number in "2580":
            next_num_col = (key_pad.index(number)) // 3
            next_num_row = (key_pad.index(number)) % 3
            
            left_point = key_pad.index(left_location)
            right_point = key_pad.index(right_location)
            
            # 각각 현재 위치에서 거리 구하기
            left_distance = abs(next_num_col - left_point // 3) + next_num_row - (left_point % 3)
            right_distance = abs(next_num_col - right_point // 3) + (right_point % 3) - next_num_row

            if left_distance < right_distance:
                answer += 'L'
                left_location = number
            elif left_distance > right_distance:
                answer += 'R'
                right_location = number
            else:
                answer += hand
                if hand == 'R':
                    right_location = number
                else:
                    left_location = number
    
    return answer