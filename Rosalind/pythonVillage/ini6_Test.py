import unittest
from ini6 import countWords

dataset = "We tried list and we tried dicts also we tried Zen"

expected = { 
'and': 1, 
'We': 1,
'tried': 3,
'dicts': 1,
'list': 1,
'we': 2,
'also': 1,
'Zen': 1
}

class Test_ini6_Test(unittest.TestCase):
    def testcountWords(self):
        output = countWords(dataset)
        self.assertEquals(output, expected)

#if __name__ == '__main__':
#    unittest.main()
