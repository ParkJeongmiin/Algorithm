import math
from functools import reduce


def get_lcm(number_list):
    return reduce(lambda a, b: a * b // math.gcd(a, b), number_list)


def check(t, signal):
    G, Y, R = signal
    return 1 <= (t % (G + Y + R)) - G <= Y
    

def solution(signals):
    cycle_time = list(sum(s) for s in signals)
    max_time = get_lcm(cycle_time)
    t = 0
    
    for t in range(1, max_time + 1):
        for s in signals:
            if not check(t, s): # 하나라도 노란불 아니면 다음 시간 탐색
                break
        else:
            return t
        
    return -1