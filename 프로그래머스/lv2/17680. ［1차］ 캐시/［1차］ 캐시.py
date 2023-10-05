def solution(cacheSize, cities):
    answer = 0
    cache = []
    
    if cacheSize == 0:
        return 5 * len(cities)
    
    for city in cities:
        city = city.upper()
        
        if city in cache:       # cache hit
            cache.remove(city)
            cache.append(city)
            answer += 1
        else:                   # cache miss
            if len(cache) >= cacheSize:
                cache.pop(0)
            
            cache.append(city)
            answer +=5
    
    return answer