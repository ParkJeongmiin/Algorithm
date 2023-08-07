def solution(numbers):
    
    # 주어진 리스트를 str형으로 변환
    numbers = list(map(str, numbers))
    
    # 앞자리가 큰 숫자를 기준으로 내림차순 정렬
    # 문자열 비교는 ASCII 코드로 변환 후 비교하게 된다.
    # x*3 인 이유는 원소가 1000까지 입력되기 때문이다.
    """
    예를 들어 3, 30을 비교하게 되면 3이 앞으로 가야한다.
    *3을 하게 되면 333, 303030이 되고
    이 숫자 2개를 비교하게 되면 333이 앞에 가게 된다.
    """
    numbers.sort(key = lambda x:x*3, reverse = True)
    
    """
    str 그대로 출력하게되면
    [0, 0, 0, 0] 인 특이 케이스에서 정답은 "0" 이지만
    "0000"으로 출력하게되 오답이 된다.
    그래서 "0000"을 int 형으로 변환해 "0"이 되도록 한다.
    """
    answer = str(int(''.join(numbers)))
    
    return answer