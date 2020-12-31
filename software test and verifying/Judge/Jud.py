import unittest
import sys,pprint
class JudgeMethod:
    def TriJud(self,a,b,c):
        if a+b<=c or a+c<=b or b+c <=a:
            return "not a triangle"

        if not(a==b or a==c or b==c):
            return "scalene"
        elif a==b and b==c:
            return "equilateral"
        else:
            return "isosceles"

