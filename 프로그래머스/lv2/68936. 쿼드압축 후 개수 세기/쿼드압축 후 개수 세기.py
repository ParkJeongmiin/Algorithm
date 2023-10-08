def solution(arr):
    answer = [0, 0]
    
    def check(y, x, size):
        value = arr[y][x]

        for row in range(y, y + size):
            for col in range(x, x + size):
                if value != arr[row][col]:
                    size //= 2
                    check(y, x, size)
                    check(y, x + size, size)
                    check(y + size, x, size)
                    check(y + size, x + size, size)
                    return
        
        answer[value] += 1

    check(0, 0, len(arr)) 
    
    return answer
'''
len(arr) = 8 = 2 ** 3(n) ==> 나누기 n 번 반복
len(arr[0]) // 2 > col  |   len(arr[0]) // 2 < col 
                        |
            00 01 02 03 | 04 05 06 07
            10 11 12 13 | 14 15 16 17
            20 21 22 23 | 24 25 26 27
            30 31 32 33 | 34 35 36 37    len(arr) // 2 > row
            ------------|----------------------------
            40 41 42 43 | 44 45 46 47    len(arr) // 2 < row
            50 51 52 53 | 54 55 56 57
            60 61 62 63 | 64 65 66 67
            70 71 72 73 | 74 72 76 77

전체 배열이 같은 숫자인지 확인한다.

같은 숫자이면 정답의 개수 더하고, 아니면 4등분한다.


'''