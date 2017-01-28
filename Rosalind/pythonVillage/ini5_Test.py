import unittest
from ini5 import evenLines

dataset = """Bravely bold Sir Robin rode forth from Camelot
Yes, brave Sir Robin turned about
He was not afraid to die, O brave Sir Robin
And gallantly he chickened out
He was not at all afraid to be killed in nasty ways
Bravely talking to his feet
Brave, brave, brave, brave Sir Robin
He beat a very brave retreat"""

output = """Yes, brave Sir Robin turned about
And gallantly he chickened out
Bravely talking to his feet
He beat a very brave retreat"""

class Test_ini5_Test(unittest.TestCase):
    def testEvenLines(self):
        lines = dataset.splitlines(True)
        text = evenLines(lines)
        self.assertEqual(text, output)

#if __name__ == '__main__':
#    unittest.main()
