def equilateral(sides ):
    a, b, c = sides 
    if not all(x > 0 for x in (a, b, c)):
        return False
    else:
        return a == b == c
        
def isosceles(sides):
    a, b, c = sides 
    if not all(x > 0 for x in (a, b, c)):
        return False 
    if a + b <= c or b + c <= a or a + c <= b:
        return False
    if a==b or b==c or c==a:
        return True
    else:
        return False
    
def scalene(sides):
    a, b, c = sides 
    if not all(x > 0 for x in (a, b, c)):
        return False 
    if a + b <= c or b + c <= a or a + c <= b:
        return False
    if a!=b and b!=c and c!=a:
        return True
    else:
        return False