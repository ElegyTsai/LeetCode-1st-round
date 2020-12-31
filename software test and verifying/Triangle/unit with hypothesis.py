import unittest
from hypothesis import given,settings
import hypothesis.strategies as st
from Judge.Jud import JudgeMethod



class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.obj=JudgeMethod()


    @given(a=st.integers(max_value=100,min_value=2), b=st.integers(max_value=100,min_value=2))
    def test_case1(self,a,b):
        c=a+b+1
        print("test the case of not a triangle for ",a,b,c)
        self.assertEqual(self.obj.TriJud(a, b, c),"not a triangle")
        self.assertEqual(self.obj.TriJud(a, c, b), "not a triangle")
        self.assertEqual(self.obj.TriJud(c, a, b), "not a triangle")


    @given(a1=st.integers(max_value=100,min_value=2), b1=st.integers(max_value=100,min_value=2))
    def test_case2(self,a1,b1):
        if a1==b1:
            return
        c=a1+b1-1
        print("test the case of scalene for ",a1,b1,c)
        self.assertEqual(self.obj.TriJud(a1, b1, c),"scalene")
        self.assertEqual(self.obj.TriJud(a1, c, b1), "scalene")
        self.assertEqual(self.obj.TriJud(c, a1, b1), "scalene")

    @given(a2=st.integers(max_value=100,min_value=2))
    def test_case3(self,a2):

        print("test the case of equilateral for ",a2,a2,a2)
        self.assertEqual(self.obj.TriJud(a2,a2,a2),"equilateral")

    @given(a3=st.integers(max_value=100,min_value=2), b3=st.integers(max_value=100,min_value=2))
    def test_case4(self,a3,b3):

        if a3==b3:
            return
        c=max(a3,b3)
        print("test the case of isosceles for ",a3,b3,c)
        self.assertEqual(self.obj.TriJud(a3, b3, c),"isosceles")
        self.assertEqual(self.obj.TriJud(a3, c, b3), "isosceles")
        self.assertEqual(self.obj.TriJud(c, a3, b3), "isosceles")


if __name__ == '__main__':
    unittest.main()
