# encoding=utf-8
#-------------------------------------------------------------------------------
# Description:
# Author:      ccat
# Created:     30/Nov/2014
#-------------------------------------------------------------------------------


import unittest

def testTarget(a=1,b=1):
    return a*b


class UnittestExample(unittest.TestCase):
    def setUp(self):
        self.a=1
        self.b=1

    def test_a(self):
        self.assertEqual(testTarget(self.a),1)
        self.a=2
        self.assertEqual(testTarget(self.a),2)

    def test_b(self):
        self.assertEqual(testTarget(self.a,self.b),1)
        self.b=2
        self.assertEqual(testTarget(b=self.b),2)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()

