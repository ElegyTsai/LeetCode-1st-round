import unittest
from Judge.Jud import JudgeMethod


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.obj=JudgeMethod()

    def test_case1(self):
        print("test the case of not a triangle")
        self.assertEqual(self.obj.TriJud(1, 2, 3),"not a triangle")
        self.assertEqual(self.obj.TriJud(2, 1, 3), "not a triangle")
        self.assertEqual(self.obj.TriJud(3, 2, 1), "not a triangle")
        self.assertEqual(self.obj.TriJud(3, 7, 3), "not a triangle")
        self.assertEqual(self.obj.TriJud(4, 7, 3), "not a triangle")

    def test_case2(self):
        print("test the case of scalene")
        self.assertEqual(self.obj.TriJud(2,4,3),"scalene")
        self.assertEqual(self.obj.TriJud(7, 5, 3), "scalene")
        self.assertEqual(self.obj.TriJud(3, 5, 6), "scalene")

    def test_case3(self):
        print("test the case of equilateral")
        self.assertEqual(self.obj.TriJud(2,2,2),"equilateral")
        self.assertEqual(self.obj.TriJud(3, 3, 3), "equilateral")
        self.assertEqual(self.obj.TriJud(5, 5, 5), "equilateral")

    def test_case4(self):
        print("test the case of isosceles")
        self.assertEqual(self.obj.TriJud(2, 2, 3),"isosceles")
        self.assertEqual(self.obj.TriJud(3, 4, 3), "isosceles")
        self.assertEqual(self.obj.TriJud(6, 5, 5), "isosceles")


if __name__ == '__main__':
    unittest.main()
