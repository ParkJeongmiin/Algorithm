import math
from functools import reduce


def get_lcm(number_list):
    return reduce(lambda a, b: a * b // math.gcd(a, b), number_list)


def check(t, signal):
    G, Y, R = signal
    return True if 1 <= (t % (G + Y + R)) - G <= Y else False
    

def solution(signals):
    cycle_time = list(sum(s) for s in signals)
    max_time = get_lcm(cycle_time)
    t = 0
    
    while t <= max_time:
        t += 1
        
        for s in signals:
            if check(t, s):
                continue
            else:
                break
        else:
            return t
        
    return -1