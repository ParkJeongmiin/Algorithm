from itertools import permutations

def solution(k, dungeons):
    answer = -1
    all_thing = []
    
    for i in permutations(dungeons, len(dungeons)):
        all_thing.append(i)
        
    possible = []
    i = 0
    while i < len(all_thing):
        
        percent = k
        count = 0
        
        for must, sub in all_thing[i]:
            if percent >= must:
                percent -= sub
                count += 1
            elif percent < must:
                break
                
        possible.append(count)
        i += 1
        
    return max(possible)