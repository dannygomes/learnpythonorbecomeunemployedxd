def score(x, y):
    position = x**2 + y**2
    
    if position <= 1:
        return 10
    if position <= 25:
        return 5
    if position <= 100:
        return 1
    return 0
