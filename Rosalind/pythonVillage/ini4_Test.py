import unittest
from ini4 import sumOdd

class Test_ini4_Test(unittest.TestCase):
    def testOddSum(self):
        sum = sumOdd(100, 200) 
        print sum
        self.assertEqual(sum, 7500)

#if __name__ == '__main__':
#    unittest.main()
