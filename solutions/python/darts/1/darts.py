def score(x, y):
    point = ((x ** 2) + (y ** 2))** 0.5 

    if point > 10:
        return int(0)
    elif point > 5:
        return int(1)
    elif point > 1:
        return int(5)
    elif point >= 0: 
        return int(10)
    else:
        return point