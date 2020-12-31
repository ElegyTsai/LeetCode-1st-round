
def TriJug(a,b,c):
    if a+b<=c or a+c<=c or b+c <=a:
        return "not a triangle"

    if not(a==b or a==c or b==c):
        return "scalene"
    elif a==b and b==c:
        return "equilateral"
    else:
        return "isosceles"

