from collections import deque

def solution(cacheSize, cities):
    time = 0
    q = deque()
    if cacheSize == 0:
        return 5 * len(cities)
    for city in cities:
        city = city.upper()
        if city in q:
            time += 1
            q.remove(city)
            q.append(city)
        else:
            time += 5
            if len(q) < cacheSize:
                q.append(city)
            else:
                q.popleft()
                q.append(city)
    return time