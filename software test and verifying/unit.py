from Judge.Jud import JudgeMethod

#import sys,pprint
#pprint.pprint(sys.path)

import unittest

class Test1(unittest.TestCase):
    def test_my_judge_1(self):
        print('execute test_one')
        obj = JudgeMethod()
        assert obj.TriJud(1, 2, 3) == "not a triangle"

    def test_my_judge_2(self):
        print('execute test_two')
        obj = JudgeMethod()
        assert obj.TriJud(1, 2, 2) == "isosceles"

    def test_my_judge_3(self):
        print('execute test_three')
        obj = JudgeMethod()
        assert obj.TriJud(2, 2, 3) == "isosceles"

    def test_my_judge_4(self):
        print('execute test_four')
        obj = JudgeMethod()
        assert obj.TriJud(1, 2, 1) == "not a triangle"

    def test_my_judge_5(self):
        print('execute test_five')
        obj = JudgeMethod()
        assert obj.TriJud(1, 1, 1) == "equilateral"

if __name__ == '__main__':
    unittest.main()
